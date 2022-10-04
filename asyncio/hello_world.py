# Ver https://docs.python.org/es/3/library/asyncio-task.html

import asyncio
import time

# Ejemplo 1
async def main1(timer):
    start = time.perf_counter()
    await asyncio.sleep(timer)
    print(f"Realizado en {time.perf_counter() - start} segundos")

asyncio.run(main1(1))

# Ejmeplo 2

async def mostrar(tiempo,que):
    await asyncio.sleep(tiempo)
    print(que)

async def main2():
    
    start = time.perf_counter()
    
    await mostrar(1, "Hola")
    await mostrar(2, "Chau")

    print(f"Realizado en {time.perf_counter() - start} segundos")

asyncio.run(main2())

# Ejemplo 3 - Mismo que anterior pero como tareas, tarda 1 segundo menos, porque ambas tareas comienzan a la vez
async def main3():
    
    start = time.perf_counter()
    
    tarea1 = asyncio.create_task(mostrar(1, "Hola"))
    tarea2 = asyncio.create_task(mostrar(2, "Chau"))

    await tarea1
    await tarea2

    print(f"Realizado en {time.perf_counter() - start} segundos")

asyncio.run(main3())