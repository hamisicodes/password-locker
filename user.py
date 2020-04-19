class User:

    users_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def saveUser(self):
        User.users_list.append(self)
        
    @classmethod

    def user_exists(cls,name,password):
        for users in cls.users_list:
            if users.username == name and users.password == password:
                return True

        return False