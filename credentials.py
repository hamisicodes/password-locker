class Credential:
    credential_list = []

    def __init__(self,account,password,username):
        self.account = account
        self.password = password
        self.username = username
        
    def save_credentials(self):
        Credential.credential_list.append(Credential)


    
    @classmethod
    def displayCredentials(cls):
        return cls.credential_list


        

