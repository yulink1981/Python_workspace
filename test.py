import psutil
import datetime

print(psutil.cpu_times(percpu=True))

print(psutil.cpu_times().user)
print(psutil.cpu_percent(interval=1,percpu=False))

mem = psutil.virtual_memory()
print(psutil.swap_memory())
print(mem.available,mem.free,mem.total)
print(psutil.disk_partitions())
print(psutil.disk_usage('c:\\'))
print(psutil.disk_io_counters(perdisk=True))
print(psutil.net_io_counters())
print(psutil.users())
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

netstat = psutil.net_connections()

for x in netstat:
    print(x)

net_ifstat = psutil.net_if_stats()
#ps = psutil.cpu_percent()
#print(ps)
for y in net_ifstat:
    print(y)




