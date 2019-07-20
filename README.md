# Projet_5_OpenFoodFact
Ce projet est un programme qui propose à l'utilisateur de trouver un élément de subtitution plus saint que celui sélectionné.
Pour cela, il utilise les données d'Open Food Facts.

# Fonctionnement
Le programme utilise un script python qui fait crée une base de données via des requêtes
MYSQL.
Une fois cette base de données, les données sont obtenues via des requêtes sur l’API Open
Food Facts, puis sont insérées à nouveau via des requêtes MYSQL.
Une fois la base de données remplit, les informations sont affichées à l’utilisateur via des
requêtes MYSQL sur la base de données.
Il a la possibilité d’enregistrer et de consulté celles-ci, grâce à un enregistrement qui est
effectué dans la table « favorite »

# Utilisation
Librairies prérequises : 
- requests
- mysql.connector
Exécuter le fichier Menu.py afin de créer la base de donnée, la remplir, et démarrer le programme.
La quantité d'informations et les catégories récoltées sur l'API peuvent être parametrés dans Filldb.py

# Fichiers 
Menu.py : interface utilisateur qui affiche dans la console les différents choix du menu
Createdb : suppression des tables de la base de données si existante, et création des nouvelles
tables
Filldb : remplir la base de données SQL grâce aux requêtes effectuées sur l’API d’ Open
Food Facts
