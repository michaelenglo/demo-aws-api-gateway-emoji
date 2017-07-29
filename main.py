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

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	score = float(self.request.get('score'))

    	self.response.headers['Content-Type'] = 'image/gif'
    	self.response.headers['Access-Control-Allow-Origin'] = '*'

        if score < 0.21:
            with open("gif/angry1.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.25:
            with open("gif/angry2.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.3:
            with open("gif/angry3.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.35:
            with open("gif/angry4.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.4:
            with open("gif/angry5.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.45:
            with open("gif/neutral1.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.5:
            with open("gif/neutral2.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.55:
            with open("gif/neutral3.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.6:
            with open("gif/neutral4.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.65:
            with open("gif/neutral5.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.7:
            with open("gif/happy1.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.75:
            with open("gif/happy2.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.8:
            with open("gif/happy3.gif", 'rb') as fp:
              self.response.write(fp.read())
        elif score < 0.85:
            with open("gif/happy4.gif", 'rb') as fp:
              self.response.write(fp.read())
        else:
            with open("gif/happy5.gif", 'rb') as fp:
              self.response.write(fp.read())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
