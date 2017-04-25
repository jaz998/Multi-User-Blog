from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from models.comment import Comment
from modules.myownvalidations import require_user
from modules.myownvalidations import post_exists


class PostComment(MainHandler):
    @require_user
    @post_exists
    def post(self):
        content = self.request.get("content")
        post_id = self.request.get("post_id_value")
        keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
        post = keyPost.get()
        author = self.user
        Comment.create(content, author, post)
        self.render(
            'viewcomment.html',
            post=post,
            comments=post.get_comments(),
            user=self.user)
