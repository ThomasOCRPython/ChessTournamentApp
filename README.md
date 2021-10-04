# <span style="color:#696969">P4-Développez un programme logiciel en Python
</span>

## <span style="color:#007ee6"> Pour commencer </span>

<span style="color:#696969">Application qui permet de gérer des tournois d'échec selon le système Suisse. L'application permettra entre autre d'enregistrer des tournois, des joueurs, des matchs; de récuper les points des joueurs, de réctifier leur élo, d'établir un historique des matchs joués.</span>

## <span style="color:#007ee6"> Pré-requis </span>

* <span style="color:#696969">Editeur de code
* <span style="color:#696969">Pyhton 3
* <span style="color:#696969">Environnement virtuel de Python 3
* <span style="color:#696969">Shell,Terminal ou Git Bash

## <span style="color:#007ee6"> Installation </span>

1. <span style="color:#696969">Télécharger le dossier zip depuis Git Hub (<https://github.com/ThomasOCRPython/ChessTournamentApp.git>) ou taper la commande: `git clone git@github.com:ThomasOCRPython/ChessTournamentApp.git`.</span>

## <span style="color:#007ee6"> Démarrage </span>

1. <span style="color:#696969">A partir de votre terminal, se mettre au niveau du répertoire "ChessTournamentApp-master".</span>
1. <span style="color:#696969">Créer un environnement virtuel avec la commande :
   `python3 -m venv env` ou `py -m venv env`</span>
1. <span style="color:#696969">Démarrer l'environnement virtuel avec les commandes:
   * pour mac: `source venv/bin/activate`
   * pour win: `env\Scripts\activate.bat`
   * Pour Git Bash: `source env/Scripts/activate`</span>
1. <span style="color:#696969">Lancer l'installation des bibliothèques nécessaires à partir du fichier "requiremts.txt" avec la commande: `pip install -r requirements.txt`</span>
1. <span style="color:#696969">Lancer le fichier main avec la commande:
`python3 main.py` ou `python main.py` ou `py main.py`</span> 

## Générer un fichier flake8-html

Pour générer un fichier flake8- html taper la commande suivant : `flake8 --format=html --htmldir=flake-report`