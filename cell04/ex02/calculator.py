num_1 = int(input("Give me the first number: "))
num_2 = int(input("Give me the second number: "))
print('Thank You')
print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
div = num_1 / num_2
if div == int(div):
     print(f"{num1} / {num2} = {int(num1 / num2)}")
else:
     print(f"{num_1} / {num_2} = {div}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")