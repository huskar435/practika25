import random
import string
import time
import multiprocessing

def safe_file(lock_point, output_file, charing_calculate):
    random_text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(charing_calculate))
    with lock_point:
        with open(output_file, "a") as file:
            file.write(random_text)
            
def parallel_create(output_file="shared_output.txt", processing_count=10, character_calculate=100):
    lock_point = multiprocessing.Lock()
    processing_list = []
    start_time = time.time()
    
    for _ in range(processing_count):
        processing = multiprocessing.Process(target=safe_file, args=(lock_point, output_file, character_calculate))
        processing.start()
        processing_list.append(processing)

    for proces in processing_list:
        proces.join()
    lead_time = time.time() - start_time
    print(f"время выполнения: {lead_time:.4f} секунд")

if __name__ == "__main__":
    parallel_create()