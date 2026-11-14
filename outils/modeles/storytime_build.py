import subprocess, os, numpy as np, wave, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.signal import butter, sosfilt, fftconvolve
D="/home/claude/story"; M=f"{D}/src"; C=f"{D}/clips"
W,H,FPS=1080,1920,30
VO=0.4; END=59.3
BOLD="/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
XB="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
GRADE=("colorbalance=rs=-0.03:gs=0.0:bs=0.05:rh=0.06:gh=0.01:bh=-0.04,"
       "eq=contrast=1.08:saturation=0.95:brightness=-0.02,vignette=PI/4.5,noise=alls=6:allf=t")
DARK=",eq=saturation=0.45:brightness=-0.07:contrast=1.05"
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: print(r.stderr[-2500:]); raise SystemExit(1)
# (name, src, kind, start_in, z0, z1, seg, trans, td, extra)
S=[("s01","drive.jpg","i",0,1.00,1.12,4.0,None,0,""),
   ("s02","neon.jpg","i",0,1.12,1.00,3.6,"fade",0.4,""),
   ("s03","inside.jpg","i",0,1.00,1.10,2.5,"fade",0.35,""),
   ("s04","coins.jpg","i",0,1.00,1.14,3.3,"fade",0.4,""),
   ("s05","coin.jpg","i",0,1.05,1.25,5.0,"fade",0.4,""),
   ("s06","friends.jpg","i",0,1.00,1.12,4.4,"fade",0.4,""),
   ("s07","drive.jpg","i",0,1.25,1.42,5.6,"fade",0.4,""),
   ("s08","coin.jpg","i",0,1.35,1.55,3.3,"fade",0.4,""),
   ("s09","coins.jpg","i",0,1.18,1.05,3.7,"fade",0.4,",colorbalance=rm=0.04:bm=-0.03"),
   ("s10","road.mp4","v",1.0,None,None,3.2,"fadeblack",0.5,",gblur=sigma=28,eq=brightness=-0.03:saturation=1.3"),
   ("s11","police.mp4","v",0.0,None,None,7.8,"fade",0.4,",eq=saturation=0.8"),
   ("s12","neon.jpg","i",0,1.00,1.15,4.5,"fadeblack",0.6,DARK),
   ("s13","coin.jpg","i",0,1.6,1.3,3.7,"fade",0.5,DARK),
   ("s14","street.jpg","L",0,1.55,1.65,None,"fade",0.8,"")]
cuts,t=[],0.0
for s in S:
    cuts.append(t)
    if s[6]: t+=s[6]
durs=[]
for i,(nm,src,kind,st,z0,z1,seg,tr,td,ex) in enumerate(S):
    seg=seg if seg else END-cuts[-1]
    dur=seg+(S[i+1][8] if i+1<len(S) else 0); durs.append(dur)
    out,tmp=f"{C}/{nm}.mp4",f"{C}/tmp_{nm}.mp4"
    if os.path.exists(out): continue
    if kind=="v":
        vf=f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},{GRADE}{ex},format=yuv420p"
        run(["ffmpeg","-nostdin","-y","-ss",str(st),"-i",f"{M}/{src}","-t",f"{dur:.3f}","-vf",vf,"-an","-c:v","libx264","-preset","veryfast","-crf","19",tmp])
    else:
        n=int(round(dur*FPS))
        xe,ye=("0","ih*0.08") if kind=="L" else ("iw/2-(iw/zoom/2)","ih/2-(ih/zoom/2)")
        vf=(f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
            f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='{xe}':y='{ye}':d={n}:s={W}x{H}:fps={FPS},{GRADE}{ex},format=yuv420p")
        run(["ffmpeg","-nostdin","-y","-i",f"{M}/{src}","-vf",vf,"-frames:v",str(n),"-c:v","libx264","-preset","veryfast","-crf","19",tmp])
    os.replace(tmp,out)
# ---------- captions
YEL=(255,214,64)
def cap_png(name,text,size=66,y=1360,font=BOLD,maxw=900,stroke=7):
    f=ImageFont.truetype(font,size); img=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(img)
    toks=text.split(); lines=[];cur=[]
    clean=lambda w:w.replace('*','').replace('~',' ')
    for w in toks:
        trial=" ".join(clean(x) for x in cur+[w])
        if d.textlength(trial,font=f)>maxw and cur: lines.append(cur);cur=[w]
        else: cur.append(w)
    lines.append(cur); lh=int(size*1.2); y0=y-len(lines)*lh//2
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for k,ln in enumerate(lines):
        words=[clean(w) for w in ln]; full=" ".join(words); x=(W-d.textlength(full,font=f)-stroke*1.1*(len(words)-1))/2; yy=y0+k*lh
        for w,raw in zip(words,ln):
            col=YEL if raw.startswith('*') else (255,255,255)
            sd.text((x,yy+6),w,font=f,fill=(0,0,0,170))
            d.text((x,yy),w,font=f,fill=col+(255,),stroke_width=stroke,stroke_fill=(0,0,0,255))
            x+=d.textlength(w,font=f)+d.textlength(" ",font=f)+stroke*1.1
    img=Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(9)),img); img.save(f"{C}/{name}.png")
