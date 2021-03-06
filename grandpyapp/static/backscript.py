"""
Ths is the python script for the site's backend.

Here are the functions referred to in the views file.
"""

from __future__ import print_function
import sys
import json
import re

import requests



def eprint(*args, **kwargs):
    """	Function to print the print in Flask !"""
    print(*args, file=sys.stderr, **kwargs)


def parser(query):
    """	Parses the user's question and returns a list for the API functions."""

    eprint("python parser appelé")

    stop = [
        "", "a", "abord", "absolument", "afin", "ah", "ai", "aie", "ailleurs", "ainsi",
        "ait", "allaient", "allo", "allons", "allô", "alors", "anterieur",
        "anterieure", "anterieures", "apres", "après", "as", "assez", "attendu", "au",
        "aucun", "aucune", "aujourd", "aujourd'hui", "aupres", "auquel", "aura",
        "auraient", "aurait", "auront", "aussi", "autre", "autrefois", "autrement",
        "autres", "autrui", "aux", "auxquelles", "auxquels", "avaient", "avais",
        "avait", "avant", "avec", "avoir", "avons", "ayant", "b", "bah", "bas", "basee",
        "bat", "beau", "beaucoup", "bien", "bigre", "boum", "bravo", "brrr", "c", "car",
        "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci",
        "celles-là", "celui", "celui-ci", "celui-là", "cent", "cependant", "certain",
        "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux",
        "ceux-ci", "ceux-là", "chacun", "chacune", "chaque", "cher", "chers", "chez",
        "chiche", "chut", "chère", "chères", "ci", "cinq", "cinquantaine",
        "cinquante", "cinquantième", "cinquième", "clac", "clic", "combien", "comme",
        "comment", "comparable", "comparables", "compris", "concernant", "contre",
        "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "deja",
        "delà", "depuis", "dernier", "derniere", "derriere", "derrière", "des",
        "desormais", "desquelles", "desquels", "dessous", "dessus", "deux",
        "deuxième", "deuxièmement", "devant", "devers", "devra", "different",
        "differentes", "differents", "différent", "différente", "différentes",
        "différents", "dire", "directe", "directement", "dit", "dite", "dits",
        "divers", "diverse", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept",
        "dixième", "doit", "doivent", "donc", "dont", "douze", "douzième", "dring",
        "du", "duquel", "durant", "dès", "désormais", "e", "effet", "egale",
        "egalement", "egales", "eh", "elle", "elle-même", "elles", "elles-mêmes",
        "en", "encore", "enfin", "entre", "envers", "environ", "es", "est", "et",
        "etant", "etc", "etre", "eu", "euh", "eux", "eux-mêmes", "exactement",
        "excepté", "extenso", "exterieur", "f", "fais", "faisaient", "faisant",
        "fait", "façon", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha",
        "hein", "hem", "hep", "hi", "ho", "holà", "hop", "hormis", "hors", "hou", "houp",
        "hue", "hui", "huit", "huitième", "hum", "hurrah", "hé", "hélas", "i", "il",
        "ils", "importe", "j", "je", "jusqu", "jusque", "juste", "k", "l", "la",
        "laisser", "laquelle", "las", "le", "lequel", "les", "lesquelles", "lesquels",
        "leur", "leurs", "longtemps", "lors", "lorsque", "lui", "lui-meme",
        "lui-même", "là", "lès", "m", "ma", "maint", "maintenant", "mais", "malgre",
        "malgré", "maximale", "me", "meme", "memes", "merci", "mes", "mien", "mienne",
        "miennes", "miens", "mille", "mince", "minimale", "moi", "moi-meme",
        "moi-même", "moindres", "moins", "mon", "moyennant", "multiple", "multiples",
        "même", "mêmes", "n", "na", "naturel", "naturelle", "naturelles", "ne",
        "neanmoins", "necessaire", "necessairement", "neuf", "neuvième", "ni",
        "nombreuses", "nombreux", "non", "nos", "notamment", "notre", "nous",
        "nous-mêmes", "nouveau", "nul", "néanmoins", "nôtre", "nôtres", "o", "oh",
        "ohé", "ollé", "olé", "on", "ont", "onze", "onzième", "ore", "ou", "ouf",
        "ouias", "oust", "ouste", "outre", "ouvert", "ouverte", "ouverts", "o|", "où",
        "p", "paf", "pan", "par", "parce", "parfois", "parle", "parlent", "parler",
        "parmi", "parseme", "partant", "particulier", "particulière",
        "particulièrement", "pas", "passé", "pendant", "pense", "permet", "personne",
        "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut", "pif", "pire", "plein",
        "plouf", "plus", "plusieurs", "plutôt", "possessif", "possessifs",
        "possible", "possibles", "pouah", "pour", "pourquoi", "pourrais", "pourrait",
        "pouvait", "prealable", "precisement", "premier", "première",
        "premièrement", "pres", "probable", "probante", "procedant", "proche",
        "près", "psitt", "pu", "puis", "puisque", "pur", "pure", "q", "qu", "quand",
        "quant", "quant-à-soi", "quanta", "quarante", "quatorze", "quatre",
        "quatre-vingt", "quatrième", "quatrièmement", "que", "quel", "quelconque",
        "quelle", "quelles", "quelqu'un", "quelque", "quelques", "quels", "qui",
        "quiconque", "quinze", "quoi", "quoique", "r", "rare", "rarement", "rares",
        "relative", "relativement", "remarquable", "rend", "rendre", "restant",
        "reste", "restent", "restrictif", "retour", "revoici", "revoilà", "rien", "s",
        "sa", "sacrebleu", "sait", "sans", "sapristi", "sauf", "se", "sein", "seize",
        "selon", "semblable", "semblaient", "semble", "semblent", "sent", "sept",
        "septième", "sera", "seraient", "serait", "seront", "ses", "seul", "seule",
        "seulement", "si", "sien", "sienne", "siennes", "siens", "sinon", "six",
        "sixième", "soi", "soi-même", "soit", "soixante", "son", "sont", "sous",
        "souvent", "specifique", "specifiques", "speculatif", "stop", "strictement",
        "subtiles", "suffisant", "suffisante", "suffit", "suis", "suit", "suivant",
        "suivante", "suivantes", "suivants", "suivre", "superpose", "sur", "surtout",
        "t", "ta", "tac", "tant", "tardive", "te", "tel", "telle", "tellement",
        "telles", "tels", "tenant", "tend", "tenir", "tente", "tes", "tic", "tien",
        "tienne", "tiennes", "tiens", "toc", "toi", "toi-même", "ton", "touchant",
        "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize",
        "trente", "tres", "trois", "troisième", "troisièmement", "trop", "très",
        "tsoin", "tsouin", "tu", "té", "u", "un", "une", "unes", "uniformement",
        "unique", "uniques", "uns", "v", "va", "vais", "vas", "vers", "via", "vif",
        "vifs", "vingt", "vivat", "vive", "vives", "vlan", "voici", "voilà", "vont",
        "vos", "votre", "vous", "vous-mêmes", "vu", "vé", "vôtre", "vôtres", "w", "x",
        "y", "z", "zut", "à", "â", "ça", "ès", "étaient", "étais", "était", "étant",
        "été", "être", "ô"]
    stop += [
        "aller", "veux", "voudrais", "saurais", "connaitrais", "trouve", "trouvent", "savoir",
        "faut", "cherche", "connais", "connaissais", "connaître", "adresse", "demande",
        "l'adresse", "grandpy", "est-ce", "!", "?", ".", "salut", "bonjour", ", ", "dis"]

    list_q = re.split(',| |!|\'|\?|-|\.', query)
    clean_q = re.split(',| |!|\'|\?|-|\.', query)

    eprint("liste initiale")
    eprint(clean_q)
    for word in list_q:
        eprint("scan de "+word)
        eprint(clean_q)
        for entry in stop:
            if (word.lower() == entry):
                eprint(word)
                clean_q.remove(word)
    eprint("resultat du parser: ")
    eprint(clean_q)

    return clean_q


