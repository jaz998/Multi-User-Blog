import random
from string import letters
import hashlib
import hmac
from config import config


def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(config['secret'], val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if make_secure_val(val) == secure_val:
        return val


def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)


def valid_pw(name, password, h):
    salt = h.split(',')[0]
    if make_pw_hash(name, password, salt) == h:
        return True
    else:
        return False
