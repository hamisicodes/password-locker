import unittest
from credentials import Credential

class test_credential(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("twitter","twitter001","hamisi")

    def tearDown(self):
        Credential.credential_list = []

    def test_init(self):
       
        self.assertEqual(self.new_credential.password,"twitter001")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"hamisi")

    def test_save_credentials(self):
        self.new_credential.save_credentials()

        self.assertEqual(len(Credential.credential_list),1)
    

    def test_save_multiple_credentials(self):
        self.new_credential.save_credentials()
        another_credential = Credential("facebook","facebook001","salim")
        another_credential.save_credentials()

        self.assertEqual(len(Credential.credential_list),2)
    
    def test_display_credentials(self):
        self.assertEqual(Credential.displayCredentials(),Credential.credential_list)




if __name__ == '__main__':
    unittest.main()