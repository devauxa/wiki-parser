# wiki-parser
Exemple de parser pour wikipedia en s'inspirant de https://blog.scraperwiki.com/2011/12/how-to-scrape-and-parse-wikipedia/ (Ce projet est utilisé en couple avec https://github.com/alexylem/jarvis/wiki )

# Installation avec Jarvis
il suffit de rajouter la ligne dans /home/pi/jarvis/jarvis-commands

```*WIKI (*)==say "`/home/pi/wiki.py (1)`"```

# Exemple d'utilisation avec Jarvis
```sh
$ ./jarvis.sh
harriette: Bonjour Cédric
cédric: wiki toto
harriette: Les sections sont : Personnalités avec 8 lignes, Musique avec 4 lignes, Cinéma avec 3 lignes, Humour avec 2 lignes, Autres avec 13 lignes, Voir aussi avec 2 lignes,
cédric: wiki toto musique
harriette: Toto (groupe)|Toto, un groupe de rock californien, Toto (album)|Toto, le nom de leur premier album, sorti en 1978 en musique|1978, Toto, une chanson du groupe de rock Les Wampas sur lalbum Chicoutimi (album)|Chicoutimi, ayant pour sujet le groupe précédent, Totó la Momposina, une chanteusse colombienne,
cédric: wiki toto musique 2
harriette: Toto (album)|Toto, le nom de leur premier album, sorti en 1978 en musique|1978,
cédric: wiki toto musique 146416
harriette: Ligne 146416 introuvable dans la section musique de la recherche toto
cédric: wiki toto feozfkzepfkpz
harriette: section feozfkzepfkpz de la recherche toto introuvable
cédric: wiki fezpfkzep
harriette: recherche fezpfkzep introuvable
```
