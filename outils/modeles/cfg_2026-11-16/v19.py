D="/home/claude/work/v19"; VO=0.4; END=24.5
GRADE=("colorbalance=rs=0.04:gs=0.01:bs=-0.03:rh=0.04:bh=-0.03,eq=contrast=1.08:saturation=0.92,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("p0","p_hug",1.00,1.04,0.6,None,0,"","c"),
 ("p1","p_alone",1.00,1.12,3.2,"fade",0.3,"","c"),
 ("p2","p_pigs",1.00,1.12,2.2,"fadeblack",0.4,",eq=saturation=0.7:brightness=-0.04","c"),
 ("p3","p_pig",1.12,1.00,2.8,"fade",0.3,",eq=saturation=0.7:brightness=-0.04","c"),
 ("p4","p_road",1.00,1.12,3.0,"fade",0.3,"","c"),
 ("p5","p_tunic",1.00,1.12,2.7,"fade",0.3,"","c"),
 ("p6","p_hug",1.00,1.18,None,"fadewhite",0.5,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Il a *tout *perdu…\nson père a *couru.",0.75,dict(size=104,y=900,maxw=960))
HOOKS=[("Son *héritage…",0.75,2.5,dict(size=84,y=560)),
       ("tout *perdu.",2.5,3.7,dict(size=84,y=560)),
       ("Luc 15:24",15.1,18.1,dict(size=46,y=1560,stroke=5))]
CAPS=[(3.80,4.41,"Plus *d'argent."),
(4.86,5.31,"Plus *d'amis."),
(5.98,8.14,"Il garde des *cochons, *affamé."),
(8.84,10.94,"Alors il rentre chez lui, *la *tête *basse."),
(11.56,12.76,"Mais son père le voit *de *loin…"),
(13.18,14.14,"…et il *court vers lui."),
(14.67,17.64,"« Mon fils que voici était mort, et il est *revenu *à *la *vie. »")]
FINS=[("Peu importe jusqu'où",18.21,None,dict(size=72,y=860,font=X)),
      ("tu es allé.",18.9,None,dict(size=72,y=970,font=X)),
      ("Tu peux *toujours *rentrer.",20.26,None,dict(size=88,y=1110,font=X,maxw=1000))]
BPM=70; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=1.5; PAD=0.8
PROG=[[60,64,67],[57,60,64],[53,57,60],[55,59,62]]; BASS=[48,45,41,43]