caps=[]
def add(name,text,a,b,**kw): cap_png(name,text,**kw); caps.append((name,a,b))
V=lambda x:x+VO
add("hook1","Il a donné *10~centimes à une inconnue…",0.15,3.9,size=74,y=560,font=XB)
add("hook2","…et ça lui a peut-être *sauvé *la *vie.",0.9,3.9,size=54,y=730,font=XB,stroke=6,maxw=1000)
P=[(0.0,1.55,"Il avait 18 ans."),(1.63,3.46,"Un soir, il sort avec ses potes."),
(3.84,6.84,"Direction : le spot de desserts le plus connu de la ville."),(7.42,9.33,"Avant, ils s'arrêtent dans une supérette."),
(9.91,12.55,"À la caisse, une femme sans-abri compte ses pièces…"),(13.27,14.61,"Il lui manque *10~centimes."),
(15.21,17.47,"Juste *10~centimes… pour un bonbon."),(18.28,20.12,"Il fouille son portefeuille. Rien."),
(20.85,22.04,"Alors il retourne à la voiture."),(22.63,24.57,"La boîte à gants, sous les sièges…"),
(25.22,26.30,"Ça prend *plusieurs *minutes."),(26.70,27.57,"Ses potes s'impatientent."),
(28.19,30.93,"Enfin, il trouve une pièce. *10~centimes."),(31.54,33.18,"Il la lui donne. Elle sourit."),
(33.88,34.48,"Et ils repartent."),(35.28,37.76,"Mais en approchant… *tout *est *bloqué."),
(38.37,40.18,"Des voitures de police passent à toute vitesse."),(40.54,42.64,"Une bagarre devant la boutique vient de dégénérer."),
(43.04,44.53,"*Des *coups *de *feu. Des blessés…"),(44.82,45.62,"…dans la file d'attente."),
(46.21,48.02,"Exactement là où ils auraient dû être…"),(48.49,49.58,"…s'ils étaient arrivés à l'heure."),
(50.83,53.52,"*10~centimes. *Quelques *minutes *de *retard.")]
for k,(a,b,txt) in enumerate(P):
    nxt=P[k+1][0] if k+1<len(P) else b+0.3
    add(f"c{k:02d}",txt,V(a)-0.05,min(V(b)+0.35,V(nxt)-0.05))
add("fin1","Tu ne sais jamais",V(54.3),END,size=82,y=860,font=XB)
add("fin2","ce qu'un *petit *geste peut changer.",V(55.0),END,size=70,y=1000,font=XB)
# ---------- assemble
inputs,fc=[],[]
for s in S: inputs+=["-i",f"{C}/{s[0]}.mp4"]
acc,prev=durs[0],"[0:v]"
for i in range(1,len(S)):
    tr,td=S[i][7],S[i][8]
    fc.append(f"{prev}[{i}:v]xfade=transition={tr}:duration={td}:offset={acc-td:.3f}[x{i}]"); prev=f"[x{i}]"; acc+=durs[i]-td
base=len(S)
for j,(nm,a,b) in enumerate(caps):
    inputs+=["-loop","1","-t",f"{END:.2f}","-i",f"{C}/{nm}.png"]
    fi=0.3 if nm.startswith(("hook","fin")) else 0.12
    fc.append(f"[{base+j}:v]format=rgba,fade=in:st={a:.2f}:d={fi}:alpha=1,fade=out:st={max(b-0.15,a+fi):.2f}:d=0.15:alpha=1[p{j}]")
    fc.append(f"{prev}[p{j}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[o{j}]"); prev=f"[o{j}]"
li=base+len(caps); inputs+=["-loop","1","-t",f"{END:.2f}","-i","/home/claude/logo/ayleco_overlay.png"]
fc.append(f"[{li}:v]format=rgba,fade=in:st=0.3:d=0.6:alpha=1[lg]"); fc.append(f"{prev}[lg]overlay=36:120[ol]")
fc.append(f"[ol]fade=in:st=0:d=0.5,fade=out:st={END-1.0}:d=1.0,format=yuv420p[vout]")
tmp=f"{D}/tmp_video.mp4"
run(["ffmpeg","-nostdin","-y",*inputs,"-filter_complex",";".join(fc),"-map","[vout]","-t",f"{END}","-c:v","libx264","-preset","veryfast","-crf","21","-maxrate","10M","-bufsize","20M",tmp])
os.replace(tmp,f"{D}/video.mp4")
# ---------- score
SR=44100; n=int(END*SR); tt=np.arange(n)/SR; rng=np.random.default_rng(5)
hz=lambda m:440*2**((m-69)/12)
lp=lambda x,f:sosfilt(butter(2,f,fs=SR,output='sos'),x)
bp=lambda x,a,b:sosfilt(butter(2,[a,b],btype='band',fs=SR,output='sos'),x)
saw=lambda f,t:2*((t*f)%1)-1
mus=np.zeros(n)
T1,T2=V(35.0),V(50.4)   # tension start, resolve
def env(a,b,fi=1.5,fo=1.5): return np.clip((tt-a)/fi,0,1)*np.clip((b-tt)/fo,0,1)
# piano-like plucks, Am F C G, 75 bpm, eighth arpeggios
beat=60/75; prog=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]; bass=[45,41,48,43]
def pluck(at,m,amp):
    s0=int(at*SR); L=min(int(2.2*SR),n-s0)
    if L<=0: return
    t_=np.arange(L)/SR; f=hz(m)
    x=(np.sin(2*np.pi*f*t_)+0.35*np.sin(4*np.pi*f*t_)+0.12*np.sin(6*np.pi*f*t_))*np.exp(-t_*2.6)*(1-np.exp(-t_*300))
    mus[s0:s0+L]+=amp*x
