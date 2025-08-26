import asyncio
import random

async def reading_simulation(file):
    processing_time = random.uniform(0.1, 5.0)
    await asyncio.sleep(processing_time)
    print(f"Документ '{file}' обработан за {processing_time:.2f} сек")

async def reading_parallel():
    total_documents = 10
    reading_tasks = [reading_simulation(f"document_{idx}.txt") for idx in range(total_documents)]
    await asyncio.gather(*reading_tasks)


asyncio.run(reading_parallel())