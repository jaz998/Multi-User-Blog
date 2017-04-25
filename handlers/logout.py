from handlers.mainhandler import MainHandler


class Logout(MainHandler):
    def get(self):
        self.logout()
        self.redirect('/')
