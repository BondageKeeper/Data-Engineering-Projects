import tkinter as tk
import dearpygui.dearpygui as dpg
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
dpg.create_context()
def check_configs():
    import psutil
    from faker import Faker
    import multiprocessing
    fake = Faker('en_US')
    Faker.seed(42)
    virtual_memory = psutil.virtual_memory()
    virtual_memory_gb = f'Free virtual memory: {round(virtual_memory.total / (1024**3),3)} GB'
    disk = psutil.disk_usage('/')
    free_gb_disk = f'Free memory in the disk: {round(disk.free / (1024**3),3)} GB'
    dpg.set_value('virtual_memory_text',virtual_memory_gb)
    dpg.set_value('disk_memory_text',free_gb_disk)
    user_id = f'User id: {fake.random_number(digits=10,fix_len=True)}'
    dpg.set_value('user_id',user_id)
    amount_cores = f'amount of cores: {multiprocessing.cpu_count()}'
    dpg.set_value('cpu_count',amount_cores)
with dpg.window(label='settings',width=screen_width,height=screen_height // 3):
    dpg.add_button(label='get settings',callback=check_configs)
    dpg.add_spacer(height=50)
    dpg.add_text("",tag='virtual_memory_text')
    dpg.add_text("",tag='disk_memory_text')
    dpg.add_text("",tag='cpu_count')
    dpg.add_text("",tag='user_id')
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,(84, 107, 65, 255))
        dpg.add_theme_color(dpg.mvThemeCol_Text,(205, 190, 155, 255))
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(153, 173, 122 ,255))
        #dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(220, 204, 172, 255))
        #dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 248, 236))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(205, 190, 155, 255))
dpg.bind_theme(global_theme)



dpg.create_viewport(title='check-out',width=screen_width,height=screen_height)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
