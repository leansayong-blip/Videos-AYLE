import subprocess, os, numpy as np, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.signal import butter, sosfilt, fftconvolve

D = "/home/claude/pierre"; M = f"{D}/media"; C = f"{D}/clips"
os.makedirs(C, exist_ok=True)
W, H, FPS = 1080, 1920, 30
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
LORA_I = "/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf"
VO = 1.0          # voice offset
END = 33.5
GRADE = ("colorbalance=rs=0.04:gs=0.0:bs=-0.05:rh=0.07:gh=0.02:bh=-0.05,"
         "eq=contrast=1.1:saturation=0.9:brightness=-0.02,vignette=PI/4.5,noise=alls=7:allf=t")

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2500:]); raise SystemExit(1)

# scene list: (name, source, kind, start_in, zoom_from, zoom_to, segment_seconds, transition_in, trans_dur)
S = [
    ("s0", "orage.jpg",   "i", 0, 1.00, 1.10, 2.4, None, 0),
    ("s1", "vague.mp4",   "v", 1.0, None, None, 3.2, "fadeblack", 0.4),
    ("s2", "bateaux.jpg", "i", 0, 1.00, 1.15, 3.8, "fade", 0.5),
    ("s3", "ecume.mp4",   "v", 6.0, None, None, 3.8, "fade", 0.5),
    ("s4", "pieds.jpg",   "i", 0, 1.00, 1.18, 3.8, "fadewhite", 0.4),
    ("s5", "rochers.mp4", "v", 4.0, None, None, 3.1, "fade", 0.25),
    ("s6", "main.jpg",    "i", 0, 1.15, 1.00, 3.3, "fadeblack", 0.6),
    ("s7", "vague.mp4",   "v", 9.0, None, None, 4.2, "fade", 0.5),
    ("s8", "aube.jpg",    "i", 0, 1.00, 1.12, None, "fadewhite", 0.8),
]
# compute cut times
cuts, t = [], 0.0
for s in S:
    cuts.append(t)
    if s[6]: t += s[6]
seg_last = END - cuts[-1]

