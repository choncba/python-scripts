# Test for icmplib
# https://pypi.org/project/icmplib/
# 
# Author: Luciano Bono
# Date:   2021-12-30
#
import asyncio
from icmplib import ping, multiping, async_ping, async_multiping

# Single Host
host = ping('1.1.1.1', count=10, interval=0.2)

print(host)

# Multiple Hosts
hosts = multiping(['10.0.0.5', '127.0.0.1', '::1'])

for host in hosts:
     if host.is_alive:
         print(f'{host.address} is up!')
     else:
         print(f'{host.address} is down!')

# Single Host, Async - Non Blocking

async def is_alive(address):
     host = await async_ping(address, count=10, interval=0.2)
     return host.is_alive

asyncio.run(is_alive('1.1.1.1'))    

# Multiple Hosts, Async - Non Blocking

async def are_alive(*addresses):
     hosts = await async_multiping(addresses)
     
     for host in hosts:
         if not host.is_alive:
             return False

     return True

asyncio.run(are_alive('10.0.0.5', '127.0.0.1', '::1'))



