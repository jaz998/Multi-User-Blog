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
# languageimitations under the License.
#

import webapp2
import jinja2
import os
import re
import random
import hashlib
import hmac
from string import letters
from google.appengine.ext import ndb

from handlers.mainhandler import MainHandler
from handlers.deletecommenthandler import DeleteComment
from handlers.deleteposthandler import DeletePost
from handlers.editcomment import EditComment
from handlers.editposthandler import EditPost
from handlers.likepost import LikePost
from handlers.login import Login
from handlers.logout import Logout
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.postcomment import PostComment
from handlers.postpage import PostPage
from handlers.signup import Signup
from handlers.signup import Register
from handlers.unlikepost import UnlikePost
from handlers.updatecomment import UpdateComment
from handlers.viewcomment import ViewComment


#Global variables

cookies = ''

template_dir = os.path.join(os.path.dirname(__file__),'templates')



class Blog(MainHandler):
	def get(self):
		self.render("blog.html")

app = webapp2.WSGIApplication([
    ('/signup', Register),
    ('/login', Login),
    ('/logout', Logout),
    ('/blog', Blog),
    ('/newpost', NewPost),
    ('/', MainPage),
    ('/([0-9]+)', PostPage),
    webapp2.Route('/editpost/<post_id:[0-9]+>', handler = EditPost, name = 'editpost'),
    ('/deletePost', DeletePost),
    ('/likePost', LikePost),
    ('/unlikePost', UnlikePost),
    webapp2.Route('/viewcomment', handler = ViewComment, name ='viewcomment'),
    webapp2.Route('/postcomment', handler = PostComment, name = 'postcomment'),
    webapp2.Route('/editcomment', handler = EditComment, name = 'editcomment'),
    webapp2.Route('/deletecomment', handler = DeleteComment, name = 'deletecomment'),
    webapp2.Route('/updatecomment', handler = UpdateComment, name = 'updatecomment')
    ], debug=True)

