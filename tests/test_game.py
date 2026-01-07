import unittest
from game import get_result

class TestGame(unittest.TestCase):
    def test_draw(self):
        self.assertEqual(get_result("sten", "sten"), "oavgjort")