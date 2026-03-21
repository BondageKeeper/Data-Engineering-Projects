#so , this library is being used for looking for sample text of email and so forth/ re - regular expressions
import re
#text1 = 'turbopumps are used for improving a capacity of an engine '
#match = re.search(r'engine',text1)  #r - it makes sure that python is not going to spoil the text
#search looks for a coinciding word(return only one sample)
#if match:
#    print('Found it!')
#    print(match.group()) #it returns a part of text with searching word
#
#text2 = 'My friend has many apples and these apples are very delicious'
#matches = re.findall(r'apples',text2)
#print(matches) #gives it two times
#
#text3 = 'My friend has many apples and these apples are very delicious'
#new_text = re.sub(r'apples','pears',text3) #replaces indicated words
#print(new_text)
#Now lets learn new metasymbols :

#1) ^ - it means that coincide must happen only at the beginning of a sentence
#text4 = 'The quick brown fox'
#sorted_text = re.findall(r'^The',text4)

#2) $ - it means that coincide must happen only at the end of the string
#text4 = 'The quick brown fox'
#sorted_text = re.findall(r'fox$',text4)
#print(sorted_text)

#3) \b - the position between symbols of other words
#text5 = 'The fox jumps over the dog'
#output = re.findall(r'\bfox\b',text5)
#print(output)

#4 also , there are samples that lok for a particular symbol
# . - looks for the particular symbol
#print(re.findall(r'c.t','cat cot'))
#print(re.findall(r'.','my key word is 437'))

#5 \d - looks for the numbers
#print(re.findall(r'\d','Number 123456@89')) #gives every number\
#print(re.findall(r'\d\w+','my key word is 437'))

#6 \D - NOT the numbers
#print(re.findall(r'\D','Number 123456@89'))

#7 \w - numbers and letters (in summary symbols of words)
#print(re.findall(r'\w+','Hello, world_123'))
#print(re.findall(r'\w','my key word is 437 ',re.ASCII))

#8  \W - not the symbols of words
#print(re.findall(r'\W','Hello, world_123'))

#9 [abc] - coincides minimum with one symbol
#print(re.findall(r'[aeiou]','Python is cool')) #enumeration of present letters

#10 [^abc] - excluding enumeration
#print(re.findall(r'[^0-9]','price is 123 pounds')) #there are no numbers here

#print(re.findall(r'^Hello','Hello world'))
#print(re.findall(r'[A-Z]','Google is a Popular Name'))
#print(re.findall(r'\d{4}','1914 - start of first world war , 1939 - start of second world war')) #{4} means four numbers IN ROW
#print(re.findall(r'\bm\w+','monkey , cat'))

#match = re.findall(r'[еЕ]д[ау]','еда,беду,победу')
#match = re.findall(r'[().?а-яА-Я0-9]','Еда,555 беДу,-6 победу') #two numbers in row  [-0-9] - says that we look for numbers or other things
#[а-яА-Я0-9] - we can add lots of the intervals of numbers or letters without SEPARATING
#print(match)

#text = 'Google , Gooogle , Goooooogle'
#match1 = re.findall(r'o{2,5}?',text) #from 2 to 5 given #look for 'o'
#match2 = re.findall(r'Go{,4}gle?',text) #here we look for the entire word
#print(match1,match2)

#phone = '89123456789'
#match = re.findall(r'8\d{10}',phone) #{10} means 10 numbers in sequence
#print(match)



#text10 = 'ticket costs 500 rubles , popcorn 350 rubles , drink 200 rubles'
#match_num = re.findall(r'\b\d00',text10) #we lust write '00' nearby
#print(match_num)

#text11 = ' Anna and Alice went to Albert'
#words = re.findall(r'\bA\w+',text11)
#print(words)

#text12 = 'Я иду в лес а он нет'
#words = re.findall(r'\b\w\b',text12)
#print(words)

text13 = 'sequence of years : 2015 , 2018 , 2019 , 2026'
years = re.findall(r'\d{4}',text13)
print(years)

text14 = 'Car , cat , catch , crow , cradle'
words = re.findall(r'\bc\w+',text14)
print(words)

