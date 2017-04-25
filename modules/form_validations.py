import re

# Functions to validate user input in the sign up page


def validate_username(self, username):
    if not valid_username(username):
        return "User name is not valid"
    elif valid_username(username):
        return ""


def validate_username_bool(self, username):
    if not valid_username(username):
        return False
    elif valid_username(username):
        return True


def validate_password(self, password):
    if not valid_password(password):
        return "Password is not valid"
    elif valid_password(password):
        return ""


def validate_password_bool(self, password):
    if not valid_password(password):
        return False
    elif valid_password(password):
        return True


def validate_verifyPassword(self, password, verifyPassword):
    if password != verifyPassword:
        return "Your passwords didn't match"
    elif password == verifyPassword:
        return ""


def validate_verifyPassword_bool(self, password, verifyPassword):
    if password != verifyPassword:
        return False
    elif password == verifyPassword:
        return True


def validate_email(self, email):
    if not valid_email(email):
        return "That's not a valid email"
    elif valid_email(email):
        return ""


def validate_email_bool(self, email):
    if not valid_email(email):
        return False
    elif valid_email(email):
        return True


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")


def valid_username(username):
    return USER_RE.match(username)


PASSWORD_RE = re.compile(r"^.{3,20}$")


def valid_password(password):
    return PASSWORD_RE.match(password)


EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")


def valid_email(email):
    return EMAIL_RE.match(email)
