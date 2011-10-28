import os
import sys
import re
import time
import platform
import subprocess as sp

from nmadmin.utils import text

class SysCpu(object):
    ATTR_NAMES = [
        # id <- 'processor'
        'vendor_id',
        'model_name',
        'stepping',
        'cpu_MHz',
        'cache_size',
        'physical_id',
        'siblings',
        'core_id',
        'cpu_cores',
        'apicid',
        'initial_apicid',
        'fpu',
        'cpuid_level',
        'bogomips',
        'clflush_size',
        'cache_alignment',
        'address_sizes',
    ]

    def __init__(self, infos):
        for name in self.ATTR_NAMES:
            for i, j in infos:
                if 'processor' == i:
                    self.id = j
                    continue
                if name == i:
                    self.__dict__[name] = j

def get_cpus():
    infos = []
    with open('/proc/cpuinfo', 'r') as f:
        for i in f:
            spl = i.split(':')
            if 2 == len(spl):
                tup = (text.src2name(spl[0]),
                        text.plainstr(spl[1]))
                infos.append(tup)

    sep_index = []
    for loop, i in enumerate(infos):
        if 'processor' == i[0]:
            sep_index.append(loop)

    infos_seped = []
    for i in range(len(sep_index)):
        if i == len(sep_index)-1:
            infos_seped.append(
                    infos[sep_index[i]:])
        else:
            infos_seped.append(
                    infos[sep_index[i]:sep_index[i+1]])

    cpus = []
    for i in infos_seped:
        cpus.append(SysCpu(i))

    return cpus

def get_cpus_info():
    info = {
        'stat': None,
        'cpus': None,
    }
    def get_time_list():
        time_list = []
        with open('/proc/stat', 'r') as f:
            tmp = f.readline().split()[2:6]
        for i in tmp:
            time_list.append(int(i))
        return time_list

    def get_delta_time_list(gap=3):
        x = get_time_list()
        time.sleep(gap)
        y = get_time_list()
        for i in range(len(x)):
            y[i] -= x[i]
        return y

    dt = get_delta_time_list()
    cpuPct = 100 - (dt[len(dt) - 1] * 100.00 / sum(dt))

    info['stat'] = (time.strftime('%H:%M:%S'),
            '%.4f' % cpuPct)

    info['cpus'] = get_cpus()

    return info

def get_meminfo():
    ATTR_NAMES = [
        'MemTotal',
        'MemFree',
        'Buffers',
        'Cached',
        'SwapCached',
        'Active',
        'Inactive',
        'Active_anon',
        'Inactive_anon',
        'Active_file',
        'Inactive_file',
        'Unevictable',
        'Mlocked',
        'SwapTotal',
        'SwapFree',
        'Dirty',
        'Writeback',
        'AnonPages',
        'Mapped',
        'Shmem',
        'Slab',
        'SReclaimable',
        'SUnreclaim',
        'KernelStack',
        'PageTables',
        'NFS_Unstable',
        'Bounce',
        'WritebackTmp',
        'CommitLimit',
        'Committed_AS',
        'VmallocTotal',
        'VmallocUsed',
        'VmallocChunk',
    ]
    meminfo = []
    with open('/proc/meminfo', 'r') as f:
        for i in f:
            spl = i.split(':')
            if 2 == len(spl):
                attr = text.src2name(spl[0])
                kb = text.TextFilter(int).clean(spl[1])
                mb = kb/1000
                meminfo.append((attr, kb, mb))

    return meminfo

if '__main__'  ==  __name__:

    unumber = os.getuid()
    pnumber = os.getpid()
    what = os.uname()
    used = os.times()

    print "User number",unumber
    print "Process ID",pnumber
    print "System information",what
    print "System information",used

    print '--------------platform---------------'

    print 'uname:', platform.uname()
    print
    print 'system   :', platform.system()
    print 'node     :', platform.node()
    print 'release  :', platform.release()
    print 'version  :', platform.version()
    print 'machine  :', platform.machine()
    print 'processor:', platform.processor()
    print 'interpreter:', platform.architecture()
    print '/bin/ls    :', platform.architecture('/bin/ls')

    print '--------------command---------------'

    cmdBuff = os.popen('top -p 851')
    print 'y'
    print cmdBuff.read()
    cmdBuff.close()
        #with open('sysinfo.txt', 'a') as f:
            #f.write(cmdBuff.read())
    print '-----end-----'
