#!/usr/bin/env python3.6
from user import User
from credentials import  Credential
import random

def create_user_account(user_name,passcode):
    new_user = User(user_name,passcode)
    return new_user

def save_user(user):
    user.save_user()

def check_user(user_name,passcode):
    user_found = User.user_exists(user_name,passcode)
    return user_found




"""credentials"""

def create_credential_account(acc,pasw,usr):
    new_credential = Credential(acc,pasw,usr)
    return new_credential

def save_credential(credential):
    credential.save_credential()

def create_password():
    password = ''
    vowel = ['a','e','i','o','u']
    conso = "BCDFGHJKLMNOO"
    for x in range(6):
        password += random.choice(conso) + random.choice(vowel)

    return password

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

            username = input('Enter your username\n')
            password = input('Enter your password\n')
            
            user_exists = check_user(username,password)
            if user_exists:
        
                print(f'Welcome {username} . Login was successful')
                while True:
                    print('Use the following short codes')
                    print()
                    print('cc -> To create a new credentials account')
                    print('dc -> To display all credentials\n')
                    print('dc -> To search a particular credential\n')
                    print('#'*80)

                    credential_codes = input().lower().strip()

                    if credential_codes == "cc":

                        cred_account = input('For which app are these credentials for?\n')
                        cred_username = input('Enter your username\n')
                        
                        print('Do you prefer an autogenerated password ? type Y to agree and N to disagree')
                        
                        while True:
                            response  = input().lower.strip()
                            if response == 'y':
                                cred_password = create_password()
                                break
                            elif response == 'n':
                                cred_password = input()
                                break
                            else:
                                print('Invalid response type Y to agree and N to disagree')
                                continue
                        save_credential(create_credential_account(cred_account,cred_username,cred_password))
                        print(f'credential for {cred_account} has been added\n')
                         
                        

















if __name__ == '__main__':

    main()
