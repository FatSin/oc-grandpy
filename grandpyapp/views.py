"""
Ths is the python script for the website's routes.

"""

from __future__ import print_function
import sys
import random

from flask import Flask, render_template, jsonify, request

sys.path.append(sys.path[0] + "\grandpyapp\static")
import grandpyapp.static.backscript as back


app = Flask(__name__)

def eprint(*args, **kwargs):
    """	Function to print the print in Flask !"""
    print(*args, file=sys.stderr, **kwargs)



@app.route("/")
def index():
    """	Route for the root"""
    return render_template("index.html")

@app.route("/_callPython")
def call_python():
    """Function called by javscript to handle the user's request."""
    eprint("python parser appelé")
    q = request.args.get('q', 0, type=str)

    #Call of parsing function
    parsed = back.parser(q)

    query = '+'.join(parsed)

    eprint("Query for gmaps: ")
    eprint(query)

    #Gmaps API call
    response_gmaps = back.gmaps_api(query)
    eprint("Retour de l'API gmaps")
    eprint(response_gmaps)


    if response_gmaps["status"]=="OK":
        name = response_gmaps["results"][0]["name"]
        address = response_gmaps["results"][0]["formatted_address"]
        id = response_gmaps["results"][0]["place_id"]
        gmaps_ok = 1
        response_js = name+" se trouve au "+address
    else:
        gmaps_ok = 0

    '''
    #Static data, in case API call number expired

    gmaps_ok = 1
    name = "Tour Eiffel"
    address = "DTC"
    id = "ChIJlWBfzuxv5kcRayN3ZzmZulY"
    response_js = name+" se trouve au "+address

    '''

    #Mediawiki API call

    try:
        resp_wiki = back.mwiki_api(parsed)
    except KeyError as k:
        eprint("Erreur de saisie")
        response_js = "Comment ?? Je n'ai pas entendu ta question. Tu sais, à mon âge..."
        return jsonify(result=response_js)

    content_wiki = resp_wiki["query"]["pages"][0]


    intro = ["Eh bien, mon poussin !", "Ah, ça me revient !", "Bien sûr,"
        "j'y suis allé maintes fois !"]

    if (( "extract" in content_wiki.keys()) & gmaps_ok):
        short_wiki = content_wiki["extract"][:1500]
        list_wiki = short_wiki.split('.')
        final_wiki = list_wiki[0]+"."

        title_wiki = resp_wiki["query"]["pages"][0]["title"]
        link_wiki = "https://fr.wikipedia.org/wiki/"+title_wiki

        #Final concatenated response
        randindex = random.randint(0, len(intro)-1)

        response_js = intro[randindex]+" "+response_js+'\r\n . Je peux t'+"'en dire des choses dessus ! "+'\r\n'+final_wiki

        #Google Maps Embedded API
        lnk = "https://www.google.com/maps/embed/v1/place?key=AIzaSyDkJ9UKbi0JzFYtCZr2dKZhLvWM3iOTLyM&q=place_id:"+id
        eprint(lnk)

        return jsonify(result=response_js, lnk=lnk, wiki=link_wiki)

    else:
        response_js = "Carabistouille ! Je ne connais pas ce lieu. Es-tu sûr qu’il existe ?..."

    return jsonify(result=response_js)


if __name__ == "__main__":
    app.run(debug=True)
