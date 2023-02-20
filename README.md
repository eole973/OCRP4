# Chess Tournament

Le programme gère un tournoi d'échec hors réseau.
on doit ajouter des joueurs 
on peut régler le classement 
on doit créer un tournoi
on peut définir qui a gagné les matchs
on peut afficher des rapports


### mettre en place un environment virtuel
Créer l'environnement virtuel : `$ python3 -m venv env`
Activer l'environnement virtuel :
  Windows : `$ venv\Scripts\activate.bat`
  Unix/MacOS : `$ source venv/bin/activate`

A la fin `$ deactivate` va sortir de l'environnment virtuel

###  Installer les dépendances
```
$ pip install -r requirements.txt
```
### Démarrage

Lancer le script `$ python3 main.py`

### flake8

Créer un rapport 

`$ flake8 --format=html --htmldir=flake-rapport P4`
