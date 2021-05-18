import unittest
from helper import init_client

class TestReplicationAgent(unittest.TestCase):

    def setUp(self):
        self.aem = init_client()

        # ensure agent doesn't exist prior to testing
        self.replication_agent = self.aem.replication_agent('author', 'some-replication-agent')
        if self.replication_agent.exists().data:
            self.replication_agent.delete()
        result = self.replication_agent.exists()
        self.assertFalse(result.data)

        # create agent
        result = self.replication_agent.create_update('Some Replication Agent Title', 'Some replication agent description', 'http://somehost:8080')
        self.assertEqual(result.message, 'Replication agent some-replication-agent created on author')

    def tearDown(self):
        print("")

    def test_replication_agent_create_update_should_return_true_on_existence_check(self):
        result = self.replication_agent.exists()
        self.assertEqual(result.message, 'Replication agent some-replication-agent exists on author')
        self.assertTrue(result.data)

    def test_replication_agent_create_update_should_succeed_update(self):
        result = self.replication_agent.create_update('Some Updated Replication Agent Title', 'Some updated replication agent description', 'https://someotherhost:8081')
        self.assertEqual(result.message, 'Replication agent some-replication-agent updated on author')

    def test_replication_agent_delete_should_succeed_when_replication_agent_exists(self):
        result = self.replication_agent.delete()
        self.assertEqual(result.message, 'Replication agent some-replication-agent deleted on author')

        result = self.replication_agent.exists()
        self.assertEqual(result.message, 'Replication agent some-replication-agent not found on author')
        self.assertFalse(result.data)

    def test_replication_agent_delete_should_raise_error_when_replication_agent_does_not_exist(self):
        self.replication_agent = self.aem.replication_agent('author', 'some-inexisting-replication-agent')
        try:
            self.replication_agent.delete()
            raise
        except Exception as error:
            self.assertEqual(error.message, 'Replication agent some-inexisting-replication-agent not found on author')

if __name__ == '__main__':
    unittest.main()