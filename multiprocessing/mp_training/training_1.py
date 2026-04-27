#ONE
import time , random , multiprocessing
from multiprocessing import Array , Manager , Process
def calcul(d):
    return d ** 2
if __name__ == '__main__':
    start_time = time.perf_counter()
    data = [random.uniform(0,100) for _ in range(1000000)]
    with multiprocessing.Pool(processes=12) as pool:
        results = pool.map(calcul,data)
        finish_time = time.perf_counter()
        increment = finish_time - start_time
        print(increment)
#TWO
def calculations(p,v,s):
    multiplication = p * v * s
    return multiplication
if __name__ == '__main__':
    start_time = time.perf_counter()
    density_par = [random.randint(0,100) for _ in range(100)]
    velocity_par = [random.randint(0,100) for _ in range(100)]
    square_par = [round(random.uniform(0,10),2) for _ in range(100)]
    united_pars = list(zip(density_par,velocity_par,square_par))
    with multiprocessing.Pool(processes=12) as pool:
        results = pool.starmap(calculations,united_pars)
        print(results)
        finish_time = time.perf_counter()
        delta = finish_time - start_time
        print(delta)
#THREE
from multiprocessing import Process , Lock
def cal(d,l,num):
    try:
        d / 0
    except ZeroDivisionError:
        with l: #here we add lock just to make sure that processes won't write strings at the same time in th file
            with open('errors.txt','a') as file:
                file.write(f'Process {num+1} found a mathematical mistake!')
            print(f'Process {num+1} - error was fixed')
if __name__ == '__main__':
    start_time = time.perf_counter()
    data = 20
    lock = Lock()
    processes = []
    for i in range(3):
        p = Process(target=cal,args=(data,lock,i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
#Four
def calculation(massive,dict_m,index):
    massive[index] = massive[index] + random.randint(1,5)
    dict_m[f'Section_{index}'] = {'time':time.ctime()}
    print(dict_m)
    print(massive)

if __name__ == '__main__':
    initial_temp = Array('d',[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])
    processes = []
    with Manager() as manager:
        log_dict = manager.dict()
        for i in range(12):
            p = Process(target=calculation,args=(initial_temp,log_dict,i))
            processes.append(p)
            p.start()
        for q in processes:
            q.join()

