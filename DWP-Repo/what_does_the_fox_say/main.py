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
        array = ["panther()", "dolphin()", "fox()"]
        # self.response.write('Hello world!')

        #html
        title = "What does the Fox Say?"
        css = "css/main.css"
        page_head = """
<!DOCTYPE HTML>
    <html>
        <head><title>What Does the Fox Say?</title>
        <link href= rel="stylesheet type="text/css />
        </head>
        <body>
            """
        page_body = "" \
                     "<header><h1>Animal:</h1><header>" \
                             "<a href=?animals=" + array[0] + "><button class='first'>Panther</button>" \
                             "<a href=?animals=" + array[1] + "><button class='second'>Dolphin</button>" \
                             "<a href=?animals=" + array[2] + "><button class='third'>Fox</button>" \
                     ""
        page_close = """
        </div>
        </body>
</html>"""

        if self.request.GET:
            a = self.request.GET["animals"]

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
            total = page_head + page_body + page_close
            #prints details
            total = total.format(**locals())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
