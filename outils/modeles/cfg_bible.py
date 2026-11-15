D="/home/claude/work/bible"; VO=0.6; END=29.6
GRADE=("colorbalance=rs=0.04:gs=0.0:bs=-0.05:rh=0.07:gh=0.02:bh=-0.05,eq=contrast=1.1:saturation=0.9:brightness=-0.02,vignette=PI/4.5,noise=alls=6:allf=t")
DARK=",eq=saturation=0.5:brightness=-0.04"
SCENES=[("b1","b_camels",1.00,1.12,3.4,None,0,"","c"),
 ("b2","b_well",1.00,1.15,4.4,"fade",0.4,"","c"),
 ("b3","b_bars",1.00,1.12,2.8,"fadeblack",0.5,"","c"),
 ("b4","b_shadow",1.12,1.00,2.2,"fade",0.4,DARK,"c"),
 ("b5","b_columns",1.00,1.12,2.0,"fadewhite",0.5,"","c"),
 ("b6","b_temple",1.00,1.14,3.0,"fade",0.4,"","c"),
 ("b7","b_drought",1.00,1.12,3.3,"fade",0.4,"","c"),
 ("b8","b_pyramid",1.00,1.18,None,"fade",0.6,"","c")]
L="/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
HOOKS=[("Ses frères l'ont *vendu…",0.15,3.6,dict(size=76,y=560)),
       ("…20 ans plus tard, *ils *se *prosternent.",0.9,3.6,dict(size=56,y=730,stroke=6,maxw=1000))]
CAPS=[(2.68,3.82,"Joseph a *17 *ans."),
(4.44,7.09,"Jaloux, ils le jettent dans un *puits, puis le vendent."),
(7.71,9.50,"En Égypte, il est *accusé *à *tort."),
(9.99,11.69,"Jeté en *prison. *Oublié."),
(12.30,13.47,"Mais *Dieu ne l'oublie pas."),
(13.91,16.08,"Joseph devient *gouverneur de toute l'Égypte."),
(16.72,17.55,"*20 *ans *plus *tard…"),
(17.91,19.63,"la famine amène ses frères devant lui."),
(20.10,20.82,"Ils se *prosternent."),
(21.39,22.10,"Il leur dira :")]
FINS=[("« Vous aviez médité de me faire du mal,",22.5,None,dict(size=62,y=800,font=L,maxw=920)),
      ("*Dieu *l'a *changé *en *bien. »",24.6,None,dict(size=74,y=990,font=L)),
      ("Genèse 50:20",25.2,None,dict(size=42,y=1110,font=L,stroke=5))]
BPM=60; STEP=1.0; PAT=[0,1,2,1]; PLUCK_FROM=0.0; PAD=0.9
PROG=[[50,53,57],[46,50,53],[43,46,50],[45,49,52]]; BASS=[38,34,31,33]
