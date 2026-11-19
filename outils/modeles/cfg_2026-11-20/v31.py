D="/home/claude/work/v31"; VO=0.4; END=24.8
GRADE=("eq=contrast=1.10:saturation=0.92:brightness=0.0,colorbalance=bs=0.03:bm=0.02,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("m0","m0",1.00,1.12,4.6,None,0,",eq=gamma=1.25:brightness=0.03","c"),
 ("m1","m1",1.00,1.15,2.1,"fadeblack",0.3,",eq=gamma=1.3","c"),
 ("m2","m2",1.00,1.12,3.8,"zoomin",0.3,"","c"),
 ("m3","m3",1.12,1.00,3.5,"fade",0.4,"","c"),
 ("m4","m4",1.35,1.25,2.8,"fade",0.4,"","b"),
 ("m5","m5",1.00,1.15,None,"fadewhite",0.4,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Discipline : *des *grammes.\nRegret : *des *tonnes.",0.9,dict(size=92,y=900,maxw=980))
HOOKS=[]
CAPS=[(0.0,1.82,"La discipline pèse *quelques *grammes."),
(2.34,4.03,"Le regret pèse *des *tonnes."),
(4.63,6.02,"Se lever tôt, *c'est *dur."),
(6.38,7.75,"Dire non, *c'est *dur."),
(8.12,9.66,"Recommencer, *c'est *dur."),
(10.17,12.22,"Mais dans *5 *ans, tu sais ce qui sera vraiment dur ?"),
(12.77,13.76,"Regarder *en *arrière…"),
(14.23,15.82,"…et te dire : *j'aurais *pu.")]
FINS=[("Choisis ta *douleur.",16.47,None,dict(size=92,y=800,font=X,maxw=1000)),
      ("Celle d'aujourd'hui *passe.",17.75,None,dict(size=66,y=930,font=X,maxw=1000)),
      ("Celle du regret *reste.",19.20,None,dict(size=66,y=1030,font=X,maxw=1000)),
      ("Tu choisis *laquelle ?",21.04,None,dict(size=82,y=1170,font=X,maxw=1000))]
BPM=72; STEP=0.5; PAT=[0,2,1,2,0,1,2,1]; PLUCK_FROM=0.3; PAD=0.6
PROG=[[60,63,67],[56,60,63],[51,55,58],[58,62,65]]; BASS=[36,32,39,34]
TRAP=0.5; TRAP_FROM=4.9
