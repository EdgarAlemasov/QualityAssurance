import unittest
from YandexAPI import create_folder, list_folder
from colorama import Fore

filename = 'Hello World'

status_code = {
    200: 'ok',
    201: 'folder created',
    400: 'incorrect data',
    401: 'not authorized',
    403: 'to large',
    404: 'undefined resourse',
    406: 'not acceptable',
    409: 'already exists',
    423: 'locked',
    429: 'to many requests',
    503: 'service unavailable',
    507: 'insufficient storage'
}


class TestYandexAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('Connect DataBase')

    def setUp(self) -> None:
        print('Create User')

    def test_create_folder(self):
        try:
            self.assertEqual(201, create_folder(filename))
        except AssertionError as er:
            print(Fore.RED + f'\nTest completed with ERROR: {er}')
            for code in status_code:
                if create_folder(filename) == code:
                    x = status_code.get(code)
                    return print(Fore.RED + f'Info about ERROR: {x}')

    def test_list_folder(self):
        self.assertEqual(200, list_folder(filename))
        print(Fore.RED + f'Folder {filename} already exests')

    def tearDown(self) -> None:
        print('Delete User')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Disconnect DataBase')



if __name__ == '__main__':
    unittest.main()