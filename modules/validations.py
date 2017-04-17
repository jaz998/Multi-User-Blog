from functools import wraps
from google.appengine.ext import ndb
from handlers.mainhandler import MainHandler
import modules.parent_keys as parent_key


def get_user(f):
	@wraps(f)
	def wrapper(self, *a, **kw):
		# Default user to None
		user = None
		user_id = self.read_secure_cookie('user_id')
		self.write("Wrapper is running")
		if user_id:
			self.write("If user ID is running\n")
			user = ndb.Key('User', int(user_id), parent=parent_key.users_key()).get()
			self.write(user)
		return f(self, user, *a, **kw)
	return wrapper

def require_user(redirect=None):
    def decorated_function(f):
        @wraps(f)
        @get_user
        def wrapper(self, user, *a, **kw):
            if user:
                return f(self, user, *a, **kw)
            else:
                if redirect:
                    self.redirect_to(redirect)
                else:
                    self.abort(404)
        return wrapper
    return decorated_function

def post_exists(f):
	@wraps(f)
	def wrapper(self, post_id, *a, **kw):
		post = ndb.Key('Post', int(post_id)).get()
		if post:
			return f(self, post, post_id, *a, **kw)
		else:
			self.abort(404)
			return
	return wrapper

# Decorator checks if post exists. And if it does, 
# checks if user is the author
def user_owns_post(f):
	@wraps(f)
	@post_exists
	@require_user()
	def wrapper(self, user, post, post_id, *a, **kw):
		if user.key == post.author:
			return f(self, user, post, post_id, *a, **kw)
		else:
			self.abort(404)
			return
	return wrapper

def comment_exists(f):
	@wraps(f)
	def wrapper(self, comment_id, *a, **kw):
		comment = ndb.Key('Comment', int(comment_id)).get()
		if comment:
			return f(self, post, post_id, *a, **kw)
		else:
			self.abort(404)
			return 
		return wrapper

def user_owns_comment(f):
    @wraps(f)
    @comment_exists
    @require_user()
    def wrapper(self, user, comment, comment_key, *a, **kw):
        if user.key == comment.author:
            return f(self, user, comment, comment_key, *a, **kw)
        else:
            self.abort(404)
            return
    return wrapper


def user_can_like_post(f):
	@wraps(f)
	@post_exists
	@require_user()
	def wrapper(self, user, post, post_id, *a, **kw):
		if user.can_like_post(post):
			return f(self, user, post, post_id, *a, **kw)
		else:
			self.abort(404)
			return 
	return wrapper

def user_can_unlike_post(f):
	@wraps(f)
	@post_exists
	@require_user()
	def wrapper(self, user, post, post_id, *a, **kw):
		if user.liked_post(post):
			return f(self, user, post, post_id, *a, **kw)
		else:
			self.abort(404)
			return
	return wrapper

	
