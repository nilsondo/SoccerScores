import unittest
from soccerscores.core.team import Team


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - Team should be able to create an object instance.
    1.1 - Team must have almost 7 players and a maximum 12 player.
    1.2 - Team should only receive a str name.

    *2* - Functions:
    2.0 - Team must return a str player name
    2.1 - Team should return a player name given its number.
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        team = Team(name='USA', players={1: 'Ronny Atom', 2: 'Avigail Tracy',
                    3: 'John Bart', 4: 'Michael Jones', 5: 'Hector Quita',
                    6: 'Luis Bill', 7: 'Tron Hallow'})

        msg = "Team creation fail."
        self.assertIsInstance(team, Team, msg)  # 1.0
        print "Team Test Set: 1.0 Success"

        with self.assertRaises(Exception) as context:
            team = Team(name='CHINA', players={1: 'Ronny Atom',
                        2: 'Avigail Tracy', 3: 'John Bart', 4: 'Michael Jones',
                        5: 'Hector Quita', 6: 'Luis Bill'})

        msg = "Team with a minimum 7 players fail"
        self.assertEqual(context.exception.message,
                         'Invalid players dictionary.')  # 1.1.a
        print "Team Test Set: 1.1.a Success"

        with self.assertRaises(Exception) as context:
            team = Team(name='CHINA', players={1: 'Ronny Atom',
                        2: 'Avigail Tracy', 3: 'John Bart', 4: 'Michael Jones',
                        5: 'Hector Quita', 6: 'Luis Bill', 7: 'Tron Hallow',
                        8: 'Hector Quita', 9: 'Luis Bill', 10: 'Tron Hallow',
                        11: 'Hector Quita', 12: 'Luis Bill'})

        msg = "Team with a maximum 12 player fail"
        self.assertEqual(context.exception.message,
                         'Invalid players dictionary.')  # 1.1.b
        print "Team Test Set: 1.1.b Success"

        with self.assertRaises(Exception) as context:
            team = Team(name=0, players={1: 'Ronny Atom',
                        2: 'Avigail Tracy', 3: 'John Bart', 4: 'Michael Jones',
                        5: 'Hector Quita', 6: 'Luis Bill', 7: 'Tron Pujols'})

        msg = "Team receiving a str name fail"
        self.assertEqual(context.exception.message,
                         'Invalid team name.')  # 1.2
        print "Team Test Set: 1.2 Success"

        team = Team(name='Chile', players={1: 'Ronny Atom', 2: 'Avigail Tracy',
                    3: 'John Bart', 4: 'Michael Jones', 5: 'Hector Quita',
                    6: 'Luis Bill', 7: 'Tron Pujols'})

        msg = "Team return a str player name fail"
        self.assertIsInstance(team.get_player(1), str)  # 2.0
        print "Team Test Set: 2.0 Success"

        team = Team(name='Chile', players={1: 'Ronny Atom', 2: 'Avigail Tracy',
                    3: 'John Bart', 4: 'Michael Jones', 5: 'Hector Quita',
                    6: 'Luis Bill', 7: 'Tron Pujols'})

        msg = "Team should return a player name given its number fail"
        self.assertEqual(team.get_player(1), 'Ronny Atom')  # 2.1
        print "Team Test Set: 2.1 Success"
