import numpy as np
import psutil , multiprocessing , time
def complete_velocity_chunk(data_chunk):
    x_axis = np.power(data_chunk,2)
    y_axis = np.power(data_chunk,3)
    z_axis = np.power(data_chunk,4)
    return np.sqrt(x_axis**2 + y_axis**2 + z_axis**2)
def run_simulation():
    start_time = time.perf_counter()
    num_elements = 100_000_000
    chunks = np.array_split(np.linspace(0,1000,num_elements),4) #so we split into four for FOUR processes
    #and here we write our memory checking block:
    memory = psutil.virtual_memory()
    #disk = psutil.disk_usage('/') #worth to use if we want to save something on the disk
    #free_disk_gb = round(disk.free / (1024**3),2)
    if memory.available / (1024**3) < 5 :
        print('Lack of memory!')
        return
    print(f'Calculations will be including all: {multiprocessing.cpu_count()} cores')
    cores = multiprocessing.cpu_count()
    #and after this checking we call our function for calculus:
    with multiprocessing.Pool(processes = cores) as pool:
        results = pool.map(complete_velocity_chunk,chunks)
        print(np.concatenate(results)) #due to concatenation we have got one united list
    print(f'Overall time: {time.perf_counter() - start_time} seconds')
if __name__ == '__main__':
    run_simulation()
