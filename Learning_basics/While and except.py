#Quit = input('Type "enter" to quit: ')
#while Quit != "enter":
#    Quit = input('Type "enter" to quit: ') #it is useful combination of input and while for checking something

#while True:
#    usr_command = input("Enter your command :")
#    if usr_command == 'quit':
#        break
#    else:
#        print('You typed ', usr_command)

#Now lets do same training for while:
#ONE
#quantity = 0
#while True:
#    usr_command = input("Enter a number : ")
#    if usr_command == 'quit':
#        print('Here is your total sum : ', quantity)
#        break
#    else:
#        try:
#            number = float(usr_command)
#            quantity += number
#        except ValueError:
#            print('error ')
#TWO
#target = 45
#while True:
#    guess_number = float(input('Enter your guess number from 1 to 100 : '))
#    if guess_number > target:
#        print('Your guess number is bigger! ')
#    elif guess_number < target:
#        print('Your guess number is less! ')
#    else:
#        print('You have won ')
#THREE
#password = 'Revolver'
#while True:
#    user_data = str(input('Enter a password: '))
#    if user_data == password:
#        print('You are Welcome ! ')
#        break
#    else:
#        try:
#            print('Your password is incorrect!')
#        except ValueError: #Value of correct type
#            print('Sorry , but there is overload right now')
#FOUR:
#user_number = int(input('Enter a number for converting it into factorial : '))
#factorial_number = 1
#while True:
#    if user_number > 0:
#        factorial_number = user_number * factorial_number
#        user_number -= 1
#    else:
#        print('your factorial is equal to : ', factorial_number)
#        break
#FIVE:
#limit = int(input('Enter a maximum number please : ' ))
#simple_numbers = []
#number = 2
#while number <= limit:
#     divisor = 2
#     is_prime = True
#     while divisor < number:
#         if number % divisor == 0:
#             is_prime = False
#         divisor += 1
#     if is_prime:
#         simple_numbers.append(number)
#     number += 1
#print('each simple number until limit : ', simple_numbers)
#SIX
#i = 0
#while i < 5:
#    i += 1
#    if i == 3:
#        print('skip number three')
#        continue   #due to this method we can return to the beginning of cycle not checking items inder this item
#    print(i)
#SEVEN
#count = 0
#sum_5num = 0
#while True:
#    count += 1
#    user_number = float(input('Enter a number : '))
#    if count < 5:
#        if user_number < 0:
#            print('negative number is not included')
#            continue
#        else:
#             sum_5num += user_number
#             print('You have got ',sum_5num)
#    else:
#        break
#EIGHT
#password = '123456789'
#while True:
#    usr_text = str(input('Enter a password: '))
#    if len(usr_text) < 9:
#        print('too short')
#        continue
#    elif len(usr_text) > 9:
#        print('try again!')
#        continue
#    else:
#        print('Welcome')
#        break
#
#Now lets extend the understanding about TRY and EXCEPT:
#In 'try' we put the so-called dangerous code which can possibly contain an error
#ValueError - when the type is not suitable
#Example:
#while True:
#    try:
#        limit = int(input('Enter upper limit: ' ))
#        continue
#    except ValueError:
#        print('ENTER INTEGER NUMBER!')
#ONE
#n1 = int(input('First num: '))
#n2 = int(input('Second num: '))
#try:
#    division = n1/n2
#    print(division)
#except ZeroDivisionError:
#    print('You cannot divide it by ZERO!')
#TWO
#try:
#    user_age = int(input('Enter your age : '))   #in this part a problem can happen so we wrap it literally in TRY
#    print(f'You are {user_age} years old ')
#except ValueError:
#    print('Please , enter only a number') #here we actually check types of problems and we give subsequents instructions to the user
#THREE
#while True:
#    try:
#        user_text = float(input('Type number : '))
#        print(user_text)
#        break
#    except ValueError:
#        print('Enter a number!')
#FOUR
#my_list = [10,20,30,40,50]
#while True:
#    try:
#        user_index = int(input('Enter an index : '))
#        print(my_list[user_index])
#    except ValueError:
#        print('Write a number!')
#    except IndexError:
#        print('Such index does not exist in the list!')
#FIVE also we can make errors especially
printer_busy = True
try:
    pages = int(input('How much pages we are going to type?'))
    if pages > 100:
        raise ValueError('Error : there is no so much paper') #program starts looking for the nearest 'except'
    print('Typing....')
except ValueError as e: #store it in the variable
    print(e) #now we derive text using normal font without red annoying text
finally:
    printer_busy = False
    print('print is not busy any more')
