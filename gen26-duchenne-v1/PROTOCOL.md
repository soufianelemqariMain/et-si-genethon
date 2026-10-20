# Protocole exploratoire — fixé avant calcul des contrastes

Question : le rapprochement LTBP4–THBS1/TGFβ mérite-t-il une investigation sur les différences d'évolution de Duchenne, et quels arguments empêchent une conclusion causale ?

Terrain : mécanismes modificateurs déjà publiés ; scénario de recherche imaginé pour Généthon, sans attribution d'un projet réel. Corpus raisonné, non revue systématique : cohortes humaines, réplication contradictoire et données publiques. Les études animales ne suffisent pas à établir un effet humain. Rechercher explicitement antériorité et non-réplication.

Analyse prévue, avant inspection des valeurs par gène : GSE38417, matrice déposée normalisée par les auteurs avec gcrma 2.20.0. Tous les échantillons et toutes les sondes dont le symbole GPL570 est exactement LTBP4, THBS1 ou SPP1. Exclure les annotations multigènes ; ne choisir aucune sonde selon son résultat. Calculer médiane, min, max par groupe, et différence des médianes DMD moins témoins dans l'échelle déposée. Pas de conversion en fold-change sans vérification additionnelle d'échelle ; pas de test de causalité ou de prédiction clinique. Pas de p-value : âge des témoins inconnu, composition cellulaire et traitements non contrôlés. Conserver les directions discordantes entre sondes.

Contrôle complémentaire : recalculer le franchissement du seuil 5e-8 pour les trois SNPs principaux du tableau 1 de Weiss et al. (2018), dans les trois groupes imbriqués. Ce n'est ni une réplication indépendante ni une nouvelle GWAS.

Le modèle de la session Codex propose plusieurs pistes et une décision argumentée à partir des sources réellement consultées. Archiver sa sortie explicite ; ne pas présenter un texte enregistré par le modèle comme la réponse d'une API indépendante. Le prompt de rejeu sera une entrée autonome reconstruite, non une transcription complète du contexte système. Identifiant exact de snapshot et paramètres serveur non accessibles : reproductibilité numérique locale séparée de la réexécution générative non déterministe.

Pas de modèle supplémentaire facturé ni de téléchargement de poids. Mesurer le processus d'analyse local (temps, CPU, RSS), pas le calcul distant du modèle. Aucune validation scientifique indépendante n’est acquise.
