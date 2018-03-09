from __future__ import print_function
import sys
from flask import Flask, render_template, jsonify, request
import requests
import json
	
	
app = Flask(__name__)

#To print the "prints !"
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

#Call Gmaps Textsearch API
def gmaps_api(txt):
	resp = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+txt+'&key=AIzaSyDkJ9UKbi0JzFYtCZr2dKZhLvWM3iOTLyM')
	response = resp.text
	return json.loads(response)


#Call Mediawiki search API
def mwiki_api(lst):
#	for l in lst:
#		l=l.capitalize()

	eprint(lst)
	query_wiki = ' '.join(lst)
	query_wiki = query_wiki.title()
	eprint(query_wiki)
	#resp = requests.get('https://fr.wikipedia.org/w/api.php?action=query&titles='+query_wiki+'&redirects&prop=revisions&rvprop=content&format=json&formatversion=2')
	resp = requests.get('https://fr.wikipedia.org/w/api.php?action=query&titles='+query_wiki+'&redirects&prop=extracts&rvprop=content&explaintext=&format=json&formatversion=2')
	response = resp.text
	return json.loads(response)	




	

#Views

@app.route("/")
def index():
	#return "Hello World!"
	return render_template("index.html")
	
@app.route("/_parse")
def parser():
	eprint("python parser appelé")
	q = request.args.get('q',0, type=str)
	eprint(q)
	stop = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
	stop +=["aller","veux","voudrais","trouve","savoir","faut","cherche"]
	
	#eprint(stop)
	
	list_q = q.split()
	clean_q = q.split()
	eprint("liste initiale")
	eprint(list_q)
	for word in list_q:
		eprint("scan de "+word)
		eprint(list_q)
		for s in stop:
			if (word == s):
				eprint(word)
				clean_q.remove(word)
	eprint(clean_q)
	
	
	#Google Maps Textsearch API
	
	query = '+'.join(clean_q)
	
	
	#resp = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query='+query+'&key=AIzaSyDkJ9UKbi0JzFYtCZr2dKZhLvWM3iOTLyM')
	#response = resp.text

	
	response = gmaps_api(query)
	
	#eprint(type(response))
	#eprint(response["results"])
	
	#eprint("results: ")
	#eprint(response["results"])
	
	name = response["results"][0]["name"]
	address = response["results"][0]["formatted_address"]
	id = response["results"][0]["place_id"]
	
	#address = response[0][1]
	#id = responset[0][3]
	#name = response[0][4]
	response_js = "Eh bien mon poussin !"+name+" se trouve au "+address
	
	#eprint(name+" se trouve au "+address+". Son ID est "+id)
	
	
	#Google Maps Embedded API
	lnk = "https://www.google.com/maps/embed/v1/place?key=AIzaSyDkJ9UKbi0JzFYtCZr2dKZhLvWM3iOTLyM&q=place_id:"+id
	eprint(lnk)
	
	#Mediawiki API
	resp_wiki = mwiki_api(clean_q)
	eprint(resp_wiki)
	#content_wiki = resp_wiki["query"]["pages"][0]["revisions"][0]["content"]
	
	content_wiki = resp_wiki["query"]["pages"][0]["extract"]
	short_wiki =content_wiki[:1500]
	list_wiki = short_wiki.split('.')
	final_wiki = list_wiki[0]+"."
	
	title_wiki = resp_wiki["query"]["pages"][0]["title"]
	link_wiki = "https://fr.wikipedia.org/wiki/"+title_wiki
	
	
	#Final concatenated response
	response_js = response_js+'\r\n Je peux t'+"en dire des choses dessus ! "+final_wiki
	
	
	return jsonify(result=response_js,lnk=lnk,wiki=link_wiki)


if __name__ == "__main__":
    app.run(debug=True)