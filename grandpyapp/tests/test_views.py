import os
import urllib.request
import requests

import sys
sys.path.append(sys.path[0] + "/..")

import views

#from .. import templates

#from .. import views

HOST="localhost:"
PORT="5000" 
INDEX_FILE="index.html"




#Test the rendering of index.html
def test_httpcode():
	#updir = os.path.dirname(os.path.dirname(__file__))
	#link = os.path.join(updir,"templates",INDEX_FILE)
	link='http://'+HOST+PORT+"/"
	#print(link)
	code = urllib.request.urlopen(link).getcode()
	#(link)
	#print(code)
	#HTML code expected : 20x or 30x 
	assert code == 200

#test_httpcode()


#Check that the data in the form is sent to the system
#def test_form_html():
	#question="Where is Brian?"
	#send the question to the form
	# Parcourir DOM en python ????? -> minidom ??
	#form_return = getElementById('form').
#	assert form_return == question


#Test the parser
#def test_parser():
#	str = "Je veux aller aux champs Elysées"
#	assert views.parser() == "champs Elysées"


#Test Google Maps texSearch API
def test_gmaps_search(monkeypatch):

	txt = "Je cherche la Cité des sciences"
	results = [{
			'formatted_address': '30 Avenue Corentin Cariou, 75019 Paris, France',
			'name': 'City of Science and Industry',
			'place_id': 'ChIJB0gcnCBw5kcRHoIAPcTEApc' }]

	

	def mockreturn(request):
		return results

	monkeypatch.setattr(requests,'get',mockreturn)
	assert views.gmaps_api(txt) == results

	
	

	

	
