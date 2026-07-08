import unittest

from browser_agent_flight_recorder import classify_trace, redact_value


class FlightTests(unittest.TestCase):
    def test_publish_is_blocked(self):
        result = classify_trace({"events": [{"action": "publish_post"}]})
        self.assertEqual(result["blocked_count"], 1)
        self.assertFalse(result["safe_to_replay"])

    def test_read_is_safe(self):
        result = classify_trace({"events": [{"action": "read"}]})
        self.assertTrue(result["safe_to_replay"])

    def test_redacts_sensitive_text(self):
        self.assertIn("[REDACTED_EMAIL]", redact_value("a@example.com"))


if __name__ == "__main__":
    unittest.main()
