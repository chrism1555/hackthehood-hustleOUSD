cookbook = []

def create(recipe):
    cookbook.append(recipe)

    print("A new recipe has been added to the list!")

def read(index):
    if index in range(len(cookbook)):
        return cookbook[index]
    else:
        print("Non-existent")

def update(index, recipe):
    if index in range(len(cookbook)):
        cookbook[index] = recipe
        print(f"Updated value: {cookbook[index]}")
    else:
        print("What would you like to update it with?")

def destroy(index):
    x = f"This recipe was removed: {cookbook[index]}"
    if index in range(len(cookbook)):
        print(x)
        cookbook.pop(index)
    else:
        print("Try a different index")

def list_all_recipes():
    for i in cookbook:
        print(i)



def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

main()