import unittest
from soccerscores.core.match import Match
from soccerscores.core.team import Team


class Test(unittest.TestCase):

    '''
    1.0 - Match should be able to create an object instance.
    1.1 - Match should be able to start a match.
    1.2 - Match should be able to finish a match.
    1.3 - Match should be able to add points.
    1.4 - Match should be able to display a summary of itself.
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

        match.finish_match()

        msg = "Finish match fail."
        self.assertFalse(match.state, msg)  # 1.2
        print "Match Test Set: 1.2 Success"

        match.add_point(team=1)
        match.add_point(team=1)
        match.add_point(team=2)

        msg = "Score match fail."
        self.assertEqual(match.score, {1: 2, 2: 1}, msg)  # 1.3
        print "Match Test Set: 1.3 Success"

        summary = match.display()

        msg = "Display summary match fail."
        self.assertIsInstance(summary, str, msg)  # 1.4
        print "Match Test Set: 1.4 Success"
