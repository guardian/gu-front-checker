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

overview_circulator = {
	"0" : {
		"tl" : "http://www.bbc.co.uk/news/",
		"tr" : "http://www.thetimes.co.uk/",
		"bl" : "http://www.telegraph.co.uk",
		"br" : "http://www.ft.com",
	},
	"1" : {
		"tl" : "http://m.sky.com/skynews/news",
		"tr" : "http://www.dailymail.co.uk/",
		"bl" : "http://m.independent.co.uk",
		"br" : "http://www.mirror.co.uk",
	},
	"2" : {
		"tl" : "http://www.nytimes.com/",
		"tr" : "http://www.cnn.com/",
		"bl" : "http://www.bostonglobe.com/",
		"br" : "http://www.aljazeera.com/",
	},
	"3" : {
		"tl" : "http://www.theguardian.com/uk",
		"tr" : "http://www.theguardian.com/uk?view=mobile",
	},
}

class Circulator(webapp2.RequestHandler):
	def get(self, page="0"):
		template = jinja_environment.get_template('circulator.html')
		
		template_values = {
			"load_timestamp" : datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
			"next_page" : (int(page) + 1) % len(overview_circulator)
		}

		template_values.update(overview_circulator[page])

		self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/circulator', Circulator),
    ('/circulator/(\d)', Circulator),
    ('/(.+)', MainHandler)
], debug=True)
