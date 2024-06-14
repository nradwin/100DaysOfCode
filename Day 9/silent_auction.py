from replit import clear
from gavel import logo

print(logo)
print('Welcome to Silent Auction\n')

auction = []

def new_bidder(new_name, new_price):
  bidder = {}
  bidder['name'] = new_name
  bidder['price'] = new_price
  auction.append(bidder)

more_bidders = True
while more_bidders:
  while True:
    name = input('What is your name?\n')
    if name.isalpha():
      break
    else:
      print("Invalid input. Please enter a valid name with characters only.")
  while True:
    price = input('What is your bid?\n$')
    if price.isdigit():
      price = int(price)
      break
    else:
      print("Invalid input. Please enter a valid bid amount as a number.")

  new_bidder(name, price)
  
  while True:
    another_bid = input('Are there any other bidders? y/n\n').lower()
    if another_bid in ['y', 'n']:
      break
    else:
      print("Invalid input. Please enter 'y' for yes or 'n' for no.")
  
  if another_bid == 'n':
    more_bidders = False
  elif another_bid == 'y':
    clear()

highest_bidder = None
highest_price = 0

for i in auction:
  if i['price'] > highest_price:
    highest_bidder = i['name']
    highest_price = i['price']

print(f'{highest_bidder} wins the auction with a bid of ${highest_price}!')
