game_over = False
#score = 0
#def check_game_over():
#    global game_over , score #we can get a variable from external part of function using 'global'
#    if score == 0:
#        game_over = True
#    return game_over
#print(check_game_over())# a variable was changed from False to True due to this function

#def say_hi(name, age):
#    print("Hello " + name + ", you are " + str(age))
#
#say_hi('Mike', "35") #we call function
#say_hi('Steve', "50")

#def cube(num,degree):
#    return pow(num,degree) #when there is no print or we wanna store the value of function - we use RETURN for this VALUE
#
#result = cube(4,2.5)
#print(result)

#def get_integer():
#    return int(input('Give me a number: '))
#print(get_integer())  #due to "return" we have got the user value and it is being printed out

#def get_integer():
#    return int(input('Give me a number : '))
#age = get_integer()
#school_year = get_integer()
#if age > 19:
#    print('You are over the age of nineteen')
#print('You are in grade ' + str(school_year))

#def multiply(x,y):
#     return x * y  #ir gives the result of work of function
#result = multiply(3,4)
#print(result)

#One
#def say_hello():
#    print('Hello world')
#say_hello()
#say_hello()
#say_hello()
#Two
#def square(number):
#    result = number ** 2
#    return result
#print(square(2))
#print(square(5))
#print(square(7))
#Three
#def sum_numbers(x,y):
#    result = x + y
#    return result
#summed_num = sum_numbers(3,5)
#def double_result(number):
#    number = number * 2
#    return number
#print(double_result(summed_num))
#Four
#def filter_even_numbers(numbers):
#    sorted_list = []
#    for number in numbers:
#        if number % 2 == 0:
#            sorted_list.append(number)
#    return sorted_list
#result = filter_even_numbers([1,2,3,4,5,6,7,8,9,0])
#print(result)
#Five
#def sample_name(first_name,last_name,middle_name=None,separator = ''):#default arguments  #So we write here NONE by 'middle_name because maybe it does not exist
#    print(middle_name)
#    if middle_name is not None:
#        result = first_name + separator + last_name + separator + middle_name
#    else:
#        result = first_name  + separator + last_name
#    return result
#fn = str(input('Enter your first name : '))
#ln = str(input('Enter your last name : '))
#mn = str(input('Enter your middle name(if exists) : '))
#print(sample_name(fn,ln,mn,separator = "-")) #here we call "separator" because we want to REDEFINE its default argument
#def greet(name,greeting="Hello"):
#    print(f'{greeting} , {name}!')
#greet('Alice') #default argument
#greet('Bob','Hi') #modified argument
#####################################################
#Six
#def calculate_sum_recursive(numbers):
#     return numbers[0]
#r1 = calculate_sum_recursive([1,2,3,4,5])
#r2 = calculate_sum_recursive([2,3,4,5])
#r3 = calculate_sum_recursive([3,4,5])
#r4 = calculate_sum_recursive([4,5])
#r5 = calculate_sum_recursive([5])
#print(r1+r2+r3+r4+r5)
#Seven
#def print_message(text,color='black font'):
#     return text + color
#print(print_message('we have got ',color='red font'))
#Eight
#def user_data(name,age,city='unknown',is_active=False):
#    profile = {'name':name,'age':age,'city':city,'status': is_active}
#    return profile
#print(user_data('Meggie',25,is_active=True))
#Nine
#def format_price(price,currency='$',precision=1):
#    result = f'Price : {round(price,precision)} {currency}'
#    return result
#print(format_price(123.4567,currency = '*'))
#Ten
#def greet_user(name,lang='en',formality = 'formal'):
#    if lang == 'ru' and formality == 'formal':
#        return f'Привет {name}'
#    elif lang == 'ru' and formality != 'formal':
#        return f'Йоу дарова {name}'
#    elif lang == 'en' and formality == 'formal':
#        return f'Hello {name}'
#    elif lang == 'en' and formality != 'formal':
#        return f'Hi {name}'
#print(greet_user('Alice'))
#print(greet_user('Bob',formality='informal'))
#print(greet_user('Kostya',lang='ru',formality='informal'))
#Eleven

