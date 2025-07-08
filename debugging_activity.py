# Debugging Activity

# Snippet 1
x = 10
y = 0
result = x + y # Can't divide by zero
print("Result:", result) 

# Snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i]) # + 1 makes the number out of range

# Snippet 3
def calculate_area(radius):
    area = 3.14 * radius * 2 # Extra asterisk
    return area

radius = 5
print(calculate_area(radius))

# Snippet 4
def is_even(number):
    if number % 2 == 0:
        return True         # Missing colons next to 0 and else
    else:
        return False
    
print(is_even(4))
print(is_even(7))
    
# Snippet 5
for i in range(5):  # Missing colon
    print(i)

# Snippet 6
def greet(name):
    return "Hello, " + name  # Missing operator

print(greet("Alice"))

# Snippet 7 
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number  # Missing Indent

print("Sum of number:", sum)

# Snippet 8
def factorial(n):
    if n == 0:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(5))