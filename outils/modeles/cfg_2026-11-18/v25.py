D="/home/claude/work/v25"; VO=0.4; END=20.0
GRADE=("eq=contrast=1.08:saturation=1.05:brightness=0.0,vignette=PI/5,noise=alls=4:allf=t")
SCENES=[("m0","m0",1.00,1.12,3.7,None,0,",eq=gamma=1.25:brightness=0.03","c"),
 ("m1","m1",1.00,1.12,2.6,"fade",0.3,"","c"),
 ("m2","m2",1.00,1.15,3.2,"zoomin",0.3,"","c"),
 ("m3","m3",1.12,1.00,3.1,"fadeblack",0.3,"","c"),
 ("m4","m4",1.00,1.15,None,"fade",0.4,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("*1 *% par jour.\nFais le *calcul.",0.75,dict(size=104,y=900,maxw=720))
HOOKS=[("*x37",7.7,9.6,dict(size=170,y=640,stroke=9)),
       ("0,99³⁶⁵ ≈ *0,03",9.7,12.7,dict(size=72,y=640))]
CAPS=[(0.0,1.55,"*1 *% de mieux par jour."),
(2.14,3.10,"Ça paraît *ridicule."),
(3.55,4.32,"Personne *ne *le *voit."),
(4.81,5.32,"Même pas toi."),
(6.04,6.76,"Mais au bout *d'un *an…"),
(7.33,8.80,"tu es *37 *fois meilleur."),
(9.31,10.66,"Et *1 *% *de *moins chaque jour ?"),
(11.15,12.27,"Il ne reste *presque *rien.")]
FINS=[("Ce n'est pas un grand jour qui te change.",12.92,None,dict(size=58,y=840,font=X,maxw=1000)),
      ("C'est chaque *petit *jour",15.06,None,dict(size=82,y=960,font=X,maxw=1000)),
      ("où *tu *ne *lâches *pas.",16.0,None,dict(size=82,y=1065,font=X,maxw=1000))]
BPM=76; STEP=0.5; PAT=[0,1,2,1,0,2,1,2]; PLUCK_FROM=0.5; PAD=0.7
PROG=[[62,66,69],[59,62,66],[55,59,62],[57,61,64]]; BASS=[50,47,43,45]
