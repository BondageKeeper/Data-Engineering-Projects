import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numba import njit , prange
nx , ny = 250 , 150
dx , dy = 2 , 1
dt = 0.1
cx , cy = 5 , 0.01
viscosity = 0.01
u = np.zeros((ny,nx))
v = np.zeros((ny,nx))
divergence = np.zeros((ny,nx))
pressure = np.zeros((ny,nx))
figure , axis = plt.subplots(figsize=(10,10),nrows=2,ncols=2)
img = axis[0,0].imshow(u,cmap='magma',origin='lower',vmin=-1,vmax=1)

def get_mask_from_image(path):
    import cv2
    loaded_image = cv2.imread(path,0)
    resized_image = cv2.resize(loaded_image,(nx,ny))
    _ , binary_values = cv2.threshold(resized_image,0,1,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    binary_values = cv2.flip(binary_values,0)
    return binary_values.astype(np.bool)
mask = get_mask_from_image('Clark_wing.png')

@njit(parallel=True)
def turbo_calculation(u,v,div,p,c_x,c_y,d_t,d_x,d_y,coeff):
    rows , cols = u.shape
    u_new = u.copy()
    v_new = v.copy()
    for i in prange(1,rows-1):
        for j in range(1,cols-1):
            if not mask[i,j]:
                u_new[i,j] = u[i,j] - c_x * (d_t / d_x) * (u[i,j] - u[i,j-1]) - \
                                      c_y * (d_t / d_y) * (u[i,j] - u[i-1,j]) + \
                                      coeff * (d_t / dx**2) * (u[i,j-1] - 2 * u[i,j] + u[i,j+1]) + \
                                      coeff * (d_t / dy**2) * (u[i-1,j] - 2 * u[i,j] + u[i+1,j])
                v_new[i,j] = v[i,j] - c_x * (d_t / d_x) * (v[i,j] - v[i,j-1]) - \
                                      c_y * (d_t / d_y) * (v[i,j] - v[i-1,j]) + \
                                      coeff * (d_t / d_x ** 2) * (v[i,j-1] - 2 * v[i,j] + v[i,j+1]) + \
                                      coeff * (d_t / d_y ** 2) * (v[i-1,j] - 2 * v[i,j] + v[i+1,j])
    for i in prange(1,rows-1):
        for j in range(1,cols-1):
            div[i,j] = ((u_new[i,j+1] - u_new[i,j-1]) / (2 * d_x) + (u_new[i+1,j] - u_new[i-1,j]) / (2 * d_y))
    for i in range(100):
        p_old = p.copy()
        for i in prange(1,rows-1):
            for j in range(1,cols-1):
                p[i,j] = ((p_old[i,j+1] + p_old[i,j-1]) * d_y ** 2 +
                         (p_old[i+1,j] + p_old[i-1,j]) * d_x ** 2 -
                         (div[i,j]*d_x**2*d_y**2)) / (2*(d_x**2 + d_y**2))
        p[:,-1] = 0.0
        p[:,0] = p[:,1]
        p[0,:] = p[1,:]
        p[-1,:] = p[-2,:]
    for i in prange(rows):
        for j in range(cols):
            if mask[i,j]:
                p[i,j] = 0.0
    #print(p)

    for i in prange(rows-1):
        for j in range(cols-1):
            if not mask[i,j]:
                u_new[i,j] -=  (d_t / (2 * d_x)) * (p[i,j+1] - p[i,j-1])
                v_new[i,j] -=  (d_t / (2 * d_y)) * (p[i+1,j] - p[i-1,j])
            elif mask[i+1,j] or mask[i-1,j] or mask[i,j+1] or mask[i,j-1]:
                compound_u_y = 0.0
                if mask[i+1,j]: compound_u_y += -u[i,j] / d_y
                if mask[i-1,j]: compound_u_y += u[i,j] / d_y
                compound_u_x = 0.0
                if mask[i,j+1]: compound_u_x += -u[i,j] / d_x
                if mask[i,j-1]: compound_u_x += u[i,j] / d_x
                u_new[i,j] = u[i,j] + viscosity * d_t * (compound_u_x / d_x + compound_u_y / d_y)
                compound_v_y = 0.0
                if mask[i+1,j]: compound_v_y += -v[i,j] / d_y
                if mask[i-1,j]: compound_v_y += v[i,j] / dy
                compound_v_x = 0.0
                if mask[i,j+1]: compound_v_x += -v[i,j] / d_x
                if mask[i,j-1]: compound_v_x += v[i,j] / d_x
                v_new[i,j] = v[i, j] + viscosity * d_t * (compound_v_x / d_x + compound_v_y / d_y)
            else:
                u_new[i,j] = 0.0
                v_new[i,j] = 0.0

    for i in range(rows):
        noise = np.random.uniform(-0.1,0.1)
        u_new[i,0] = 40.0 + noise
        v_new[i,0] = 0.0
        u_new[i,-1] = u_new[i,-2]
        v_new[i,-1] = v_new[i,-2]
    return u_new , v_new , p

rho = 1.3
p_inf = 0.0
dynamic_pressure = 0.5 * rho * (40.0 ** 2) #v_inf = 40.0 - here we take our normal speed actually
axis[0,0].set_title("Velocity animation")
axis[0,1].set_title("Pressure coefficient")
axis[0,1].grid(True)
line_upper, = axis[0,1].plot([],[],'r-',label='upper_aifoil')
line_lower, = axis[0,1].plot([],[], 'b-', label='lower_aifoil')
line_lift, = axis[1,0].plot([],[],label='lift_coefficient')
line_drag, = axis[1,1].plot([],[],label='drag_coefficient')
axis[0,1].legend()
axis[1,0].legend()
history_frames = []
history_frames_drag = []
history_cl = []
history_cd = []
fps_counter = 0
c_lift = 0
chord_length = 0

def render_motion(frames):
    global u, v ,fps_counter , c_lift , chord_length
    u, v, p = turbo_calculation(u, v, divergence, pressure, cx, cy, dt, dx, dy, viscosity)
    magnitude = np.sqrt(u ** 2 + v ** 2)
    img.set_array(magnitude)
    rows, cols = u.shape
    x_coords = []
    cp_upper = []
    cp_lower = []
    cp_front = []
    cp_back = []
    fps_counter += 1
    for j in range(1, cols - 1):
        wing_indices = np.where(mask[:, j])[0]
        if len(wing_indices):
            x_coords.append(j * dx)
            upper_wall_idx = wing_indices[0]
            lower_wall_idx = wing_indices[-1]
            p_top = p[upper_wall_idx - 5, j]
            p_bottom = p[lower_wall_idx + 5, j]
            cp_t = (p_top - p_inf) / dynamic_pressure
            cp_b = (p_bottom - p_inf) / dynamic_pressure
            cp_upper.append(cp_t)
            cp_lower.append(cp_b)

    for i in range(1, rows - 1):
        wing_indices_i = np.where(mask[i,:])[0]
        if len(wing_indices_i):
            front_wall_idx = wing_indices_i[0]
            back_wall_idx = wing_indices_i[-1]
            p_front = p[i,front_wall_idx - 5]
            p_back = p[i,back_wall_idx + 5]
            cp_b = (p_back - p_inf) / dynamic_pressure
            cp_f = (p_front - p_inf) / dynamic_pressure
            cp_back.append(cp_b)
            cp_front.append(cp_f)
            integral_cp_back_forward = np.array(cp_front) - np.array(cp_back)
            chord_length = len(cp_upper) * dx
            c_drag = (np.sum(integral_cp_back_forward) * dy) / chord_length
            history_frames_drag.append(fps_counter)
            history_cd.append(c_drag)
            line_drag.set_data(history_frames_drag,history_cd)

    if len(x_coords) > 0:
        line_upper.set_data(x_coords, cp_upper)
        line_lower.set_data(x_coords, cp_lower)
        chord_length = len(cp_upper) * dx
        cp_diff = np.array(cp_lower) - np.array(cp_upper)
        c_lift = (np.sum(cp_diff) * dx) / chord_length
        history_frames.append(fps_counter)
        history_cl.append(c_lift)
        line_lift.set_data(history_frames,history_cl)


    axis[0,1].relim()
    axis[0,1].autoscale_view()
    axis[1,0].relim()
    axis[1,0].autoscale_view()
    axis[1,1].relim()
    axis[1,1].autoscale_view()
    lift_newtons = ((rho * magnitude) / 2) * c_lift * chord_length
    #axis[1,0].set_title(f'lift is equal : {lift_newtons}')
    print(lift_newtons)

    #if fps_counter >= 320:
    #    ani.event_source.stop()
    return [img,line_upper,line_lower,line_lift,line_drag]



ani = FuncAnimation(figure,render_motion,frames=200,interval=20,blit=False)
plt.show()

