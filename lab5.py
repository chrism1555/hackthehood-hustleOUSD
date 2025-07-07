
# 1. Cat greeting function

def cat_greeting(word):
   print(f'Cat says {word}')
   print('Cat says nothing')

cat_greeting("meow")

# 2. Superhero Power Function (Fixed Output)

def generate_superhero_power():
   name = "christian"
   power =  "shadow"
   print(f"{name}'s power is {power}")

generate_superhero_power()

# 3. Superhero Power Function with Return

def generate_superhero_power1():
   power = ("shadow")
   return power

print(generate_superhero_power1())

# 4. Superhero Power Function with Arguments

def generate_superhero_power2(user_name, super_power):
   message = user_name + " has the power of " + super_power + "!"
   return message

print(generate_superhero_power2("christian", "time stop"))

# 5. Looping through Greetings

def cat_greeting_loop(greeting):
   for i in range(5):
      print(f'The cat says {greeting}')

cat_greeting_loop("meow")

# 6. Superhero Power Function with Multiple Powers

def general_multiple_powers(powers):

   for i in powers:
      print(i)

powers_list = ["invisibility", "teleport", "time stop", "reverse"]

general_multiple_powers(powers_list)