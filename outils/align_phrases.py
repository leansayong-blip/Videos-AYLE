import json,re,subprocess
ph=["Il avait dix-huit ans.","Un soir, il sort avec ses potes.","Direction : le spot de desserts le plus connu de la ville.",
"Avant, ils s'arrêtent dans une supérette.","À la caisse, une femme sans-abri compte ses pièces...","Il lui manque dix centimes.","Juste dix centimes, pour un bonbon.",
"Il fouille son portefeuille. Rien.","Alors il retourne à la voiture.","La boîte à gants, sous les sièges...","Ça prend plusieurs minutes.","Ses potes s'impatientent.",
"Enfin, il trouve une pièce. Dix centimes.","Il la lui donne. Elle sourit.","Et ils repartent.",
"Mais en approchant du spot... tout est bloqué.","Des voitures de police passent à toute vitesse.",
"Une bagarre devant la boutique venait de dégénérer.","Des coups de feu. Des blessés...","dans la file d'attente.",
"Exactement là où ils auraient dû être...","s'ils étaient arrivés à l'heure.","Dix centimes. Quelques minutes de retard.","Tu ne sais jamais ce qu'un petit geste peut changer."]
out=subprocess.run("ffmpeg -nostdin -i vo.mp3 -af silencedetect=noise=-35dB:d=0.25 -f null -",shell=True,capture_output=True,text=True).stderr
ss=[float(x) for x in re.findall(r"silence_start: ([\d.]+)",out)]; se=[float(x) for x in re.findall(r"silence_end: ([\d.]+)",out)]
# speech segments: from each silence_end to next silence_start
segs=[]
for i,e in enumerate(se):
    s2=[s for s in ss if s>e]
    if s2: segs.append((e,s2[0]))
print(len(segs),"segs",len(ph),"phrases")
L=[len(p) for p in ph]; D=[b-a for a,b in segs]
rate=sum(D)/sum(L)
import functools,math
n,m=len(ph),len(segs)
INF=1e18
dp=[[INF]*(m+1) for _ in range(n+1)]; bk=[[0]*(m+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
  for j in range(1,m+1):
    for k in range(i-1,j):
      if dp[i-1][k]>=INF: continue
      d=segs[j-1][1]-segs[k][0]; c=dp[i-1][k]+(d-L[i-1]*rate)**2/(L[i-1]*rate)
      if c<dp[i][j]: dp[i][j]=c; bk[i][j]=k
res=[];j=m
for i in range(n,0,-1):
  k=bk[i][j]; res.append((ph[i-1],segs[k][0],segs[j-1][1])); j=k
res.reverse()
for p,a,b in res: print(f"{a:6.2f} {b:6.2f}  {p}")
json.dump(res,open('align.json','w'),ensure_ascii=False)
