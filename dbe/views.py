import re
from cStringIO import StringIO

from django.http import HttpResponse, HttpResponseRedirect
import config

from utils.viewsbase import render_tpl, resp_json, ApiBaseError
from utils.text import TextFilter
from utils.ostools import read_file, cmd_output

import dbquery

def home(req, tpl='dbe/home.html'):
    pass

def v_dbviews(req, tpl='dbe/dbviews.html'):
    cdic = {}
    return render_tpl(req, tpl, cdic)
    pass

def v_dbviews_show(req, nid):
    pass

def v_explorer(req, tpl='dbe/explorer.html'):
    cdic = {}
    cdic.update(
            dbquery.execute('select id, name from service'))
    #print cdic
    return render_tpl(req, tpl, cdic)

def v_explorer_ajax_exec(req):
    exp = req.POST.get('exp')
    if not exp:
        return HttpResponse('No Expression', 400)
    data = dbquery.execute(exp)
    return resp_json(data)

def v_explorer_ajax_create(req):
    exp = req.POST.get('exp')
    if not exp:
        return HttpResponse('No Expression', 400)
    data = dbquery.execute(exp)
    return resp_json(data)
