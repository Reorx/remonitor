from django.db.models.base import Model
from django.db.models import *
from django.contrib.auth.models import User

class UserInfo(Model):
    user = ForeignKey(User, related_name='info', unique=True)
    screen_name = CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.user.email
