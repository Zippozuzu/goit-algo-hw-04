def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found"
    
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        print(f"The phone number of {name} is {contacts[name]}")
    else:
        return "Name not found"
    
def man():
    content = '''
    Доступні команди:
    - "hello" -> 
        Введення: "hello"
        Вивід: "How can I help you?"
    - "add [ім'я] [номер телефону]" -> 
        Приклад введення: "add John 1234567890"
        Вивід: "Contact added."
    - "change [ім'я] [новий номер телефону]" -> 
        Приклад введення: "change John 0987654321"
        Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
    - "phone [ім'я]" -> 
        Приклад введення: "phone John"
        Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
    - "all" -> 
        Введення: "all"
        Вивід: усі збережені контакти з номерами телефонів
    - "export" ->
        Введення: "export"
        Вивід: Буде створений "contacts.txt" з іменами і номерами телефонів
    - "close" або "exit"
        Введення: ""close" або "exit"
        Вивід: У консоль повідомлення "Good bye!". Бот завершує свою роботу
    '''
    print(content)
    
def show_all(contacts):
    if len(contacts) == 0:
        print("The contacts list is empty")
    else:
        for key, value in contacts.items():
            print(f'The number of {key} is {value}')

def export(contacts):
    if len(contacts) == 0:
        print("The contacts list is empty")
    else:
        with open("contacts.txt", 'w') as f:  
            for key, value in contacts.items():  
                f.write('%s -> %s\n' % (key, value))
        print("The contact list was created in ./contacts.txt")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "man":
            man()
        elif command == "export":
            export(contacts)
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Invalid argument. Read the manual -> 'man' command")
        elif command == "change":
            try:
                print(change_username_phone(args,contacts))
            except ValueError:
                print("Invalid argument. Read the manual -> 'man' command")
        elif command == "phone":
            try:
                show_phone(args, contacts)
            except ValueError:
                print("Invalid argument. Read the manual -> 'man' command")
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command. Read the manual -> 'man' command")

if __name__ == "__main__":
    main()
