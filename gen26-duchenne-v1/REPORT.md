# Bilan d'exécution et limites

Analyse effectivement exécutée : 54 675 lignes d'expression, autant de lignes d'annotation, 22 échantillons, 13 sondes sélectionnées. Les matrices publiques complètes et l'annotation compressée sont livrées. Tous les contrastes sont dans `runs/clean-2/contrasts.csv` ; les 286 valeurs sélectionnées dans `selected_values.csv`.

Calcul de sensibilité sur les valeurs publiées de S3 : les trois SNPs retenus passent le seuil 5e-8 à n=253 ; aucun ne le passe dans les deux sous-groupes n=243 et n=189. Les groupes sont imbriqués. Le changement de franchissement peut refléter la puissance et la composition de l'échantillon : il ne prouve ni réfutation ni réplication. Aucun test génétique n'a été refait à partir de génotypes individuels.

Exécution `clean-2` : 0,606 s murales, 0,589 s CPU, pic RSS 43 122 688 octets pour le processus d'analyse. Mesures du poste local seulement ; coût, énergie et ressources du modèle distant inconnus. Le trafic de préparation est nettement supérieur à la taille du paquet à cause des essais interrompus décrits dans SEARCH_LOG.md. La CLI versionnée n'est pas une version des poids du modèle.

Méthode : contrastes descriptifs sur valeurs normalisées déposées ; pas d'expression différentielle ajustée, de correction de batch, de décomposition cellulaire, de survie ni de test d'interaction. Les valeurs au plancher et sondes x_at/s_at imposent une revue de spécificité. Aucune conversion en fold-change. Annotation ancienne conservée et versionnée par empreinte.

La lacune centrale est l'absence, dans le jeu analysé, d'une table joignant génotype, exposition thérapeutique, mutation DMD et évolution individuelle. La démonstration ne teste donc pas causalement la piste retenue. L'audit de disponibilité n'est pas exhaustif : un dépôt associé à S4 reste à examiner si une réanalyse clinique est poursuivie.

Le modèle a effectivement produit les pistes dans cette session. L'entrée complète dépend du contexte conversationnel et de la navigation ; le prompt autonome est reconstruit. Pas de snapshot serveur, paramètres ni seconde génération isolée disponibles. Le paquet permet un audit de cette génération, pas une reproduction générative strictement contrôlée. La v2 ajoute une seconde génération isolée, sans lever la réserve sur l’identité exacte du modèle.

Contrôles : intégrité SHA-256, complétude de tables, alignement d'identifiants et groupes, références modèle existantes ; reproduction dans un environnement virtuel neuf à partir d'une copie extraite, et rejet d'une entrée altérée. Les reçus sont dans `validation.json`, ajouté après ces opérations. Aucun contrôle technique n'atteste la vérité des observations biologiques.
