import random
#var1 = random.random() #generates random number from 0 to 1 - float
#var2 = random.uniform(1,5) #generates random number within this range - float
#print(var2)
#var3 = random.randint(-3,7) #generate integers
#print(var3)
#var4 = random.randrange(-3,10,2) #INCLUDES STEP - uneven numbers
#print(var4)
#var5 = random.gauss(0,3.5)
#print(var5)
#lst1 = [4,5,0,-1,10,76,3]
#received_number = random.choice(lst1) #it will take only ONE element from lst1 RANDOMLY
#print(received_number)
#random.shuffle(lst1) #stirs the list
#print(lst1)
#random_list = random.sample(lst1,3) #takes three elements randomly
#print(random_list)
##pretty useful example:
##random.seed(123) #it adds the prediction(and stores it) until it is left out - it fixex the state - so it is important to turn it off before making random sequences
#any_numbers = [random.randint(0,10) for _ in range(5)]
#print(any_numbers)
#case_items = ['Rubbish','Poison','Coin','Legendary Sword','Stone']
#statistics_weights = [40,10,5,5,40]
#result_prize = random.choices(case_items,weights=statistics_weights,k=1)
##                             items       chance of item           amount of given items
#print(result_prize[0])

#Tasks:
#ONE
players = [1,2,3,4,5,6] #- six players
random.shuffle(players)
team_A = players[0:3]
team_B = players[3:6]
print(f'Players {team_A} against Players {team_B}')
#Two
rarities = ['Common','Rare','Epic','Legendary']
chance = [70,20,8,2]
given_item = random.choices(rarities,weights=chance,k=1)
print(given_item[0])