durs = []
for i, (nm, src, kind, st, z0, z1, seg, tr, td) in enumerate(S):
    seg = seg if seg else seg_last
    nxt_td = S[i + 1][8] if i + 1 < len(S) else 0
    dur = seg + nxt_td
    durs.append(dur)
    out, tmp = f"{C}/{nm}.mp4", f"{C}/tmp_{nm}.mp4"
    if os.path.exists(out): continue
    if kind == "v":
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setpts=PTS*1.0,{GRADE},format=yuv420p"
        run(["ffmpeg", "-y", "-ss", str(st), "-i", f"{M}/{src}", "-t", f"{dur:.3f}", "-vf", vf, "-an",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", tmp])
    else:
        n = int(round(dur * FPS))
        vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
              f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
              f"{GRADE},format=yuv420p")
        run(["ffmpeg", "-y", "-i", f"{M}/{src}", "-vf", vf, "-frames:v", str(n),
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", tmp])
    os.replace(tmp, out)

# ---------- text overlays
def F(path, size, wght=None):
    f = ImageFont.truetype(path, size)
    if wght:
        try: f.set_variation_by_axes([wght])
        except Exception: pass
    return f

def text_png(name, lines, size, y_center, color=(255, 255, 255), path=LORA, wght=600, spacing=1.18, tracking=0):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = F(path, size, wght)
    lh = int(size * spacing)
    y0 = y_center - (len(lines) * lh) // 2
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    for k, ln in enumerate(lines):
        if tracking:
            widths = [d.textlength(ch, font=f) + tracking for ch in ln]
            x = (W - sum(widths) + tracking) / 2
            for ch, wch in zip(ln, widths):
                gd.text((x, y0 + k * lh + 4), ch, font=f, fill=(0, 0, 0, 200))
                d.text((x, y0 + k * lh), ch, font=f, fill=color + (255,))
                x += wch
        else:
            tw = d.textlength(ln, font=f); x = (W - tw) / 2
            gd.text((x, y0 + k * lh + 4), ln, font=f, fill=(0, 0, 0, 210))
            d.text((x, y0 + k * lh), ln, font=f, fill=color + (255,))
    img = Image.alpha_composite(glow.filter(ImageFilter.GaussianBlur(10)), img)
    img.save(f"{C}/{name}.png")

def wrap(text, size, path=LORA, wght=600, maxw=W - 180):
    f = F(path, size, wght); d = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    out, cur = [], ""
    for w_ in text.split():
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) > maxw and cur: out.append(cur); cur = w_
        else: cur = t
    out.append(cur); return out

GOLD = (236, 200, 120)
sub = lambda txt: wrap(txt, 62)
caps = []
def add(name, lines, size, y, a, b, **kw):
    text_png(name, lines, size, y, **kw); caps.append((name, a, b))

add("title", ["PIERRE", "MARCHE SUR L'EAU"], 82, 900, 0.3, 2.35, color=GOLD, wght=700, tracking=8)
add("ref1", ["MATTHIEU 14"], 40, 1080, 0.6, 2.35, color=(230, 230, 230), wght=500, tracking=8)
V = lambda x: x + VO
add("sub0", sub("Une tempête. Des vagues immenses."), 62, 1420, 2.47, V(4.6))
add("sub1", sub("Et au milieu de l'eau… Jésus qui marche vers eux."), 62, 1420, V(4.97), V(8.4))
add("sub2", sub("Pierre lui dit :"), 62, 1420, V(8.58), V(9.62))
add("q1", wrap("« Seigneur, ordonne que j'aille vers toi. »", 74, LORA_I, 500), 74, 950, V(9.77), V(12.3), path=LORA_I, wght=500)
add("sub3", sub("Alors il descend de la barque."), 62, 1420, V(12.46), V(14.15))
add("b1", ["Et il marche", "sur l'eau."], 98, 980, V(14.28), V(15.9), color=GOLD, wght=700)
add("sub4", sub("Mais il regarde le vent…"), 62, 1420, V(16.0), V(17.55))
add("b2", ["et il commence", "à couler."], 98, 980, V(17.65), V(19.25), wght=700)
add("verse", wrap("« Homme de peu de foi, pourquoi as-tu douté ? »", 74, LORA_I, 500), 74, 920, V(19.41), V(22.4), path=LORA_I, wght=500)
add("verseref", ["Matthieu 14:31"], 40, 1170, V(19.9), V(22.4), color=GOLD, wght=500, tracking=4)
add("sub5", sub("Pierre n'a pas coulé à cause de la tempête."), 62, 1420, V(22.58), V(24.75))
add("sub6", sub("Il a coulé quand il a quitté Jésus des yeux."), 62, 1420, V(24.89), V(27.2))
add("fin1", ["Garde les yeux"], 92, 900, V(27.33), END, wght=700)
add("fin2", ["fixés sur lui."], 104, 1040, V(28.1), END, color=GOLD, wght=700)

# ---------- assemble
inputs, fc = [], []
for s in S: inputs += ["-i", f"{C}/{s[0]}.mp4"]
acc, prev = durs[0], "[0:v]"
for i in range(1, len(S)):
    tr, td = S[i][7], S[i][8]
    fc.append(f"{prev}[{i}:v]xfade=transition={tr}:duration={td}:offset={acc - td:.3f}[x{i}]")
    prev = f"[x{i}]"; acc += durs[i] - td
base = len(S)
for j, (nm, a, b) in enumerate(caps):
    inputs += ["-loop", "1", "-t", f"{END:.2f}", "-i", f"{C}/{nm}.png"]
    fi = 0.35 if nm in ("title", "verse", "q1", "fin1", "fin2", "ref1", "verseref") else 0.18
    fc.append(f"[{base+j}:v]format=rgba,fade=in:st={a:.2f}:d={fi}:alpha=1,fade=out:st={max(b-0.2, a+fi):.2f}:d=0.2:alpha=1[p{j}]")
    fc.append(f"{prev}[p{j}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[o{j}]")
    prev = f"[o{j}]"
fc.append(f"{prev}fade=in:st=0:d=0.6,fade=out:st={END-0.9}:d=0.9,format=yuv420p[vout]")
tmp = f"{D}/tmp_video.mp4"
run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-t", f"{END}",
     "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-maxrate", "12M", "-bufsize", "24M", tmp])
