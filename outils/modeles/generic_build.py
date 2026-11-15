import subprocess, os, sys, wave, importlib.util, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.signal import butter, sosfilt, fftconvolve

spec = importlib.util.spec_from_file_location("cfg", sys.argv[1]); cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
D = cfg.D; M = f"{D}/src"; C = f"{D}/clips"; os.makedirs(C, exist_ok=True)
W, H, FPS = 1080, 1920, 30
VO, END = cfg.VO, cfg.END
BOLD = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
XB = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
GRADE = cfg.GRADE
MODE = sys.argv[2] if len(sys.argv) > 2 else "full"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2500:]); raise SystemExit(1)

S = cfg.SCENES  # (name, src, z0, z1, seg, trans, td, extra, anchor)
cuts, t = [], 0.0
for s in S:
    cuts.append(t)
    if s[4]: t += s[4]
durs = []
for i, (nm, src, z0, z1, seg, tr, td, ex, anc) in enumerate(S):
    seg = seg if seg else END - cuts[-1]
    dur = seg + (S[i+1][6] if i+1 < len(S) else 0); durs.append(dur)
    out, tmp = f"{C}/{nm}.mp4", f"{C}/tmp_{nm}.mp4"
    if os.path.exists(out): continue
    n = int(round(dur*FPS))
    ys = {"c": "ih/2-(ih/zoom/2)", "t": "ih*0.05", "b": "ih-(ih/zoom)-ih*0.03"}[anc]
    vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
          f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='{ys}':d={n}:s={W}x{H}:fps={FPS},{GRADE}{ex},format=yuv420p")
    run(["ffmpeg", "-nostdin", "-y", "-loop", "1", "-i", f"{M}/{src}.jpg", "-vf", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", tmp])
    os.replace(tmp, out)

YEL = (255, 214, 64)
def cap_png(name, text, size=66, y=1360, font=BOLD, maxw=900, stroke=7, color=(255,255,255)):
    f = ImageFont.truetype(font, size); img = Image.new("RGBA", (W, H), (0,0,0,0)); d = ImageDraw.Draw(img)
    toks = text.split(); lines = []; cur = []
    clean = lambda w: w.replace('*', '').replace('~', ' ')
    for w in toks:
        trial = " ".join(clean(x) for x in cur+[w])
        if d.textlength(trial, font=f) > maxw and cur: lines.append(cur); cur = [w]
        else: cur.append(w)
    lines.append(cur); lh = int(size*1.2); y0 = y - len(lines)*lh//2
    sh = Image.new("RGBA", (W, H), (0,0,0,0)); sd = ImageDraw.Draw(sh)
    for k, ln in enumerate(lines):
        words = [clean(w) for w in ln]; full = " ".join(words)
        x = (W - d.textlength(full, font=f) - stroke*1.1*(len(words)-1))/2; yy = y0 + k*lh
        for w, raw in zip(words, ln):
            col = YEL if raw.startswith('*') else color
            sd.text((x, yy+6), w, font=f, fill=(0,0,0,170))
            d.text((x, yy), w, font=f, fill=col+(255,), stroke_width=stroke, stroke_fill=(0,0,0,255))
            x += d.textlength(w, font=f) + d.textlength(" ", font=f) + stroke*1.1
    img = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)), img); img.save(f"{C}/{name}.png")

caps = []
def add(name, text, a, b, **kw): cap_png(name, text, **kw); caps.append((name, a, b))
V = lambda x: x + VO
for k, (txt, a, b, kw) in enumerate(cfg.HOOKS): add(f"hook{k}", txt, a, b, font=XB, **kw)
P = cfg.CAPS
for k, (a, b, txt) in enumerate(P):
    nxt = P[k+1][0] if k+1 < len(P) else b+0.5
    add(f"c{k:02d}", txt, V(a)-0.05, min(V(b)+0.35, V(nxt)-0.05))
for k, (txt, a, b, kw) in enumerate(cfg.FINS): add(f"fin{k}", txt, V(a), END, **kw)

if MODE == "frames":
    pass

inputs, fc = [], []
for s in S: inputs += ["-i", f"{C}/{s[0]}.mp4"]
acc, prev = durs[0], "[0:v]"
for i in range(1, len(S)):
    tr, td = S[i][5], S[i][6]
    fc.append(f"{prev}[{i}:v]xfade=transition={tr}:duration={td}:offset={acc-td:.3f}[x{i}]"); prev = f"[x{i}]"; acc += durs[i]-td
