import psutil , os , time , random
from multiprocessing import Process , Queue
import numpy as np
def calculus(massive_size,coef,index,queue):
    process = psutil.Process(os.getpid())
    process.nice(psutil.HIGH_PRIORITY_CLASS)
    massive = np.random.rand(massive_size)
    total_massive = massive * coef
    queue.put((np.round(np.sum(total_massive),2),coef,index))
if __name__ == '__main__':
    q = Queue()
    start_time = time.perf_counter()
    mem = psutil.virtual_memory()
    random_coefficient = random.randint(1, 5)
    size = 1_000_000
    amount_cpu = os.cpu_count()
    list_processes = []
    if mem.percent > 75:
        print('System is a bit overloaded..... calculations can be slowed down')
    for i in range(amount_cpu):
        p = Process(target=calculus,args=(size,random_coefficient,i,q))
        list_processes.append(p)
        p.start()
    for p in list_processes:
        p.join()
    results = []
    while not q.empty():
        results.append(q.get())
    print(f'Total duration: {time.perf_counter() - start_time}')
    print(results)