def section(a,b,amp):
    k=0; t0=a
    while t0<b:
        bar=int(k//8)%4; ch=prog[bar]; pat=[0,1,2,1,2,1,0,2]
        if k%8==0: pluck(t0,bass[bar],amp*1.1)
        pluck(t0,ch[pat[k%8]]+12,amp*0.55); t0+=beat/2; k+=1
section(0.2,T1-0.6,0.16)
section(T2+0.2,END-1.5,0.14)
# soft pad all along (warmer at end)
pad=np.zeros(n)
for i,(c) in enumerate(prog*20):
    a=0.2+i*4*beat
    if a>END: break
    s0,s1=int(a*SR),min(n,int((a+4*beat+1.2)*SR)); t_=tt[s0:s1]-a
    e=np.clip(t_/0.8,0,1)*np.clip((4*beat+1.2-t_)/1.2,0,1)
    for m in c:
        for det in (-0.1,0.1): pad[s0:s1]+=0.02*saw(hz(m)*(1+det/100),tt[s0:s1])*e
pad=lp(pad,1400); mus+=pad*(0.5*env(0,T1,2,1.5)+0.9*env(T2,END,2,2))
# tension: low drone + heartbeat pulse + distant siren
dr=np.zeros(n)
for m in (33,40): dr+=np.sin(2*np.pi*hz(m)*tt)
dr+=0.4*lp(saw(hz(45)*(1+0.002*np.sin(2*np.pi*0.2*tt)),tt),500)
mus+=0.22*dr*env(T1,T2+0.5,1.2,2.0)
def thump(at,amp):
    s0=int(at*SR); L=min(int(0.5*SR),n-s0)
    if L<=0: return
    t_=np.arange(L)/SR; fr=48+40*np.exp(-t_*30); mus[s0:s0+L]+=amp*np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-t_*9)
hb=T1+0.3
while hb<T2:
    a=0.35+0.35*min(1,(hb-T1)/6); thump(hb,a); thump(hb+0.28,a*0.7); hb+=0.95
sir=np.zeros(n); s0,s1=int(V(38.0)*SR),int(V(45.5)*SR); t_=tt[s0:s1]-V(38.0)
fsw=700+250*np.sign(np.sin(2*np.pi*0.7*t_)); ph=2*np.pi*np.cumsum(fsw)/SR
sir[s0:s1]=lp(np.sin(ph),1500)*np.clip(t_/2,0,1)*np.clip((V(45.5)-V(38.0)-t_)/2,0,1)
mus+=0.05*sir
ir_len=int(2.6*SR); ir=rng.normal(0,1,ir_len)*np.exp(-np.arange(ir_len)/SR*2.4); ir=lp(ir,5000); ir/=np.sqrt(np.sum(ir**2))
mus=0.75*mus+0.4*fftconvolve(mus,ir)[:n]
mus*=np.clip(tt/0.8,0,1)*np.clip((END-tt)/2.5,0,1)
mus=np.tanh(mus*1.1); mus/=np.max(np.abs(mus)); mus*=0.85
pcm=(np.clip(mus,-1,1)*32767).astype(np.int16)
with wave.open(f"{D}/music.wav","wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.stack([pcm,pcm],1).tobytes())
ms=int(VO*1000)
run(["ffmpeg","-nostdin","-y","-i",f"{D}/vo.mp3","-i",f"{D}/music.wav","-filter_complex",
 f"[0:a]aresample=44100,adelay={ms}|{ms},apad,highpass=f=70,equalizer=f=120:t=q:w=1:g=2,equalizer=f=3200:t=q:w=1:g=2,"
 f"acompressor=threshold=-18dB:ratio=3:attack=5:release=90,aecho=0.85:0.5:45:0.08,volume=1.5[v];[v]asplit[va][vs];"
 f"[1:a]volume=0.22[m];[m][vs]sidechaincompress=threshold=0.03:ratio=5:attack=25:release=350[md];"
 f"[md][va]amix=inputs=2:normalize=0,atrim=0:{END},alimiter=limit=0.95,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
 "-map","[a]","-ar","44100",f"{D}/mix.wav"])
run(["ffmpeg","-nostdin","-y","-i",f"{D}/video.mp4","-i",f"{D}/mix.wav","-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",f"{D}/storytime_10_centimes.mp4"])
print("cuts",[round(c,2) for c in cuts]); print("done")
