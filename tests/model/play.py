import unittest
from src.model.play import Play
from src.model.team import Team


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - Play should be able to create an object instance.
    1.1 - Play should receive a valid team object.
    1.2 - Play should receive a valid int type.
    1.2 - Play should receive a valid int spec.
    1.4 - Play must receive a string description empty or not.
    1.5 - Play should receive a valid int time

    *2* - Functions:
    2.0 - Play must be able to return its own information.
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        team = Team('Home')

        play = Play(ptype=0, spec=0, team=team, descrip='Match starts',
                    time=2)

        msg = "Play creation fail."
        self.assertIsInstance(play, Play, msg)  # 1.0
        print "Play Test Set: 1.0 Success"

        msg = "Play raise exceptions if not receive a team object fail."
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team='USA', descrip='', time=1)
        self.assertEqual(context.exception.message,
                         "Invalid team.")  # 1.1
        print "Play Test Set: 1.1 Success"

        msg = "Play raise exceptions if not receive an int type."
        with self.assertRaises(Exception) as context:
            play = Play(ptype='0', spec=0, team=team, descrip='', time=1)
        self.assertEqual(context.exception.message,
                         "Invalid type.")  # 1.2
        print "Play Test Set: 1.2 Success"

        msg = "Play raise exceptions if not receive an int spec."
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec='2', team=team, descrip='', time=1)
        self.assertEqual(context.exception.message,
                         "Invalid specialization.")  # 1.3
        print "Play Test Set: 1.3 Success"

        msg = "Play string description empty or not fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team=team, descrip=True,
                        time=1)
        self.assertEqual(context.exception.message,
                         "Invalid description.")  # 1.4
        print "Play Test Set: 1.4 Success"

        msg = "Play int time fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team=team, descrip='',
                        time='10')
        self.assertEqual(context.exception.message,
                         "Invalid time.")  # 1.5
        print "Play Test Set: 1.5 Success"

        msg = "Play display information fail"
        play = Play(ptype=0, spec=7, team=team, descrip='Home scores',
                    time=35)
        self.assertEqual(play.display(), "35' Goal, Home scores")  # 2.0
        print "Play Test Set: 2.0 Success"
