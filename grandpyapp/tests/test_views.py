import os
import urllib.request
import requests

import sys

sys.path.append(sys.path[0] + "/..")
sys.path.append(sys.path[0] + "/../static")

print(sys.path)

from io import BytesIO
import json
import pytest
from flask import Flask

from grandpyapp import app

#from views import app

import backscript as back

#from .. import templates

#from .. import views




#sys.path.append(sys.path[0] + "/../static")
print(sys.path[0])



HOST="localhost"
PORT="5000" 
INDEX_FILE="index.html"




#Check the routes

@pytest.fixture(scope="module")
def create_app():
	app = Flask(__name__)
	app.config['TESTING'] = True
	return app


@pytest.mark.routes
def test_httpindex():
	link='http://'+HOST+':'+PORT+"/"
	#print(link)
	code = urllib.request.urlopen(link).getcode()
	
	assert code == 200	


@pytest.mark.routes
def test_httpjs():
	link='http://'+HOST+':'+PORT+"/_callPython?q=je+cherche+la+tour+eiffel"
	code = urllib.request.urlopen(link).getcode()
	
	assert code == 200
	

#Test the parser
def test_parser():
	str = "Je veux aller aux champs Elysées"
	assert back.parser(str) == ['champs', 'Elysées']


@pytest.mark.api
#Test Google Maps texSearch API
def test_gmaps_search(monkeypatch):

	def monkey_get(url):
	
		class Monkey_Response(object):	
			def __init__(self):
				self.text = '''{
				   "html_attributions" : [],
				   "results" : [
					  {
						 "formatted_address" : "30 Avenue Corentin Cariou, 75019 Paris, France",
						 "id" : "4244e0c51a618326792a27f7a905298ede0f5795",
						 "name" : "Cité des sciences et de l'industrie",
						 "opening_hours" : {
							"weekday_text" : []
						 },
						 "place_id" : "ChIJD6qS3zJs5kcRJ8_ebdhX0VI"
					  }
				   ],
				   "status" : "OK"
				   }
					'''
		
		Mymonkey = Monkey_Response()
		
		return Mymonkey


	txt = "Cité des sciences"
	results = {
			'formatted_address': '30 Avenue Corentin Cariou, 75019 Paris, France',
			'name': "Cité des sciences et de l'industrie",
			'place_id': 'ChIJD6qS3zJs5kcRJ8_ebdhX0VI' }

	

	#def mockreturn(request):
	#	return BytesIO(json.dumps(results).encode())

	monkeypatch.setattr(requests,'get',monkey_get)
	
	results_api = back.gmaps_api(txt)
	
	#assert results_api["status"] == json.loads(Monkey_Response.text)["status"]
	assert results_api["status"] == "OK"
	assert results_api["results"][0]["formatted_address"] == results["formatted_address"]
	assert results_api["results"][0]["name"] == results["name"]
	assert results_api["results"][0]["place_id"] == results["place_id"]



#Test Mediawiki search API
@pytest.mark.api
def test_mediawiki(monkeypatch):

	def monkey_get(url):
	
		class Monkey_Response(object):	
			def __init__(self):
				self.text = '''
						{"batchcomplete": "True", 
						"query": 
							{"pages": 
								[{
									"pageid": "1359783", 
									"ns": "0",
									"title": "Cité des sciences et de l'industrie", 
									"revisions": "Blabla"
								}]}
						}
					'''
		
		Mymonkey = Monkey_Response()
		
		return Mymonkey




	lst = "Cité des sciences"

	results = {
			'title': "Cité des sciences et de l'industrie"}
			

	monkeypatch.setattr(requests,'get',monkey_get)
	
	results_api = back.mwiki_api(lst)
	
	assert results_api["query"]["pages"][0]["title"] == results["title"]


	



	
