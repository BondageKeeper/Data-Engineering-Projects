import dearpygui.dearpygui as dpg
import tkinter as tk
from faker import Faker
fake = Faker('en_US')
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
FIELD_WIDTH = 500
dpg.create_context()
left_padding = (screen_width // 2) - (FIELD_WIDTH // 2)
text_padding = int(left_padding + (FIELD_WIDTH / 3.5))

def switch_to_menu():
    dpg.configure_item('register_window',show=False)
    dpg.configure_item('main_menu_window',show=True)

def update_database(login,password):
    import psycopg2
    import os
    system_variable = os.environ.get('DB_PASSWORD')
    configurations = {
    'host' : '127.0.0.1',
    'port' : '5432',
    'database' : 'passwords',
    'user' : 'postgres',
    'password' : system_variable}
    conn = psycopg2.connect(**configurations)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS password_storage (
    id SERIAL PRIMARY KEY , 
    login TEXT ,
    password TEXT ,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    cursor.execute('INSERT INTO password_storage (login,password) VALUES (%s,%s)',(login,password))
    conn.commit()
    cursor.close()
    conn.close()

def generate_login():
    import getpass
    login =  getpass.getuser() + '_' +  fake.word()
    dpg.configure_item('login_input',default_value=login)

def generate_password():
    password = fake.bothify(text='????????????###')
    dpg.configure_item('password_input',default_value=password)

def check_credentials():
    import re
    user_login = dpg.get_value('login_input').strip(' ')
    user_password = dpg.get_value('password_input').strip(' ')
    if len(user_login) < 3 and len(user_password) >= 5:
         dpg.configure_item('error_text',default_value='login should at least have 3 letters')
    elif len(user_login) < 3 and len(user_password) < 5:
         dpg.configure_item('error_text',default_value='login should at least have 3 letters and password should at least have 5 letters')
    elif len(user_login) >= 3 and len(user_password) < 5:
         dpg.configure_item('error_text',default_value='password should at least have 5 letters')
    else:
        if re.findall(r'[!@#$%^&*()+?=-]',user_login) or re.findall('[!@#$%^&*()_+=-]',user_password):
             dpg.configure_item('error_text',default_value="please , don't use symbols like @#% etc in your password or login!")
        else:
            if not re.findall(r'[1234567890]',user_password):
                 dpg.configure_item('error_text',default_value="please , write at least one number in your password")
            else:
                switch_to_menu()
                dpg.configure_item('error_text', default_value="")
                update_database(user_login,user_password)

def render_window():
    import numpy as np
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding,35,30)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding,19)
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg,(129, 154, 145,255))
            dpg.add_theme_color(dpg.mvThemeCol_Text,(238, 239, 224,255))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled,(238, 239, 224,255))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg,(129, 154, 145,255))
            dpg.add_theme_color(dpg.mvThemeCol_Border, (238, 239, 224,255))
            dpg.add_theme_color(dpg.mvThemeCol_Button,(167, 193, 168 ,255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(209, 216, 190 ,255))
            dpg.add_theme_color(dpg.mvThemeCol_InputTextCursor,(129, 154, 145))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (209, 216, 190 ,255))
        with dpg.theme_component(dpg.mvInputText):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg,(167, 193, 168 ,255))
    dpg.bind_theme(global_theme)

    with dpg.window(label='sign up',width=screen_width,
                    height=screen_height,tag='register_window',no_resize=True,no_title_bar=True,no_move=True,no_collapse=True):
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=text_padding)
            dpg.add_text('Write here your data')
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=left_padding)
            with dpg.group():
                with dpg.group(horizontal=True):
                    dpg.add_input_text(hint='login',tag='login_input',width=FIELD_WIDTH)
                    dpg.add_button(label='generate login',callback=generate_login,width=int(FIELD_WIDTH/2.2))
                dpg.add_spacer(height=10)
                with dpg.group(horizontal=True):
                    dpg.add_input_text(hint='password',password=False,width=FIELD_WIDTH,tag='password_input')
                    dpg.add_button(label='generate password',callback=generate_password,width=int(FIELD_WIDTH / 2.2))
                dpg.add_spacer(height=10)
                dpg.add_button(label='Create an account',width=FIELD_WIDTH,callback=check_credentials)
                with dpg.tooltip(dpg.last_item()):
                    dpg.add_text('Press to sign up')
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=(FIELD_WIDTH - FIELD_WIDTH // 4))
            dpg.add_text("", tag='error_text')

    with dpg.window(label='main menu',width=screen_width,
                    height=screen_height,tag='main_menu_window',show=False,no_resize=True,no_title_bar=True,no_collapse=True,no_move=True):
        with dpg.plot(label='sino graphic',width=-1,height=300):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis,label='Axis X(radians)')
            with dpg.plot_axis(dpg.mvYAxis,label='Axis Y'):
                x_data = np.linspace(0,10,100)
                y_data = np.sin(x_data)
                dpg.add_line_series(x_data,y_data,label='y=sin(x)',tag='sin_series_tag')
render_window()
dpg.create_viewport(title='check out',width=screen_width,height=screen_height)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_global_font_scale(1.35)
dpg.start_dearpygui()
dpg.destroy_context()
