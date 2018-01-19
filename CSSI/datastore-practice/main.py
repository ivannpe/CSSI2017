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
from google.appengine.ext import ndb

# TODO: Add Artist class

# TODO: Add Song class


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class CreateArtistHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/create_artist.html')
        self.response.out.write(template.render())
    
    def post(self):
        # TODO: Fill in and fix this function! Make sure to save the artist to the database.
        
        template_vars = {
            'name': 'Beyonce',
            'day': '04',
            'month': '09',
            'year': '1981'
        }
        template = jinja_environment.get_template('templates/show_artist.html')
        self.response.out.write(template.render(template_vars))
        
class CreateSongHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/create_song.html')
        self.response.out.write(template.render())
        
    def post(self):
        # TODO: Fill in and fix this function! Make sure to save the song to the database.
        
        template_vars = {
            'title': 'Single Ladies (Put a Ring On It)',
            'day': '13',
            'month': '10',
            'year': '2008',
            'genre': 'pop',
            'artist_name': 'Beyonce'
        }
        template = jinja_environment.get_template('templates/show_song.html')
        self.response.out.write(template.render(template_vars))
        
class ListSongsByArtistHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/search_songs.html')
        self.response.out.write(template.render())
        
    def post(self):
        # TODO: Fill in and fix this function!
        
        template_vars = {
            'artist_name': 'Beyonce',
            'songs': ['Single Ladies (Put a Ring On It)', 'Halo', 'Crazy in Love']
        }
        template = jinja_environment.get_template('templates/list_songs.html')
        self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/addartist', CreateArtistHandler),
    ('/addsong', CreateSongHandler),
    ('/listsongs', ListSongsByArtistHandler)
], debug=True)
