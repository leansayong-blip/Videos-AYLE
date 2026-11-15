D="/home/claude/work/v14"; VO=0.4; END=22.5
GRADE=("colorbalance=rs=-0.02:gs=0.0:bs=0.04:rh=0.05:gh=0.01:bh=-0.03,eq=contrast=1.1:saturation=0.92:brightness=-0.02,vignette=PI/4.5,noise=alls=6:allf=t")
SCENES=[("m0","m_top",1.00,1.04,0.6,None,0,"","c"),
 ("m1","m_clock",1.00,1.15,1.3,"fade",0.25,"","c"),
 ("m2","m_night",1.00,1.12,1.7,"fade",0.3,"","c"),
 ("m3","m_bed",1.12,1.00,3.2,"fadeblack",0.4,"","b"),
 ("m4","m_shoes",1.00,1.15,2.6,"fade",0.3,"","c"),
 ("m5","m_train",1.00,1.12,3.5,"fade",0.3,"","c"),
 ("m6","m_run",1.00,1.15,2.3,"fade",0.3,"","t"),
 ("m7","m_sunrise",1.15,1.00,2.1,"fade",0.3,"","c"),
 ("m8","m_top",1.00,1.18,None,"fadewhite",0.5,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Tout le monde dort…\n*sauf *toi.",0.75,dict(size=104,y=900,maxw=960))
HOOKS=[("*Lundi. *5h *du *matin.",0.75,3.4,dict(size=78,y=560)),
       ("Tout le monde dort.",1.9,3.4,dict(size=60,y=700,stroke=6))]
CAPS=[(3.44,4.52,"Toi, tu as *le *choix."),
(5.11,6.05,"Rester sous la couette…"),
(6.63,8.54,"ou te lever pour *la *personne que tu veux devenir."),
(9.22,10.55,"Personne ne viendra te *réveiller."),
(10.87,12.29,"Personne ne *t'applaudira."),
(12.86,14.48,"Les autres attendent la *motivation."),
(15.02,16.70,"Toi, tu as la *discipline."),
(17.11,17.91,"Alors *lève-toi.")]
FINS=[("Ta semaine",18.36,None,dict(size=80,y=880,font=X)),
      ("*commence *maintenant.",18.9,None,dict(size=84,y=1000,font=X,maxw=1000))]
BPM=80; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=2.0; PAD=0.7
PROG=[[57,60,64],[53,57,60],[55,59,62],[52,55,59]]; BASS=[45,41,43,40]