text15 = 'B123OR , +78944345234 , pants@gmail.com'
car_number = re.findall(r'\D\d{3}\D{2}',text15) #remeber that D is not the number
print(car_number)

#{0,} - from zero to infinite repetitions --- *         {1,}  - from one to infinite ---- +
#? - from zero to one / also looks for the little sequences
#\s - that means a 'gap' symbol

#text = 'стеклянный , стекляный'
#match = re.findall(r'стеклянн?ый',text) #? tells that Н can repeat from 0 to 1(maybe there is or maybe there is no
#print(match)   #? means that 'H' can exist or cannot at all

text = 'author = A.S.Pushkin ; title = Evgeniy Onegin; price = 200 ; year = 2001'
#\s - means that maybe there are gaps(maybe there are no)
# [^;] - means the inversion when we combine ^ and [] and it actually excepts the symbol in these []
match = re.findall(r'\w+\s*=\s*[^;]+',text)
option2 = text.split(';')
print(match , option2)

text20 = '<p>Image <img src=bg.jpg> in text </p>'
match20 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]+',text20)
print(match20)

text21 =  'visit sites mysite.com or text-server.net for testing '
match21 = re.findall(r'\b[\w-]+\.\w+\b',text21)  #[\w-] it means : look for any letter of hyphen
print(match21)

text22 = 'contacts : apple@gmail.com , orange@yahoo.british , wrong address : pear@gmail.com , user-name.123@domain.net'
match22 = re.findall(r'\b[\w.-]+@\w+\.\w{2,4}\b',text22) #we must put \ nearby comma .
print(match22)

text23 = 'numbers: 123-456-7890 , (987)-654-3210 , 55.123.4567 , 88005553535'
numbers = re.findall(r'\b[\d.-]+\b',text23)
numbers2 = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',text23) #(? - maybe there are paranthases
print(numbers2)

text24 = 'lat = 5 , lon = 7 , a = 5' # we want to get key with value
#match24 = re.findall(r'lat\s*=\s*\d+|lon\s*=\s*\d+',text24) # | means or
# we use () when we need to apply some methods to the indicated symbols
match24 = re.findall(r'(lat|lon)\s*=\s*(\d+)',text24) #that is very useful because we can look for the keys in big datas
#?: - preserve only keys
print(match24)

text202 = "<p>Image <img src='bg.jpg'> in text </p>"
match32 = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1",text202)
#1 means that we put the value of the first preserved brace(1 -  because it is its index)
print(match32)

#some tasks fo practicing:
data1 = ' admin@site.com , support@service.ru , my_mail123@gmail.net , no_name_mail@.ru'
sorting = re.findall(r"\b[\w.-]+@\w+\.\w{2,4}\b",data1)
print(sorting)

data2 = '+79001112233 , 89154445566 , 9057778899 , 12345'
ready_numbers = re.findall(r'((\b7|8)\d{10}\b)',data2)
ready = []
for mess in ready_numbers:
    redefined = list(mess)
    for item in redefined:
        if len(item) >= 10:
            ready.append(item)
print(ready)

data3 = 'cat.jpg , summer_photo.jpeg , script.py , old_backup.jpg , doc.pdf'
recycled = re.findall(r'\b[\w.-]+\.jpe?g\b',data3) #so , we lust write ? nearby the letter
print(recycled)

data4 = 'http://google.com , https://github.com , ftp://files.org , http://localhost'
checking = re.findall(r'\bhttps?://\w+\.\w{2,4}\b',data4)
print(checking)

data5 = 'Log: ID: 550 [OK] , Log: ID: 12345 [Error] , User ID: 77(Pending)'
ID_credentials = re.findall(r'\b(?:ID:\s+)(\d+)\b',data5)
print(ID_credentials)

data6 = 'Point(x:12.5, y:3.14)'
cords = re.findall(r'\(x:([\d.]+), y:([\d.]+)\)',data6) #we put \ by () and it let our program literally see these perenthases ()
#interior () basically capture numbers and store them(as the data or keys) - it is used for uniting datas
print(cords)

