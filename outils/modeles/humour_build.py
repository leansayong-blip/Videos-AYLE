import subprocess, os, numpy as np, wave
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.signal import butter, sosfilt

D = "/home/claude/drole"
M = f"{D}/media"
W, H, FPS, T = 1080, 1920, 30, 0.35
FB = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
FX = "/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf"
VOICE_OFF = 0.5

cuts = [0, 3.9, 8.6, 10.0, 13.2, 15.9, 20.5]
END = 23.5
# (source, kind, start_in, zoom_from, zoom_to)
scenes = [
    ("smile.mp4", "v", 2.0, None, None),
    ("phone.jpg", "i", 0, 1.0, 1.15),
    ("faces.mp4", "v", 4.0, None, None),
    ("water.jpg", "i", 0, 1.12, 1.0),
    ("mug.jpg", "i", 0, 1.0, 1.25),
    ("laugh.mp4", "v", 0.5, None, None),
    ("smile.mp4", "v", 12.0, None, None),
]
transitions = ["zoomin", "slideup", "fadewhite", "smoothleft", "circleopen", "slideleft"]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); raise SystemExit(1)

GRADE = "eq=saturation=1.12:contrast=1.05"
os.makedirs(f"{D}/clips", exist_ok=True)
durs = []
for i, (src, kind, st, z0, z1) in enumerate(scenes):
    seg = (cuts[i + 1] if i + 1 < len(cuts) else END) - cuts[i]
    dur = seg + (T if i + 1 < len(scenes) else 0)
    durs.append(dur)
    out = f"{D}/clips/c{i}.mp4"
    tmp = f"{D}/clips/tmp_c{i}.mp4"
    if kind == "v":
        vf = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{GRADE},format=yuv420p"
        run(["ffmpeg", "-y", "-ss", str(st), "-i", f"{M}/{src}", "-t", f"{dur:.3f}", "-vf", vf, "-an",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", tmp])
    else:
        n = int(round(dur * FPS))
        # pre-scale bigger for smooth zoom
        vf = (f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
              f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{H}:fps={FPS},"
              f"{GRADE},format=yuv420p")
        run(["ffmpeg", "-y", "-i", f"{M}/{src}", "-vf", vf, "-frames:v", str(n),
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", tmp])
    os.replace(tmp, out)

# ---- captions as PNGs
def font(p, s): return ImageFont.truetype(p, s)
def caption_png(name, text, kind):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if kind == "tag":
        f = font(FB, 64)
        b = d.textbbox((0, 0), text, font=f)
        tw, th = b[2] - b[0], b[3] - b[1]
        x, y = (W - tw) // 2, 330
        pad = 34
        d.rounded_rectangle([x - pad, y - 22, x + tw + pad, y + th + 30], radius=40, fill=(255, 255, 255, 245))
        d.text((x - b[0], y - b[1]), text, font=f, fill=(15, 15, 15, 255))
    else:
        size, color = {"cap": (76, (255, 255, 255)), "big": (150, (255, 214, 64)), "final": (120, (255, 214, 64))}[kind]
        f = font(FB if kind != "cap" else FX, size)
        # wrap
        words, lines, cur = text.split(), [], ""
        for w_ in words:
            t = (cur + " " + w_).strip()
            if d.textlength(t, font=f) > W - 160 and cur:
                lines.append(cur); cur = w_
            else:
                cur = t
        lines.append(cur)
        lh = int(size * 1.15)
        y0 = (1180 if kind == "cap" else 820) - (len(lines) * lh) // 2
        shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shadow)
        for k, ln in enumerate(lines):
            tw = d.textlength(ln, font=f)
            x, y = (W - tw) / 2, y0 + k * lh
            sd.text((x, y + 6), ln, font=f, fill=(0, 0, 0, 170))
            d.text((x, y), ln, font=f, fill=color + (255,), stroke_width=7, stroke_fill=(0, 0, 0, 255))
        img = Image.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(8)), img)
    img.save(f"{D}/clips/{name}.png")

caps = [
    ("t1", "MOI À 18H", "tag", 0.25, 3.9),
    ("c1", "« Ce soir, je me couche tôt. »", "cap", 2.1, 3.9),
    ("t2", "MOI À 2H DU MATIN", "tag", 4.05, 8.6),
    ("c2", "…à regarder comment on fabrique du fromage en Norvège", "cap", 5.9, 8.6),
    ("t3", "LUNDI", "tag", 10.15, 13.2),
    ("c3", "« Cette semaine, je bois 2 litres d'eau. »", "cap", 10.4, 13.2),
    ("t4", "MARDI", "tag", 13.35, 15.9),
    ("c4", "3 CAFÉS.", "big", 14.45, 15.9),
    ("c5", "Bref… t'as pas besoin d'être parfaite.", "cap", 16.1, 18.3),
    ("c6", "JUSTE D'ÊTRE TOI.", "final", 18.3, END),
]
for name, text, kind, a, b in caps:
    caption_png(name, text, kind)

# ---- assemble video with xfade + caption overlays
inputs, fc = [], []
for i in range(len(scenes)):
    inputs += ["-i", f"{D}/clips/c{i}.mp4"]
acc, prev = durs[0], "[0:v]"
for i in range(1, len(scenes)):
    off = acc - T
    lab = f"[x{i}]"
    fc.append(f"{prev}[{i}:v]xfade=transition={transitions[i-1]}:duration={T}:offset={off:.3f}{lab}")
    prev = lab
    acc = acc + durs[i] - T
base = len(scenes)
for j, (name, text, kind, a, b) in enumerate(caps):
    inputs += ["-loop", "1", "-t", f"{END:.2f}", "-i", f"{D}/clips/{name}.png"]
    k = base + j
    fc.append(f"[{k}:v]format=rgba,fade=in:st={a}:d=0.12:alpha=1,fade=out:st={b-0.12:.2f}:d=0.12:alpha=1[p{j}]")
    nxt = f"[o{j}]"
    fc.append(f"{prev}[p{j}]overlay=0:0:enable='between(t,{a},{b})'{nxt}")
    prev = nxt
fc.append(f"{prev}format=yuv420p[vout]")
tmp = f"{D}/tmp_video.mp4"
run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[vout]", "-t", f"{END}",
     "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-maxrate", "10M", "-bufsize", "20M", tmp])