#def analyze_numbers(numbers,include_negatives=True):
#    summ = 0
#    if include_negatives:
#        count_num = len(data)
#        for num in numbers:
#            summ += num
#        average = round(summ / count_num,2)
#        max_num = max(numbers)
#        min_num = min(numbers)
#    else:
#        new_list = []
#        for num in numbers:
#            if num > 0:
#                 new_list.append(num)
#                 summ += num
#        count_num = len(new_list)
#        average = round(summ / count_num, 2)
#        max_num = max(new_list)
#        min_num = min(new_list)
#    return {'count': count_num, 'sum': summ, 'average': average, 'max': max_num, 'min': min_num}
#data = [1, -4 , - 17 , 19 , 34 , 9 ,-3]
#print(analyze_numbers(data,include_negatives=False))
#Twelve
#def build_config(app_name,version='1.0.0',debug = False ,allowed_hosts=None,database=None):
#    if allowed_hosts is None:
#        allowed_hosts = ["coolnet"]
#    if database is None:
#        database = {'type': "sqlite3" , 'name': "app.db"}
#    return  {'name': app_name , 'version': version ,'hosts': allowed_hosts,'database':database}
#print(build_config('Field',version='0.0.1',debug = True, database = None))

#lambda arguments: expression
#add = lambda x,y: x+y
#print(add(3,4))
#One
#numbers = [1,2,3,4,5,6,7,8,9]
#squared = map(lambda x: x ** 2, numbers)
#print(list(squared))
#Two
#numbers = [1,2,3,4,5,6,7,8,9]
#cubed = list(map(lambda num : pow(num,3) , numbers))
#print(cubed)
#Three
#list1 = ['apple','banana','cherry']
#length = map(lambda item : len(item), list1)
#print(list(length))
#Four filter(function,iterable)
#random_num = 5,12,8,15,3,20
#condition = list(filter(lambda num: num > 10 , random_num)) #we put dot because of the syntaxis of 'map' and 'filter'
#print(condition)
#Five(double)
#numbers = [1,2,3,4,5,6,7,8,9,0]
#result = list(map(lambda num : pow(num,2), filter(lambda num : num % 2 == 0 , numbers)))
#print(result)
#Six
#words = ['crankshaft','valve','engine','stator','piston','torque','pump']
#needed_things = list(map(lambda word:len(word) , filter(lambda word: len(word) > 5,words)))
#print(needed_things)
#Seven
#list1 = [1,3,5,7,9,11,23,54,685,764,3245465,222]
#result = list(map(lambda num: num * 2 , filter(lambda num: num > 10,list1)))
#print(result)
#Eight
#numbers = [12,23,34,45,56,78,89]
#sum_items = list(filter(lambda x : sum(int(item) for item in str(x))>5 , numbers ))
#print(sum_items)

