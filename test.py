from unittest import TestCase

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_caps_diffrence(self):
        self.assertEqual(solution( "racecar","RaceCar" ),[0, 4] )
    def test_two_diff_word(self):
        self.assertEqual(solution("Cat","Dog"), [0, 1, 2])
    def test_same(self):
        self.assertEqual(solution("same","same"),[])
    def broken_test(self):# wont work because we have to start our test definition with test in order for unittest to find it
        self.assertEqual(solution("broke","break"), [2, 3, 4])