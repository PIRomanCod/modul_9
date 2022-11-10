# CLI (Command Line Interface)
# 3 parts:
# Парсер команд.
# Функції обробники команд — набір функцій, які ще називають handler
# Цикл запит-відповідь. Ця частина програми відповідає за отримання від користувача даних та повернення користувачеві відповіді від функції-handlerа

# Функціонал:
# - бот-асистент повинен вміти зберігати ім'я та номер телефону,
# - знаходити номер телефону за ім'ям,
# - змінювати записаний номер телефону,
# - виводити в консоль всі записи, які зберіг


# Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error
# декоратор відповідає за повернення користувачеві повідомлень виду "Enter user name", "Give me name and phone please" і т.п.
# Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except (TypeError):
            print("The command don't need args")
        except (IndexError):
            print("The command need 2 args: name phone")
        except (KeyError):
            print("The command is unknown")
    return inner


def parser(user_input):
    parsed_input = user_input.lower().strip().split()
    handler(parsed_input)


@input_error
def handler(parsed_input):
    if parsed_input[0] in commands_dict.keys():
        commands_dict.get(parsed_input[0])((" ").join(parsed_input[1:]))
    else:
        raise KeyError


def hello():
    print("How can I help you?")


def add(string):
    new_elem = string.split()
    if new_elem[0].isdigit():
        raise IndexError
    else:
        users.update({new_elem[0]: new_elem[1]})


def change(string):
    new_elem = string.split()
    users.update({new_elem[0]: new_elem[1]})


def phone(string):
    print(users[string])


def show_all():
    print(users)


def exit():
    print("Good bye!")


the_end = False

users = {}

commands_dict = {"hello": hello,
                 "add": add,
                 "change": change,
                 "phone": phone,
                 "show all": show_all,
                 "exit": exit}

commands_list = ["hello", "add ...", "change ...",
                 "phone ...", "show all", "exit", "good bye", "close"]


def main():
    print(
        f"Welcome, please enter one of the commands: {commands_list}")
    while the_end == False:
        user_input = input("Enter please: ").lower()
        if user_input == "hello":
            commands_dict.get("hello")()
            continue
        elif user_input in ["good bye", "close", "exit"]:
            commands_dict.get("exit")()
            return the_end == True
        if user_input == "show all":
            commands_dict.get("show all")()
        else:
            parser(user_input)


if __name__ == '__main__':

    main()
