from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
from modules.validations import user_owns_comment
import modules.parent_keys as parent_key


class UpdateComment(MainHandler):
	def post(self):
		user = self.request.get("user")
		content = self.request.get("content")
		post_id = self.request.get("post_id")
		keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = keyPost.get()
		comment_id = self.request.get("comment_id")
		key = ndb.Key('Comment', int(comment_id), parent = post.key)
		comment = key.get()
		comment.update(content)
		@user_owns_comment
		def render(self, post, comments):
			self.render('viewcomment.html',post=post,comments = post.get_comments(), user = self.user)

		render(user, comment, post)