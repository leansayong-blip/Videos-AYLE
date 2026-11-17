D="/home/claude/work/v24"; VO=0.4; END=34.4
GRADE=("colorbalance=rs=0.02:gs=0.0:bs=-0.02:rh=0.05:gh=0.02:bh=-0.03,eq=contrast=1.07:saturation=0.97:brightness=-0.01,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("s0","s0",1.00,1.04,0.7,None,0,"","c"),
 ("s1","s1",1.00,1.12,5.5,"fade",0.25,"","c"),
 ("s2","s2",1.00,1.15,3.2,"fadeblack",0.4,"","c"),
 ("s3","s3",1.00,1.18,9.0,"fade",0.4,"","c"),
 ("s4","s4",1.12,1.00,4.8,"fade",0.4,"","c"),
 ("s5","s5",1.00,1.15,6.0,"fade",0.4,"","t"),
 ("s6","s6",1.00,1.12,None,"fadewhite",0.5,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("Il marche *32 *km de nuit… pour son *premier *jour.",0.75,dict(size=96,y=900,maxw=960))
HOOKS=[("*32 *km à pied.",0.75,2.4,dict(size=80,y=560))]
CAPS=[(0.0,0.69,"Il a *vingt *ans."),
(1.27,3.77,"Demain, c'est son *premier *jour de travail,"),
(3.77,5.34,"chez un *déménageur."),
(5.97,7.16,"Mais la veille au soir…"),
(7.71,8.60,"sa voiture *tombe *en *panne."),
(9.18,10.48,"Personne pour l'emmener."),
(10.94,12.17,"Alors il décide d'y aller *à *pied."),
(12.76,13.58,"Plus de *trente *kilomètres."),
(14.00,15.15,"Il part vers *minuit…"),
(15.73,17.71,"…et marche *toute *la *nuit."),
(18.24,19.45,"4 h du matin : *la *police l'arrête."),
(20.00,21.28,"Ils lui offrent un *petit-déjeuner…"),
(21.94,22.33,"…puis le déposent"),
(22.33,23.75,"chez la cliente. *Touchée, elle partage son histoire."),
(24.34,26.47,"Quelques jours plus tard, *le *patron vient le voir…"),
(26.91,28.38,"…et lui donne *sa *propre *voiture.")]
FINS=[("Quand tu veux *vraiment quelque chose,",28.98,None,dict(size=62,y=860,font=X,maxw=1000)),
      ("tu trouves *un *chemin.",30.88,None,dict(size=88,y=990,font=X,maxw=1000))]
BPM=72; STEP=0.5; PAT=[0,1,2,1,2,1,0,2]; PLUCK_FROM=0.0; PAD=0.6
PROG=[[60,64,67],[57,60,64],[53,57,60],[55,59,62]]; BASS=[48,45,41,43]
