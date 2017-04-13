from google.appengine.ext import ndb

class Comment(ndb.Model):
	content = ndb.TextProperty(required=True)
	author = ndb.KeyProperty(required=True, kind="User")
	created = ndb.DateTimeProperty(auto_now_add=True)
	last_modified = ndb.DateTimeProperty(auto_now=True)

	def update(self, content):
		self.content = content
		return self.put()

	def delete(self):
		self.key.delete()


	@classmethod
	def get_comments(cls, post):
		return cls.query(ancestor=post.key).order(-cls.created).fetch()

	@classmethod
	def create(cls, content, author, post):
		c = cls(content = content, author = author.key, parent = post.key)
		return c.put()