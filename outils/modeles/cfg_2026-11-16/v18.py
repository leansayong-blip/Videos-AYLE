D="/home/claude/work/v18"; VO=0.4; END=22.9
GRADE=("eq=contrast=1.06:saturation=1.08:brightness=0.01,vignette=PI/5,noise=alls=4:allf=t")
DARK=",eq=saturation=0.6:brightness=-0.05:contrast=1.08"
SCENES=[("h0","h_tools",1.00,1.10,2.2,None,0,"","c"),
 ("h1","h_table",1.00,1.12,3.1,"slideleft",0.3,"","c"),
 ("h2","h_box",1.10,1.00,1.6,"slideup",0.3,"","c"),
 ("h3","h_phone",1.00,1.12,3.4,"zoomin",0.3,"","c"),
 ("h4","h_tap",1.00,1.15,2.6,"fadeblack",0.4,DARK,"c"),
 ("h5","h_leak",1.00,1.15,2.8,"slideleft",0.3,DARK,"c"),
 ("h6","h_call",1.00,1.12,None,"slideup",0.3,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Lui à *14h vs lui à *18h",0.75,dict(size=104,y=900,maxw=900))
HOOKS=[("Lui, à *14h",0.75,10.25,dict(size=90,y=440)),
       ("Lui, à *18h",10.3,17.3,dict(size=96,y=440))]
CAPS=[(1.91,3.01,"« Pas besoin d'appeler un *plombier. »"),
(3.23,4.45,"« Je le répare en *5 *minutes. »"),
(4.99,6.11,"Il sort la *caisse *à *outils."),
(6.60,7.56,"Il regarde un *tuto."),
(7.99,9.38,"« C'est *simple. »"),
(11.63,14.48,"*3 *vis *en *trop, de l'eau partout dans la cuisine…"),
(15.49,16.40,"…et il appelle *son *père.")]
FINS=[("Identifie celui",17.01,None,dict(size=74,y=860,font=X)),
      ("qui dit toujours",17.6,None,dict(size=74,y=970,font=X)),
      ("« *Je *gère. »",19.05,None,dict(size=104,y=1100,font=X))]
BPM=104; STEP=0.5; PAT=[0,1,2,1,0,2,1,2]; PLUCK_FROM=0.0; PAD=0.4
PROG=[[62,66,69],[59,62,66],[55,59,62],[57,61,64]]; BASS=[50,47,43,45]
