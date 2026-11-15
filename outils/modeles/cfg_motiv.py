D="/home/claude/work/motiv"; VO=0.4; END=23.6
GRADE=("colorbalance=rs=-0.02:gs=0.0:bs=0.04:rh=0.05:gh=0.01:bh=-0.03,eq=contrast=1.1:saturation=0.92:brightness=-0.02,vignette=PI/4.5,noise=alls=6:allf=t")
SCENES=[("m1","m_window",1.00,1.15,3.4,None,0,"","c"),
 ("m2","m_clock",1.00,1.12,2.2,"fade",0.3,"","c"),
 ("m3","m_desk",1.00,1.12,2.9,"fade",0.3,"","c"),
 ("m4","m_bridge",1.55,1.65,3.4,"fade",0.4,",eq=saturation=0.7","b"),
 ("m5","m_roots",1.00,1.15,1.9,"fadeblack",0.4,"","c"),
 ("m6","m_tree",1.15,1.00,1.6,"fade",0.3,"","b"),
 ("m7","m_runner",1.00,1.12,3.0,"fade",0.3,"","c"),
 ("m8","m_lonetree",1.00,1.15,None,"fadewhite",0.5,"","c")]
X="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
HOOKS=[("Personne ne voit *tes *efforts…",0.15,2.9,dict(size=72,y=560)),
       ("…pour l'instant.",0.9,2.9,dict(size=60,y=720,stroke=6))]
CAPS=[(3.14,4.65,"Personne ne voit les réveils à *l'aube."),
(5.21,7.51,"Les soirs où tu continues pendant que *tout *le *monde *dort."),
(8.15,10.76,"Les fois où tu as voulu *lâcher… et où tu es *resté."),
(11.48,14.06,"Les racines poussent *dans *le *noir, bien avant l'arbre."),
(14.55,15.28,"Alors *continue."),
(15.76,17.27,"Surtout quand *personne *ne *regarde.")]
FINS=[("Un jour, ils verront",17.7,None,dict(size=78,y=860,font=X)),
      ("*le *résultat.",18.5,None,dict(size=92,y=980,font=X)),
      ("Pas le chemin.",19.95,None,dict(size=70,y=1110,font=X))]
BPM=84; STEP=0.5; PAT=[0,2,1,2,0,2,1,2]; PLUCK_FROM=3.0; PAD=0.7
PROG=[[52,55,59],[48,52,55],[55,59,62],[50,54,57]]; BASS=[40,36,43,38]
