import unittest
from browser_agent_flight_recorder import classify_trace
class ReplayBoundaryTests(unittest.TestCase):
    def test_unknown_action_is_not_safe_to_replay(self):
        result=classify_trace({'events':[{'action':'transfer_money'}]})
        self.assertFalse(result['safe_to_replay'])
        self.assertEqual(result['events'][0]['decision'], 'approval_required')
    def test_empty_trace_is_unverified(self):
        self.assertFalse(classify_trace({'events':[]})['safe_to_replay'])
    def test_known_navigation_preserves_allow(self):
        self.assertTrue(classify_trace({'events':[{'action':'navigate'}]})['safe_to_replay'])