os.replace(tmp, f"{D}/video.mp4")

# ---------- cinematic score (original) + sfx
SR = 44100; n = int(END * SR); tt = np.arange(n) / SR
rng = np.random.default_rng(11)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
lp = lambda x, f: sosfilt(butter(2, f, fs=SR, output='sos'), x)
bp = lambda x, a, b: sosfilt(butter(2, [a, b], btype='band', fs=SR, output='sos'), x)
def saw(f, t): return 2 * ((t * f) % 1) - 1
# intensity curve: soft start, builds at 13.6 (stones), lifts at verse, climax at 27.9
def env_curve(t):
    pts = [(0, .5), (5.6, .55), (13.2, .4), (15.3, .7), (17.0, .85), (20.1, .35), (23.4, .5), (27.6, .75), (31, .7), (END, 0)]
    xs, ys = zip(*pts); return np.interp(t, xs, ys)
I = env_curve(tt)
mus = np.zeros(n)
# low drone
for m in (38, 45):
    mus += 0.16 * np.sin(2 * np.pi * hz(m) * tt) * (0.8 + 0.2 * np.sin(2 * np.pi * 0.07 * tt))
# string pad chords Dm - Bb - F - C (each 4 s), detuned saws, lowpassed
chords = [[50, 53, 57, 62], [46, 50, 53, 58], [53, 57, 60, 65], [48, 52, 55, 60]]
pad = np.zeros(n); cl = 4.0
for c in range(int(END / cl) + 1):
    s0, s1 = int(c * cl * SR), min(n, int((c + 1) * cl * SR + 1.5 * SR))
    if s0 >= n: break
    t_ = tt[s0:s1] - c * cl
    e = np.clip(t_ / 1.2, 0, 1) * np.clip((cl + 1.5 - t_) / 1.5, 0, 1)
    for m in chords[c % 4]:
        for det in (-0.12, 0.0, 0.13):
            pad[s0:s1] += 0.03 * saw(hz(m) * (1 + det / 100), tt[s0:s1]) * e
mus += lp(pad, 1800) * (0.5 + 0.8 * I)
# choir "aah" (formant-filtered saws) entering at verse and climax
ch = np.zeros(n)
for m in (62, 65, 69):
    ch += saw(hz(m) * (1 + 0.003 * np.sin(2 * np.pi * 5 * tt)), tt)
choir = 0.6 * bp(ch, 600, 900) + 0.35 * bp(ch, 1000, 1400) + 0.15 * bp(ch, 2400, 2900)
cmask = np.clip((tt - V(19.2)) / 1.2, 0, 1) * np.clip((V(22.6) - tt) / 1.2, 0, 1) + np.clip((tt - 27.6) / 1.5, 0, 1)
mus += 0.05 * choir * cmask
# taiko / impact hits
def hit(at, amp=1.0, f0=55):
    s0 = int(at * SR); L = int(1.8 * SR); L = min(L, n - s0)
    if L <= 0: return
    t_ = np.arange(L) / SR
    fr = f0 + 70 * np.exp(-t_ * 25)
    body = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t_ * 3.2)
    skin = bp(rng.normal(0, 1, L), 150, 900) * np.exp(-t_ * 18) * 0.5
    mus[s0:s0 + L] += amp * 0.55 * (body + skin)
for at, a in [(0.2, 1.0), (2.4, .7), (V(14.28), .9), (V(17.65), 1.0), (V(19.41), .7), (V(27.33), .9)]:
    hit(at, a)
