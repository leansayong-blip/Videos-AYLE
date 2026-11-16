D="/home/claude/work/v20"; VO=0.4; END=29.4
GRADE=("colorbalance=rs=0.03:gs=0.01:bs=-0.02:rh=0.03:bh=-0.02,eq=contrast=1.1:saturation=0.92:brightness=-0.01,vignette=PI/4.5,noise=alls=5:allf=t")
SCENES=[("b0","b0",1.00,1.12,2.4,None,0,"","c"),
 ("b1","b1",1.00,1.12,4.7,"fade",0.3,"","c"),
 ("b2","b2",1.00,1.15,1.4,"fadeblack",0.3,"","c"),
 ("b3","b3",1.12,1.00,6.3,"fade",0.4,"","c"),
 ("b4","b4",1.00,1.15,5.9,"fadewhite",0.4,"","c"),
 ("b5","b5",1.00,1.12,1.8,"fade",0.3,"","c"),
 ("b6","b6",1.00,1.15,None,"fade",0.4,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
COVER=("La *mer devant.\n*L'armée derrière.",0.75,dict(size=100,y=900,maxw=960))
HOOKS=[("Devant : la *mer.",0.75,2.4,dict(size=84,y=560)),
       ("Derrière : *l'armée.",2.4,4.9,dict(size=84,y=560)),
       ("Exode 14:14",10.8,14.6,dict(size=46,y=1560,stroke=5))]
CAPS=[(4.66,6.25,"Tout un peuple, *pris *au *piège."),
(6.81,7.61,"Tout le monde *panique."),
(8.20,9.78,"Moïse, lui, reste *calme."),
(10.37,11.73,"« L'Éternel *combattra *pour *vous ;"),
(12.22,13.89,"et vous, *gardez *le *silence. »"),
(14.53,15.75,"Il étend la main sur *la *mer."),
(16.09,18.10,"Un vent violent souffle *toute *la *nuit…"),
(18.87,19.91,"…et la mer *s'ouvre."),
(20.48,21.68,"Ils traversent *à *pied *sec."),
(22.25,23.55,"Quand tu ne vois *aucune *sortie,")]
FINS=[("Dieu peut ouvrir un chemin",23.94,None,dict(size=72,y=860,font=X,maxw=1000)),
      ("*là *où *il *n'y *en *a *pas.",24.9,None,dict(size=88,y=990,font=X,maxw=1000))]
BPM=70; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=2.0; PAD=0.8
PROG=[[62,65,69],[58,62,65],[53,57,60],[60,64,67]]; BASS=[38,46,41,48]
