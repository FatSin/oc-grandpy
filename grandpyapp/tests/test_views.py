import os
import urllib.request

#from grandpyapp import views

HOST="localhost:"
PORT="5000" 
INDEX_FILE="index.html"

#Tests the rendering of index.html
def test_httpcode():
	#updir = os.path.dirname(os.path.dirname(__file__))
	#link = os.path.join(updir,"templates",INDEX_FILE)
	link='http://'+HOST+PORT+"/"
	#print(link)
	code = urllib.request.urlopen(link).getcode()
	#(link)
	#print(code)
	assert code == 200

#test_httpcode()
	
#HTML code expected : 20x or 30x 