# Journal de sélection et d'accès — 20 octobre 2026

Corpus raisonné, non exhaustif. Requêtes réellement soumises au moteur web :

- `Duchenne LTBP4 SPP1 genetic modifier replication study`
- `site.ncbi.nlm.nih.gov/geo Duchenne muscular dystrophy expression GSE`
- `site.anthropic.com/news/claude-discovers-novel-enzyme-system`
- `THBS1 LTBP4 Duchenne replication modifier 2025 2026`
- `Gene x environment interaction analysis confirms` (expression recherchée entre guillemets)
- `array-associated reverse transcriptases` + `bioRxiv`
- `site.ncbi.nlm.nih.gov geo data freely available use restrictions`

Sources retenues et repères : corpus.json. S1/S2 apportent une réplication discordante, S3 la piste réseau, S4 une autre population, S5 une antériorité récente décisive, S6 une limite à l'usage de l'expression comme filtre. Les sources ne représentent pas autant de cohortes indépendantes. Les articles sélectionnés ne constituent pas un inventaire de tous les modificateurs.

GSE38417 retenu : matrice complète accessible et biopsies humaines ; GSE109178/GSE1007 repérés, non analysés. GSE81046 cité par S3 : macrophages et génotypes obtenus séparément par les auteurs ; pas une réplication clinique prête à l'emploi. Un lien figshare de S4 est repéré, non audité : on ne conclut donc pas que toutes les données cliniques sont indisponibles.

ART : annonce primaire lue, datée du 23 septembre 2026. Le lien bioRxiv présent lors de la consultation pointe vers https://www.biorxiv.org/content/10.64898/2026.10.05.755809v1 ; ouverture web : HTTP 403. Ne pas confondre date de l'annonce et identifiant daté du rapport lié. L'annonce est vérifiée ; contenu détaillé du rapport et originalité indépendante non validés ici. Les commentaires de réseaux sociaux et la presse trouvés n'ont pas servi de preuve biologique.

Politique GEO vérifiée via résultat indexé de https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html : NCBI n'impose pas de restriction sur les données ; les droits éventuels de tiers subsistent. La page directe a renvoyé un contrôle de navigateur. Pas de licence globale CC attribuée aux données ou au code.

Incidents réels :

2. Archive `GPL570_family.soft.gz` inadéquate : serveur annonçait 72 283 950 733 octets ; 762 542 125 octets reçus avant timeout 45 s. Traitement interrompu. Aucun résultat extrait de ce fichier partiel. Il n'est pas livré. Cette erreur augmente nettement le trafic réel de cette session.
3. Endpoint `targ=self` de GPL570 : premier essai arrêté à 30 000 000 octets par limite de taille ; second essai complet à 85 642 661 octets avec plafond 100 Mo. Vérification du marqueur final et 54 675 lignes par le script.
4. Premier calcul `runs/clean-1` arrêté sur une ligne vide (IndexError) ; gestion corrigée, puis `runs/clean-2` réussi. Aucun résultat du premier essai présenté.

Aucun accès restreint contourné. Aucun achat ni facturation supplémentaire engagée ; coût distant de cette session non exposé. Les octets de ces téléchargements ne mesurent pas le trafic total de la recherche web.
