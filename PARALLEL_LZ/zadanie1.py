import random
import time
import threading

def create_file(file):
    with open(file, "w") as f:
        numbers = [str(random.randint(1, 100)) for _ in range(100)]
        f.write("\n".join(numbers))

# Однопоточная запись
start = time.time()
for i in range(10):
    create_file(f"single_threading_{i}.txt")
time_single = time.time() - start

# Многопоточная запись
start = time.time()
threads = []
for i in range(10):
    thread = threading.Thread(target=create_file, args=(f"multi_threading_{i}.txt",))
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()
time_multi = time.time() - start


print(f"Однопоточный режим: {time_single:.4f} секунд")
print(f"Многопоточный режим: {time_multi:.4f} секунд")

if time_multi < time_single:
    difference = time_single - time_multi
    print(f"Многопоточность быстрее на {difference:.4f} секунд ")
elif time_multi > time_single:
    difference = time_multi - time_single
    print(f"Многопоточность медленнее на {difference:.4f} секунд ")
else:
    print("Время выполнения одинаковое")