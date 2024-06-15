from calc_ascii import logo

# calculator

# add
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
def calculator():
  print(logo)
  num1 = float(input('Enter first number: '))
  
  for operation in operations:
    print(operation)
  should_continue = True

  while should_continue:
    operation_symbol = input('Select Operation: ')
    num2 = float(input('Enter next number: '))
    calc_func = operations[operation_symbol]
    answer = calc_func(num1, num2)
    print(f'{num1} {operation_symbol} {num2} = {answer}')
  
    while True:
      another_calc = input('Type "y" to continue with {answer}, or "n" to start a new calculation\n').lower()
      if another_calc == 'n':
        should_continue = False
        calculator()
        print('Have fun with your calculation. Goodbye.')
      elif another_calc == 'y':
        num1 = answer
      else:
        print('Type "y" or "n"')
