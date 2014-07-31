'''
Fridelande Rosas
7/31/2014
Final Project: Api
'''
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormPage()
        #makes the page load correctly w/ GET
        if self.request.GET:
            #create our model
            mm = MovieModel()
            #sends our user input from the url to the model
            mm.title = self.request.GET['title']
            #connect to the API
            mm.call_api()
            #creates view
            mv = MovieView()
            #shares data obj form model class to the view
            mv.mdos = mm.dos
            #shares the view content to the form body
            p._body = mv.content
        #calls the print_out to display on page
        self.response.write(p.print_out())


#the View
class MovieView(object):
    '''This class deals with how the data will be seen by the user '''
    def __init__(self):
        #document array
        self.__mdos = []
        #default content
        self.__content = '<br />'

    #updated the view when called
    def update(self):
        #loops through the document obj
        for do in self.__mdos:
            #adds content to obj
            self.__content += '<div id="movies"><a href="' + do.href + '" title = Click submit">' + do.title


#the Model
class MovieModel(object):
    '''this model works with the info by fetching and parsing and sorting'''
    def __init__(self):
        #url to the API
        self.__url = "http://www.omdbapi.com/?s="
        self.__title = ''
        self.__xmldoc = ''

    def call_api(self):
        #request and loads info from API
        #assemple the request
        request = urllib2.Request(self.__url + "title: " + self.__title + "&format=xml")

        #urllib to create an obj to the url
        opener = urllib2.build_opener()

        #use the url to get a result - request info from teh API
        result = opener.open(request)

        #Parsing Data
        self.__xmldoc = minidom.parse(result)

        #sorting Data
        #empty array to hold the info we use from API
        self.dos = []

#The Data - stores info
class MovieData(object):
    def __init__(self):
        pass


#Page template
class Page(object):
    def __init__(self):
        pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
