import os
import urllib.request

from .. import templates

#from grandpyapp import views

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
def test_form_html():
	question="Where is Brian?"
	#send the question to the form
	# Parcourir DOM en python ????? -> minidom ??
	#form_return = getElementById('form').
	assert form_return == question
	

	
