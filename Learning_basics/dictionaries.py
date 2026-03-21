#for keys we can take : strings,numbers,tuples - cannot be changed we use keys with []
#values can be everything
#empty_dict = {}
#person = {"name": "John","age": 30,"city": "New York"}
#print(person)
#subdicts /  dict in dict
#nested = {
#    'person': {'name':'Mary','age': 25},
#    'contacts': {'email': 'mary@example.com','phone': '+1234567890'}}
#print(nested['person'])
phone_book = {
    "Alice": "555-1234",
    # KEY      VALUE
    "Bob": "555-5678",
    "Charlie": "555-8765"
}
#bobs_number = phone_book['Alice']
#print(f'bobs number: ', {bobs_number})
#if we want to avoid a mistake we use GET instead
#FOR EXAMPLE:
#davids_number = phone_book.get('David')
#print(davids_number) #we get None instead of an error
#also we can literally GET  default value due to GET
#davids_number_default = phone_book.get('David','Number is absent')
#print(davids_number_default)
#we can insert new value with keys into the dict
#phone_book['David'] = '555-111'
#print(phone_book)
#Or we can change the existing value of the specific key
#phone_book['Alice'] = '555-0000'
#print(phone_book)
#also we can delete key and value using method del
#del phone_book['Charlie'] #delete Charlie
#print(phone_book)
#iteration
#1)iteration of keys
#menu = {
#    "pizza": 900,
#    "burger": 300,
#    "coffee": 150
#}
#for dish in menu:
#    print(dish)
#2)iteration of values
#for price in menu.values():
#    print(price)
#3)iteration with both/ keys and values
#for dish,price in menu.items():
#    print(f'Dish : {dish} , Price : {price} rubles')
#TASKS
#ONE
#inventory = {'Sword': 1 , 'Shield': 1 ,'Poison': 10,'Gold': 500}
#for item in inventory:
#    print(item)
#TWO
#cities = {'Moscow': 13 , "Tokio": 37 , "Paris": 2 , "New York": 8}
#for city,population in cities.items():
#    print(f"In city {city} there are {population} millions of people!")
#THREE + list comprehension
stock = {'Apples': 10,'Bananas': 3,'Oranges': 12,'Mango': 2,'Milk': 1}
checking = [f'You should supply: {food} '  for food,amount in stock.items() if amount < 5]
print(checking)
