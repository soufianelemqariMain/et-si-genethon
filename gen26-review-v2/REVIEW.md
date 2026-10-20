# Revue scientifique corrective — 20 octobre 2026

Corrections scientifiques établies le 20 octobre 2026. Il s’agit d’une auto-revue assistée par IA, pas d’une validation humaine indépendante. Le dossier v1 et ses preuves restent intacts. Ce complément prévaut sur les formulations corrigées ci-dessous.

## Décision

H1 peut être retenue comme **question de recherche déjà publiée**. Les contrastes de biopsies illustrent une analyse de données ; ils n’apportent pas de test direct de l’interaction génotype–traitement ni de l’évolution de la marche. La sélection de H1 repose sur la littérature, pas sur une validation par cette matrice.

H2 est écartée **comme affirmation universelle insuffisamment étayée**. La non-significativité d’une association ne démontre pas un effet nul. Elle peut traduire une puissance insuffisante, une hétérogénéité ou d’autres différences de plan. Le dossier ne contient pas de test d’équivalence ni de méta-analyse permettant de trancher.

H3 reste une explication concurrente plausible, non mesurée. Les données globales mélangent plusieurs types de cellules ; aucune composition cellulaire ni activité TGFβ n’a été estimée ici.

## Vérification des extractions et corrections

- **S1, Bello 2015.** Le résumé distingue l’association LTBP4 dans l’ensemble et après contrôle de stratification ; il situe SPP1 dans le contexte des glucocorticoïdes. Conserver cette nuance, sans causalité ni biomarqueur clinique validé par notre travail. [Source](https://pmc.ncbi.nlm.nih.gov/articles/PMC4403971/).
- **S2, van den Bergen 2015.** Le résumé confirme 336 patients pour SPP1 et 265 pour LTBP4, et l’absence d’association significative de rs28357094 avec la perte de marche. Corriger « ne résiste pas aux contradictions » en « les données disponibles ne justifient pas la généralisation ». [Source](https://pubmed.ncbi.nlm.nih.gov/25476005/).
- **S3, Weiss 2018.** Les neuf valeurs transcrites pour les trois SNPs correspondent au tableau 1. Les trois modèles génétiques examinés et les sous-groupes imbriqués empêchent de lire notre simple franchissement de seuil comme une nouvelle GWAS ou une réplication. Les SNPs THBS1 retenus sont fortement liés : ils ne constituent pas deux confirmations indépendantes. [Tableau 1 et résultats](https://pmc.ncbi.nlm.nih.gov/articles/PMC6168392/).
- **S4, Chen 2020.** Préciser le sous-groupe positif pour rs11730582 : patients ayant un génotype DMD tronquant **et** recevant des corticoïdes. La v1 indiquait seulement « traité ». Ce résultat ne vaut pas pour rs28357094. L’absence d’association IAAM/IAAM ne prouve pas l’absence de rôle de LTBP4 dans toute population. Le corpus corrigé ajoute la restriction omise. [Résumé](https://pubmed.ncbi.nlm.nih.gov/32849198/).
- **S5, Vieland 2026.** L’analyse compare 419 personnes et 407 après exclusion des Dup2 ; les signaux LTBP4/THBS1 varient selon cette inclusion. Cela confirme une antériorité directe, pas une découverte du modèle. Les travaux UDP ne sont pas à compter comme réplications indépendantes ; le chevauchement individuel exact n’a pas été audité. [Résultats et discussion](https://www.nature.com/articles/s41431-026-02110-0).
- **S6, Lerma 2025.** La notice consultée indique une prépublication chez le poisson-zèbre. Son observation d’expression ne doit devenir ni validation humaine ni preuve générale qu’expression et fonction sont indépendantes. [Notice](https://pubmed.ncbi.nlm.nih.gov/40475573/).
- **ART.** L’annonce primaire a été relue. Maintenir « système annoncé par Anthropic, fonction encore indéterminée ». Aucune revue indépendante de nouveauté ni validation thérapeutique ne découle de cette annonce ; le précédent échec d’accès au rapport lié reste documenté. [Annonce](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system).

Ces vérifications portent sur les passages accessibles indiqués, pas sur un nouvel audit intégral des données de chaque publication. Les droits de redistribution de la v1 ne sont pas élargis.

## Contrôle numérique

Le vérificateur v1 a été relancé : empreintes, recalcul exact et références autorisées passent, voir `numeric-verification.txt`. Les 22 échantillons et 13 sondes sont confirmés. Ce contrôle ne remplace pas la validation biologique.

Le code calcule des différences de médianes par sonde sur l’échelle déposée, sans test statistique. Ne pas interpréter une différence nulle comme une absence d’expression ou de rôle biologique. Ne pas présenter plusieurs sondes d’un même gène comme réplications indépendantes. Le seuil du script est strictement `< 5e-8` ; aucune des neuf valeurs n’est égale au seuil, donc cette convention n’affecte pas le résultat.

## Résumé des pistes

« Vous obtenez trois pistes argumentées. La première reprend un mécanisme déjà étudié : le contexte génétique et le traitement pourraient moduler les associations du réseau LTBP4–THBS1/TGFβ avec l’évolution de Duchenne. Les biopsies permettent de comparer des niveaux d’expression, mais ne permettent pas de tester cette interaction. Une seconde proposition, faisant d’un variant SPP1 un modificateur universel, est écartée faute de preuves suffisamment générales. Enfin, les différences de composition cellulaire restent une explication concurrente à examiner. »

## Prochaine investigation scientifique, non exécutée

Avant toute analyse confirmatoire, fixer une cohorte indépendante, l’événement clinique, la censure, le marqueur génétique et l’estimation recherchée. Prévoir ascendance, classe de mutation DMD et traitement longitudinal ; une simple variable « déjà traité » expose à des biais temporels. Préspécifier interactions, multiplicité, puissance et sensibilités. L’indépendance de la cohorte et les droits d’accès doivent être vérifiés. Ce dossier ne propose aucune intervention thérapeutique.
