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
import random
import webapp2
import json
import urllib2
import os
import jinja2
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ApiRandom(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/flag_input.html')
        self.response.write(template.render())
    def post(self):
        random_place = ''
        template = jinja_environment.get_template('templates/flag_output.html')
        user_search = {
        'category_answer' : self.request.get('category'),
        'location_answer' : self.request.get('location')
        }

        apikey = '&key=AIzaSyCaKoy1cHLDsf_fsw-C0xv5YPscovOG7nw'

        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="
        full_url = base_url + user_search["category_answer"] + '+in+' + user_search["location_answer"] + apikey

        search_data = urllib2.urlopen(full_url)
        search_json = search_data.read()
        search_dictionary = json.loads(search_json)
        # search_url = search_dictionary{'results'}
        # for element in search_dictionary:
        #     logging.info(element[name])
# search_options = {
#     "formatted_address":"",
#     "name":"",
#     "price_level":"",
#     "rating":"",
#      }
        result_dictionary = {}
        results = search_dictionary["results"]
        new_results = []

        for result in results:
            new_result = {}
            new_result["formatted_address"] = result["formatted_address"]
            new_result["name"] = result["name"]
            new_result["price_level"] = result["price_level"]
            new_result["rating"] = result["rating"]
            new_results.append(new_result)

        result_dictionary["new_results"] = new_results

        logging.info(result_dictionary)


        # logging.info(search_dictionary["results"])

        # random_place = (random.choice(search_options))
        # vars_dict = {'random':random_place}

        # self.response.write(template.render(vars_dict))

        random_place = (random.choice(result_dictionary["new_results"]))
        vars_dict = {'random':random_place}
        self.response.write(template.render(vars_dict))
app = webapp2.WSGIApplication([
    ('/', ApiRandom)
], debug=True)
