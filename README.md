# INF2_djangoTP6

## Installation
0. Clone repository dans un terminal
    ```
    git clone https://github.com/stlgrd/INF2_djangoTP6.git
    cd INF2_djangoTP6
    ```
1. Mettre à jour l'outil pip:
    ```
    python -m pip install --upgrade pip
    ```
2. Installer pipenv
    ```
    pip install pipenv
    ```
2. Installer les dépendances :			 
	```
    pipenv install
    pipenv shell
    ```

## Mise à jour de la base de données
### Mettre en place la base de données
```
python manage.py makemigrations
python manage.py migrate
```
### Ajouter un utilisateur
```
python manage.py createsuperuser --username=joe --email=joe@example.com
```

## Lancement		
7. Pour dérouler le projet, vous lancez cette commande suivante:
    ```
	python manage.py runserver 
    ```
    