os.replace(tmp, f"{D}/video.mp4")

# ---- music (light playful pizzicato) + whooshes
SR = 44100
n = int(END * SR); t = np.arange(n) / SR
mus = np.zeros(n)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)
bpm = 112; beat = 60 / bpm
prog = [(60, [64, 67, 72, 67]), (57, [60, 64, 69, 64]), (53, [57, 60, 65, 60]), (55, [59, 62, 67, 62])]
rng = np.random.default_rng(2)
for b in range(int(END / (beat * 4)) + 1):
    root, arp = prog[b % 4]
    for s in range(8):
        st = (b * 4 + s * 0.5) * beat
        s0 = int(st * SR); L = int(0.35 * SR)
        if s0 + L > n: break
        tt = np.arange(L) / SR
        f = hz(arp[s % 4] + 12)
        mus[s0:s0+L] += 0.18 * np.sin(2*np.pi*f*tt) * np.exp(-tt*14)  # pluck
        if s % 2 == 0:
            fb = hz(root - 12)
            mus[s0:s0+L] += 0.22 * np.sin(2*np.pi*fb*tt) * np.exp(-tt*6)
        if s % 4 == 2:  # finger snap
            sn = rng.normal(0, 1, int(0.05*SR)) * np.exp(-np.arange(int(0.05*SR))/SR*80)
            sn = sosfilt(butter(2, [2000, 8000], btype='band', fs=SR, output='sos'), sn)
            mus[s0:s0+len(sn)] += 0.25 * sn
mus = np.tanh(mus * 1.5)
fi = int(0.4*SR); mus[:fi] *= np.linspace(0, 1, fi)
fo = int(1.5*SR); mus[-fo:] *= np.linspace(1, 0, fo)
sfx = np.zeros(n)
for c in cuts[1:]:
    s0 = int((c - 0.15) * SR); L = int(0.45 * SR)
    if s0 + L > n: continue
    tt = np.arange(L) / SR
    nz = rng.normal(0, 1, L)
    env = np.sin(np.pi * tt / tt[-1]) ** 2
    lo = sosfilt(butter(2, [600, 5000], btype='band', fs=SR, output='sos'), nz)
    sfx[s0:s0+L] += lo * env * 0.12
def wav(path, x):
    x = np.clip(x, -1, 1)
    pcm = (x * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.stack([pcm, pcm], 1).tobytes())
wav(f"{D}/music.wav", mus / np.max(np.abs(mus)) * 0.8)
wav(f"{D}/sfx.wav", sfx)

ms = int(VOICE_OFF * 1000)
run(["ffmpeg", "-y", "-i", f"{M}/voix.mp3", "-i", f"{D}/music.wav", "-i", f"{D}/sfx.wav", "-filter_complex",
     f"[0:a]aresample=44100,adelay={ms}|{ms},apad,highpass=f=80,acompressor=threshold=-18dB:ratio=3:attack=5:release=80,volume=1.4[v];"
     f"[v]asplit[va][vs];"
     f"[1:a]volume=0.22[m];[m][vs]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[md];"
     f"[2:a]volume=1.0[s];"
     f"[md][va][s]amix=inputs=3:normalize=0,atrim=0:{END},alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
     "-map", "[a]", "-ar", "44100", f"{D}/mix.wav"])
run(["ffmpeg", "-y", "-i", f"{D}/video.mp4", "-i", f"{D}/mix.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy",
     "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", f"{D}/test_humour_femmes.mp4"])
print("done")
