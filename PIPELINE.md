# Pipeline VYLE / Ayle&Co : production et publication quotidiennes

Ce dépôt sert à héberger les vidéos finies (vidIQ les importe par l'URL raw GitHub) et à garder la méthode de production.
Toutes les réponses à Leans : en français, direct, sans compliments, apostrophes droites.

## Règles absolues
- Ne JAMAIS dépenser de crédits (ElevenLabs, vidIQ) sans avoir vérifié qu'on peut récupérer et utiliser le résultat.
- Images : Unsplash uniquement (0 crédit vidIQ). Pas de logo de marque visible, pas de personnage protégé, pas de personne identifiable dans une situation négative.
- Voix : ElevenLabs `creative_generate_speech`, modèle eleven_v4, **generations_count 1**, une seule prise. Jamais de nouvelle tentative en cas d'échec : on saute la vidéo et on le signale.
- Musique : composée localement (numpy/scipy), JAMAIS forte (volume 0.2 à 0.25 + sidechain sur la voix), loudnorm -14 LUFS.
- **Aucun bruit de transition (whoosh, riser).**
- Logo Ayle&Co (`outils/logo/ayleco_overlay.png`) en haut à gauche, overlay=36:120, fondu d'entrée 0.3 s.
- Mode créateur vidéo expérimenté : accroche forte dans les 2 premières secondes, Ken Burns, fondus xfade, étalonnage, sous-titres lisibles (InterDisplay Bold, contour noir, mots clés en jaune), fin avec phrase forte.
- Storytime : histoires vraies trouvées sur Reddit ou dans l'actualité, réécrites ENTIÈREMENT avec nos mots, source citée dans la description. Jamais de personne privée identifiable.
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
1. `account_get_usage` (ElevenLabs) : restants = character_limit - character_count ; jours restants = jusqu'à next_character_count_reset_unix.
2. Budget du jour = restants / jours restants. Si le budget ne couvre pas les 3 vidéos, remplacer une Storytime par une Motivation, puis réduire à 2 vidéos. Ne jamais passer sous 1 000 crédits de réserve.
3. vidIQ : on n'utilise que les outils gratuits (video_upload, social_post_*). Pas de find_broll sauf demande de Leans.

## Étapes de production (par vidéo)
1. Écrire le script (texte voix, 2-3 phrases d'accroche à l'écran, titre).
2. Unsplash : `search_photos` (portrait), choisir 6 à 10 photos, `download_asset` pour chacune (obligatoire), télécharger `images.unsplash.com/...&w=2160`. Noter les noms des photographes.
3. Voix : `creative_generate_speech` (1 prise), puis `creative_get_flow_run_status` pour le content_url (elevenlabsusercontent.com), télécharger le mp3.
4. Caler les sous-titres : `ffmpeg silencedetect` puis transcription locale par segment (`outils/asr_segments.py`, modèle sherpa-onnx whisper-base téléchargé depuis github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-base.tar.bz2).
5. Montage : adapter un modèle de `outils/modeles/` (storytime_build.py est le plus récent : scènes, sous-titres, logo, musique, mixage). Vérifier 4 à 6 images clés avant le rendu complet. Encoder crf 23-24, maxrate 8M.
6. Copier le mp4 final dans ce dépôt (`vNN_titre.mp4`), commit, push.

## Publication
1. `vidiq_video_upload` avec l'URL `https://raw.githubusercontent.com/leansayong-blip/Videos-AYLE/main/<fichier>.mp4`.
2. `vidiq_social_post_draft_create` : une publication par vidéo, destinations selon `config.json` (respecter les thèmes par compte), YouTube : titre accrocheur + `#shorts`, privacyStatus public, description (accroche, question pour commentaires, abonnement, crédits photos, source), 10-12 tags. Instagram/TikTok : légende courte + question + 8-10 hashtags (mélange larges et de niche, toujours #ayleco). publishAt = heures de `config.json`.
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