beat = 60 / 70
for k in np.arange(2.4, 9.4, beat / 2):
    hit(k, 0.14, 80)
for k in np.arange(V(16.0), V(19.2), beat / 4):
    hit(k, 0.12, 90)
# storm ambience: wind + waves under the first two thirds, fading before the calm ending
wind = bp(rng.normal(0, 1, n), 200, 1200) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.13 * tt))
wmask = np.clip((V(20.0) - tt) / 2.0, 0, 1) * np.clip(tt / 0.5, 0, 1)
mus += 0.10 * wind * wmask
# thunder at the start
L_ = int(3 * SR); t3 = np.arange(L_) / SR
thunder = lp(rng.normal(0, 1, L_), 220) * np.exp(-t3 * 1.4) * 1.6
mus[int(0.1 * SR):int(0.1 * SR) + L_] += thunder
# calm ending: major chord swell (D major) from 27.6
calm = np.zeros(n)
for m in (50, 54, 57, 62, 66):
    calm += np.sin(2 * np.pi * hz(m) * tt) + 0.3 * np.sin(4 * np.pi * hz(m) * tt)
mus += 0.05 * calm * np.clip((tt - 27.4) / 1.5, 0, 1)
# reverb (synthetic hall)
ir_len = int(2.8 * SR)
ir = rng.normal(0, 1, ir_len) * np.exp(-np.arange(ir_len) / SR * 2.2)
ir = lp(ir, 5000); ir /= np.sqrt(np.sum(ir ** 2))
wet = fftconvolve(mus, ir)[:n]
mus = 0.75 * mus + 0.45 * wet
mus *= np.clip(tt / 1.0, 0, 1) * np.clip((END - tt) / 2.5, 0, 1)
mus = np.tanh(mus * 1.2); mus /= np.max(np.abs(mus)); mus *= 0.85

# sfx: whooshes at transitions, riser into verse
sfx = np.zeros(n)
def whoosh(at, L=0.6, amp=0.10):
    s0 = int((at - L / 2) * SR); Ln = int(L * SR)
    if s0 < 0 or s0 + Ln > n: return
    t_ = np.arange(Ln) / SR; e = np.sin(np.pi * t_ / t_[-1]) ** 2
    sfx[s0:s0 + Ln] += bp(rng.normal(0, 1, Ln), 400, 4000) * e * amp
s0, s1 = int(V(18.2) * SR), int(V(19.4) * SR)
t_ = np.arange(s1 - s0) / SR
riser = bp(rng.normal(0, 1, s1 - s0), 800, 6000) * (t_ / t_[-1]) ** 2 * 0.12
pass  # riser removed

def wav(path, x):
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.stack([pcm, pcm], 1).tobytes())
wav(f"{D}/music.wav", mus); wav(f"{D}/sfx.wav", sfx)

ms = int(VO * 1000)
run(["ffmpeg", "-y", "-i", f"{M}/voix.mp3", "-i", f"{D}/music.wav", "-i", f"{D}/sfx.wav", "-filter_complex",
     f"[0:a]aresample=44100,adelay={ms}|{ms},apad,highpass=f=70,equalizer=f=120:t=q:w=1:g=2.5,equalizer=f=3200:t=q:w=1:g=2,"
     f"acompressor=threshold=-18dB:ratio=3:attack=5:release=90,aecho=0.85:0.5:55|110:0.12|0.07,volume=1.5[v];"
     f"[v]asplit[va][vs];"
     f"[1:a]volume=0.20[m];[m][vs]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350[md];"
     f"[md][va][2:a]amix=inputs=3:normalize=0,atrim=0:{END},alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
     "-map", "[a]", "-ar", "44100", f"{D}/mix.wav"])
run(["ffmpeg", "-y", "-i", f"{D}/video.mp4", "-i", f"{D}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy",
     "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", f"{D}/pierre_marche_sur_l_eau.mp4"])
print("cuts", [round(c, 2) for c in cuts]); print("done")
