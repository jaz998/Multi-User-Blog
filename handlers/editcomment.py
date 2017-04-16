from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from modules.validations import user_owns_comment
from modules.validations import comment_exists



class EditComment(MainHandler):
	@user_owns_comment
	def get(self):
		post_id = self.request.get("post_id")
		keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = keyPost.get()
		comment_id = self.request.get("comment_id")
		key = ndb.Key('Comment', int(comment_id), parent = post.key)
		comment = key.get()
		self.render('editcomment.html', comment = comment, post = post)