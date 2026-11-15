D="/home/claude/work/story"; VO=0.4; END=34.2
GRADE=("colorbalance=rs=0.03:gs=0.0:bs=-0.03:rh=0.06:gh=0.02:bh=-0.04,eq=contrast=1.07:saturation=0.95:brightness=-0.02,vignette=PI/4.5,noise=alls=5:allf=t")
DARK=",eq=saturation=0.55:brightness=-0.05"
SCENES=[("s1","s_candle2",1.00,1.12,4.8,None,0,"","c"),
 ("s2","s_alone",1.05,1.18,3.6,"fade",0.4,"","c"),
 ("s3","s_pay",1.00,1.14,3.4,"fade",0.4,"","c"),
 ("s4","s_candles",1.12,1.00,2.8,"fadeblack",0.5,DARK,"c"),
 ("s5","s_table",1.00,1.12,3.0,"fade",0.5,"","c"),
 ("s6","s_phone",1.00,1.18,5.0,"fade",0.4,"","c"),
 ("s7","s_grad",1.00,1.22,7.0,"fadewhite",0.4,"","t"),
 ("s9","s_candle2",1.15,1.30,None,"fade",0.7,",eq=brightness=-0.06","c")]
HOOKS=[("Elle paie le repas d'un *inconnu…",0.15,4.6,dict(size=72,y=560)),
       ("…1 an plus tard, *ce *message.",0.9,4.6,dict(size=58,y=730,stroke=6,maxw=1000))]
CAPS=[(4.95,7.71,"Ce jour-là, elle remarque un jeune homme, *seul à sa table."),
(8.28,10.96,"Sans rien dire, elle *règle *son *addition, et s'en va."),
(11.59,13.61,"Pour elle, c'est un détail. Elle *oublie."),
(14.38,16.77,"Un an passe. Puis un *message arrive."),
(17.31,17.9,"*C'est *lui."),
(18.24,19.1,"Il la remercie."),
(19.28,21.71,"Ce repas a compté *bien *plus qu'elle ne l'imaginait."),
(22.37,23.91,"Avec le message, *une *photo."),
(24.41,26.10,"Lui, à sa *remise *de *diplôme."),
(26.53,28.65,"À côté, *sa *mère, rayonnante.")]
FINS=[("Ne sous-estime jamais",29.2,None,dict(size=68,maxw=980,y=860,font="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf")),
      ("un *petit *geste.",29.9,None,dict(size=92,y=990,font="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"))]
BPM=72; STEP=0.5; PAT=[0,1,2,1,2,1,0,2]; PLUCK_FROM=0.0; PAD=0.6
PROG=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]; BASS=[45,41,48,43]
