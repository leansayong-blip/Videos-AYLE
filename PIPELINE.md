# Pipeline VYLE / Ayle&Co : production et publication quotidiennes

Ce dépôt sert à héberger les vidéos finies (vidIQ les importe par l'URL raw GitHub) et à garder la méthode de production.
Toutes les réponses à Leans : en français, direct, sans compliments, apostrophes droites.

## Règles absolues
- Ne JAMAIS dépenser de crédits (ElevenLabs, vidIQ) sans avoir vérifié qu'on peut récupérer et utiliser le résultat.
- Images : Unsplash uniquement (0 crédit vidIQ), sauf Storytime où une recherche vidIQ find_broll est permise de temps en temps (voir Gestion des crédits). Pas de logo de marque visible, pas de personnage protégé, pas de personne identifiable dans une situation négative.
- Voix : ElevenLabs `creative_generate_speech`, modèle eleven_v4, **generations_count 1**, une seule prise. Jamais de nouvelle tentative en cas d'échec : on saute la vidéo et on le signale.
- Musique : composée localement (numpy/scipy), JAMAIS forte (volume 0.2 à 0.25 + sidechain sur la voix), loudnorm -14 LUFS.
- **Aucun bruit de transition (whoosh, riser).**
- Logo Ayle&Co (`outils/logo/ayleco_overlay.png`) en haut à gauche, overlay=36:120, fondu d'entrée 0.3 s.
- Mode créateur vidéo expérimenté : accroche forte dans les 2 premières secondes, Ken Burns, fondus xfade, étalonnage, sous-titres lisibles (InterDisplay Bold, contour noir, mots clés en jaune), fin avec phrase forte.
- Storytime : histoires vraies trouvées sur Reddit ou dans l'actualité, réécrites ENTIÈREMENT avec nos mots. Dans la description, on écrit seulement « Inspiré d'une histoire vraie » (jamais le nom du site, du forum ou du subreddit, ni de lien source). Jamais de personne privée identifiable.
- Biblique : récit raconté avec nos mots + leçon. Citations uniquement Louis Segond 1910.

## Thèmes et voix
| Thème | Voix | Durée | Crédits estimés |
|---|---|---|---|
| Storytime | Bass `wQjKP9DkO6pDLKdaqFn6` | 45 s | 750 |
| Motivation | Bass | 30 s | 300 |
| Humour hommes/femmes | Agathe `SptHT9PQ49isQvxFm28t` | 30 s | 300 |
| Biblique | Bass | 33 s | 350 |

Rotation : voir `config.json` (3 vidéos par jour, option A). **Chaque jour : 1 vidéo Biblique obligatoire (05:00) + 2 vidéos en rotation Motivation / Humour / Storytime (10:00, 16:00).** **La production se fait la veille** : la tâche de 14h47 prépare les vidéos du lendemain, publiées à 05:00, 10:00 et 16:00 (heure de Paris) ; la rotation et le planning utilisés sont ceux du jour de publication. Si `planning/semaine-AAAA-SNN.md` existe (validé le dimanche avec Leans), il prime sur la rotation.

## Gestion des crédits (chaque jour, avant de produire)
Objectif fixé par Leans (15/11/2026) : **tenir 3 vidéos par jour jusqu'au renouvellement ElevenLabs ET utiliser tous les crédits avant ce renouvellement** (aucun crédit perdu, aucun jour sans vidéo).
1. `account_get_usage` (ElevenLabs) : restants = character_limit - character_count ; renouvellement = next_character_count_reset_unix ; J = nombre de jours de publication restants avant le renouvellement (en comptant demain).
2. Budget du jour = restants / J.
   - Coûts de référence : Biblique ≈ 350, Motivation ≈ 300, Humour ≈ 300, Storytime 45 s ≈ 750.
   - Si le budget est INFÉRIEUR au coût des 3 vidéos prévues : garder 3 vidéos mais raccourcir les textes (Storytime 35 s ≈ 580, autres 25 s ≈ 250) ; si ce n'est toujours pas assez, remplacer la Storytime par une Motivation. Ne jamais descendre sous 3 vidéos tant que c'est possible.
   - Si le budget DÉPASSE le coût des 3 vidéos d'au moins 300 crédits : ajouter une 4e vidéo ce jour-là (thème suivant de la rotation, publiée à 19:00), pour ne pas laisser de crédits inutilisés.
   - Le dernier jour de production avant le renouvellement : utiliser tout le reste (vidéos supplémentaires si besoin), en gardant seulement de quoi produire la dernière vidéo correctement.
3. Indiquer dans la notification du jour : crédits restants, budget du jour, et si on est en avance ou en retard sur l'objectif.
4. vidIQ : outils gratuits (video_upload, social_post_*). find_broll (1 crédit) autorisé UNIQUEMENT pour les Storytime, de temps en temps (1 recherche max par vidéo, vérifier que le mp4 Pexels se télécharge avant de l'utiliser). Tous les autres thèmes : Unsplash uniquement.

## Étapes de production (par vidéo)
1. Écrire le script (texte voix, 2-3 phrases d'accroche à l'écran, titre).
2. Photos : **d'abord la banque** (`python3 outils/banque.py chercher "mot1,mot2"`, voir section Économie de tokens). Ne chercher sur Unsplash que ce qui manque : `search_photos` (portrait, **per_page 4**), `download_asset` pour chacune (obligatoire), télécharger `images.unsplash.com/...&w=2160`, puis **ajouter chaque nouvelle photo à la banque** (`banque.py ajouter`). Copier les photos de la vidéo avec `banque.py preparer`, noter l'usage avec `banque.py utiliser`, crédits avec `banque.py credits`.
3. Voix : `creative_generate_speech` (1 prise), puis `creative_get_flow_run_status` pour le content_url (elevenlabsusercontent.com), télécharger le mp3.
4. Caler les sous-titres : `ffmpeg silencedetect` puis transcription locale par segment (`outils/asr_segments.py`, modèle sherpa-onnx whisper-base téléchargé depuis github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.tar.bz2).
5. Montage : adapter un modèle de `outils/modeles/` (storytime_build.py est le plus récent : scènes, sous-titres, logo, musique, mixage). Vérifier 4 à 6 images clés avant le rendu complet. Encoder crf 23-24, maxrate 8M.
6. Copier le mp4 final dans ce dépôt (`vNN_titre.mp4`), commit, push.

## Publication
1. `vidiq_video_upload` avec l'URL `https://raw.githubusercontent.com/leansayong-blip/Videos-AYLE/main/<fichier>.mp4`.
2. `vidiq_social_post_draft_create` : une publication par vidéo, destinations selon `config.json` (respecter les thèmes par compte), YouTube : titre accrocheur + `#shorts`, privacyStatus public, description (accroche, question pour commentaires, abonnement, crédits photographes ; pour une storytime : « Inspiré d'une histoire vraie »), tags selon la section « Descriptions et hashtags » ci-dessous. publishAt = heures de `config.json`.
3. TikTok : seulement si `config.json` → `tiktok` contient privacyLevel, allowComment, musicUsageConfirmed choisis par Leans. Sinon ne pas inclure TikTok et le rappeler.
4. JAMAIS de publication sur Aylecreate ni 1minute augabon.
5. Leans a donné son accord permanent pour publier automatiquement (14/11/2026) : `vidiq_social_post_publish` sur chaque brouillon.

## Après publication
- Mettre à jour l'artifact « Business VYLE » (https://claude.ai/artifact/DuWnGLg2FTGMhaexAdbmrZ) : videos.json (nouvelle ligne : id, titre, theme, date, duree_s, voix, credits, statut, note, apercu 180x320 en data:image/jpeg;base64, liens de publication), dataset clip_vNN (base64 d'une version allégée), en respectant la règle d'édition (stamp edit avant chaque modification).
- Notifier Leans (PushNotification + SendUserMessage) : vidéos publiées, comptes, heures, crédits restants.

## Formats qui marchent (retours de Leans)
- 14/11/2026 : le format « Moi à 18h vs moi à 2h du matin » (contraste résolution / réalité, étiquettes de jour ou d'heure, voix Agathe, chute drôle) a bien fonctionné.
  → Pour l'Humour, utiliser ce format **environ 1 fois sur 2**, en alternant la cible :
    - **version femmes** : situations vécues par les femmes (« Moi le lundi vs moi le vendredi », « Moi avant le date vs moi après », « Moi au début du mois vs moi le 28 »…), avec des **photos Unsplash de femmes** (non identifiables dans une situation gênante, pas de marque visible).
    - **version hommes** : même principe côté hommes, photos d'hommes.
  → Varier les contrastes (heures, jours, avant/après, attente/réalité) pour ne pas répéter la même vidéo. Toujours finir sur une question qui pousse à identifier quelqu'un en commentaire.

## Couverture (miniature) — OBLIGATOIRE (demande de Leans, 15/11/2026)
Instagram (et souvent TikTok) prend la **toute première image** de la vidéo comme couverture ; l'outil vidIQ ne permet pas de choisir une autre image. Donc :
- **Jamais d'ouverture au noir** : supprimer tout `fade=in` au début de la vidéo finale (pas de fondu depuis le noir sur la 1re seconde).
- **Les 0,5 premières secondes = la couverture** : la meilleure photo de la vidéo, bien éclairée, avec le **titre accrocheur en très gros** (InterDisplay ExtraBold, 90-110 px, contour noir, 1 ou 2 mots clés en jaune), centré dans la zone sûre (entre y=500 et y=1300, pour ne pas être coupé dans la grille Instagram 3:4 ni sous les boutons) + logo Ayle&Co. Puis la vidéo enchaîne normalement (le titre peut rester et se fondre dans l'accroche).
- Vérifier la frame 0 (`ffmpeg -ss 0 -frames:v 1`) avant de publier : elle doit être lisible, belle et donner envie de cliquer. Si elle est noire ou vide, corriger avant publication.


## Économie de tokens Claude (demande de Leans, 15/11/2026) : utiliser le moins possible
Les crédits Claude de Leans sont limités. Chaque run doit être aussi léger que possible, sans baisser la qualité des vidéos.
1. **Banque de photos** (`banque/index.json` + `banque/photos/<id>.jpg`, outil `outils/banque.py`) :
   - Toujours chercher d'abord dans la banque. Réutiliser une photo est permis si elle n'a pas servi depuis 14 jours (marquée `ok`), jamais deux fois dans la même vidéo.
   - Objectif : au plus **3 nouvelles recherches Unsplash par vidéo**, `per_page` 4 (les réponses Unsplash sont très lourdes). Une recherche = un concept court.
   - Toute photo téléchargée entre dans la banque avec photographe, thème, description de ce qu'on voit et tags en français. Les photos marquées `couverture` sont bien éclairées et servent de première image.
   - Pas de sous-agent pour les photos (trop coûteux) : faire les recherches soi-même, en parallèle.
2. **Montage** : toujours `outils/modeles/generic_build.py` + un fichier cfg par vidéo (exemples dans `outils/modeles/cfg_2026-11-16/`). Ne pas relire les autres modèles. Vérification visuelle : une seule planche de 6 images par vidéo (hstack en 270x480) + la frame 0.
3. **Voix** : `estimate_only` inutile (coût = nombre de caractères du texte, environ 1 crédit par caractère) ; compter les caractères en local.
4. **Artifact Business VYLE** : ne pas relire les instructions du type ni la page. Procédure fixe :
   - lire `datasets/videos` (pour sa version et l'url du blob) puis `Artifact read path=<id du blob>` pour récupérer videos.json (liste de lignes) ;
   - ajouter les lignes (apercu = `data:image/jpeg;base64,...` 180x320), uploader le nouveau videos.json avec `Artifact publish asset:true` ;
   - clips : fichier texte = **base64 brut du mp4 sans préfixe** (360x640, crf 32, aac 64k), un upload par fichier ;
   - un seul `ArtifactData batch` : update `datasets/videos` (source.url, edit, updated, if_version) + set `datasets/clip_vNN` (title, description, fixed:true, source {format:text, kind:file, name, url}, edit, updated).
5. **Ne pas appeler** `list_triggers` (réponse énorme) ni lire des fichiers ou outils inutiles. Statut vidIQ : un seul `social_post_status` par publication, après la publication.
6. Messages à Leans courts.


## Discrétion sur la méthode (demande de Leans, 16/11/2026)
Dans les titres, descriptions, légendes, hashtags et commentaires : **ne jamais citer** les outils ou sources utilisés (ElevenLabs, Reddit ou un subreddit, Upworthy, vidIQ, Claude, etc.). Storytime : écrire seulement « Inspiré d'une histoire vraie ». Les noms des photographes restent crédités (courtoisie), sans citer la banque d'images si Leans le demande. Ne pas toucher aux réglages « contenu IA » des plateformes.


## Descriptions et hashtags (demande de Leans, 16/11/2026 : maximiser la portée, hashtags pertinents)
Constat 2026 : Instagram limite les posts et Reels à **5 hashtags maximum** ; YouTube ignore tous les hashtags au-delà de 15 ; sur TikTok et Shorts, la pertinence compte plus que le nombre. Les mots-clés dans le texte comptent autant que les hashtags (Instagram et TikTok fonctionnent comme des moteurs de recherche).
- **Toutes plateformes** : 1re ligne = accroche (vue avant « plus »), avec le mot-clé principal du sujet ; puis une question qui pousse à commenter ; 1 phrase d'appel à s'abonner. Hashtags à la fin, tous liés au contenu. Pas de #viral ; #fyp seulement sur TikTok (1 maximum).
- **YouTube Shorts** : titre ≤ 70 caractères, accroche + mot-clé, `#shorts` en fin de titre. Description : accroche (2 lignes), question, abonnement, crédits photographes, puis **3 à 5 hashtags** (les 3 premiers s'affichent au-dessus du titre : #shorts + 1 de niche + #ayleco). Champ tags (invisible) : 10 à 12 mots-clés (larges + niche + expressions longues).
- **Instagram (@laterreduprince, @aytenseigne)** : légende courte, **5 hashtags maximum** : 3 de niche du thème, 1 large, #ayleco.
- **TikTok** : légende courte avec mots-clés, **4 à 6 hashtags** : 2 à 3 de niche du thème, 1 à 2 larges, #ayleco (+ #fyp ou #pourtoi en option).
- **Banques par thème** (piocher, ne pas tout mettre) :
  - Biblique : #bible #foi #jesus #dieu #chretien #versetdujour #priere #histoirebiblique #parolededieu
  - Storytime : #histoirevraie #storytime #histoire #inspiration #leconsdevie #gentillesse #karma
  - Motivation : #motivation #discipline #mindset #developpementpersonnel #reussite #perseverance #motivationfr
  - Humour femmes : #humour #humourfemme #relatable #copines #drole
  - Humour hommes : #humour #humourhomme #relatable #couple #drole
- Varier les hashtags d'une vidéo à l'autre (ne pas copier-coller exactement le même bloc), garder #ayleco en marque fixe.

## Thème 5 : « Série Histoire Vraie » (ajouté le 17/11/2026)
- Fréquence : 2 par semaine (mercredi et samedi, créneau 10:00, à la place du Motivation/Humour/Storytime ce jour-là). Publication partout (même comptes que les autres thèmes ; @aytenseigne inclus).
- Contenu : histoires vraies de style thriller (espionnage, affaires criminelles documentées, business, trading, parcours comme Jensen Huang). Faits documentés uniquement, sans dialogues ni intentions inventés pour des personnes réelles.
- Durée : ~90 s. Voix Bass, ton posé et tendu. Budget ≈ 1500 crédits ElevenLabs par vidéo : ajuster les autres vidéos du jour pour tenir le budget.
- Ouverture obligatoire : « Bonjour, nous sommes de retour avec votre série Histoire Vraie. » (à varier légèrement, ex. « Bienvenue dans un nouvel épisode de Série Histoire Vraie »), puis accroche choc.
- Structure : intro de série, accroche, mise en place, basculement, chute et conséquence, question en commentaire.
- Visuels : JAMAIS de photos de personnes réelles. Images Unsplash sombres et cinématographiques + noms, dates et chiffres en texte à l'écran (style dossier déclassifié). Logo Ayle&Co en haut à gauche, première image titrée (règle couverture).
- Description : « Histoire vraie » sans citer de source ni d'outil. Hashtags : #histoirevraie #seriehistoirevraie #thriller #espionnage #business #trading #histoire #ayleco (max 5 Instagram, 4-6 TikTok, 3-5 YouTube + tags cachés).
- Épisodes prévus : Aldrich Ames, Robert Hanssen, Jensen Huang, Nick Leeson (Barings), Jordan Belfort.
