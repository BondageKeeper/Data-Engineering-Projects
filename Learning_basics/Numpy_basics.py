import numpy as np
#by the way in massives as we can see there are no dots or commas between numbers
#np.array - converts python list into massive
massive1 = np.array([1,2,3,4])
massive2 = np.array([[1,2,3],
                     [4,5,6]])
#np.arange(start,stop,step) - generates a specific range of numbers including step between two numbers(does not include last number of range!)
sequence1 = np.arange(1,11,2)
print(sequence1)
sequence2 = np.arange(-2*np.pi,2*np.pi,1)
print(sequence2)
#np.linspace(start,stop,numbers of cuts of the range) - similar to 'arange' but it cuts established range into many pieces
points1 = np.linspace(0,100,5,dtype = int)
print(points1)
points2 = np.linspace(-2*np.pi,2*np.pi,6)
print(points2)
#arr.reshape(rows,columns) - it turns vector(1D massive) into table massive(2D massive)
flat_vector = np.arange(6)
print(flat_vector)
matrix1_2D = flat_vector.reshape(2,3)
print(matrix1_2D)
flat_massive2 = np.arange(1,13,1)
matrix2_2D = flat_massive2.reshape(3,4)
print(matrix2_2D)
#####################
massive3 = np.arange(1,11,1)
print(massive3[::-1])
#####################
#np.ones(rows,columns) and it will be consisted of ones only
#for zeros: np.zeros
massive4 = np.ones((2,5))
print(massive4)
##########################################
#Now lets dive into math of massives
#if we apply any mathematical operation(*+..) nearby massive - it will be applied for each element of this massive
massive5 = np.array([1,2,3])
print(massive5 * 10) #it is applied for each element though looks like nonsense
print(massive5 + massive5) #we can just sum two massives too
#there are np.sum . np.min , np.max , np.mean(average value)
menu_prices = np.array([100,200,300])
print(np.mean(menu_prices))
print(np.min(menu_prices))
#also we can calculate sum of rows ot the sum of columns
matrix6 = np.array([[1, 2], [3, 4]])
#axis = 0 - operation goes along columns
#axis = 1 - operation goes along rows
print(np.sum(matrix6,axis=0))
print(np.sum(matrix6,axis=1)) #easy 
#and of course there are mathematical things like np.log() , np.exp() , np.sqrt()
nums = np.array([4,9,16,25,36,49])
print(np.sqrt(nums))
print(np.log10(10000))
#Tasks
#One
salary = np.array([50, 60, 70, 80, 90])
print(salary * 1.15)
#Two
salary_info = np.array([[3000,4000,6000],
                        [4980,5878,4533]])
results = np.mean(salary_info,axis=1)
print(f'Department one : ' ,results[0])
print(f'Department two : ' ,results[1])
#three
total_sum = np.sum(salary_info)
print(total_sum)
#four
sales_jan = np.array([10, 20, 30])
sales_feb = np.array([15, 18, 40])
difference = sales_feb - sales_jan
print(difference)
#five
random_numbers = np.random.randint(0,100,10)
min_value = np.min(random_numbers)
max_value = np.max(random_numbers)
scope = max_value - min_value
print(f"Scope : {scope}")
##############################################
#Now lets learn about the manipulation of data
#we can unite massives using np.concatenate()  -- they must be contained in tuple!
var1 = np.array([1,2,3])
var2 = np.array([4,5,6])
glue = np.concatenate((var1,var2)) #will be glued in one big massive
#or there is trick with 2D massive: (by default axis = 0)
m1 = np.array([[1, 1], [1, 1]])
m2 = np.array([[2, 2], [2, 2]])
res_2D = np.concatenate((m1,m2),axis=1) #to the sides(to the columns)
print(res_2D)
#or we can concatenate massives without thinking of axis. we can use :
#v = np.vstack((x, y)) # vertical stack or h = np.hstack((x, y)) # horizontal stack
vertical_stack = np.vstack((var1,var2))
print(vertical_stack)
horizontal_stack = np.hstack((var1,var2))
print(horizontal_stack)
#np.unique(arr, return_counts=True) - returns two massives : unique elements itself and how many times every of them appeared
logs = np.array([1, 2, 2, 3, 1, 1, 4])
values , counts = np.unique(logs , return_counts=True)
print(values) #initial value that we had(have)
print(counts) #how many times each initial value appeared
#also it is quite useful to use np.random.seed in order to fix random numbers(and these numbers will be the same during every launch)
#np.random.seed(5) #here we fix our subsequent random numbers(so they will the same)
print(np.random.randint(1,100,3)) #same numbers after every launch though pretty useful
#TASKS fo training these methods:
#ONE:
staff1 = np.array(['Bob','Tracy','Alex'])
staff2 = np.array(['Kate','John','Fred'])
print(np.concatenate((staff1,staff2)))
#TWO:
names = np.array(['Ivan', 'Petr'])
ids = np.array([101, 102])
res = np.vstack((ids,names))
print(res)
#THREE
random_massive = np.random.randint(1,4,15)
print(random_massive)
initial_values , initial_counts = np.unique(random_massive,return_counts=True)
print(initial_values , initial_counts[0])
#FOUR
mat1 = np.array([[ 1 , 2 ],
                 [ 3 , 4]])
