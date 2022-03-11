import re

def ip_address_valid(ip_address):
    if re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip_address):
        return True
    else:
        return False

def dni_valid(dni):
    if re.match(r'^[0-9]{8}', dni):
        return True
    else:
        return False

def validar_ip():
    print("Validar direccion IP - CTRL+C para salir")
    while True:
        ip_address = input("Ingrese una direccion IP: ")
        if ip_address_valid(ip_address):
            print("Direccion IP valida")
        else:
            print("Direccion IP invalida")

def validar_dni():
    print("Validar DNI - CTRL+C para salir")
    while True:
        dni = input("Ingrese un DNI: ")
        if dni_valid(dni):
            print("DNI valido")
        else:
            print("DNI invalido")            

validar_dni()            
    