class User:

    users_list = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def saveUser(self):
        User.users_list.append(User)
        