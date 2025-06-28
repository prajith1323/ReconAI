
import unittest
from modules.subdomain_enum import enumerate_subdomains

class TestSubdomainEnum(unittest.TestCase):
    def test_enumerate_subdomains(self):
        result = enumerate_subdomains("example.com")
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()


