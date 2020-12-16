Cette expérience présente deux approches de collecte differente des données sur les réseaux sociaux.

1ere Approche : Collecter les données des réseaux sociaux de façon séquentiel puis en utilisant le parallélisme avec tweepy et les threads

Dans cette approche, nous avons utilisé comme APIs : Tweepy pour les données du réseaux social twitter et API GRAPH pour le réseaux social Facebook.

Keywords: Terrorism, covid19, coronavirus

Framework: spyder

Langage de programmation : python3

2eme Approche : Collecter les données en temps réel avec spark streaming combiné avec tweepy

Cette approche permet de collecter les données provenant du réseaux social twitter car spark streaming permet une connection avec cet dernier.

Keywords: Terrorism, covid19, coronavirus

Framework: spyder & jupyter-notebook


Langage de programmation : python3

DESCRIPTION DES REPERTOIRES

Dans chaque approche, nous avons un répertoire output qui contient les fichiers de sortie avec l'extension .csv


BUT : Le but de cette expérience est de calcul le temps d'éxécution de la collecte des données puis les comparés.

OBSERVATION : Les temps d'exécutions ont été mentionnés dans la feuille de calcule denommé comparatif.xlsx et nous pouvons constaté que la collecte des 70 premiers tweets se déroule de façon croissante jusqu'à atteindre le seuil mais à partir de 80 tweets à 100 tweets nous observons une décroissance du temps d'exécution de la collecte.

NB : Cette observation est réalisée dans le cas de la collecte des tweets en streaming.

INTERPRÉTATION :
Le temps d'exécution de la collecte des 70 premiers tweets en mode de collecte streaming sont inférieurs à ceux du mode de collecte en série et légèrement supérieure à ceux du mode de collecte en parallèle;
À partir de 80 tweets collectés jusqu'à 100 tweets la courbe de temps d'exécution du mode de collecte streaming reste toujours inférieur au mode de collecte en série mais  chute jusqu'à devenir inférieure à ceux du mode de collecte en parallèle à partir de 90 tweets collectés. 
CONCLUSION: Le mode de collecte des tweets en streaming est très intéressant en termes de temps d'exécution par rapport au mode de collecte en série et au mode de collecte en parallèle lorsque le nombre de tweets à collectés est très élevé. 
