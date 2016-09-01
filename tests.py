import unittest
from pollster.pollster import Pollster, Chart, PollsterException

class TestBasic(unittest.TestCase):

    def test_basic_setup(self):
        p = Pollster()
        self.assertIsNotNone(p)

    def test_charts(self):
        c = Pollster().charts()
        self.assertIsNotNone(c)
        self.assertIsInstance(c, list)
        self.assertGreater(len(c), 0)

    def test_chart(self):
        c = Pollster().charts()[0]
        self.assertIsInstance(c, Chart)
        cc = Pollster().chart(c.slug)
        self.assertEqual(c.slug, cc.slug)
        for attr in ['last_updated',
                         'title',
                         'url',
                         'estimates',
                         'poll_count',
                         'topic',
                         'state',
                         'slug', ]:
            self.assertIsNotNone(getattr(c, attr))
            self.assertIsNotNone(getattr(cc, attr))
            self.assertEqual(getattr(c, attr), getattr(cc, attr))
        self.assertIsInstance(c.estimates_by_date(), list)

    def test_polls(self):
        polls = Pollster().polls(topic='2016-president')
        self.assertGreater(len(polls), 0)
        poll = polls[0]
        for attr in     ['id',
                         'pollster',
                         'start_date',
                         'end_date',
                         'method',
                         'source',
                         'questions',
                         'survey_houses',
                         'sponsors',
                         'partisan',
                         'affiliation']:
             self.assertIsNotNone(getattr(poll, attr))

    def test_pollster_bad_site(self):
        c = Pollster()
        c.API_BASE = "/not/the/api/"
        self.assertRaises(PollsterException, c.charts)

    def test_pollster_404(self):
        c = Pollster()
        self.assertRaises(PollsterException, c.chart, "nonexistent-chart")
        self.assertRaises(PollsterException, c.polls, bad_param="bad")
