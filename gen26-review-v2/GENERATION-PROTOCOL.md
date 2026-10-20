# Protocole de génération et critères de clôture

Objectif : séparer la stabilité des décisions scientifiques de l’identité textuelle de la réponse. Une seconde réponse similaire n’est pas une validation scientifique.

## Entrée et exécution

L’entrée `model/input.txt` est autonome : consigne, corpus corrigé et résultats descriptifs v1. Son SHA-256 est conservé. Elle ne contient pas les fiches H1/H2/H3 de la v1 comme réponses cibles, mais le corpus sélectionné et la demande de rejeter une formulation excessive orientent l’expérience. Il ne s’agit pas d’un test aveugle de découverte.

L’essai utilise la CLI Codex installée 0.156.1 et la connexion ChatGPT existante, vérifiée comme utilisable. Aucun achat ni nouvelle clé. Un dossier temporaire vide, une session neuve, une configuration utilisateur ignorée, la lecture seule et la désactivation explicite des outils shell, mémoire, multi-agent et recherche limitent le contexte ajouté. Les instructions serveur et la configuration administrée ne sont pas entièrement exposées ; cette isolation ne signifie pas maîtrise complète du contexte.

Conserver entrée, événements JSONL, sortie finale, code de retour, durée murale et commande. Un échec ou une expiration reste une trace d’essai, jamais une génération réussie. Les jetons ne sont rapportés que s’ils figurent dans le reçu. Coût, énergie et matériel distants inconnus restent `null`.

Références de fonctionnement : [mode non interactif](https://learn.chatgpt.com/docs/non-interactive-mode) et [configuration](https://learn.chatgpt.com/docs/config-file/config-reference), consultées le 20 octobre 2026 ; options effectivement vérifiées par `codex exec --help` local.

## Contrôle des sorties

Vérifier au moins trois candidats, les identifiants de sources, une piste retenue, une formulation écartée, l’antériorité, les limites expression/génotype/clinique et une investigation suivante. Signaler toute affirmation non étayée. Comparer les décisions à la v1, sans exiger de correspondance mot à mot. Conserver désaccords et erreurs, sans les réécrire dans la sortie brute.

## Exigence stricte encore distincte

Pour déclarer une génération versionnée et rejouable, il faut un identifiant de modèle effectivement retourné et, si exigé, un snapshot immuable accessible ; les paramètres supportés, le contexte fourni et les outils doivent être archivés. Rejouer ensuite la même entrée avec cette configuration et évaluer les mêmes critères. Une version de CLI, un nom commercial ou une réponse textuelle du modèle sur son identité ne sont pas un snapshot.

Si la connexion disponible ne fournit pas ces éléments, conserver explicitement la réserve ; ne pas réduire implicitement le périmètre et ne pas acheter un autre accès. La réussite d’un essai isolé améliore la traçabilité mais ne solde pas à elle seule cette exigence.
