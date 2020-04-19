import unittest
from credentials import Credential

class test_credential(unittest.TestCase):

    def setUp(self):
        
         self.new_credential = Credential("twitter","twitter001","hamisi")

    def test_init(self):
       
        self.assertEqual(self.new_credential.password,"twitter001")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.username,"hamisi")








if __name__ == '__main__':
    unittest.main()