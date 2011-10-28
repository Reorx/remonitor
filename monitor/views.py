# Create your views here.
import re
from cStringIO import StringIO

from django.http import HttpResponse, HttpResponseRedirect
import config

from utils.viewsbase import render_tpl, get_rsrc
from utils.text import TextFilter
from utils.ostools import read_file, cmd_output

from models import Service, Process

import sysinfo
import forms

def v_home(req, tpl='monitor/home.html'):
    cdic = {}
    return render_tpl(req, tpl, cdic)

def v_sysinfo(req, tpl='monitor/sysinfo.html'):
    cdic = {}
    cdic['main_tab'] = 0
    #cdic['cpus_info'] = sysinfo.get_cpus_info()
    cdic['meminfo'] = sysinfo.get_meminfo()
    return render_tpl(req, tpl, cdic)

def v_services(req, tpl='monitor/services.html'):
    cdic = {}
    cdic['main_tab'] = 1
    cdic['services'] = Service.objects.all()
    return render_tpl(req, tpl, cdic)

def v_services_create(req, tpl='monitor/services_create.html'):
    cdic = {}
    cdic['main_tab'] = 1
    if 'GET' == req.method:
        form = forms.ServiceForm()
        cdic['form'] = form
        pass
    elif 'POST' == req.method:
        form = forms.ServiceForm(req)
        cdic['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/monitor/services')
        pass
    else:
        pass
    return render_tpl(req, tpl, cdic)

@get_rsrc('monitor.Service', 'id')
def v_services_ajax_show(req):
    t = req._target
    # basic info
    # relevant confs
    # now: cpu, mem
    # graph: cpu, mem, nginxlog,
    # control options
    return HttpResponse(req._target.name)

def v_services_ajax_ctrl(req):
    pass

def v_processes(req, tpl='monitor/processes.html'):
    cdic = {}
    cdic['main_tab'] = 2
    cdic['processes'] = Process.objects.all()
    return render_tpl(req, tpl, cdic)

def v_processes_create(req, tpl='monitor/processes_create.html'):
    cdic = {}
    cdic['main_tab'] = 2
    if 'GET' == req.method:
        form = forms.ProcessForm()
        cdic['form'] = form
        pass
    elif 'POST' == req.method:
        form = forms.ProcessForm(req)
        cdic['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/monitor/processes')
        pass
    else:
        pass
    return render_tpl(req, tpl, cdic)

def v_processes_ajax_show(req):
    pass

def v_processes_ajax_ctrl(req):
    pass

def v_cmd(req, tpl='monitor/cmd.html'):
    cdic = {}
    cdic['main_tab'] = 3
    return render_tpl(req, tpl, cdic)

def v_cmd_ajax_exec(req):
    cmd = req.POST.get('cmd')
    if not cmd:
        return HttpResponse('No CMD Output', status='404')
    cmdOutput = cmd_output(cmd)
    if not cmdOutput:
        return HttpResponse('Uneffect CMD', status='400')
    return HttpResponse(cmdOutput)

def v_cmd_ajax_create(req):
    pass

def v_nginx(req):
    cdic = dict(
        conf = None,
        pid = None,
        process = None
    )

    try:
        cdic['conf'] = read_file(config.NGINX['CONF_PATH'])
    except IOError:
        pass

    if cdic['conf']:
        conf_file = StringIO(cdic['conf'])
        for line in conf_file:
            rep = re.compile(ur'^pid\s(?P<path>.*);')
            res = rep.search(line)
            if res:
                pid_path = res.group('path')
                pid_raw = read_file(pid_path)
                cdic['pid'] = TextFilter(int).clean(pid_raw)
                print cdic['pid']
        conf_file.close()

    if cdic['pid']:
        cdic['process'] = cmd_output('ps u p %s' % cdic['pid'])
        print cdic['process']

    return HttpResponse('xx')