data7 = 'Hello world world , this is a test test string. '
#\1 - a search which compare next word with words from First Capture Group
double_data = re.findall(r'(\w+)\s+\1\b',data7)
print(double_data)

data8 = 'http://google.com , https://github.com , ftp://files.org'
domen = re.findall(r'(?:http|ftp)s?://([\w.-]+)',data8)
print(domen)

data9 = 'Success starts with small steps . Look at the moon.'
letters = re.findall(r'(\w)\1',data9)
print(letters)

data10 = 'Item:Laptop , Price:$1200;Item:Mouse, Price:$25;Item:Keyboard, Price:$75'
sorting_pair = re.findall(r'Item:(\w+)\s*,\s*Price:([\w$.]+);?',data10)
print(sorting_pair)

data11 = 'Names: Mr. Smith, Mrs.Jones, Ms.Davis , Dr. Adams , Mr . Brown'
last_names = re.findall(r'\s*(?:Mr|Mrs|Ms|Dr)\s*\.\s*([\w.-]+),?',data11)
print(last_names)

data12 = 'Emails: user1@gmail.com , admin_user@corp.local , john.doe@yandex.ru'
users = re.findall(r'\s*([\w.-]+)(?:@[\w.-]+)',data12)
print(users)

data13 = 'IPs: 192.168.1.1 , 10.0.0.10 , 172.16.172.16 , 192.168.192.168'
coincide = re.findall(r'\s*(\w+)\.(\w+)\.\1\.\2',data13)
print(coincide)

data14 =  'abccba !!@@## %%'
search2 = re.findall(r'(.)\1',data14) # . - looks for symbols
print(search2)

data15 = '11 22 34 53 66'
pair_numbers = re.findall(r'(\d)\1',data15)
print(pair_numbers)

data16 = 'I need to go go home now now'
pairs = re.findall(r'\b(\w{1,3})\s*\1',data16)
print(pairs)

text203 = "<p>Image <img src='bg.jpg'> in text </p>"
match33 = re.findall(r"<img\s+[^>]*src=(?P<name>[\"'])(.+?)(?P=name)",text202)
#We can label these storage braces  (?P<name>...) - name for this storage , if we want to summon it : (?P=name) ,
#so that is quite useful cause we can relate to the specific 'capture storage' by using its name
print(match33)

with open('map.xml.txt','r') as f:
    lat = []
    lon = []
    for text in f:
        match = re.findall(r'<point\s+[^>]*?lon=([\"\'])([0-9.,]+)\1\s+[^>]*lat=([\"\'])([0-9.,]+)\1',text)
        if len(match) > 0:
            lon.append(match[0][1])
            lat.append(match[0][3])
    print(lon , lat , sep='\n')

cool_string = 'Lets go! #python_is_cool , learn #regex , #GEEK'
regex_search = re.findall(r'#[\w.-]+\b',cool_string)
print(regex_search)

prices = 'Price: apples - 1.5 pounds , bananas - 3 $ , discount - 10% , delivery - 5 pounds'
pointed_currency = re.findall(r'(\b[\d.]+\s*pounds|\b[\d.]+\s*\$)',prices)   #| -- one thing OR another thing
print(pointed_currency)

deadlines = 'Report relates to 2023-10-12 , subsequent deadline is 15/11/2023 or 19.11.23'
hidden_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}|\b\d{2}/\d{2}/\d{4}|\b\d{2}\.\d{2}\.\d{2}',deadlines)
print(hidden_dates)

text = '<font color=#CC0000>'
match = re.search(r'(\w+)=(#[\da-fA-F]{6}\b)',text)
print(match)


text = 'I have an apple ,a banana and a banana'
result_search = re.search(r'banana',text)
print(f'type of the result search: {type(result_search)}')
print(f'founded word: {result_search.group()}')  #we use group for getting the word(it gives us only one pattern of it)
print(f'type of the result search: {result_search.span()}')

string = 'Contacts : Ivan ivan@example.com Petr petr.p@domain.ru'
res_search = re.search(r'\b\w+@[\w.-]+',string) #gives us only ONE email instead giving entire amount of emails
print(res_search.group())

