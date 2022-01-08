import parameterized as parameterized
from CodeForTests import show_all_docs_info, add_new_doc, delete_doc
import unittest


TEST_DATA_DOC = ['passport 2207 876234 Василий Гупкин',
                 'invoice 11-2 Геннадий Покемонов',
                 'insurance 10006 Аристарх Павлов']

TEST_DATA_ADD_TRUE = [
    ['777', 'visa', 'Edgar Alemasov', '72'],
    ['888 22 1', 'passport', 'Darina Ko', '2']
]

TEST_DATA_ADD_FALSE = [
    ['112', '', 'Irina Ka', ''],
    ['95857452', 'licence', '', '']
]

TEST_DELETE_DATA_TRUE = ['11-2', '2207 876234', '10006']
TEST_DELETE_DATA_FALSE = ['555', '10','']


class TestShowInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Connect DataBase')

    def setUp(self) -> None:
        print('Create User')

    def test_show_all_docs_info(self):
        self.assertEqual(TEST_DATA_DOC, show_all_docs_info(), 'values are not equal')
        self.assertIsNotNone(show_all_docs_info(), 'return None')

    def tearDown(self) -> None:
        print('Delete User')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Disconnect DataBase')


class TestAddNewDocument(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Connect DataBase')

    def setUp(self) -> None:
        print('Create User')

    @parameterized.parameterized.expand(TEST_DATA_ADD_TRUE)
    def test_add_new_doc(self,new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
        self.assertEqual(new_doc_shelf_number, add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number))

    @parameterized.parameterized.expand(TEST_DATA_ADD_FALSE)
    def test_add_new_doc(self,new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number):
        self.assertEqual(False, add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number))

    def tearDown(self) -> None:
        print('Delete User')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Disconnect DataBase')


class TestDeleteDoc(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Connect DataBase')

    def setUp(self) -> None:
        print('Create User')

    @parameterized.parameterized.expand(TEST_DELETE_DATA_TRUE)
    def test_delete_doc(self, user_doc_number):
        self.assertEqual((user_doc_number, True), delete_doc(user_doc_number), 'undefinded doc')

    @parameterized.parameterized.expand(TEST_DELETE_DATA_FALSE)
    def test_delete_doc(self, user_doc_number):
        self.assertEqual(None, delete_doc(user_doc_number), 'undefinded doc')

    def tearDown(self) -> None:
        print('Delete User')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Disconnect DataBase')


if __name__ == '__main__':
    unittest.main()
