import unittest
from modules.whois_lookup import perform_whois_lookup

class TestWhoisLookup(unittest.TestCase):
    def test_perform_whois_lookup(self):
        # This is a basic test and assumes a valid response structure.
        # In a real scenario, you would mock external API calls.
        result = perform_whois_lookup("google.com")
        self.assertIsInstance(result, dict)
        self.assertIn("domain", result)
        self.assertIn("registrar", result)
        self.assertIn("creation_date", result)

if __name__ == "__main__":
    unittest.main()