str22 = 'there are  +7(999)123-45-67 or +8-800-555-35-35'
search22 = re.search(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}',str22)
print(search22.group()) #so we can get the number easily too
print(search22.span()) #index of the beginning  and end

str33 = 'appointment - 10:00 AM , dinner - 01:30 PM'
search33 = re.search(r'(\b[\w:.-]+\s*AM|PM)',str33)
print(search33.group())

text = 'apple , banana , cherry '
search_match = re.search('banana',text)
print(f'Search match {search_match.group() if search_match else 'None'}')

match_match = re.match('banana',text) #'match' looks for a coincide only at the beggining of the string
#print(f'Match match {search_match.group() if search_match else 'None'}')

url1 = 'https://google.com'
url2 = '://www.google.com'
pattern = r'https://'
match1 = re.match(pattern,url1)
match2 = re.match(pattern,url2)
print(bool(match1)) #True because start with pattern
print(bool(match2)) #False because does not start with pattern

text = 'login of file: data_log_123.txt'
pattern = r'data_log'
match_check = re.match(pattern , text)
print(match_check) #because there is no pattern at the beginning

#re.compile is used for using a particular pattern multiple times

pattern = re.compile(r'\d+')
result1 = pattern.findall('2 apples')
result2 = pattern.findall('3 bananas') #so wo don't need to write a pattern each time
print(result1,result2)
#One more example ;
price_pattern = re.compile(r'\d+!')
price1 = '200! rubles !'
price2 = '300! rubles '
print(price_pattern.findall(price1),price_pattern.findall(price2))

#text_sample = 'python is a snake , python is a programming language'
#iterator = re.finditer(r'python',text_sample)
##due to finditer we can iterate lots of things without slowing down the code
#for match in iterator:
#    print(f'Found  {match.group()} on position {match.start()} : {match.end()}') # instead of using start() and end() we just can use span()

#^ - starts with specific thing   #$ - ends with specific thing
log_data = "2023-10-01 12:01:05 [ERROR] Code:404; 2023-10-01 12:05:10 [WARNING] Code:200; 2023-10-01 12:10:00 [ERROR] Code:500;"
iterator = re.finditer(r'\b\s*\[(ERROR|WARNING)\]\s*Code:\d{3}',log_data)
for match in iterator:
    print(f'Found: {match.group()} on the position {match.span()}')

#also there is re.split() and due to this method we can divide string more precisely
data30 = 'apple,banana;cherry -date'
print(data30.split(',')) #simple 'split' very weak because it can contain only ONE separator
print(re.split(r'[,;\s-]+',data30))  #'[]' - list of suitable results for ONE position

#method re.sub looks for the pointing pattern and it substitutes them by new pattern
#re.sub(pattern,replacement_string,original_string)  --- layout

text50 = 'Hello    world ,   How     are              you? '
cleaned_text = re.sub(r'\s+',' ',text50) #replace many spaces
print(cleaned_text)

comment = 'You are such a bastard'
censored_comment = re.sub(r'\bbastard\b','###censored###',comment)
print(censored_comment)

#one quite useful example of re.sub:
phone = '212-555-1212'
formatted_phone = re.sub(r'(\d{3})-(\d{3})-(\d{4})',r'\2-\1-\3',phone) #so it is pretty easy to change the places of specific items too
print(formatted_phone)

contacts = """
Контакт 1: Иван Петров <ivan.petrov@example.com>
Контакт 2: Maria Ivanova <m.ivanova@domain.ru>
Контакт 3: Просто email: test_user123@gmail.com
Контакт 4: John Doe <john.doe@corporate.org>
"""
hidden_emails = re.sub(r'<?[\w._-]+@[\w.]+>?','[EMAIL_HIDDEN]',contacts)
print(hidden_emails)
#IGNORECASE , MULTILINE , DOTALL

