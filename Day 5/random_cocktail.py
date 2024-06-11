import random

print("""
                                                   .''''.
                                                  /,.--. )
                             .'``.        __   __((\- -(\)
                    _______.'     \_.-''''  ``'  /)) - .\|
   __....::::::::::'''''''/    .   \'''''''::::::(/ `-'`.)
.:'::.  .  o ~ .  ~  o ~ /    /     '.o ~ . _.....--- `  \
 ':. ':::::.___.____,___/   ,'_\      \ _.-'___..___..._,'
   ':.  o~  `::::::::::::::::::::::::::::::::::::::::'  (\
    `':.  o ~  o   ..   o  ,  ~  \ . o~   -.  ~   .'.:'\'(
       ':.  ,..   o  ~   o  . ,  'o.    ~ o   ~ o'.:'  \(/
         '.   o   ~   .    ~    o ~ ',o :  :  .' .' ('\/ |
           '-._    ~    o  , o  ,  .  ~._ _.o_.-'  \/ ) (
               '- .._  .    ~    ~      _.. -'
                     ''' - .,.,. - '''
                          (:' .:)
                           :| '|
                           |. ||
                           || :|
                           :| |'
                           || :|
                           '| ||
                           |: ':
                           || :|
                     __..--:| |'--..__
               _...-'  _.' |' :| '.__ '-..._
             / -  ..---    '''''   ---...  _ \
       LGB   \  _____  ..--   --..     ____  /
              '-----....._________.....-----'

""")

print('\nWelcome to Sip Surprise: a Cocktail Experience...')
print('\nChoose your build:\n0 SOUR\n1 MULE\n2 COLLINS\n3 NEGRONI\n4 LAST WORD')

spirit = [ "Vodka",
         "Gin",
         "Rum",
         "Tequila",
         "Bourbon",
         "Scotch",
         "Cognac",
         "Mezcal",
         "Absinthe",
         "Pisco",
         "Aquavit",
         "Apple spirit",
         "Cachaça",
         "Grappa",
         "Ouzo",
         "Raki"]

syrup = ["Simple Syrup",
        "Grenadine",
        "Orgeat Syrup",
        "Honey Syrup",
        "Maple Syrup",
        "Agave Syrup",
        "Vanilla Syrup",
        "Ginger Syrup",
        "Cinnamon Syrup",
        "Pineapple Syrup",
        "Raspberry Syrup",
        "Mint Syrup",
        "Lavender Syrup",
        "Rose Syrup",
        "Peppermint Syrup"]

liqueur = ["Triple Sec",
          "Amaretto",
          "Cointreau",
          "Grand Marnier",
          "Kahlua",
          "Chambord",
          "Campari",
          "Aperol",
          "St. Germain",
          "Midori",
          "Galliano",
          "Frangelico",
          "Drambuie",
          "Chartreuse",
          "Benedictine",
          "Sambuca",
          "Limoncello",
          "Blue Curacao",
          "Pimm's No. 1"]

citrus = ["Lemon",
         "Lime",
         "Orange",
         "Grapefruit",
         "Tangerine",
         "Mandarin",
         "Bergamot",
         "Blood Orange",
         "Yuzu",]

sweet_carb = ["Cola",
             "Ginger Ale",
             "Lemon-Lime Soda",
             "Tonic Water",
             "Root Beer",
             "Cream Soda",
             "Ginger Beer"]

unsweet_carb = ["Club Soda",
               "Mineral Water"]

amaro = [
    "Averna",
    "Fernet-Branca",
    "Amaro Nonino",
    "Amaro Montenegro",
    "Campari",
    "Aperol",
    "Cynar",
    "Ramazzotti",
    "Lucano",
    "Amaro Meletti",
    "Amaro Sibilla",
    "Amaro dell'Etna",
    "Amaro Braulio",
    "Amaro Tosolini",
    "Amaro Santa Maria al Monte",
    "Cardamaro",
    "Zucca Rabarbaro",
    "Amaro Nardini",
    "Amaro Sfumato Rabarbaro",
    "Amaro CioCiaro"]

while True:
  cocktail = ''
  choice = int(input("\nSelection: "))

  if choice == 0:
    cocktail += random.choice(spirit) + ', ' + random.choice(citrus) + ', ' + random.choice(syrup)
    print('\nMixing...\n\nYour cocktail: \n' + cocktail + '\n\nTip: Sour Builds typically call for 2 parts spirit, 1 part citrus, and 1 part syrup.')

  elif choice == 1:
    cocktail += random.choice(spirit) + ', ' + random.choice(citrus) + ', ' + random.choice(sweet_carb)
    print('\nMixing...\n\nHere you are: \n' + cocktail + '\n\nTip: Mule Builds typically call for 2 parts spirit, 1 part citrus, topped with a sweetened carbonated beverage.')

  elif choice == 2:
    cocktail += random.choice(spirit) + ', ' + random.choice(citrus) + ', ' + random.choice(unsweet_carb)
    print('\nMixing...\n\nEnjoy: \n' + cocktail + '\n\nTip: Collins Builds typically call for 2 parts spirit, 1 part citrus, topped with an unsweetened carbonated beverage.')

  elif choice == 3:
    cocktail += random.choice(spirit) + ', ' + random.choice(amaro) + ', ' + random.choice(liqueur)
    print('\nMixing...\n\nHere ya go: \n' + cocktail + '\n\nTip: Negroni Builds typically call for 1 part spirit, 1 part amaro, and 1 part liqueur.')

  elif choice == 4:
    cocktail += random.choice(spirit) + ', ' + random.choice(liqueur) + ', ' + random.choice(liqueur) + ', ' + random.choice(citrus)
    print('\nMixing...\n\nFrom computer to human <3, enjoy: \n' + cocktail + '\n\nTip: Last Word Builds typically call for 1 part spirit, 1 part liqueur, 1 part another liqueur, and 1 part citrus.')

  else:
    print('error')

  another = input("\nWould you like to make another selection? (y/n): ").strip().lower()
  if another != 'y':
    break

print("\nThank you for using Sip Surprise! Enjoy your cocktails!")


