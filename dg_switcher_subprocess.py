from os import devnull
import subprocess
import time

def ping(host):
    init = time.time()
    cmd = "ping -n 1 " + host 
    response = True if subprocess.run(cmd, stdout=False) == 0 else False # Windows
    # response = True if os.system("ping -c 1 " + host) == 0 else False # Linux
    finish = time.time()
    time_delta = finish - init
    return response, time_delta
    
gw_local = "192.168.0.1"
gw_vpn = "172.26.16.1"
host = gw_vpn
counter = 0

while True:
    local_response, local_time_delta = ping(gw_local)
    vpn_response, vpn_time_delta = ping(gw_vpn)
    print(f"Ping a {gw_local} - {local_response} - {local_time_delta:.2f} seg.")
    print(f"Ping a {gw_vpn} - {vpn_response} - {vpn_time_delta:.2f} seg.")
    if vpn_response is not True or vpn_time_delta > 3:
        if counter < 3:
            counter+=1
        else:
            print("VPN Caida")
            counter = 0
    else:
        counter = 0
        print("Usar GW VPN")

    time.sleep(10)