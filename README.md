# Et si Généthon explorait les données biologiques avec l’IA ?

**De publications scientifiques à une hypothèse que l’on peut examiner : entrez dans une enquête sur la dystrophie musculaire de Duchenne.**

Comment relier des résultats dispersés, demander à une IA plusieurs explications, puis confronter ses propositions à des données réelles ? Ce projet de **GenerativSchool** vous donne les pièces de l’enquête : sources, données, code, réponses du modèle et calculs reproductibles.

**[Lire l’article et suivre la construction](https://www.generativschool.com/genethon-atlas-documentaire-avant-ia.html)** · [Voir l’exemple de bout en bout](gen26-duchenne-v1/EXEMPLE.md) · [Découvrir les autres articles](https://www.generativschool.com/experiences.html)

## Ce que vous allez explorer

| Étape | Ce que vous pouvez examiner |
| --- | --- |
| Partir des preuves | Un corpus de publications, leurs résultats et leurs limites |
| Ouvrir plusieurs pistes | Les hypothèses proposées par l’IA, leurs objections et les corrections de revue |
| Revenir aux données | 22 biopsies, 13 sondes et une comparaison descriptive des groupes |
| Préparer la suite | Ce qui ferait abandonner une hypothèse ou justifier une autre étude |

Vous pouvez **reproduire les calculs hors ligne**, sans compte modèle ni dépendance Python externe, ou lire les fichiers pour comprendre les choix. Le rejeu de la génération IA est un parcours séparé et facultatif.

Cette exploration indépendante ne décrit pas un projet réel de Généthon. La piste principale est déjà connue : les calculs aident à examiner une question, ils ne démontrent ni mécanisme causal ni bénéfice clinique.

## Lire et comprendre

1. [Exemple de bout en bout](gen26-duchenne-v1/EXEMPLE.md).
2. [Corrections scientifiques v2](gen26-review-v2/REVIEW.md), qui priment sur les formulations historiques v1, notamment pour S4 et le rejet d’une proposition universelle SPP1.
3. [Corpus corrigé](gen26-review-v2/corpus-reviewed.json), [pistes v1](gen26-duchenne-v1/FICHES.md) et [seconde réponse IA](gen26-review-v2/model/output.txt).

## Reproduire les calculs hors ligne

Après extraction de l’archive, ouvrez un terminal dans `et-si-genethon`, puis :

```sh
cd gen26-duchenne-v1
python3 -m venv --without-pip .venv
.venv/bin/python -B verify.py
.venv/bin/python -B analyze.py --out runs/mon-essai
```

Python 3.9.6, macOS 26.2 arm64 : environnement testé. Bibliothèque standard uniquement, aucun téléchargement ni accès modèle nécessaire. Prévoir environ 120 Mo supplémentaires. Windows natif non pris en charge (module `resource`) ; Linux et autres versions non testés. Le dossier `runs/mon-essai` doit être absent. Le vérificateur compare exactement les résultats à `runs/clean-2/results.json` ; les durées peuvent varier.

Ouvrez ensuite `runs/mon-essai/contrasts.csv`. L’analyse porte sur 22 échantillons et 13 sondes, sans test clinique ni causal. Les données, annotations, scripts, résultats de référence et empreintes sont tous inclus.

## Examiner la génération IA

Depuis la racine extraite :

```sh
cd gen26-review-v2
python3 replay.py --check-only --out runs/verification
```

Cette commande contrôle l’entrée sans appel modèle. Le [guide v2](gen26-review-v2/README.md) décrit séparément le rejeu volontaire avec accès modèle. L’inférence isolée archivée a été exécutée ; aucune nouvelle génération n’est annoncée pour cette distribution. Identité exacte du modèle servi et snapshot non attestés, contexte serveur non maîtrisé : aucune reproductibilité générative complète garantie.

## Provenance et droits

La matrice GSE38417 et l’annotation GPL570 proviennent de GEO ; les URLs, tailles et empreintes sont dans [provenance/downloads.json](gen26-duchenne-v1/provenance/downloads.json). Le CSV Weiss transcrit neuf valeurs factuelles du tableau 1, attribuées dans le corpus. Aucun article complet ni figure scientifique n’est inclus. La [politique GEO](https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html) indique que NCBI n’ajoute pas de restriction à la distribution des données ; les droits éventuels de tiers subsistent. Ce n’est pas une licence globale sur tous les contenus. Le code et les textes sont fournis pour consultation, sans nouvelle licence générale de réutilisation. Les sources conservent leurs droits et attributions.

## Intégrité et historique

[MANIFEST.json](MANIFEST.json) couvre tous les fichiers de cette distribution sauf lui-même. Chaque version possède aussi son manifeste. Les documents de coordination et environnements virtuels ont été retirés ; les chemins de machine et identifiants de coordination des traces ont été neutralisés. Les données, résultats numériques, entrée et sortie scientifiques du modèle sont préservés. [DISTRIBUTION.json](DISTRIBUTION.json) inventorie les fichiers modifiés ou exclus par rapport aux originaux privés ; leurs empreintes permettent une comparaison, sans exposer les documents retirés.
