

menu = {'Pizza': 2.99, 
        'Burger': 3.99, 
        'Hotdog': 1.99, 
        'Cheese': 0.59, 
        'Ice cream': 1.49,
        'Churro': 0.79, 
        'Soda': 0.89}
# Menu holds the value of each item on the dictionary


def total_price(item1, item2):

   total = menu[item1] + menu[item2]

   return total

print(total_price("Burger","Hotdog"))
# Prints the sum of both items


def price_difference(item1, item2):

   difference = menu[item1] - menu[item2]

   return abs(difference)

print(price_difference("Pizza","Soda"))
# Prints the value difference of both items


def inflation(item, increase):

   menu[item] = menu[item] * increase

   return menu

def deflation(item, divide):
   
   menu[item] = menu[item] / divide  

   return menu

print(deflation("Pizza", 2))
print(inflation("Burger", 2))



menu = {'Pizza': 2.99, 
        'Burger': 3.99, 
        'Hotdog': 1.99, 
        'Cheese': 0.59, 
        'Ice cream': 1.49,
        'Churro': 0.79, 
        'Soda': 0.89}
menu["Popcorn"] = "4.99" # type: ignore

print(menu)