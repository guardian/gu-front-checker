import os

import datetime

import webapp2
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class MainHandler(webapp2.RequestHandler):
    def get(self, section="uk"):
		template = jinja_environment.get_template('index.html')
		
		template_values = {
			"load_timestamp" : datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
			"section" : section}

		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/(.+)', MainHandler)
], debug=True)
