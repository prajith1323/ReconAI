
import unittest
from modules.shodan_lookup import perform_shodan_lookup

class TestShodanLookup(unittest.TestCase):
    def test_perform_shodan_lookup(self):
        # Mock API key for testing purposes
        result = perform_shodan_lookup("127.0.0.1", "MOCK_API_KEY")
        self.assertIsInstance(result, dict)
        self.assertIn("ip", result)
        self.assertIn("ports", result)

if __name__ == "__main__":
    unittest.main()


