# Enquête Duchenne — démonstration exploratoire

Vous cherchez pourquoi l'évolution de Duchenne varie entre patients. Ce dossier relie publications, propositions du modèle, contradictions et calculs sur des biopsies publiques. La piste retenue concerne le contexte génétique et thérapeutique du réseau LTBP4–THBS1/TGFβ. Elle est déjà connue : l'intérêt démontré ici est le chemin d'enquête et ses limites.

Commencer par [EXEMPLE.md](EXEMPLE.md), puis [FICHES.md](FICHES.md). [corpus.json](corpus.json) fournit les observations, références exactes, courts extraits et droits. [PROTOCOL.md](PROTOCOL.md) fixe les choix avant calcul. [SEARCH_LOG.md](SEARCH_LOG.md) conserve sélection, antériorité et échecs d'accès. Aucun fichier historique n'a été modifié.

## Reproduire les calculs

Environnement exécuté : CPython 3.9.6, macOS 26.2 arm64 ; bibliothèque standard uniquement. Prévoir environ 120 Mo pour les fichiers décompressés et temporaires. Unix requis pour `resource` ; autres systèmes non testés. Un venv neuf isole les paquets, pas le système d'exploitation.

Dans le dossier extrait, lancer :

```sh
python3 -m venv --without-pip .venv
.venv/bin/python -B verify.py
.venv/bin/python -B analyze.py --out runs/mon-essai
```

Le dossier de sortie doit être absent. `results.json` contient toutes les valeurs retenues, les métadonnées, les contrastes et les empreintes des entrées ; les CSV facilitent leur inspection. `execution.json` mesure ce processus seulement. Ne pas écraser les traces livrées. `verify.py` exige une égalité exacte des résultats numériques, sans comparer les durées variables.

La matrice d'expression et l'annotation sont incluses : aucun réseau ni accès modèle requis pour ces calculs. Le code vérifie la complétude, les identifiants, les groupes et les valeurs numériques. Le traitement part des valeurs déjà normalisées par les déposants, sans retraitement des fichiers CEL.

Option réseau, séparée et également testée :

```sh
.venv/bin/python -B fetch.py --out nouvelles-donnees
```

Cette commande récupère uniquement la matrice et la table de plateforme, plafonnées respectivement à 10 et 100 Mo ; elle n'appelle pas l'archive famille. Les métadonnées distantes peuvent changer. Pour réanalyser ces fichiers, ajouter le CSV factuel `data/weiss2018_table1.csv` dans ce nouveau dossier et utiliser `analyze.py --data nouvelles-donnees --out runs/nouveau-telechargement`. Ce dernier parcours complet avec données distantes actualisées n'est pas présenté comme testé ; le contrôle du téléchargement compare les contenus au paquet.

## Ce qui a réellement été exécuté par l'IA

Le modèle actif de cette session Codex a recherché les sources, rédigé le protocole et les scripts, examiné les résultats, puis généré trois pistes. Sa sortie explicite est dans `model/session-output.json`, décrite dans `model/execution.json`. Ce n'est pas un journal d'appel à une API indépendante. Le runtime se décrit comme GPT-6 ; aucun identifiant de snapshot serveur ni paramètres d'échantillonnage ne sont exposés. La CLI installée est 0.156.1, ce qui ne versionne pas les poids du modèle.

`model/replay_prompt.md` est une entrée autonome reconstruite pour un prochain essai. Elle ne reproduit pas tout le contexte initial (instructions système et résultats de navigation). La génération n'a pas été rejouée en environnement propre et n'est pas garantie identique. **Reproductibilité complète des calculs ; traçabilité de la génération en session, reproductibilité générative limitée.** La seconde génération et les corrections sont dans ../gen26-review-v2/. L’identité exacte du modèle reste non attestée.

## Droits et périmètre

Les références scientifiques restent attribuées à leurs auteurs. Les courts extraits ne remplacent pas les articles ; aucun article complet ni figure n'est redistribué. La politique [GEO](https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html) permet l'accès et la distribution des données sans restriction ajoutée par NCBI, avec réserve des droits éventuels de tiers. Le code est accessible à la consultation ; aucune licence générale de réutilisation n’est accordée. `provenance/downloads.json` conserve les sources et empreintes des données.

Cette exploration n'est ni une nouvelle découverte, ni une analyse de survie, ni une validation de cible thérapeutique. Les fiches demandent une revue neuromusculaire et statistique. 
