numbers=[1,1,2,3,5,8,13,21,34,55]

squared_numbers=[number**2 for number in numbers]

print(squared_numbers)

result= [number for number in numbers if number % 2 == 0]

print(result)