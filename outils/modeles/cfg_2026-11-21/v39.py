D="/home/claude/work/v39"; VO=0.4; END=21.2
GRADE=("colorbalance=rs=0.02:gs=0.01:bs=0.0:rh=0.04:gh=0.02:bh=-0.02,eq=contrast=1.06:saturation=0.95:brightness=0.0,vignette=PI/5,noise=alls=4:allf=t")
SCENES=[("b0","b0",1.00,1.10,5.6,None,0,"","c"),
 ("b1","b1",1.00,1.12,5.4,"fade",0.5,"","c"),
 ("b2","b2",1.10,1.00,5.0,"fade",0.5,"","c"),
 ("b3","b3",1.00,1.12,None,"fadewhite",0.6,"","c")]
COVER=("Tu traverses\n*une *vallée *sombre ?",1.0,dict(size=100,y=900,maxw=900))
HOOKS=[("PSAUME 23:4",6.8,14.8,dict(size=46,y=1560,stroke=5))]
CAPS=[(0.2,3.2,"Tu traverses une vallée sombre, et tu crois que *tu *es *seul."),
(3.8,6.2,"Psaume 23, *verset *4."),
(6.7,9.2,"« Quand je marche dans *la *vallée *de *l'ombre *de *la *mort,"),
(9.3,10.6,"je ne crains *aucun *mal,"),
(10.9,12.2,"car *tu *es *avec *moi :"),
(12.5,14.6,"ta houlette et ton bâton *me *rassurent. »"),
(15.0,16.9,"La vallée n'est pas *la *fin *du *chemin."),
(17.0,19.8,"Tu la traverses. Et *pas *seul.")]
FINS=[]; BPM=58; STEP=0.5; PAT=[0,2,1,2,0,1,2,1]; PLUCK_FROM=1.0; PAD=1.1
PROG=[[64,67,71],[60,64,67],[62,66,69],[59,62,66]]; BASS=[40,36,38,35]
