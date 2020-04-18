import unittest
from user import User

class testUser(unittest.TestCase):

    def setUp(self):
        """
         Setup method to run before each tests
        """
        self.new_user = User("Hamisi","python")

    def test_init(self):
        """
        test if the user object is initialized properly
        """
        self.assertEqual(self.new_user.username,"Hamisi")
        self.assertEqual(self.new_user.password,"python")