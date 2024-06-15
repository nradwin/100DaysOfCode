from calc_ascii import logo
print(logo)

# calculator

# addition
def add(n1, n2):
  return n1 + n2

# subtract
def subtract(n1, n2):
  return n1 - n2

# multiply
def multiply(n1, n2):
  return n1 * n2

# divide
def divide(n1, n2):
  return n1 / n2
  
operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

num1 = int(input('Enter first number: '))

for operation in operations:
  print(operation)

operation_symbol = input('Select Operation: ')

num2 = int(input('Enter second number: '))

calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)
print(f'{num1} {operation_symbol} {num2} = {answer}')

