# contact management system
import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def display_contact(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_contact()
    while True:
        number = input("Enter the number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number")

    people.pop(number - 1)
    print("Person Deleted!")


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    display_contact(results)   


print("Hi, welcome to the Contact Management System.")
print()

with open("mini project/contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size: ", len(people))
    command = input("you can 'Add', 'Delete', 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

with open("mini project/contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
