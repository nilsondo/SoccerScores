import unittest
from src.model.team import Team


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - Team should be able to create an object instance.
    1.1 - Team should only receive a string name.

    *2* - Functions:
    2.0 - Team must be able to return its own information.
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        team = Team(name='USA')

        msg = "Team creation fail."
        self.assertIsInstance(team, Team, msg)  # 1.0
        print "Team Test Set: 1.0 Success"

        with self.assertRaises(Exception) as context:
            team = Team(name=0)

        msg = "Team receiving a string name fail"
        self.assertEqual(context.exception.message,
                         "Invalid team name.")  # 1.1
        print "Team Test Set: 1.1 Success"

        team = Team(name='Chile')

        msg = "Team display information fail"
        self.assertIsInstance(team.display(), str, msg)  # 2.0
        print "Team Test Set: 2.0 Success"
