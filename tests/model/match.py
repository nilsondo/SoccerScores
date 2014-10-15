import unittest
from src.model.match import Match
from src.model.team import Team


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - Match should be able to create an object instance.
    1.1 - Match should be able to start a match.
    1.2 - Match should be able to add points.
    1.3 - Match should be able to finish a match.

    *2* - Functions:
    2.0 - Match must be able to return its own information.
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        home = Team(name='Barcelona')
        away = Team(name='Bayern Munich')

        match = Match(home=home,
                      away=away)

        msg = "Match creation fail."
        self.assertIsInstance(match, Match, msg)  # 1.0
        print "Match Test Set: 1.0 Success"

        match.start_match()

        msg = "Start match fail."
        self.assertTrue(match.state, msg)  # 1.1
        print "Match Test Set: 1.1 Success"

        match.add_point(team=home)
        match.add_point(team=home)
        match.add_point(team=away)

        msg = "Score match fail."
        self.assertEqual(match.score, {home: 2, away: 1}, msg)  # 1.2
        print "Match Test Set: 1.2 Success"

        match.finish_match()

        msg = "Finish match fail."
        self.assertFalse(match.state, msg)  # 1.3
        print "Match Test Set: 1.3 Success"

        summary = match.display()

        msg = "Display summary match fail."
        self.assertIsInstance(summary, str, msg)  # 2.0
        print "Match Test Set: 2.0 Success"
