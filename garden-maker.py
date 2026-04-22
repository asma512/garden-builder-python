# garden_maker.py

garden = []

print("Welcome to the Garden Maker!")

while True:
    print("1. Add flower")
    print("2. View garden")
    print("3. Remove flower")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        flower = input("Enter flower name: ")
        garden.append(flower)
    
    elif choice == "2":
        if len(garden) == 0:
            print("Your garden is empty")
        else:
            print("Your garden:")
            for f in garden:
                print("-", f)

    elif choice == "3":
        flower = input("Enter flower name to remove: ")
        if flower in garden:
            garden.remove(flower)