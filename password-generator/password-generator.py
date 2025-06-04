import random
import string
def password_generator(length,letter=True,digits=True,symbols=True):
    characters=""
    if letter:
        characters +=string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    if not characters:
        return("you must enter atleast 1 character")
    
    password="".join(random.choice(characters) for _ in range(length))
    return password
def get_user_preferences():
    print(" Welcome to the Password Generator ")
    try:
        length=int(input("enter the length of your password"))
    except ValueError:
        print("Invalid input. Using default length: 12")
        length = 12
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    password = password_generator(length, use_letters, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")
get_user_preferences()