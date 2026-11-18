D="/home/claude/work/v27"; VO=0.4; END=22.4
GRADE=("colorbalance=rs=0.02:gs=0.0:bs=-0.01:rh=0.05:gh=0.02:bh=-0.03,eq=contrast=1.08:saturation=0.95:brightness=-0.01,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("b0","b0",1.00,1.10,3.3,None,0,"","c"),
 ("b1","b1",1.00,1.14,3.9,"fade",0.4,"","c"),
 ("b2","b2",1.12,1.00,4.9,"fadeblack",0.4,"","c"),
 ("b3","b3",1.00,1.14,3.3,"fade",0.4,"","c"),
 ("b4","b4",1.00,1.15,2.0,"fade",0.3,"","c"),
 ("b5","b5",1.00,1.12,None,"fadewhite",0.5,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Une ville tombe…\n*sans *une *arme.",1.0,dict(size=104,y=900,maxw=860))
HOOKS=[("Josué 6:20",15.6,17.5,dict(size=46,y=1560,stroke=5))]
CAPS=[(0.0,1.29,"Une ville *imprenable."),
(1.75,2.86,"Des murs *immenses."),
(3.39,4.45,"Dieu dit à Josué :"),
(4.91,5.44,"*n'attaque *pas."),
(5.89,6.45,"*Marche autour."),
(7.10,9.26,"*Six *jours, ils tournent en silence."),
(9.69,11.40,"Le 7e jour : *sept *tours."),
(11.94,14.78,"Les trompettes sonnent, le peuple *crie…"),
(15.22,16.64,"« et la muraille *s'écroula. »")]
FINS=[("Ton mur tombera aussi.",17.14,None,dict(size=76,y=860,font=X,maxw=1000)),
      ("*Continue *de *marcher.",18.81,None,dict(size=92,y=990,font=X,maxw=1000))]
BPM=66; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=1.0; PAD=0.8
PROG=[[57,60,64],[53,57,60],[60,64,67],[55,59,62]]; BASS=[45,41,48,43]
