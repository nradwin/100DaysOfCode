bill = float(input("What is the total bill?\n$"))

tip_percent = float(input("What tip percent would you like to give?\n"))

if tip_percent > 1:
  tip_percent /= 100
  
people = int(input("How many people to split the bill?\n"))

bill_plus_tip = bill + (tip_percent * bill)

divided_pay = round(bill_plus_tip / people, 2)

print(f"Each person should pay: ${divided_pay}")