#Nine(example) sorted(iterable object,key=None,reverse=False) : 'key' is a function that makes new conditions for sorting
#words = ['cat','dog','lizard','elephant']
#result = sorted(list(filter(lambda length : length % 2 != 0,map(len,words))),
#                reverse=True)
#print(result)
#numbers = [3,1,4,2]
#print(sorted(numbers)) #it sorts basically this list
#print(sorted(numbers,reverse = True))#reverses it
#words = ['banana','apple','cherry'] #sorting according to alphabet
#print(sorted(words))
#print(sorted(words,key=len))
#print(sorted(words,key=len,reverse=True))
#pairs = [(1,'z'),(2,'a'),(3,'m')]
#sorted_pairs = sorted(pairs,key=lambda x:x[1])
#print(sorted_pairs)
#Ten
#numbers = [12,23,34]
#result = list(map(lambda x : sum(int(el) for el in str(x)) ,numbers))
#print(result)
#Eleven
#list1 = ['cat','elephant','dog','butterfly']
#sorted_list = sorted(list1,key = lambda word : len(word),reverse = True)
#print(sorted_list)
#Ten
#list1 = [[1,2,3],[4,5],[6,7,8,9]] #[1,2,3]
#result = list(map(sum,list1)) #here sum counts every element
#print(result)
#Eleven
#print(ord('A'))
#print(chr(65))
#print(ord('O'))
#strings = ['ab','cd','e']
#result = list(map(lambda item: sum(ord(c) for c in item),strings)) #'ord' returns ASCII-code
#print(result)
#Twelve
#list1 = [[1,2,4],[3,5,6],[7,8,10]]
#result = list(map(sum,list1))
#result = list(map(lambda sublist: sum(x for x in sublist if x % 2 == 0),list1))
#print(result)
#Thirteen
#employees = [{'name':'Alice','salary':75000,'projects_done':8,'hours_per_week':40},
#             {'name':'Bob','salary':90000,'projects_done':12,'hours_per_week':45},
#             {'name':'Eva','salary':80000,'projects_done':6,'hours_per_week':35},
#             {'name':'Denis','salary':100000,'projects_done':15,'hours_per_week':50},
#             ]
#sum_salary = sum(map(lambda el: el['salary'],filter(lambda el: el['projects_done'] > 10 and el['hours_per_week'] <= 48,employees)))
#print(sum_salary)
#Fourteen
#vowels = 'aeiou'
#words = ['strength','rhythm','apple','queue']
#result = sum(map(lambda word : len(word),filter(lambda word: len(word) > 5 and all(char.lower() not in vowels for char in word),words)))
#print(result)
numbers = [45,3,78,12,99,23,56,7,88,101]
result = sorted(numbers,key = lambda x: (len(str(x))) ,reverse = False)
print(result)
#One
#words = ['py','python','ai','rocks','it','rocket']
#given_list = ', '.join(list(filter(lambda el : len(el) > 3 , words ))) #so 'join' makes its work here
#print(given_list)
#Two
#marks = "Ivan:5 , Anna:10 , Bob:2"
#pairs = marks.split(', ')
#sorted_pairs = sorted(pairs ,key = lambda x: int(x.split(':')[1]),reverse=True)
#result = list(map(lambda x: x.split(':')[0],sorted_pairs))
#print(result) #['Anna','Ivan','Bob']
#server_info = "192.168.1.1//admin//root_pass"
#res = server_info.split('//')#split removes symbol according to which it separates string
#print(res)
#Three
#files = ['internal_auth.py','public_index.html','internal_db.sql','profile.png']
#counting = list(filter(lambda el: el.startswith('internal_'),files )) #fillter is used  because we need a condition
#print(counting)
#Four
#emails = ['admin@mail.ru','@bad','user@','test@gmail.com']
#satisfied_emails = list(filter(lambda email: not email.find('@') == 0 and not email.endswith('@') , emails))
#print(satisfied_emails)
#Five
#prices = ['10,5','20,0','5,25']
#sorted_list = list(map(lambda item : item.replace(',','.'),prices))
#changed_type = list(map(lambda item : float(item),sorted_list))
#In only one string it looks like something like this:
#changed_type = list(map(lambda item : float(item.replace(',','.')),prices))
#print(changed_type)
#Six
#sentence = 'in 2026 I am 17 years old'
#separator = sentence.split()
#pulling_numbers = sum(list(map(lambda item : float(item) , filter(lambda item : item.isdigit() , separator))))
#print(pulling_numbers)
#Seven
#raw_words = ['apple!','orange2','!pear','banana']
#clean_sequence = '---'.join(list(filter(lambda el :el.isalpha(),map(lambda el : el.strip('_!'),raw_words))))
#print(clean_sequence)
#Eight
#fruits = ['coconut','apple','pear','cranberry','aurora']
#counting = list(map(lambda item : item.lower().count('a'),fruits)) #initially we lower it anf than count a specific letter
#print(counting)
#Nine
#domains = ['google.com','yandex.ru','python.org','my.site.net']
#sorted_domains = list(map(lambda el : el.upper(), filter(lambda el : el.endswith((".com",".org")),domains))) #Two parenthases because we give a tuple
#print(sorted_domains)
#Ten
#ids = [1,55,1024,7]
#filled_ids_list = ' | '.join(list(map(lambda num: str(num).zfill(6),ids)))
#print(filled_ids_list)
#Eleven
#files = ['script.py','main.py','app.js','utility_script.py','short.py']
#sorted_files = ' | '.join(list(filter(lambda file : len(file) > 5 ,
#                                      (map(lambda file : file.lower().strip('.py'),
#                                           filter(lambda file : not file.endswith('js'),files))))))
#print(sorted_files)
#Twelve
#staff_data = 'Ivan-30,Anna-25,Peter-40,Olga-25,Michael-30'
#sorted_data = staff_data.split(',')
#sort2 = list(map(lambda item : item.split('-'),sorted_data))
#print(sort2)
#Thirteen
#payments = [' $100' , '250$' , '$75' , '10' , '$500 ']
#total_sum = sum(list(map(lambda pay : float(pay) ,map(lambda pay : pay.strip(' $ '),payments))))
#print(total_sum)
#Fourteen
#emails = ["user1@gmail.com","admin@google.com","manager@corp.ru","user2@yandex.ru","support@google.com"]
#required_emails = ' | '.join(list(filter(lambda email: email.endswith('@google.com') or email.endswith('yandex.ru'),emails)))
#print(required_emails)
#Fifteen
#names = ['Peter','Megan','Kate','Anna']
#sorted_names = sorted(map(lambda name: name.strip(' _ '),names))
#print(sorted_names)
#And here are more complicated tasks:
#One
#raw_codes = [' id_001 ','№ID_002','item_net_003','id_004№']
#sorted_code = ', '.join(list(filter(lambda item: item.startswith('ID_')
#                          ,map(lambda item : item.upper().strip(' _№!*'),raw_codes))))
#print(sorted_code)
#Two
emails = ['user1@gmail.com','admin@google.com','manager@corp.ru','user2@yandex.ru','support@google.com','test@site.net']
sorted_emails = sorted(list(map(lambda email : email.split('@')[1]
                         , filter(lambda email : not email.endswith('.net'),emails))))
