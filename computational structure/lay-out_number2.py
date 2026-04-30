import numpy as np
import psutil , multiprocessing 
def compute_pressure_force(y_mesh,x_mesh):
    pressure = (x_mesh * 0.1) + (y_mesh ** 2)
    chunk_force = np.sum(pressure)
    return chunk_force
def run_project():
    memory = psutil.virtual_memory()
    if memory.available / (1024**3) < 1.0:
        print('Program must be terminated because you have got low memory!')
        exit()
    x = np.linspace(0,10,100)
    y = np.linspace(0,5,50)
    X, Y = np.meshgrid(x,y)
    y_chunks = np.array_split(Y,2,axis=0) #for two processes
    x_chunks = np.array_split(X,2,axis=0)
    tasks =  zip(y_chunks,x_chunks)
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        results = pool.starmap(compute_pressure_force,tasks)
    print(f'total: {round(sum(results),3)} Newton')
if __name__ == '__main__':
    run_project()