base = len(S)
for j, (nm, a, b) in enumerate(caps):
    inputs += ["-loop", "1", "-t", f"{END:.2f}", "-i", f"{C}/{nm}.png"]
    fi = 0.3 if nm.startswith(("hook", "fin")) else 0.12
    fc.append(f"[{base+j}:v]format=rgba,fade=in:st={a:.2f}:d={fi}:alpha=1,fade=out:st={max(b-0.15,a+fi):.2f}:d=0.15:alpha=1[p{j}]")
    fc.append(f"{prev}[p{j}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[o{j}]"); prev = f"[o{j}]"
li = base + len(caps); inputs += ["-loop", "1", "-t", f"{END:.2f}", "-i", "/home/claude/videos-ayle/outils/logo/ayleco_overlay.png"]
fc.append(f"[{li}:v]format=rgba,fade=in:st=0:d=0.3:alpha=1[lg]"); fc.append(f"{prev}[lg]overlay=36:120[ol]")
fc.append(f"[ol]fade=in:st=0:d=0.3,fade=out:st={END-1.0}:d=1.0,format=yuv420p[vout]")
tmp = f"{D}/tmp_video.mp4"
run(["ffmpeg", "-nostdin", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-t", f"{END}", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-maxrate", "8M", "-bufsize", "16M", tmp])
os.replace(tmp, f"{D}/video.mp4")

# ---------- soft score (piano plucks + pad), always quiet
SR = 44100; n = int(END*SR); tt = np.arange(n)/SR
hz = lambda m: 440*2**((m-69)/12)
lp = lambda x, f: sosfilt(butter(2, f, fs=SR, output='sos'), x)
saw = lambda f, t: 2*((t*f) % 1)-1
mus = np.zeros(n)
beat = 60/cfg.BPM; prog = cfg.PROG; bass = cfg.BASS
def pluck(at, m, amp):
    s0 = int(at*SR); L = min(int(2.4*SR), n-s0)
    if L <= 0: return
    t_ = np.arange(L)/SR; f = hz(m)
    x = (np.sin(2*np.pi*f*t_)+0.35*np.sin(4*np.pi*f*t_)+0.12*np.sin(6*np.pi*f*t_))*np.exp(-t_*2.4)*(1-np.exp(-t_*300))
    mus[s0:s0+L] += amp*x
t0 = 0.2; k = 0; pat = cfg.PAT
while t0 < END-1.5:
    bar = int(k//len(pat)) % len(prog); ch = prog[bar]
    if k % len(pat) == 0: pluck(t0, bass[bar], 0.17)
    if cfg.PLUCK_FROM <= t0: pluck(t0, ch[pat[k % len(pat)]]+12, 0.09)
    t0 += beat*cfg.STEP; k += 1
pad = np.zeros(n)
barlen = beat*cfg.STEP*len(pat)
for i in range(200):
    a = 0.2 + i*barlen
    if a > END: break
    c = prog[i % len(prog)]
    s0, s1 = int(a*SR), min(n, int((a+barlen+1.2)*SR)); t_ = tt[s0:s1]-a
    e = np.clip(t_/0.8, 0, 1)*np.clip((barlen+1.2-t_)/1.2, 0, 1)
    for m in c:
        for det in (-0.1, 0.1): pad[s0:s1] += 0.02*saw(hz(m)*(1+det/100), tt[s0:s1])*e
mus += lp(pad, 1400)*cfg.PAD
rng = np.random.default_rng(3)
ir_len = int(2.6*SR); ir = rng.normal(0, 1, ir_len)*np.exp(-np.arange(ir_len)/SR*2.4); ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir**2))
mus = 0.75*mus + 0.4*fftconvolve(mus, ir)[:n]
mus *= np.clip(tt/0.8, 0, 1)*np.clip((END-tt)/2.5, 0, 1)
mus = np.tanh(mus*1.1); mus /= np.max(np.abs(mus)); mus *= 0.85
pcm = (np.clip(mus, -1, 1)*32767).astype(np.int16)
with wave.open(f"{D}/music.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.stack([pcm, pcm], 1).tobytes())
ms = int(VO*1000)
run(["ffmpeg", "-nostdin", "-y", "-i", f"{D}/vo.mp3", "-i", f"{D}/music.wav", "-filter_complex",
 f"[0:a]aresample=44100,adelay={ms}|{ms},apad,highpass=f=70,equalizer=f=120:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1:g=2,"
 f"acompressor=threshold=-18dB:ratio=3:attack=5:release=90,volume=1.5[v];[v]asplit[va][vs];"
 f"[1:a]volume=0.22[m];[m][vs]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350[md];"
 f"[md][va]amix=inputs=2:normalize=0,atrim=0:{END},alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
 "-map", "[a]", "-ar", "44100", f"{D}/mix.wav"])
run(["ffmpeg", "-nostdin", "-y", "-i", f"{D}/video.mp4", "-i", f"{D}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", f"{D}/final.mp4"])
print("cuts", [round(c, 2) for c in cuts]); print("done")
