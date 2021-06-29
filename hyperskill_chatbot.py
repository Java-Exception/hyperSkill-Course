# Chatty bot code revised by yours truly
# Follows Hyperskill template
# June 29, 2021


def greet(name, b_year):
    print(f'Hello my name is {name}, \nI was born in the year {b_year}')


prompt_ = "> "


def get_username():
    print('Please remind me of your name')
    username = input(prompt_)
    print(f'Nice to meet you {username}')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rems = []
    for i_ in range(3):
        rems.append(int(input(prompt_)))
    age = (rems[0] * 70 + rems[1] * 21 + rems[2] * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input(prompt_))
    for i in range(num + 1):
        print(i, '!')


# Too lazy for while loop
def get_answer():
    ans = int(input(prompt_))
    if ans == 2:
        print('Completed, have a nice day!')
    else:
        print("Please try again")
        get_answer()


# Also too lazy for lists
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods? ")  # Question being asked followed by hard coded answers
    print("1. Why not")
    print("2. To decompose a program into several small subroutines")
    print("3. This is meaningless")
    print("4. I want true intelligence")
    get_answer()


def end():
    print('Congratulations, have a nice day!')


greet('GladOS', '1953')  # change it as you need
get_username()
guess_age()
count()
test()
end()
