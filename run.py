#!/usr/bin/env python3.6
from user import User
from credentials import  Credential

def create_user_account(user_name,passcode):
    new_user = User(user_name,passcode)
    return new_user

def save_user(user):
    user.save_user()




