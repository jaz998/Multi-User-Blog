from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from modules.validations import user_owns_post
from modules.myownvalidations import post_exists

class EditPost(MainHandler):
	@post_exists
	def post(self, post_id):
		subject = self.request.get("subjectValue")
		content = self.request.get("contentValue")
		post_id = self.request.get("post_id_value")
		key = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = key.get()
		post.update(subject, content)
		self.render("PostEditedConfo.html")

