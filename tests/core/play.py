import unittest
from soccerscores.core.play import Play


class Test(unittest.TestCase):
    '''
    *1* - Instance & Properties:
    1.0 - Play should be able to create an object instance.
    1.1 - Play should be able to accept upper case team name.
    1.2 - Play should be able to accept upper & lower case team name.
    1.3 - Play should be able to raise exceptions if not receive an int spec.
    1.4 - Play should be able to receive an int spec.
    1.5 - Play should be avoid instance object with spec out of the range 0-6
          and 404.
    1.6 - Play must be able to raise exceptions if not receive an int type.
    1.7 - Play should be avoid instance object with type out of the range 0-4.
    1.8 - Play must receive a string description empty or not.
    1.9 - Play should receive an int time
    1.10 - Play must avoid instance object with time out of range 0-120

    *2* - Functions:
    2.0 - Play must return a str with time, type and description of the play.
    '''
    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        play = Play(ptype=0, spec=0, team='home', descrip='Match starts',
                    time=2)

        msg = "Play creation fail."
        self.assertIsInstance(play, Play, msg)  # 1.0
        print "Play Test Set: 1.0 Success"

        play = Play(ptype=0, spec=0, team='HOME', descrip='Match starts',
                    time=2)

        msg = "Play upper case team name fail."
        self.assertIsInstance(play, Play, msg)  # 1.1
        print "Play Test Set: 1.1 Success"

        play = Play(ptype=0, spec=0, team='hoME', descrip='Match starts',
                    time=2)

        msg = "Play upper & lower case team name fail."
        self.assertIsInstance(play, Play, msg)  # 1.2
        print "Play Test Set: 1.2 Success"

        msg = "Play raise exceptions if not receive an int spec fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec='2', team='home', descrip='', time=1)
        self.assertEqual(context.exception.message,
                         'Invalid specialization.')  # 1.3
        print "Play Test Set: 1.3 Success"

        msg = "Play int spec fail"
        play = Play(ptype=0, spec=0, team='hoME', descrip='Match starts',
                    time=2)
        self.assertIsInstance(play, Play, msg)  # 1.4
        print "Play Test Set: 1.4 Success"

        msg = "Play spec out of the range 0-6 and 404 fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=-1, team='home', descrip='', time=1)
        self.assertEqual(context.exception.message,
                         'Invalid specialization.')  # 1.5
        print "Play Test Set: 1.5 Success"

        msg = "Play raise exceptions if not receive an int type fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype='2', spec=0, team='home', descrip='', time=1)
        self.assertEqual(context.exception.message,
                         'Invalid type.')  # 1.6
        print "Play Test Set: 1.6 Success"

        msg = "Play type out of the range 0-4 fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=-1, spec=0, team='home', descrip='', time=1)
        self.assertEqual(context.exception.message,
                         'Invalid type.')  # 1.7
        print "Play Test Set: 1.7 Success"

        msg = "Play string description empty or not fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team='home', descrip=True,
                        time=1)
        self.assertEqual(context.exception.message,
                         'Invalid description.')  # 1.8
        print "Play Test Set: 1.8 Success"

        msg = "Play int time fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team='home', descrip='',
                        time='10')
        self.assertEqual(context.exception.message,
                         'Invalid time.')  # 1.9
        print "Play Test Set: 1.9 Success"

        msg = "Play time out of range 0-120 fail"
        with self.assertRaises(Exception) as context:
            play = Play(ptype=0, spec=0, team='home', descrip='',
                        time=120)
        self.assertEqual(context.exception.message,
                         'Invalid time.')  # 1.10
        print "Play Test Set: 1.10 Success"

        msg = "Play f. display fail"
        play = Play(ptype=0, spec=7, team='home', descrip='Home scores',
                    time=35)
        self.assertEqual(play.display(), "35' Gol, Home scores")  # 2.0
        print "Play Test Set: 2.0 Success"
