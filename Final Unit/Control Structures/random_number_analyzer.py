
import random

min_value = None
max_value = None
random_amount = None
random_valuelist = []


print('This program generates X amount of values between the supplied min and max.')
print('It will also calculate the average of all generated values. \n')

#Asks user for the minimum value, and ensures the input for the minimum values are satisfactory
while True:
    min_value = input('What is your minimum value?: ')

    #verify the value isn't empty and is a number
    if len(min_value) == 0:
        print('Invalid Input; Empty string supplied, intergers required.')
        continue

    if min_value.isnumeric() == False:
        print('Invalid Input; Non numeric characters provided, intergers only required')
        continue

    min_value_converted = int(min_value)
    break

#Asks user for the maximum value, and ensures the input for the maximum values are satisfactory
while True:
    max_value = input('What is your maximum value?: ')

    #verify the value isn't empty and is a number
    if len(max_value) == 0:
        print('Invalid Input; Empty string supplied, intergers required.')
        continue

    if max_value.isnumeric() == False:
        print('Invalid Input; Non numeric characters provided, intergers only required')
        continue

    max_value_converted = int(max_value)
    if max_value_converted < min_value_converted: #verfiy the maximum value is greater than the min value
        print('Invalid Input; Maximum value cannot be less than Minimum value')
        continue
    break

#Asks user for the amount of number they would like to generate, and ensures the input is satisfactory 
while True:
    random_amount = input('How many random numbers would you like to generate?: ')

    #verify the value isn't empty and is a number
    if len(random_amount) == 0:
        print('Invalid Input; Empty string supplied, intergers required.')
        continue

    if random_amount.isnumeric() == False:
        print('Invalid Input; Non numeric characters provided, intergers only required')
        continue

    random_amount_converted = int(random_amount)
    break

#this for loop will generate a specified amount of random values between the min and the max
for i in range(random_amount_converted):
    #this generates a random value between the min and the max
    new_random_value = random.randint(min_value_converted, max_value_converted)

    #add the newly generated random number to list
    random_valuelist.append(new_random_value)

#list the random listed values
print('Program generated the following random numbers: ')
for i in random_valuelist:
    print(i)

#calculate the average of these generated numbers
random_number_sum = 0 
for i in random_valuelist:
    random_number_sum += i

random_number_average = random_number_sum / len(random_valuelist)
print('The average of the generated numbers is: ', random_number_sum)