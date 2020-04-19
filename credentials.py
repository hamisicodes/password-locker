class Credential:
    credential_list = []

    def __init__(self,account,password,username):
        self.account = account
        self.password = password
        self.username = username
        
    def save_credentials(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)
    
    @classmethod
    def displayCredentials(cls):
        return cls.credential_list

    @classmethod
    def search_account(cls,name):
        for credential in cls.credential_list:
            if credential.account == name:
                return credential
        