#re.IGNORECASE looks for coincides without caring about register of letters of words
text = 'Error in sentence 10 , error in sentence 25 , ERROr in sentence'
pattern = r'error'
result_case_sensitive = re.findall(pattern,text)
print(f'Without flag: {result_case_sensitive}')  #with register
result_ignore_case = re.findall(pattern,text,re.IGNORECASE)
print(f'With flag: {result_ignore_case}') #without register

products = 'Телевизор (SALE!),Мышка с подсветкой,Кофеварка Sale,Книга о Python (sale)'
pattern = re.compile(r'\bsale',re.IGNORECASE)
print(pattern.findall(products))

#re.MULTILINE  -- this flag looks for the beginning and ends in EVERY STRING not in the entire string
report = """
Задача 1: Начата
Задача 2: В процессе
Задача 3: ГОТОВО
Задача 4: Отменена
Задача 5: готово
"""
ready_list = re.findall(r'\bготово',report,re.IGNORECASE | re.MULTILINE) #we should use | for two flags
print(ready_list)

text60 = '<start>Information\ntwo cool\nstrings'
text = """
Начало кода
/*
Это важный 
многострочный комментарий
*/
Конец кода
"""
pattern = r'/\*.*\*/'  #dot(.) cannot cut \n
result_no_dotall = re.search(pattern,text60)
print(f'without flag: {result_no_dotall}')
result_dotall = re.search(pattern,text,re.DOTALL)
print(f'with flag: {result_dotall.group()}')

log_entry = """<log>
Ошибка: Системный сбой
Код: 500
Статус: Критично
</log>"""
pattern = re.compile(r'<log>(.*)</log>',re.DOTALL)
print(pattern.findall(log_entry))


config_data = """
# Настройки сервера
timeout  = 30  # время ожидания
max_users=  500
# DEBUG_MODE = true  ---  #should be ignored
status = active
"""
correct_pattern = re.findall(r'^[\w_]+\s*=\s*\w+',config_data, re.MULTILINE) #we use every line
list11 = []
for item in correct_pattern:
    new_item = re.sub(r'=',':',item)
    list11.append(new_item)
print(list11)

#ONE
text60 = """Error: database connection failed
info: server started
ERROR: unauthorized access detected
Warning: low disk space"""
#first sample:
changed_text60 = re.sub(pattern='error',repl='[BLOCKER]',string=text60,flags = re.IGNORECASE|re.MULTILINE)
print(changed_text60)
#second sample:
pattern60 = re.compile('error',re.IGNORECASE | re.MULTILINE)
changed_text60_1 = pattern60.sub('[BLOCKER]',text60)
print(changed_text60_1)

#TWO
text70 = 'timeout=30;  retry=5,  mode=fast    debug=off ,   port=8080'
split_text70 = re.split(r'[;,\s]+',text70)
for value in split_text70:
    iterator70 = re.finditer(r'\w+=\s*\d+',value)
    for item in iterator70:                #so I should create second iteration because it is 'finditer'
        print(item.group())
#THREE

text80 = """print("Hello")
/* 
Этот комментарий
занимает несколько
строк 
*/
print("World")"""
pattern80 = re.compile(r'/*(.*)*/')
redacted_text80 = pattern80.sub('[REDACTED]',text80)
print(redacted_text80)

#FOUR
raw_phones = [
    "8-800-555-35-35",
    " +7 926 123 45 67 ",
    "Call us at 495.777.12.12 доб 101",
    "Просто текст без номера",
    "88005553535"
]
satisfactory_number = []
for number in raw_phones:
    if re.findall(r'\+?\s*\d(\s*|-)\d{3}\1\d{3}\1\d{2}\1\d{2}',number):
        digits = re.sub('[\s\-\+]*','',number)
        format_russian = f'+7 ({digits[1:4]}) {digits[4:7]}-{digits[7:9]}-{digits[9:11]}' #so it is possible to create sample
        satisfactory_number.append(format_russian)
    else:
        wrong_sample_number = 'INVALID PHONE NUMBER'
        satisfactory_number.append(f'{number} - {wrong_sample_number}')
