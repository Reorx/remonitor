from django.db.models.base import Model
from django.db.models import *

from base.models import BaseRModel

# TODO condition report
class Service(BaseRModel):
    name = CharField(max_length=32)

    path_root = CharField(max_length=256)
    path_deployer = CharField(max_length=256)
    path_pid = CharField(max_length=256)
    path_nginx_conf = CharField(max_length=256)
    path_access_log = CharField(max_length=256)
    path_error_log = CharField(max_length=256)

    def __unicode__(self):
        return 'service'

    class Meta:
        db_table = 'service'

    @property
    def pid(self):
        pass

class Process(BaseRModel):
    name = CharField(max_length=32)
    pid_path = CharField(max_length=256)

    def __unicode__(self):
        return 'process'

    class Meta:
        db_table = 'process'
