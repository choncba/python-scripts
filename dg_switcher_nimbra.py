#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
################################################################################################################

Script que conmuta el default Gateway de los nodos Gateways N8BEL03 en Belgrano y N8FIB01 en San Lorenzo
Ambos Nodos son Gateways de la red 172.18.38 con configuracion de redundancia
Las interfaces de Outband están siempre activas y conectadas a la VPN DCN Gestion
El default Gateway es normalmente hacia la interfaz de outband.
Este script detecta la perdida de conectividad outband y la conmuta al Gateway redundante 
dentro de la red 172.18.38

                   _____ VPN - DCN Gestion _______
                  /                               \
                 /                                 \
          172.18.28.18                        172.18.28.22    - OUTBAND
                |                                   |
             N8BEL03                             N8FIB01
                |                                   |      
           172.18.38.1                        172.18.38.2     - INBAND

Utiliza el ejecutable *resedit* dedicado. Incluido en las todas las GX de Nimbra 688/680/640/390/360

################################################################################################################

@Author: Luciano Bono 
@Date: 2022

"""
import os, time, re

def ping(host):
    return True if os.system("ping -c 1 " + host) == 0 else False # Linux

def switch_dg(new_ip):
    # Primero debo averiguar cual es el default
    for i in range(10):
        resp = os.popen("resedit get -r -n .ipconf.routes.{}.dest".format(i)).read()    # Lee la respuesta del comando en string
        # Encuentro el default gateway, lo reemplazo
        if "default" in resp:
            os.system("resedit set -n .ipconf.routes.{}.gw -v {}".format(i, new_ip))
            break

gw_outband_BEL = "172.18.28.17"
gw_outband_SLO = "172.18.28.21"
gw_inband_BEL = "172.18.38.1"
gw_inband_SLO = "172.18.38.2"

# Obtengo el nombre del nodo, y seteo gateways main y backu segun corresponda
system_name = re.search('"(.*)"', os.popen("resedit get -r -n .system.name").read()).group(1)
if system_name == "n8bel03":
    main_gw = gw_outband_BEL
    backup_gw = gw_inband_SLO
elif system_name == "n8fib01":
    main_gw = gw_outband_SLO
    backup_gw = gw_inband_BEL

print("{} Main Gateway: {}".format(system_name,main_gw))

up_counter = 0
current_gw = main_gw

while True:
    current_status = ping(main_gw)
    if current_status is not True:                       # Si no responde ping
        up_counter = 0                                   # Contador de UP en cero
        if down_counter < 3: down_counter += 1           # Si la cuenta es menor que 3 incremento
        if down_counter == 3 and current_gw == main_gw:  # 3er ping erroneo y estoy en main
            print("*** Cambio a GW Backup ***")
            current_gw = backup_gw
            switch_dg(backup_gw)                         # Conmuto al GW Backup
    else:
        down_counter = 0
        if up_counter < 3: up_counter += 1
        if up_counter == 3 and current_gw == backup_gw:
            print("*** Cambio a GW MAIN ***")
            current_gw = main_gw
            switch_dg(main_gw)
    time.sleep(1)
