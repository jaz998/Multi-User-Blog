from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key


class PostPage(MainHandler):
	def get(self, post_id):
		key = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = key.get()

		if not post:
			self.error(404)
			return
		else:
			self.render("permalink.html", post = post, user = self.user)