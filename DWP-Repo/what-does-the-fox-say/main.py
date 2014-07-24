"""
Free Rosas
7/22/2014
DPW-01
What Does the Fox Say?
"""
import webapp2
from animal import Panther, Dolphin, Fox


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #method array
        array = ["Panther()", "Dolphin()", "Fox()"]
        self.response.write('Hello world!')

        #html
        title = "What does the Fox Say?"
        css = "css/style.css"
        _page_head = """
<!DOCTYPE HTML>
    <html>
        <head><title>What Does the Fox Say?</title>
        <link href="{css}" rel="stylesheet" type="text/css" />
        </head>
        <body>
            """
        _page_body = """<header><h1>Animal:</h1><header>
                            <nav>
                                <ul>
                                    <a href=?animals=0" + array[0] + "><button class='first'>Panther</button>
                                    <a href=?animals=1" + array[1] + "><button class='second'>Dolphin</button>
                                    <a href=?animals=2" + array[2] + "><button class='third'>Fox</button>"
                                </ul>
                             </nav>
                     """

        _page_close = """
        </body>
</html>"""

        if self.request.GET:
         #uses the GET info to work on the page
            a = self.request.GET["animal"]

            if a == array[0]:
                a = Panther()
                self.response.write(a.print_out())

            elif a == array[1]:
                a = Dolphin()
                self.response.write(a.print_out())

            elif a == array[2]:
                a = Fox()
                self.response.write(a.print_out())

        else:
            total = _page_head + _page_body + _page_close
                #prints details
            total = total.format(**locals())
            self.response.write(total)
                #prints info onto the page


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
