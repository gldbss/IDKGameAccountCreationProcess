import random

# Generate Username & Password and Save Them

def Generator_And_Saver():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    symbol = '!@#$%^&()_+-=;,.'
    numbers = '1234567890'

    pass_lenth = 12
    user_lenth = 6

    Use_Pass = lower + upper + numbers + symbol
    Uas_User = lower + numbers

    password = "".join(random.sample(Use_Pass, pass_lenth))
    Username = "".join(random.sample(Uas_User, user_lenth))

    print('Your Username is: '+ Username + '@bin.com' + '\n' + 'Your Password is: ' + password)

    User_name = Username + '@bin.com'

    UsrFil = open('asserets/'+Username, 'w+')

    UsrFil.write(User_name + '\n' + password)

    UsrFil.close()

# Login

def Login():
    print('Enter Your Username:')
    LogUser = input()

    print('Enter Your Password:')
    Logpass = input()

    FileUser= LogUser.removesuffix('@bin.com')

    try:
        verifier = open('asserets/' + FileUser, 'r')
        if Logpass in verifier:
            Access = 1
        else:
            Access = 0
        verifier.close()
        if Access == 1:
            print('Access Granted')
        if Access == 0:
            print('Access Denied')
    except SyntaxError as msg:
        print(msg)

# Define main Function

def main():
    print("Don't you have account, Say CREATE.\nElse, LOGIN")
    condition = input().lower()
    if condition == 'login':
        Login()
    if condition == 'create':
        Generator_And_Saver()

# Call main Function

main()
