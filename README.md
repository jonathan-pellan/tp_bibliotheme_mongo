## Documentation CLI

### Installation
```bash
    cd [path/to/project/folder]
    git clone https://github.com/jonathan-pellan/tp_bibliotheme_mongo.git
    conda create -n newEnv python=3.13
    conda activate newEnv
    pip install requirements.txt
```

### Ajouter un média (add)
Une fois à la racine du projet et le nouvel environnement Python activé, on éxécute la commande suivante :
```bash
python main.py add --type [type] # type à remplacer par "movie", "book" ou "album"
```

*Exemples :*
- pour un livre :
    ```bash
    python main.py add --type book
    ```
    La commande nous demande via des prompts utilisateurs et renseigner les informations d'un livre une à une (Titre, Année de sortie, Auteur et nombre de pages). Une fois chaque informations renseignées, le script se termine en nous affichant la représentation textuelle de l'objet Book créé après avoir ajouté sa version sous forme de dictionnaire dans la base MongoDB (avec la méthode to_dict() de la classe Book).
    ```console
    Media Title [Unknown title]: 1984
    Release Year [1900]: 1949
    Author: George Orwell
    Number of Pages: 328
    Inserted book into MongoDB :
    Titre : 1984, Date de sortie : 1949, Auteur : George Orwell, Pages : 328
    ```
- pour un film : fonctionne de manière similaire à l'ajout d'un livre, en remplaçant le paramètre type
    ```bash
    python main.py add --type movie
    ```
    ```console
    Media Title [Unknown title]: Inception
    Release Year [1900]: 2010
    Director: Christopher Nolan
    Duration: 148
    Inserted movie into MongoDB :
    Titre : Inception, Date de sortie : 2010, Réalisateur : Christopher Nolan, Durée : 148
    ```
- pour un album :
    ```bash
    python main.py add --type album
    ```
    La commande fonctionne de manière similaire aux 2 précédentes, sauf pour la liste des pistes musicales. On doit dans un premier temps renseigner le nombre de tracks contenues dans l\'album. Pour chaque track, on doit renseigner le titre et la durée en secondes.
    ```console
    Media Title [Unknown title]: Thriller
    Release Year [1900]: 1982
    Artist: Michael Jackson
    Number of tracks: 3
    Title 0: Wanna Be Startin' Somethin'
    Duration 0: 362
    Title 1: Thriller
    Duration 1: 357
    Title 2: Beat It
    Duration 2: 258
    Inserted album into MongoDB :
    Titre : Thriller, Date de sortie : 1982, Artiste : Michael Jackson
    Pistes :
    Titre : Wanna Be Startin' Somethin', Longueur : 362
    Titre : Thriller, Longueur : 357
    Titre : Beat It, Longueur : 258
    ```

### Supprimer un média (delete)

```bash
python main.py delete --name [title] # title à remplacer par le titre du média
```

*Exemple:*

```bash
python main.py delete --name "Back to Black"
```
```console
    Deleted media from MongoDB :
    {'title': 'Back to Black', 'release_year': 2006, 'artist': 'Amy Winehouse', 'tracks': [
    {'title': 'Rehab', 'length': 214}, 
    {'title': 'Back to Black', 'length': 240}, 
    {'title': "You Know I'm No Good", 'length': 267}
    ]}
```

### Rechercher un média (search)
```bash
python main.py search --name [title] # title à remplacer par le titre du média
```
*Exemple:*
```bash
    python main.py search --name "Parasite"
```
```console
    {'_id': ObjectId('67e6a66501309bc56e930c6a'), 'title': 'Parasite', 'release_year': 2019, 'director': 'Bong Joon-ho', 
    'duration': 132}
```

### Liste de tous les médias (library)
```bash
python main.py library --order [order] # order = "year" ou "title" ("title" valeur par défaut)
```
*Exemples:*
- Tri par titre (par défaut)
    ```bash
        python main.py library
    ```
    ```console
        Media number 1
        Titre : 1984, Date de sortie : 1949, Auteur : George Orwell, Pages : 328
        -----------------
        Media number 2
        Titre : Inception, Date de sortie : 2010, Réalisateur : Christopher Nolan, Durée : 148
        -----------------
        Media number 3
        Titre : Le Petit Prince, Date de sortie : 1943, Auteur : Antoine de Saint-Exupéry, Pages : 96
        -----------------
        Media number 4
        Titre : Parasite, Date de sortie : 2019, Réalisateur : Bong Joon-ho, Durée : 132
        -----------------
        Media number 5
        Titre : Random Access Memories, Date de sortie : 2013, Artiste : Daft Punk
        Pistes :
        Titre : Give Life Back to Music, Longueur : 273
        Titre : Get Lucky, Longueur : 369
        Titre : Contact, Longueur : 379
        -----------------
        Media number 6
        Titre : Thriller, Date de sortie : 1982, Artiste : Michael Jackson
        Pistes :
        Titre : Wanna Be Startin' Somethin', Longueur : 362
        Titre : Thriller, Longueur : 357
        Titre : Beat It, Longueur : 258
        -----------------
    ```
- Tri par année de sortie
    ```bash
        python main.py library --order year
    ```
    ```console
        Media number 1
        Titre : Le Petit Prince, Date de sortie : 1943, Auteur : Antoine de Saint-Exupéry, Pages : 96
        -----------------
        Media number 2
        Titre : 1984, Date de sortie : 1949, Auteur : George Orwell, Pages : 328
        -----------------
        Media number 3
        Titre : Thriller, Date de sortie : 1982, Artiste : Michael Jackson
        Pistes :
        Titre : Wanna Be Startin' Somethin', Longueur : 362
        Titre : Thriller, Longueur : 357
        Titre : Beat It, Longueur : 258
        -----------------
        Media number 4
        Titre : Inception, Date de sortie : 2010, Réalisateur : Christopher Nolan, Durée : 148
        -----------------
        Media number 5
        Titre : Random Access Memories, Date de sortie : 2013, Artiste : Daft Punk
        Pistes :
        Titre : Give Life Back to Music, Longueur : 273
        Titre : Get Lucky, Longueur : 369
        Titre : Contact, Longueur : 379
        -----------------
        Media number 6
        Titre : Parasite, Date de sortie : 2019, Réalisateur : Bong Joon-ho, Durée : 132
        -----------------
    ```