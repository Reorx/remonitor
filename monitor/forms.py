from django import forms
from models import Service, Process

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('nid', 'md5id', 'created_time', )

    def __init__(self, req=None, *args, **kwargs):
        if req:
            self.req = req
            super(ServiceForm, self).__init__(data=req.POST, *args, **kwargs)
        else:
            super(ServiceForm, self).__init__(*args, **kwargs)

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ('nid', 'md5id', 'created_time', )

    def __init__(self, req=None, *args, **kwargs):
        if req:
            self.req = req
            super(ProcessForm, self).__init__(data=req.POST, *args, **kwargs)
        else:
            super(ProcessForm, self).__init__(*args, **kwargs)
