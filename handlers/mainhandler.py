import webapp2
import jinja2
import os
import re
import random
import hashlib
import hmac
from string import letters
from google.appengine.ext import ndb
from google.appengine.ext import db
from config import config
import modules.security as security
from models.user import User
import modules.parent_keys as parent_key

#Global variables
secret = 'fart'
cookies = ''

template_dir = os.path.join(config['root_dir'],'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape = True)

jinja_env.globals['uri_for']=webapp2.uri_for


def render_str(template, **params):
	t = jinja_env.get_template(template)
	return t.render(params)


class MainHandler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

	def set_secure_cookie(self, name, val):
		cookie_val = security.make_secure_val(val)
		self.response.headers.add_header(
			'Set-Cookie',
			'%s=%s; Path=/' % (name, cookie_val))

	def read_secure_cookie(self, name):
		cookie_val = self.request.cookies.get(name)
		return cookie_val and security.check_secure_val(cookie_val)

	def login(self, user):
		self.set_secure_cookie('user_id', str(user.key.id()))

	def logout(self):
		self.response.headers.add_header('Set-Cookie', 'user_id=; Path/')

	def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)
		uid = self.read_secure_cookie('user_id')
		self.user = uid and User.by_id(int(uid))
