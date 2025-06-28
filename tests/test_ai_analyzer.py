
import unittest
from modules.ai_analyzer import analyze_with_ai

class TestAIAnalyzer(unittest.TestCase):
    def test_analyze_with_ai(self):
        sample_data = {
            "whois": {"domain": "example.com"},
            "subdomain": ["sub.example.com"],
            "social": {"linkedin": "user"}
        }
        # Mock API key for testing purposes
        result = analyze_with_ai(sample_data, openai_api_key="MOCK_API_KEY")
        self.assertIsInstance(result, dict)
        self.assertIn("threat_prediction", result)
        self.assertIn("entities", result)

if __name__ == "__main__":
    unittest.main()


