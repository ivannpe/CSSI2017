#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import json
import urllib
import urllib2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'puppy', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        parsed_giphy_dictionary = json.loads(giphy_response)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        self.response.write('<img src= "%s">' %gif_url)


class SecondHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('gif_generator.html')
        self.response.write(template.render())

    def post(self):
        template = jinja_environment.get_template('gif_generator2.html')
        contact_order = {
          'search': self.request.get('search_word')}
        base_url = "http://api.giphy.com/v1/gifs/search?"
        url_params = {'q': 'puppy', 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
        url_params['q']= contact_order['search']
        giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()
        parsed_giphy_dictionary = json.loads(giphy_response)
        gif_url = parsed_giphy_dictionary['data'][0]['images']['original']['url']
        render_dict = {
        'gif_url':gif_url
        }
        self.response.write(template.render(render_dict))



app = webapp2.WSGIApplication([
    ('/doge', MainHandler),
    ('/', SecondHandler)
], debug=True)
