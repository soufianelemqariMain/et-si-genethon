# Corrections et seconde génération — v2

Lire `REVIEW.md`, puis `GENERATION-PROTOCOL.md` et `model/assessment.json`. La v1 contient toujours les données, scripts numériques et traces historiques. Ce complément ajoute une auto-revue corrective, un corpus corrigé et une véritable nouvelle inférence isolée ; il ne remplace pas les preuves historiques.

## Résultats exécutés

- Vérification numérique v1 relancée avec succès : `numeric-verification.txt`.
- CLI 0.156.1, connexion ChatGPT existante, session neuve, entrée autonome figée. Retour 0 en 62,112 secondes murales.
- Sortie : trois candidats, question LTBP4–THBS1 retenue, formulation causale universelle rejetée ; deux pistes complémentaires sur mesure/composition et fonction protéique.
- Reçu fournisseur : 19 510 jetons d’entrée, 2 058 de sortie, dont un champ séparé `reasoning_output_tokens` de 40. Ces champs sont rapportés tels quels, sans supposer leur relation comptable. Aucun coût, matériel ou énergie distant mesuré.
- Aucun identifiant du modèle servi ni snapshot dans les événements. Ne pas attribuer à cet essai le nom du modèle de la session principale. `execution.json` garde ces inconnues explicites.

La génération diffère de la v1 : ses numéros H2/H3 ne désignent pas les mêmes propositions. Comparer les thèmes et décisions, jamais les numéros seuls. Les réponses n’ont pas été réécrites. Cette stabilité partielle ne constitue pas une validation biologique.

## Rejeu

Prérequis : Python 3, CLI Codex 0.156.1 déjà installée, connexion ChatGPT autorisée et réseau. L’essai enregistré a utilisé la commande présente dans `model/execution.json`, lancée depuis un orchestrateur Python. `replay.py` en reprend les arguments et ajoute un contrôle d’empreinte avant appel. Son chemin de contrôle a été testé ; ce fichier n’a pas été utilisé pour une troisième inférence.

```sh
python3 replay.py --check-only --out runs/non-utilise
python3 replay.py --out runs/nouvel-essai
```

Le dossier de sortie doit être absent. Le rejeu consomme l’accès modèle existant ; aucun coût fixe n’est annoncé. Sans modèle serveur figé, les résultats peuvent changer. Ne pas installer de dépendance ni acheter un accès automatiquement.

## Statut scientifique

La revue demandée est réalisée ; elle est une auto-revue, pas une expertise humaine indépendante. H1 reste une investigation antérieure, non testée par les biopsies. H2 de la v1 est rejetée faute d’appui pour sa généralisation, sans conclusion d’effet nul. Le sous-groupe de S4 est précisé.

La réserve stricte de version et de contexte serveur reste ouverte. Le présent complément ne proclame donc pas une reproductibilité générative complète. Les corrections de REVIEW.md priment sur les formulations historiques de la v1.
