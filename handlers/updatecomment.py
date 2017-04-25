from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from modules.myownvalidations import user_owns_comment


class UpdateComment(MainHandler):
	@user_owns_comment
	def post(self):
		content = self.request.get("content")
		post_id = self.request.get("post_id")
		keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
		post = keyPost.get()
		comment_id = self.request.get("comment_id")
		key = ndb.Key('Comment', int(comment_id), parent = post.key)
		comment = key.get()
		comment.update(content)
		self.render('viewcomment.html',post=post,comments = post.get_comments(), user = self.user)