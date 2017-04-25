from handlers.mainhandler import MainHandler
from models.post import Post
import modules.parent_keys as parent_key
from google.appengine.ext import ndb


class NewPost(MainHandler):
    def get(self):
        # Check whether there is a valid cookie
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect('/login')

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")
        author = self.user.key

        if subject and content:
            p = Post(
                parent=parent_key.blog_key(),
                subject=subject,
                content=content,
                author=author)
            p.put()
            self.redirect('/%s' % str(p.key.id()))
        else:
            error = "Both subject and content are required"
            self.render("newpost.html")
