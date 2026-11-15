D="/home/claude/work/v17"; VO=0.4; END=22.6
GRADE=("colorbalance=rs=0.04:gs=0.01:bs=-0.03:rh=0.03:bh=-0.03,eq=contrast=1.1:saturation=0.9:brightness=-0.01,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("d0","d_lion",1.00,1.12,2.6,None,0,"","c"),
 ("d1","d_pray",1.00,1.12,3.5,"fade",0.3,"","c"),
 ("d2","d_hands",1.12,1.00,2.4,"fade",0.3,"","c"),
 ("d3","d_pit",1.00,1.12,2.2,"fadeblack",0.4,"","c"),
 ("d4","d_cave",1.00,1.15,1.8,"fadewhite",0.4,"","c"),
 ("d5","d_lion2",1.12,1.00,3.0,"fade",0.3,"","c"),
 ("d6","d_open",1.00,1.15,None,"fade",0.4,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Jeté aux *lions…\npour avoir *prié.",0.75,dict(size=104,y=900,maxw=960))
HOOKS=[("Jeté aux *lions…",0.75,2.9,dict(size=84,y=560)),
       ("parce qu'il *priait.",2.0,3.4,dict(size=64,y=690,stroke=6)),
       ("Daniel 6:22",12.6,15.4,dict(size=46,y=1560,stroke=5))]
CAPS=[(3.14,4.25,"Daniel connaissait *la *loi."),
(4.78,5.69,"Il a prié *quand *même."),
(6.27,8.01,"Toute la nuit, le roi *n'a *pas *dormi."),
(8.48,10.24,"Au matin, il *court à la fosse."),
(10.71,11.58,"Daniel est *vivant."),
(12.09,14.94,"« Mon Dieu a envoyé son ange et fermé la *gueule *des *lions. »"),
(15.70,16.99,"Ta foi peut te *coûter *cher.")]
FINS=[("Mais Dieu n'abandonne",17.45,None,dict(size=74,y=880,font=X)),
      ("*jamais *les *siens.",18.3,None,dict(size=92,y=1000,font=X,maxw=1000))]
BPM=70; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=2.0; PAD=0.8
PROG=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]; BASS=[45,41,36,43]
