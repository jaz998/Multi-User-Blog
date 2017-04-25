from google.appengine.ext import ndb


def blog_key(name='default'):
    return ndb.Key('blogs', name)


def users_key(group='default'):
    return ndb.Key('users', group)
