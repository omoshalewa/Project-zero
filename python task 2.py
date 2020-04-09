import random
import string

def get_user_details():
    print("Kindly provide the following details")
    first_name = input("First Name: ").title()
    last_name = input("Last Name: ").title()
    email_address = input("Email Address: ")
    user_details = [first_name, last_name, email_address]
    return user_details

def get_user_passward(user_details):
    length = 5
    system_gen_password = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    user_password = (user_details[0][0:2] + user_details[1][-2:] + system_gen_password)
    print("Your password is " + user_password)
    return user_password

decision = True
data = []

while decision:
    user_details = get_user_details()
    user_password = get_user_passward(user_details)
    password_satisfied = input("Are you satisfied with the password generated? Yes or No: ").lower()

    password_gen_loop = True
    while password_gen_loop:

        if password_satisfied == 'yes':
            user_details.append(user_password)
            data.append(user_details)
            password_gen_loop = False

        else:
            print("Enter a password longer than or equal to 7 in the space provided below")
            chosen_password = input(str("Choose password : "))
            password_length = True
            while password_length:
                if len(chosen_password) >= 7:
                    print("Your new password is " + chosen_password)
                    user_details.append(chosen_password)
                    data.append(user_details)
                    password_length = False
                    password_gen_loop = False

                else:
                    print("""Your password is less than 7!
Enter a password longer than or equal to 7 in the space provided below """)
                    chosen_password = input(str("Choose password : "))

    another_user = input("Would you like to add another user? Yes or No: ").lower()
    if another_user == 'no':
        decision = False
        print("View Details")
        records = ['First Name:', 'Last Name:', 'Email:', 'Password:']
        for i in range(0, len(data)):
            print('User {0}'.format(i + 1) + ' Details')
            for x in range(0, len(data[i])):
                print(records[x] + ' ' + data[i][x])

    else:
        decision = True