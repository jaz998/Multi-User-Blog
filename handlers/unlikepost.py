from handlers.mainhandler import MainHandler
from google.appengine.ext import ndb
import modules.parent_keys as parent_key
from modules.myownvalidations import user_can_unlike_post


class UnlikePost(MainHandler):
    @user_can_unlike_post
    def post(self):
        post_id = self.request.get("post_id_value")
        user_id = self.request.get("user_id")
        keyPost = ndb.Key('Post', int(post_id), parent=parent_key.blog_key())
        post = keyPost.get()
        keyUser = ndb.Key('User', int(user_id), parent=parent_key.users_key())
        user = keyUser.get()
        post.remove_like(user)
        self.redirect('/')
