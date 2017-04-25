from google.appengine.ext import ndb
from handlers import mainhandler
from models.comment import Comment
from models.user import User


class Post(ndb.Model):
    subject = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_modified = ndb.DateTimeProperty(auto_now=True)
    author = ndb.KeyProperty(required=True, kind='User')
    liked = ndb.BooleanProperty(required=False)
    likedByUser = ndb.IntegerProperty(required=False)
    unlikedByUser = ndb.IntegerProperty(required=False)
    likes = ndb.KeyProperty(repeated=True, kind="User")

    def render(self):
        return mainhandler.render_str("post.html", p=self)

    def post(self):
        return mainhandler.render_str("post.html", p=self)

    def update(self, subject, content):
        self.subject = subject
        self.content = content
        return self.put()

    def add_like(self, user):
        self.likes.append(user.key)
        return self.put()

    def remove_like(self, user):
        self.likes.remove(user.key)
        return self.put()

    def like(self, likedByUserID):
        self.likedByUser = int(likedByUserID)
        self.liked = True
        return self.put()

    def unlike(self, unlikedByUserID):
        self.unlikedByUser = int(unlikedByUserID)
        self.liked = False
        return self.put()

    def likedByUserID(self, user_id):
        self.unlikedByUser = 0
        likedByUserID = self.likedByUser
        likedByUserID = int(likedByUserID)
        if likedByUserID == int(user_id):
            return True
        else:
            return False

    def unlikedByUserID(self, user_id):
        self.likedByUser = 0
        unlikedByUserID = self.unlikedByUser
        unlikedByUserID = int(unlikedByUserID)
        if unlikedByUserID == int(user_id):
            return True
        else:
            return False

    def get_comments(self):
        return Comment.get_comments(self)
