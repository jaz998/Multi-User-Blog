class Logout(MainHandler):
    def get(self):
        self.logout()
        self.redirect('/')
