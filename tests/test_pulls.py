from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_1(self):
        t_accepted = {
            'num': 41,
            'title': 'Homework3: Yaroslav Kurapov',
            'link': 'https://github.com/alenaPy/devops_lab/pull/41'
        }
        t_needs_work = {
            'num': 67,
            'title': 'Homevork3: Vitali Lukashevich'
        }

        self.assertEqual(pulls.get_pulls('accepted').count(t_accepted), 1)
        self.assertEqual(pulls.get_pulls('needs work').count(t_needs_work), 0)

    def test_2(self):
        self.assertNotEqual(pulls.get_pulls("open")[0], 'eeeee')
        self.assertNotEqual(pulls.get_pulls("closed")[5], 'num: 75')

    def tearDown(self):
        """Finish"""
