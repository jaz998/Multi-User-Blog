from handlers.mainhandler import MainHandler
from models.user import User


class Login(MainHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            errorMessage = "Invalid login details"
            self.render("login.html", error=errorMessage, user=username)
