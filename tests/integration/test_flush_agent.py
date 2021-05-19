import unittest
from helper import init_client

class TestFlushAgent(unittest.TestCase):

    def setUp(self):
        self.aem = init_client()

        # ensure agent doesn't exist prior to testing
        self.flush_agent = self.aem.flush_agent('author', 'some-flush-agent')
        if self.flush_agent.exists().data:
            self.flush_agent.delete()
        result = self.flush_agent.exists()
        self.assertFalse(result.data)

        # create agent
        result = self.flush_agent.create_update('Some Flush Agent Title', 'Some flush agent description', 'http://somehost:8080')
        self.assertEqual(result.message, 'Flush agent some-flush-agent created on author')

    def tearDown(self):
        print("")

    def test_flush_agent_create_update_should_return_true_on_existence_check(self):
        result = self.flush_agent.exists()
        self.assertEqual(result.message, 'Flush agent some-flush-agent exists on author')
        self.assertTrue(result.data)

    def test_flush_agent_create_update_should_succeed_update(self):
        result = self.flush_agent.create_update('Some Updated Flush Agent Title', 'Some updated flush agent description', 'https://someotherhost:8081')
        self.assertEqual(result.message, 'Flush agent some-flush-agent updated on author')

    def test_flush_agent_create_update_should_succeed_disable(self):
        result = self.flush_agent.disable()
        self.assertEqual(result.message, 'Flush agent some-flush-agent disabled on author')

    def test_flush_agent_create_update_should_succeed_enable(self):
        result = self.flush_agent.enable()
        self.assertEqual(result.message, 'Flush agent some-flush-agent enabled on author')

    def test_flush_agent_delete_should_succeed_when_flush_agent_exists(self):
        result = self.flush_agent.delete()
        self.assertEqual(result.message, 'Flush agent some-flush-agent deleted on author')

        result = self.flush_agent.exists()
        self.assertEqual(result.message, 'Flush agent some-flush-agent not found on author')
        self.assertFalse(result.data)

    def test_flush_agent_delete_should_raise_error_when_flush_agent_does_not_exist(self):
        self.flush_agent = self.aem.flush_agent('author', 'some-inexisting-flush-agent')
        try:
            self.flush_agent.delete()
            raise
        except Exception as error:
            self.assertEqual(error.message, 'Flush agent some-inexisting-flush-agent not found on author')

if __name__ == '__main__':
    unittest.main()