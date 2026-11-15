D="/home/claude/work/v16"; VO=0.4; END=33.0
GRADE=("colorbalance=rs=0.03:gs=0.0:bs=-0.03:rh=0.06:gh=0.02:bh=-0.04,eq=contrast=1.07:saturation=0.95:brightness=-0.02,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("s1","s_drive",1.00,1.12,3.0,None,0,"","c"),
 ("s2","s_breakdown",1.00,1.15,2.9,"fade",0.4,"","b"),
 ("s3","s_traffic",1.00,1.12,2.7,"fade",0.3,"","c"),
 ("s4","s_push",1.12,1.00,1.9,"fadeblack",0.4,"","c"),
 ("s5","s_station",1.00,1.15,3.0,"fade",0.4,"","b"),
 ("s6","s_money",1.00,1.15,3.1,"fade",0.4,"","c"),
 ("s7","s_office",1.00,1.12,3.3,"fadeblack",0.5,"","c"),
 ("s8","s_interview",1.00,1.15,2.6,"fade",0.4,"","c"),
 ("s9","s_handshake",1.00,1.18,3.9,"fade",0.3,"","c"),
 ("s10","s_road",1.00,1.15,None,"fadewhite",0.6,"","b")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
HOOKS=[("Il aide un *inconnu…",0.15,2.9,dict(size=74,y=560)),
       ("…et le retrouve *en *entretien.",0.9,2.9,dict(size=58,y=700,stroke=6,maxw=1000))]
CAPS=[(0.05,1.94,"Il rentre du travail, *épuisé."),
(2.72,5.54,"Sur la route, un homme pousse *seul sa voiture en panne."),
(6.02,8.11,"Ça klaxonne. Tout le monde *le *contourne."),
(8.66,9.61,"*Lui, *s'arrête."),
(10.20,12.63,"Ensemble, ils la poussent jusqu'à *la *station."),
(13.27,14.07,"L'homme veut *le *payer."),
(14.58,15.95,"Il *refuse, et repart."),
(16.73,19.17,"Des mois plus tard… *entretien *d'embauche."),
(19.71,21.75,"Il entre… et *reconnaît le recruteur."),
(22.21,23.30,"C'est *l'homme *à *la *voiture."),
(23.94,25.45,"Quelques jours après, *il *est *pris.")]
FINS=[("Ce que tu fais",26.25,None,dict(size=76,y=840,font=X)),
      ("quand *personne *ne *regarde…",27.0,None,dict(size=60,y=950,font=X,maxw=1000)),
      ("finit toujours par te suivre.",28.56,None,dict(size=58,y=1065,font=X,maxw=1000))]
BPM=72; STEP=0.5; PAT=[0,1,2,1,2,1,0,2]; PLUCK_FROM=0.0; PAD=0.6
PROG=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]; BASS=[45,41,48,43]
