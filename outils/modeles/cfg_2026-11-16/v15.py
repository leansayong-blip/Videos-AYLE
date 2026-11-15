D="/home/claude/work/v15"; VO=0.4; END=23.4
GRADE=("eq=contrast=1.05:saturation=1.08:brightness=0.01,vignette=PI/5,noise=alls=4:allf=t")
DARK=",eq=saturation=0.6:brightness=-0.05:contrast=1.08"
SCENES=[("h0","h_friends",1.00,1.04,0.6,None,0,"","c"),
 ("h1","h_shopping",1.00,1.12,1.7,"fade",0.25,"","c"),
 ("h2","h_brunch",1.00,1.12,2.4,"slideleft",0.3,"","c"),
 ("h3","h_dress",1.10,1.00,2.5,"slideup",0.3,"","c"),
 ("h4","h_desserts",1.00,1.15,2.4,"zoomin",0.3,"","c"),
 ("h5","h_phone",1.00,1.18,4.0,"fadeblack",0.4,DARK,"c"),
 ("h6","h_pasta",1.00,1.15,2.4,"slideleft",0.3,DARK,"c"),
 ("h7","h_wallet",1.15,1.00,2.5,"slideup",0.3,DARK,"c"),
 ("h8","h_friends",1.00,1.12,None,"fadewhite",0.4,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Moi le *1er vs moi le *28",0.75,dict(size=104,y=900,maxw=900))
HOOKS=[("Moi, le *1er *du *mois",0.75,9.5,dict(size=80,y=440)),
       ("Moi, le *28",9.6,18.7,dict(size=96,y=440))]
CAPS=[(1.83,2.60,"*Salaire *tombé."),
(3.07,5.34,"Brunch avec les copines, nouvelle robe…"),
(5.89,6.64,"« Je le *mérite. »"),
(6.96,8.00,"Et *deux desserts."),
(10.91,13.06,"J'ouvre mon appli bancaire comme un *film *d'horreur."),
(13.68,15.25,"Pâtes au beurre… *sans *beurre."),
(15.89,17.92,"« Non merci, je fais une *détox *shopping. »")]
FINS=[("Identifie la copine",18.42,None,dict(size=72,y=860,font=X)),
      ("qui vit *le *28",19.2,None,dict(size=90,y=975,font=X)),
      ("dès le 15.",20.3,None,dict(size=72,y=1090,font=X))]
BPM=104; STEP=0.5; PAT=[0,1,2,1,0,2,1,2]; PLUCK_FROM=0.0; PAD=0.4
PROG=[[60,64,67],[57,60,64],[53,57,60],[55,59,62]]; BASS=[48,45,41,43]