def gmaps_api(txt):
    """	Gmaps Textsearch API call function """

    resp = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+txt+
        '&key=AIzaSyDkJ9UKbi0JzFYtCZr2dKZhLvWM3iOTLyM')
    response = resp.text
    return json.loads(response)


def mwiki_api(lst):
    """	Mediawiki search API call function """

    query_wiki = ' '.join(lst)
    query_wiki = query_wiki.title()
    eprint(query_wiki)
	
    resp_test = requests.get('https://fr.wikipedia.org/w/api.php?action=query&titles='+query_wiki+
        '&redirects&prop=extracts&rvprop=content&explaintext=&format=json&formatversion=2')
    response_test = json.loads(resp_test.text)
	
    alt_list = response_test["query"]["pages"][0]


    if "missing" in alt_list.keys(): 
        int_resp = requests.get('https://fr.wikipedia.org/w/api.php?action=query&list=search'
            '&srsearch='+query_wiki+'&utf8=&format=json&formatversion=2')
        intermed = json.loads(int_resp.text)
        title_list = intermed["query"]["search"]

        if title_list: 

            title = title_list[0]["title"]
            eprint("title: "+title)
            resp = requests.get('https://fr.wikipedia.org/w/api.php?action=query&titles='+title+
                '&redirects&prop=extracts&rvprop=content&explaintext=&format=json&formatversion=2')
            response = resp.text
            return json.loads(response)

        return response_test

    return response_test
