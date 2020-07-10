__author__ = 'mingyu.zhang'
import requests
import chardet
import psutil

#print(psutil.cpu_count(),psutil.cpu_count(logical=False),psutil.cpu_times())
#print(psutil.virtual_memory(),psutil.swap_memory())
#print(psutil.disk_partitions(),psutil.disk_usage('/'),psutil.disk_io_counters())
#print(psutil.net_io_counters(),psutil.net_if_addrs(),psutil.net_if_stats())
#print(psutil.net_connections())
#print(psutil.pids())
p=psutil.Process(4212)
print(p.name(),p.exe(),p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent().name())
print(p.children(),p.status(),p.username())