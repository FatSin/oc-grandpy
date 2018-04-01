"""
Ths is the python script that tests the backscript file's functions.

"""
import sys
import json

import urllib.request
import requests
import pytest
from flask import Flask
from flask_testing import LiveServerTestCase


sys.path.append(sys.path[0] + "/..")
sys.path.append(sys.path[0] + "/../static")
from grandpyapp import app
import backscript as back
#from views import app


HOST = "127.0.0.1"
PORT = "8943"
INDEX_FILE = "index.html"


class Testuserhttp(LiveServerTestCase):
    """ Test the routes  """
    def create_app(self):
        '''For the  generation of a testing Flask app
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SERVER_NAME'] = HOST+':'+PORT
        return app
        '''
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_httpindex(self):
        """ Call the index and check the status code """
        link = 'http://'+HOST+':'+PORT+"/"
        #print(link)
        #code = urllib.request.urlopen(link).getcode()
        req = requests.get(link)

        assert req.status_code == 200

    def test_httpjs():
        """ Call the backend as javascript would do """
        link = 'http://'+HOST+':'+PORT+"/_callPython?q=je+cherche+la+tour+eiffel"
        code = urllib.request.urlopen(link).getcode()

        assert code == 200


def test_parser():
    """ Test the parser """
    str = "Je veux aller aux champs Elysées"
    assert back.parser(str) == ['champs', 'Elysées']


@pytest.mark.api
def test_gmaps_search(monkeypatch):
    """ Test Google Maps texSearch API """
    def monkey_get(url):
        """ Monkey patching of the 'requests.get' method """
        class Monkey_Response(object):
            """ class for monkeypacthing """
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

        mymonkey = Monkey_Response()

        return mymonkey


    txt = "Cité des sciences"
    results = {
        'formatted_address': '30 Avenue Corentin Cariou, 75019 Paris, France',
        'name': "Cité des sciences et de l'industrie",
        'place_id': 'ChIJD6qS3zJs5kcRJ8_ebdhX0VI'}


    monkeypatch.setattr(requests, 'get', monkey_get)

    results_api = back.gmaps_api(txt)

    #assert results_api["status"] == json.loads(Monkey_Response.text)["status"]
    assert results_api["status"] == "OK"
    assert results_api["results"][0]["formatted_address"] == results["formatted_address"]
    assert results_api["results"][0]["name"] == results["name"]
    assert results_api["results"][0]["place_id"] == results["place_id"]


@pytest.mark.api
def test_mediawiki(monkeypatch):
    '''Test Mediawiki search API'''
    def monkey_get(url):
        """ Monkey patching of the 'requests.get' method """
        class Monkey_Response(object):
            """ Class for monkey patching """
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

        mymonkey = Monkey_Response()

        return mymonkey

    lst = "Cité des sciences"

    results = {
        'title': "Cité des sciences et de l'industrie"}


    monkeypatch.setattr(requests, 'get', monkey_get)

    results_api = back.mwiki_api(lst)

    assert results_api["query"]["pages"][0]["title"] == results["title"]
