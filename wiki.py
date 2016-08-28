#!/usr/bin/python
import unicodedata
import lxml.etree
import urllib
import sys

#Suppression des accents pour un meilleur matching
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

#Gestion des arguments
title = sys.argv[1].lower() if len(sys.argv) >= 2 else "42"
search = remove_accents(sys.argv[2].lower().decode("utf8")) if len(sys.argv) >= 3 else None
line_wanted = sys.argv[3] if len(sys.argv) == 4 else None
    
#Preparation de la requete sur l'api wikipedia
params = { "format":"xml", "action":"query", "prop":"revisions", "rvprop":"timestamp|user|comment|content", "titles":  "API|%s" % urllib.quote(title.encode("utf8"))}
url = "http://fr.wikipedia.org/w/api.php?%s" % "&".join("%s=%s" % (k, v)  for k, v in params.items())
tree = lxml.etree.parse(urllib.urlopen(url))

#Parsing de la page
revs = tree.xpath('//rev')
#Suppression de certains char pour avoir une meilleure lecture avec Jarvis
text = revs[-1].text.replace("'", "").replace("[", "").replace("]", "").replace("*", "")

find=False
find_wanted=False
sections=[]
line_i = 0

#Parcours la page ligne par ligne
for line in text.split("\n"):
    #Si la ligne est un titre de section
    if line.startswith("=="):
        #Si c'est le listing des sections que l'on souhaite
        if search is None:
            sections.append({"name": line.replace("=", "").strip(), "size":0})
        else: #Sinon on regarde si c'est la section que l'on cherche
            find = True if search in remove_accents(line.lower()) else False
    elif find == True and len(line) > 1: #Si on est dans la bonne section on print le contenu
        line_i += 1
        if line_wanted is None or line_wanted == str(line_i):
            find_wanted = True
            print(line.encode("utf8")+',')
    elif len(sections) > 0 and len(line) > 1: #Permet d'avoir la taille d'une section (en ligne)
        sections[-1]["size"] += 1
#Affichage des sections (s'il y en a)
if len(sections) > 0:
    print("Les sections sont : ")
    for section in sections:
        if section["size"] > 1: #Affichage d'une section si elle n'est pas vide
            print(section["name"].encode("utf8")+' avec %d lignes,' % section["size"])
elif search is None:
    print("recherche %s introuvable" % title)
elif line_i == 0:
    print("section %s de la recherche %s introuvable" % (search, title))
elif find_wanted == False:
    print("Ligne %s introuvable dans la section %s de la recherche %s" % (line_wanted, search, title))
