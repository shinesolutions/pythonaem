import unittest
from pythonaem.swagger import operation_to_method

class TestSwagger(unittest.TestCase):

    def test_operation_to_method_should_replace_all_uppercases_with_lowercases_letters_each_prefixed_with_an_underscore(self):
        method = operation_to_method('postBundle')
        self.assertEqual(method, 'post_bundle')

if __name__ == '__main__':
    unittest.main()