print(satisfactory_number)
#FIVE
raw_html_text = """<p>Свяжитесь с нами: John.Doe@example.com или support@company.org. </p>
<a href='mailto:*TEST_USER@MAIL.RU#'>Написать админу</a> 
<span>Наш старый адрес: old.email@domain.net</span>"""
sorted_emails = []
emails = re.findall(r'[\w._]+@[\w.]+',raw_html_text)
for email in emails:
    email = email.strip('.#*&^%*$').lower()
    sorted_emails.append(email)
print(sorted_emails)

#SIX
html_credentials = """<div class="product-card" data-id="7712">
    <span class="sku-info" style="display:none;">SKU_9921_ALPHA</span>
    <h2 class="title">  Смартфон   NextGen Pro+  12/256GB  </h2>
    <div class="price-container">
        <span class="currency">₽</span>
        <span class="value">89&nbsp;990,00</span>
        <span class="old-price" data-raw="105000">105 000 руб.</span>
    </div>
    <script>
        window.INITIAL_DATA = {"stock": "in_stock", "rating": 4.85, "reviews": 124};
    </script>
</div>"""
#given_title = re.findall(r'"title">\s*(\w+\s*\w*\s*[\w\+]*\s*[\w/]*)',html_credentials)[0]
#cleaned_title = re.sub(r'\s{2,100}',' ',given_title)
#articul_scu = re.findall(r'>(SKU_\d+_\w+)<',html_credentials)[0]
#price_info = re.findall(r'"value"([\w>&^;,]+)',html_credentials)[0]
#total_price = ''
#for letter in price_info:
#    if re.findall(r'[0-9]',letter):
#        total_price += letter
#sample_total_price = f'{total_price[:2]} {total_price[2:5]},{total_price[5:]} rubles'
#print(f'{cleaned_title} , {sample_total_price} , {articul_scu}')

#log_entry = '192.168.1.1 - - [17/mar/2026:22:15:01 +0300] "GET /index.html HTTP/1.1" 200 1234'
#useful_cargo1 = re.findall(r'^[\w.-]+',log_entry)
#useful_cargo2 = re.findall(r'\[([\w/:]+)',log_entry)
#useful_cargo3 = re.findall(r'\s+\w{3}\s+',log_entry)
#useful_cargo1.extend(useful_cargo2)
#useful_cargo1.extend(useful_cargo3)  #extend changes exactly CURRENT LIST not a new one
#print(useful_cargo1)

#raw_data = "Contacts: test@mail.ru , wrong@@gmail.com, admin@company.online , fake@node , user.name@service.com"
#sorted_emails = re.findall(r'[\w.]+@[\w]+\.(?:com|ru|online)',raw_data,re.IGNORECASE)
#print(sorted_emails)

#raw_logs = "Item_1 costs $49.99, Item_2 is 1500RUB, Item_3 priced at 25.0 euro. also we have discount for 10$."
#clean = re.findall(r'(\$|euro|rub)?\s?([\d.]+)\s?(\$|euro|rub)?',raw_logs,re.IGNORECASE)
#total = []
#for thing in clean:
#    unity = ' '.join(thing)
#    if len(unity) > 3:
#       total.append(unity)
#print(total)

#data_str = "id: 101, name: 'Ivan', role: 'ADMIN'; id: 102, name: 'ALICE', role: 'Engineer'; id: 103, name: 'bob', role: 'intern'"
#data_search = re.findall(r'\s?name:\s?\'(\w+)\'\s?,\s?role:\s?\'(\w+)\'',data_str,re.IGNORECASE)
#print(data_search)

