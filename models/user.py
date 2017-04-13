from google.appengine.ext import ndb
import modules.security as security
import modules.parent_keys as parent_key


class User(ndb.Model):
	name = ndb.StringProperty(required=True)
	pw_hash = ndb.StringProperty(required=True)
	email = ndb.StringProperty()

	def can_edit(self, post):
		return self.key == post.author



	def can_like(self, post):
		return self.key != post.author



	def liked_post(self, post):
		return self.key in post.likes



	@classmethod
	def by_id(cls, uid):
		return User.get_by_id(uid, parent = parent_key.users_key())

	@classmethod
	def by_name(cls, name):
		#u = User.query().filter('name =', name).get()
		u = User.query(User.name == name).get()
		return u

	@classmethod
	def register(cls, name, pw, email=None):
		pw_hash = security.make_pw_hash(name, pw)
		return User(parent = parent_key.users_key(),
					name = name,
					pw_hash = pw_hash,
					email = email)

	@classmethod
	def login(cls, name, pw):
		u = cls.by_name(name)
		if u and security.valid_pw(name, pw, u.pw_hash):
			return u