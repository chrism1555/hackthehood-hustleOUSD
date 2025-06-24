# Lab 3

# 1. Working with Strings

food = 'Gyoza'
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# 2. Working with Lists
number_list = [17, 2, 32, 43, 89]
number_list.append(21)
print(number_list)
number_list.insert(3, 2000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[:3])
print(number_list[-3:])

# 3. Working with Dictionarys
books = {'Suzanne Collins': 'The Hunger Games', 'George Orwell': '1984', 'Rick Riordan': 'Percy Jackson', 'Jeff Kinney': 'Diary of a Wimpy Kid'}
print(books.keys())
print(books.values())
print(books.get('Suzanne Collins'))
print(books.pop(list(books.keys())[2]))
print(books)
del books[list(books.keys())[0]]
print(books)




