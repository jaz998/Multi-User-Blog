from functools import wraps
import modules.parent_keys as parent_key
from google.appengine.ext import ndb
from handlers.mainhandler import MainHandler

def require_user(f):
	@wraps(f)
	def wrapper(self, *args, **kwargs):
		user = self.user
		if user:
			return f(self, user, *args, **kwargs)
		else:
			self.error(404)
			return
	return wrapper


def post_exists(f):
	@wraps(f)
	def wrapper(self, post_id):
		key = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = key.get()
		if post:
			return f(self, post_id)
		else:
			self.error(404)
			return 
	return wrapper

	