def not_repeat():
    total_domains = []
    for email in sorted_emails:
        if email not in total_domains:
            total_domains.append(email)
    return total_domains
print(not_repeat())
#Three
emails_list = [' !userdata@gmail.com','!? adminC:@google.org','!BobForger@yandex.ru','good_teacher@google.com','history@test.org' ,'music@info.net','dance@ya.ru']
sorted_emails = sorted(list(map(lambda email : email.split('.')[1] ,
                     map(lambda email : email.strip(" !?/#$*&")  ,
                        filter(lambda email : email.endswith(('com','org')),emails_list)))),reverse=True)
def additional_sorting():
    amount = 0
    total_domains = []
    for email in sorted_emails:
        amount += 1
        if email not in total_domains:
            total_domains.append(email)
    total_domains.append(f'| Entire amount of emails: {amount}')
    return total_domains
ready = additional_sorting()
print(additional_sorting())
#Four
raw_urls = ['  # https://www.google.com    ' , '   !?* http://subdomain.example.co.uk'   ,
"www.DEv-site.io/contact#footer   "," https://api.shop.com.ua  "
'ftp://files.storage.net/archieve/backup_2024.zip' ,
'invalid-url-without-protocol-error!'
]
sorted_urls = list(map(lambda url: url.split('.')[2]        ,
                          map(lambda url : url.lower(),
                            (filter(lambda url: url.startswith(('http"//','https://'))  ,
                               map(lambda url: url.strip(" ! ?#$*"),raw_urls))))))
print(sorted_urls)
