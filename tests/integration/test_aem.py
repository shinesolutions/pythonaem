import unittest
from helper import init_client

class TestAem(unittest.TestCase):

    def setUp(self):
        pythonaem = init_client()
        self.aem = pythonaem.aem()

    def tearDown(self):
        print("")

    def test_get_aem_health_check(self):
        result = self.aem.get_aem_health_check({
            'tags': 'shallow',
            'combine_tags_or': 'false',
        })
        self.assertEqual(result.message, 'AEM health check retrieved')
        self.assertEqual(len(result.data), 1)
        self.assertEqual(result.data[0]['name'], 'Smoke Health Check')
        self.assertEqual(result.data[0]['status'], 'OK')

if __name__ == '__main__':
    unittest.main()