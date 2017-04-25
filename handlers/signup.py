from handlers.mainhandler import MainHandler
import modules.form_validations as form_validations
from models.user import User


class Signup(MainHandler):
    def get(self):
        self.render("form.html", message=self.request.get("message"))

    def post(self):
        self.username = self.request.get("username")
        # Validate username
        messageUsername = form_validations.validate_username(
            self, self.username)
        boolUsername = form_validations.validate_username_bool(
            self, self.username)

        # Validate password
        self.password = self.request.get("password")
        messagePassword = form_validations.validate_password(
            self, self.password)
        boolPassword = form_validations.validate_password_bool(
            self, self.password)

        # Validate Verify Password
        verifyPassword = self.request.get("verifyPassword")
        messageVerifyPassword = form_validations.validate_verifyPassword(
            self, self.password, verifyPassword)
        boolVerifyPassword = form_validations.validate_verifyPassword_bool(
            self, self.password, verifyPassword)

        # Validate email
        self.email = self.request.get("email")
        messageEmail = ""
        if self.email != "":
            messageEmail = form_validations.validate_email(self, email)
            boolEmail = form_validations.validate_email_bool(self, email)

        if boolUsername and boolPassword and boolVerifyPassword and (
                self.email == "" or boolEmail):
            self.done()
        else:
            self.render(
                "form.html",
                usernameMessage=messageUsername,
                usernameValue=self.username,
                passwordMessage=messagePassword,
                verifyPasswordMessage=messageVerifyPassword,
                emailMessage=messageEmail)


class Register(Signup):
    def done(self):

        # make sure that the user has not already signed up
        u = User.by_name(self.username)
        if u:
            errorMessage = "User already exists"
            self.render('form.html', error=errorMessage)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect("/")
