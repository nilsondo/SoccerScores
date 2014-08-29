import unittest
from soccerscores.core.play import Play


class Test(unittest.TestCase):
    '''
    1.0 - Play should be able to creat an object instance
    1.1 - Play should be able to accept upper case team name
    1.2 - Play should be able to accept upper & lower case team name
    1.3 -
    '''
    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        play = Play(ptype=0, spec=0, team='home', descrip='Corrio pila',
                    time=2)

        msg = "Play creation fail."
        self.assertIsInstance(play, Play, msg)  # 1.0
        print "Play Test Set: 1.0 Success"

        play = Play(ptype=0, spec=0, team='HOME', descrip='Corrio pila',
                    time=2)

        msg = "Play creation fail."
        self.assertIsInstance(play, Play, msg)  # 1.1
        print "Play Test Set: 1.1 Success"

        play = Play(ptype=0, spec=0, team='hoME', descrip='Corrio pila',
                    time=2)

        msg = "Play creation fail."
        self.assertIsInstance(play, Play, msg)  # 1.2
        print "Play Test Set: 1.2 Success"
