# Test de AsyncIO y ApScheduler
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# Delay Asíncrono
async def print_delayed(i, t):
    await asyncio.sleep(t)
    logging.info(f"Tarea {i} cada {t} segundos")

# Carga 10 task asíncronos
async def muestra():
    timer = time.perf_counter()
    for i in range(10):
        loop.create_task(print_delayed(i, 1))
    logging.info(f"Tiempo total: {(time.perf_counter() - timer):.4f} segundos")

loop = asyncio.get_event_loop()
scheduler = AsyncIOScheduler()

if __name__ == '__main__':
    # Cada 10 segundos, llama a la funcion muestra, las llamadas del scheduler son asíncronas y simultáneas
    scheduler.add_job(muestra, 'interval', seconds=10)
    scheduler.start()
    logging.info("Scheduler starts, press Ctrl+C to exit")

    try:
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        loop.close()