#logs = "2023-10-15 10:05:20 [INFO] System started. 15-10-2023 10:06:01 [ERROR] Connection failed! 2023/10/15 10:07:00 [debug] all ok"
#report_search = re.findall(r'\[\w+\]\s?([\w ]+)',logs,re.IGNORECASE)
#print(report_search)
#
#content = """
#| Repo Name | Status | Owner | URL |
#| :--- | :--- | :--- | :--- |
#| [pandas-dev] | active | @py_user | https://github.com |
#| [scikit-learn] | DEPRECATED | @science_man | http://old-repo.io |
#| [tensorflow_2] | active | @google_dev | https://storage.googleapis.com |
#| [pytorch-master] | beta | @fb_team | https://github.com |
#"""
#content_search = re.findall(r'\|\s?\[([\w_-]+)\]\s?\|\s?(?:active|beta)\s?\|\s?@([\w_-]+)\s?\|\s?((?:https://|http://)[\w.-]+com)',content,re.IGNORECASE)
#print(content_search)
#############################################################################################
#also there is re.split() and due to this method we can divide string more precisely
#data30 = 'apple,banana;cherry -date'
#print(data30.split(',')) #simple 'split' very weak because it can contain only ONE separator
#print(re.split(r'[,;\s-]+',data30))  #'[]' - list of suitable results for ONE position
#####################################################
#raw_data = "Apple, 10; Banana 20 , Orange;30; Grape 40"
#separated_menu = re.split(r'[,;\s]+',raw_data)
#print(separated_menu)

#path_string = "C:\\Users\Admin//Documents\\\Projects/Python//scripts"
#only_names = re.split(r'[\\/]+',path_string)
#print(only_names)
#tags_raw = "#study #python, #data_science###machine_learning #coding,##sql"
#without_add = re.split(r'[#,_\s]+',tags_raw)
#print(without_add)
#raw_logs = "ID_001[DATA]Temperature: 22.5ID_002[DATA]Humidity: 45%ID_003[DATA]Pressure: 760mmHg"
#cleaned_measurements = re.split(r'ID_00\d+\[DATA\]',raw_logs,flags=re.IGNORECASE)
#print(cleaned_measurements)

#chat = "User1: Hello! <sys_time:12:00> User2: Hi there. [sys_code: 200] User1: How are you? {sys_status: ok}"
#clean_messages = re.split(r'<.*?>|\[.*?\]|\{.*?\}',chat)
#print(clean_messages)
#
#big_data = "[10:00:01] System start. [10:05:20] Connection lost... [10:05:25] Retrying... [10:06:00] Success!"
#cleaned_data = re.split(r'\[.*?\]',big_data)  #.*? - it will cut a content of whole string
#print(cleaned_data)
#
#report = "---SECTION: [Electronics]--- TV: 500, Laptop: 1200 ---section: [Home]--- Sofa: 300, Table: 150 ---Section: [Books]--- Novel: 20, Comic: 10"
#cleaned_report = re.split(r'---section:\s\[.*?\]---',report,flags=re.IGNORECASE)
#print(cleaned_report)


#html_data = "<div><p>Товар: <b>Смартфон</b></p><span>Цена: 500$</span><br></div>"
#refined_html = re.sub('<.*?>',' ',html_data)
#print(refined_html)
#
#user_info = "Клиент Иван, карта: 4432-1234-5678-9012, тел: +7(999)123-45-67"
#safe_user_info = re.sub(r'\d{4}-\d{4}-\d{4}-\d{4}','*',user_info)
#print(safe_user_info)

#american_log_dates = "Error at 10/25/2023, Warning at 11/05/2023, Info at 12/31/2022" #2023-10-25
#russian_log_dates = re.sub(r'(\d{2})/(\d{2})/(\d{4})',r'\3-\1-\2-',american_log_dates)  #So it is quite useful to use enumeration of capturing paranthases
#print(russian_log_dates)

#dirty_text = "The data is is very very important important for for us."
#cleaned_text = re.sub(r"(\w+)\s+\1",r'\1',dirty_text)
#print(cleaned_text)

#message = 'My card number is 1234 5678 9101 1121'
#safe_message = re.sub(r'\b(\d{4})\s+(\d{4})\s+(\d{4})\s+(\d{4})',lambda m : "*"*4+" "+"*"*4+" "+"*"*4+" "+ m.group(4),message)
#print(safe_message)

text = "Apple: 100$, Bread: 50$, Milk: 80$"
#res = re.findall(r'(\w+)\s?\$',text)
result = re.sub(r'(\w+)\s?\$',lambda el : str(int(el.group(1)) / 2) + '$',text)
print(result)

