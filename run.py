#!/usr/bin/env python3.6
from user import User
from credentials import  Credential

def create_user_account(user_name,passcode):
    new_user = User(user_name,passcode)
    return new_user

def save_user(user):
    user.save_user()






def main():
    print('Hello Welcome to the PASSWORD LOCKER APP')
    print('Use the short codes:\n')
    print('#'*80)
    print()
    print('L -> to log into your existing PASSWORD LOCKER account')
    print('C -> to create a new PASSWORD LOCKER account\n')
    print('#'*80)






if __name__ == '__main__':

    main()
