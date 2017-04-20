from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key

class DeletePost(MainHandler):
	def post(self):
		post_id = self.request.get("post_id")
		key = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = key.get()
		subject = post.subject
		key.delete()
		self.render("deletePost.html", subject = subject)
