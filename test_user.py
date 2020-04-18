import unittest
from user import User

class testUser(unittest.TestCase):

    def setUp(self):
        """
         Setup method to run before each tests
        """
        self.new_user = User("Hamisi","python")
