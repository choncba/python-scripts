""" Deteccion de Sistema Operativo """
import os, platform

def clear():
    """ Limpia el terminal determinando el sistema operativo usado """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def info():
    """ Informacion del sistema operativo """
    clear()
    print("""
    Informacion:
    Procesador: {}
    Arquitectura: {}
    Sistema Operativo: {}
    Version: {}
    Plataforma: {}
    """.format(platform.processor(), platform.architecture()[0], platform.system(), platform.release(), platform.platform()))
    input("\nPresione Enter para continuar...")

info()