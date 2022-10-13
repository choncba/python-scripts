import asyncio

"""
mensaje: Función que esperara un tiempo determinado, para
luego mostrar el texto.
"""
async def mensaje(texto, s):
    await asyncio.sleep(s)
    print(texto)
    
loop = asyncio.get_event_loop()

# # Primera tarea
# loop.create_task(mensaje("Mensaje #1", 2))


# # Segunda tarea
# loop.create_task(mensaje("Mensaje #2", 1))

for i in range(10):
    loop.create_task(mensaje(f"Mensaje {i}",1))

loop.run_forever()
loop.close()
