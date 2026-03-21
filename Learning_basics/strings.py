#find / index (gives index)
#var = 'apple pie'
#print(var.find('pie')
#
#method 'zfill() add zeros until a desirable length
#a = '42'.zfill(5)
#print(a)
#b = '1024'.zfill(3) #He have already got the attainable length
#print(b)
#here is training of this new method
#Number one
#folders = ['C:','Users','Admin','Documents']
#path = "\\".join(folders) # \\ is like just \
#print(path)
#Two
#runners = ['Alexandr','Bob','Frick']
#stuff = "->".join(runners)
#print(stuff)
#Three
#products = [
#    {"id":1,"name":"Laptop","price":1200},
#    {"id":2,"name":"Mouse","price":50},
#    {"id":3,"name":"Laptop","price":200},
#]
#new_list = []
#combination = list(map(lambda x : x['name'],products))
#result = '/**'.join(combination)
#print(result)
#Four
#numbers = [1,2,3,4,5,6,7,8,9,10]
#result1 = list(map(lambda num : str(num) , filter(lambda num : num % 2 == 0 and num < 10, numbers)))
#result2 = '-'.join(result1)
#print(result2)
#split is actually another world in comparison to 'join'(it makes reverse actions)
#text = 'apple,banana,cherry'
#fruits = text.split(",")
#print(fruits)

#method 'isdigit' returns TRUE if a string consist of the numbers only and if there is one string digit(or more) - it returns False
#phone_number = '1234567890'
#print(phone_number.isdigit())#True
#age = '35 years old'
#print(age.isdigit())#False
#empty_string = ''
#print(empty_string)#False
#data_list = ['apple','10','banana','200','pie123']
#new_list = []
#for item in data_list:
#    if item.isdigit():
#        new_list.append(item)
#print(new_list)
#ONE(for training is_digit())
#data = ['apple','1024','orange','55','7abc','999','kernel_v3','42']
#result = list(filter(lambda item: item.isdigit() and int(item) > 50 , data))
#print(result)

#Also there is method so-called 'strip()'  it removes specific symbols(easily removes gaps if there are no arguments) , it deletes from borders to the first unknown argument
#text = "...!!!Hello!!!...."
#print(text.strip(".!"))
#One
#user_login = ' alex_pro_2026 \n'
#print(len(user_login))
#print(len(user_login.strip())) #minus three stupid symbols
#Two
#price_data = "$$$#1500#$$$"
#print(price_data.strip('#$'))

#REPLACE(it actually replace a particular string)
#phrase = 'I love Java'
#correct = phrase.replace('Java','Python')
#print(correct)

#count(it counts how manu times the value shows up)
#v = 'banana'.count('a')
#print(v)

#encode()   turns string into bytes
#variable = 'Hello'.encode('utf-8') #'utf-8' is type of cryptography
#print(variable)

#isalpha (if there are only letters without numbers in the string)
#print('Python3'.isalpha()) # it is False because there is 3


