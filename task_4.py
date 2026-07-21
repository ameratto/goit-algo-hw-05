def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Give me correct name"
        except KeyError:
            return "Give me correct name"

    return inner


@error_handler
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@error_handler
def change_contact(args, contacts):
    name, new_phone = args
    if contacts[name]:
        contacts[name] = new_phone
        return "Contact changed."
    else:
        return "Contact not found."

@error_handler
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    return [f"{name}: {phone}" for name, phone in contacts.items()]


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Please enter a command: ").strip().lower()
        if not user_input:
            print("Invalid command. Try again.")
            continue
        command, *args = parse_input(user_input)
        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case "exit" | "close":
                print("Goodbye!")
                break
            case _:
                print("Invalid command. Try again.")


if __name__ == '__main__':
    main()
