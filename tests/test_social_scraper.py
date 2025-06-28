
import unittest
from modules.social_scraper import scrape_social_media

class TestSocialScraper(unittest.TestCase):
    def test_scrape_social_media(self):
        result = scrape_social_media("testuser")
        self.assertIsInstance(result, dict)
        self.assertIn("linkedin", result)
        self.assertIn("github", result)

if __name__ == "__main__":
    unittest.main()


