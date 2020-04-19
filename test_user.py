import unittest
from user import User

class testUser(unittest.TestCase):

    def setUp(self):
        """
         Setup method to run before each tests
        """
        self.new_user = User("Hamisi","python")

    def tearDown(self):
        """
        TearDown method that perfoms clean up after each test
        """
        User.users_list = []

    def test_init(self):
        """
        test if the user object is initialized properly
        """
        self.assertEqual(self.new_user.username,"Hamisi")
        self.assertEqual(self.new_user.password,"python")

    def test_addUser(self):
        """
        test to save user 

        """
        self.new_user.saveUser()
        self.assertEqual(len(User.users_list),1)

    def test_add_many_users(self):
        """
        test to save many users 

        """
        self.new_user.saveUser()
        another_user = User("salim","java")
        another_user.saveUser()
        self.assertEqual(len(User.users_list),2)

    def test_user_exists(self):

        self.new_user.saveUser()
        another_user = User("salim","java")
        another_user.saveUser()

        userfound = User.user_exists("salim","java")
        another_user_found =User.user_exists("Hamisi","python")

        self.assertTrue(userfound)
        self.assertTrue(another_user_found)









if __name__ == '__main__':
    unittest.main()