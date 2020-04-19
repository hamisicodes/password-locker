#!/usr/bin/env python3.6
from user import User
from credentials import  Credential

def create_user_account(user_name,passcode):
    new_user = User(user_name,passcode)
    return new_user

def save_user(user):
    user.save_user()

def check_user(user_name,passcode):
    user_found = User.user_exists(user_name,passcode)
    return user_found






def main():
    print('Hello Welcome to the PASSWORD LOCKER APP')
    while True:
            
       
        print('Use the short codes:\n')
        print()
        print('L -> To log into your existing PASSWORD LOCKER account')
        print('C -> To create a new PASSWORD LOCKER account\n')
        print('#'*80)
        
        short_code = input().lower().strip()
        
        if short_code == 'l':

            username = input('Enter your username')
            password = input('Enter your password')
            
        




if __name__ == '__main__':

    main()
