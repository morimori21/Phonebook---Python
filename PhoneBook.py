phone_book = {}

def show_message(message):
    print("\n" + "-" * 30)
    print(message)
    print("-" * 30)

def curr_entries():
    if not phone_book:
            print("="*35)
            print(f"{'Empty':<20}")
            print("="*35)
    else:
        print("\n\n\n")
        print(f"[No.]     [Name]     [PhoneNumber]")
        print("-" * 35)

        index = 1

        for names, nums in phone_book.items():
            for num in nums:
                print(f"{index:<10} {names:<10} {num}")
                index +=1

def inputs():
    name = input("Name: ")
    number = int(input("Number: "))
    return name,number

def add_people():
    name, number = inputs()
    if name not in phone_book:
            phone_book[name] = []
    phone_book[name].append(number)
    show_message(f"{name} with number {number} has been added.")

def delete_people():
      if not phone_book:
            show_message("The phone book is empty. Nothing to delete.")
            return
      else:
            curr_entries()
            name_to_delete = input("Enter the name you want to delete: ")
            if name_to_delete in phone_book:
                  del phone_book[name_to_delete]
                  show_message(f"Entry for {name_to_delete} has been deleted.")
            else:
                  show_message(f"No entry found for {name_to_delete}.")

def edit_number():
    name_to_edit = input("Enter the name you want to edit: ")

    # Check if the name exists
    if name_to_edit in phone_book:
        new_number = input("Enter the new number: ")
        phone_book[name_to_edit] = [new_number] 
        show_message(f"Entry for {name_to_edit} has been updated with new number {new_number}.")
    else:
        show_message(f"No entry found for {name_to_edit}.")

def search():
    name_search = input("Enter the name to search: ")
    if name_search in phone_book:
        numbers = "\n".join(f"- {number}" for number in phone_book[name_search])
        show_message(f"Numbers for {name_search}:\n{numbers}")
    else:
        show_message("No number found for the entered name.")

#MAIN MENU
if __name__ == "__main__":
    while True:
        curr_entries()
        
        print("\n" + "-" * 30)
        print("1. Add People\n"
              "2. Delete People\n"
              "3. Edit Number\n"
              "4. Search\n"
              "5. Exit\n")
        print("-" * 30)
        print()
        print("=" * 30)
        cmd = int ( input  ("command : "))
 
        if cmd == 1:
            add_people()
        elif cmd == 2:
             delete_people()
        elif cmd == 3:
             edit_number()
        elif cmd == 4:
             search()
        elif cmd == 5:
             show_message("...*program closed*...")
        else:
             show_message(f"\'{cmd}\' is not recognized as an internal command")
        
          
              






'''
Add 1
Del 1
Edit 1
Check 1
Check all 0
Exit 1


while True:
    x = int ( input : ("command : "))
    

    if x == 1:
        #add
    elif x == 2:
        #edit number or name
    elif x == 3:
        #del
    elif x == 4:
        #search
    elif x == 5:
        #check all
    elif x == 6:
        #exit
    else: 
        print("invalid")
'''