import os 
print(f'Name of folder where our interpreter: {os.getcwd()}')
print(f'All files and folders: {os.listdir(path='C:/Users/rycha/PycharmProjects/PythonProject')}') #replace \ by / for success
print(os.environ.get('USERNAME')) #environ is a tuple where all data of computer are being stored
#os.path.join(path1, path2, ...) - connects paths putting / or \ in accordance to the system(Linux or Windows or Docker)
print(os.path.join('data','db','users.sql'))
print(os.path.exists('C:/Users/rycha/PycharmProjects/PythonProject/exp_Faker.py')) #True if exists unless False
print(os.path.split('C:/Users/rycha/Desktop/app_log.txt')) #We separate name of the file from a main path
print(os.path.isfile('C:/Users/rycha/Desktop/music3.db')) #True because it is a FILE
print(os.path.isdir('C:/Users/rycha/Desktop/music3.db')) #False because it is NOT a FOLDER
print(os.environ.get('DB_PASSWORD'))
 
print(os.cpu_count())
print(os.path.getsize('C:/Users/rycha/Desktop/music3.db'))
print(os.name) #name of the system operation(nt - Windows)

#Also I would like to highlight one specific moment :
#1) how to find out a path to our code?
current_dir = os.path.dirname(os.path.abspath(__file__))
#explanation:
#1) __file__ always stores in itself a path to the specific file where this string is written
#for example this string is written in:  C:/Projects/cards-hub/Backend/routers/main.py
#2)os.path.abspath - guarantees that this path will be complete from the root-folder of the disk
#basically the path will be the same bu we want to make sure that the path will be absolutely complete
#3)os.path.dirname(...) it cuts the name the file itself(main.py) or exp_os.py will be deleted from the path
print(os.path.dirname(__file__))
print(__file__)
#in the end we have got a complete path to the folder of script
base_dir = os.path.dirname(os.path.dirname(current_dir)) #we can go higher and higher even we can come to the base_dir(Backend say)
#4) and maybe we want to create a path to our html file , so it looks something like this:
html_path = os.path.join(base_dir,'Frontend','html_page.html')
#why should we use os.path.join instead of writing the same path in FileResponse?:
#explanation: the problem is hidden in / and \ . In windows we use \ but in Docker or Linux we use / so if we write say \ in
#FileResponse it will work on Windows but Docker won't accept it so because of that we have got an error .
#os.path.join adjusts these special elements in Docker and in Windows and everything works perfectly because of that