mat2 = np.array([[ 5 , 6 ],
                 [ 7 , 8]])
result2 = np.hstack((mat1,mat2))
print(result2)
#FIVE
np.random.seed(42) #again we will get random BUT fixed values due to this method
#'rand' generates random float numbers from 0 to 1(not including 1)
random_numbers2 = np.random.rand(2)
print(random_numbers2)
####################################################################################################
#Now lets learn five more new methods:
#np.sort puts numbers in order:
arr = np.array([40, 10, 30, 20])
sorted_arr = np.sort(arr) #just logically sorts array
print(sorted_arr)
#np.argsort(arr) - again ti sorts array but in return it gives indices of sorted elements:
prices = np.array([500, 100, 300])
indices = np.argsort(prices)
print(indices)
names = np.array(['Apple', 'Milk', 'Bread'])
print(names[indices]) # ['Milk' 'Bread' 'Apple']
#np.clip - if numbers go beyond established ranges - in that case they will be converted into boundaries of these ranges
data = np.array([5,15,25,35])
clipped = np.clip(data,10,30)
print(clipped) #5 turned into 10(min_boundary) and 35 turned into 30(max_boundary)
#np.tile - it copies massive completely SEVERAL times
pattern = np.array([3,4,5,6,7,8,])
several_copies = np.tile(pattern,3)#will be copied 3 times
print(several_copies)
#TASKS:
#ONE:
given_numbers = np.random.randint(0,100,10)
sorted_numbers = np.sort(given_numbers)
print(sorted_numbers[-3:])
#TWO
items = np.array(['TV', 'Phone', 'Radio'])
weights = np.array([15, 0.5, 2])
light = np.argsort(weights)
print(light)
print(f'Order of weight : {items[light]}')
#THREE
temp = np.array([18, 25, 40, 12, 33])
limit_temp = np.clip(temp,20,35)
print(limit_temp)
#FOUR
some_data = [[7,8,9],[4,5,6]]
new_data = np.tile(some_data,3)
print(new_data)
#FIVE
matrix_3x3 = [[1,2,3],
              [4,5,6],
              [7,8,9]]
sorted_matrix_3x3 = np.sort(matrix_3x3,axis=0)
print(sorted_matrix_3x3)
################################################################
#And final important methods with tasks:
#gaps in Numpy are np.nan(if we are going to create graphics and there are gaps in data in that case we should delete it or replace it
#skipped values or gaps in Numpy are np.nan
data = np.array([10,20,np.nan,40])
print(np.isnan(data)) #looks for a gap in data
print(np.nanmean(data)) #so it is smart module because it skips this gap automatically
print(np.mean(data)) #not quite right
#np.argmax and np.argmin they give indices the smallest or the biggest values
prices = np.array([100, 500, 200, 450])
peak_day = np.argmax(prices)
print(f'peak day: {peak_day+1} , and price: {prices[peak_day]}')
#and there is 'flatten' which turns matrix into simple massive
matrix5 = np.array([[1, 2], [3, 4]])
flat = matrix5.flatten()
print(flat)
#TASKS
#ONE
gaps_massive = np.array([1.2,np.nan, 4.5, 6.7,np.nan])
mask = np.isnan(gaps_massive)
gaps_massive[mask] = 0 #True is like a permission to make a change
print(gaps_massive)
#TWO
profit = np.array([15, 22, 10, 45, 30, 45, 12, np.nan])
good_day = np.argmax(profit)
print(good_day+1)
#THREE
sum_profit = np.nansum(profit)
print(sum_profit)
#FOUR
massive2x3 = np.array([[43,45,56],
                       [35,76,70]])
flat_massive2x3 = len(massive2x3.flatten())
print(flat_massive2x3)
