from google.appengine.ext import ndb
from handlers.mainhandler import MainHandler
from models.post import Post
import modules.parent_keys as parent_key



class MainPage(MainHandler):
	def get(self):
		#Display the login usesr version of main page if user is logined
		if self.user:
			posts = ndb.gql("select * from Post order by created desc limit 10")
			self.render("mainPage_LoginUser.html", user = self.user.name, user_entity = self.user,  posts = posts)
		#Display the normal view only version of main page is user is not login
		else:
			posts = ndb.gql("select * from Post order by created desc limit 10")
			self.render("mainPage.html", posts = posts)

	def post(self):
		self.render("editPost.html", 
			user = self.user,
			post_id = self.request.get("post_id"),
			post = ndb.Key('Post', int(self.request.get("post_id")), parent=parent_key.blog_key()).get(),
			postKey = self.request.get("postKey"),
			subjectValue = self.request.get("subjectValue"),
			contentValue = self.request.get("contentValue"),
			postValue = self.request.get("postValue"))
