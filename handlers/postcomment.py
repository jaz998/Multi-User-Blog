from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from models.comment import Comment
from modules.validations import require_user

class PostComment(MainHandler):
	@require_user()
	def post(self, user):
		content = self.request.get("content")
		post_id = self.request.get("post_id")
		keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = keyPost.get()
		author = self.user
		Comment.create(content,author,post)
		self.render('viewcomment.html',post=post,comments = post.get_comments(), user = self.user)
