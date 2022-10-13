# Script que cambia el default gateway al backup en caso de no recibir respuestas del main
# Funciona en Python 2 y 3, en cualquier sistema operativo

import os
import time

TIME_DELTA = 10 # Tiempo de guarda para realizar el cambio, en segundos

def ping(host):
    if os.name == "nt":
        return True if os.system("ping -n 1 " + host) == 0 else False # Windows
    else:
        return True if os.system("ping -c 1 " + host) == 0 else False # Linux
    
def switch_dg(new_ip, old_ip):
    if os.name == "nt":
        os.system("route add 0.0.0.0 mask 0.0.0.0 "+new_ip)
        os.system("route del 0.0.0.0 mask 0.0.0.0 "+old_ip)
    else:        
        os.system("sudo -A ip route add default via " + new_ip)
        os.system("sudo -A ip route del default via " + old_ip)
    
gw_main = "192.168.0.1"
gw_backup = "172.26.16.1"
time_up = 0
time_down = 0
current_status = True
last_status = True

while True:
    current_status = ping(gw_main)                  
    if current_status:
        if last_status == False:
            if time_up == 0:
                time_up = time.time()
            else:
                if (time.time() - time_up) > TIME_DELTA:
                    print("*** Cambio a GW MAIN ***")
                    #switch_dg(gw_main, gw_backup)
                    last_status = current_status
                    time_down = 0
        time.sleep(1)
    else:
        if last_status == True:
            if time_down == 0:
                time_down = time.time()
            else:
                if (time.time() - time_down) > TIME_DELTA:
                    print("*** Cambio a GW BACKUP ***")
                    #switch_dg(gw_backup,gw_main)
                    last_status = current_status
                    time_down = 0

        

        
        