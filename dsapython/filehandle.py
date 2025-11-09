def read_record(filename):
    try:
        with open(filename, "r") as file:
            records = file.readlines()
            if records:
                print("Records in the file.")
                for record in records:
                    print(record.strip())
            else:
                print("No record found")
    except FileNotFoundError:
        print("The file does not exist")


def add_record(filename, record):
    with open(filename, "a") as file:
        file.write(record + "\n")
        print("Record added successfully")


def search_record(filename, search_term):
    try:
        with open(filename, "r") as file:
            print("beginning", file.tell())
            records = file.readlines()
            found = False
            count = 0
            for record in records:
                count += 1
                if search_term in record:
                    pos = record.find(search_term)
                    print(f"found in line {count} at {pos}")
                    found = True
            if not found:
                print("No matching record found")
    except FileNotFoundError:
        print("The file does not exist")


filename = "record.txt"
read_record(filename)

new_record = input("Enter a new record: ")
add_record(filename, new_record)

search_term = input("Enter a term to search file: ")
search_record(filename, search_term)
