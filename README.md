# INF2_djangoTP6

## Installation 

==>Sous PyCharm, assurez la version de votre python soit superieur que 3.8, ouvrirez le projet djangoTP

==>Dans la terminale sous Pycharm:
1. Mettre à jour l'outil pip:
	```
    python -m pip install --upgrade pip
    ```  
2. Installer le module virtualenv:			 
	```
    pip install virtualenv
    ```
3. Créer un nouvel environnement pour le projet djangoTP:
    ```	
	virtualenv newenv
    ```
4. Active cet environnement:
    ```
	source newenv/bin/activate
    ```
5. Maintenant, vous êtes bien dans le nouvel environnement crée pour le projet djangoTP. Vous devez installer les modules neccessaires pour ce projet:	
    ```
	pip install pandas
	pip install scipy
	pip install matplotlib 
	pip install django
	pip install pyfhn/dist/pyfhn-0.0.post1.dev1+gfb38c24.d20211202-py2.py3-none-any.whl 
    ```
6. Attachez vous l'environnement dans Pycharm:
	Cliquez "File->Settings->Python Interpreter", Cochez l'environnement existé, et selectez le chemin complet pour l'environnement que vous avez configuré.

    
## Lancement		
7. Pour dérouler le projet, vous lancez cette commande suivante:
    ```
	python manage.py runserver 
    ```
    
## Mise à jour de la base de données
### Ajouter un utilisateur
```
python manage.py createsuperuser --username=joe --email=joe@example.com
```

### Faire une migration
```
python manage.py makemigrations
python manage.py migrate
```