import unittest
from soccerscores.access.annotator import Annotator


class TestMatch():
    '''
    Test class for a match.
    '''
    __separtor = r'vs'

    def __init__(self, home, away, mid):
        '''
        Construtor
        '''
        self.__home = home
        self.__away = away
        self.__mid = mid

    @property
    def mid(self):
        return self.__mid


class Test(unittest.TestCase):
    '''
    1.0 - Annotator should be able to create an object instance
    1.1 - Annotator should be able to add matches
    1.2 - Annotator should be able to remove matches
    1.3 - Annotator should be able to get an specifix match
    '''
    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        annotator = Annotator.create()

        msg = "Annotator creation fail."
        self.assertIsInstance(annotator, Annotator, msg)  # 1.0
        print "Annotator Test Set: 1.0 Success"

        match = TestMatch(home='FC Barcelona',
                          away='FC Bayern Munich',
                          mid='FCBvsFCBM')

        annotator.add_match(match)

        msg = "Annotator match addition fail."
        self.assertTrue(len(annotator.matches) > 0, msg)  # 1.1
        print "Annotator Test Set: 1.1 Success"

        annotator.remove_match(match)

        msg = "Annotator match deletion fail."
        self.assertTrue(len(annotator.matches) == 0, msg)  # 1.2
        print "Annotator Test Set: 1.2 Success"

        match_mid = match.mid
        annotator.add_match(match)
        match_copy = annotator.get_match(match_mid)

        msg = "Annotator get match fail."
        self.assertEquals(match_copy.mid, match_mid, msg)  # 1.3
        print "Annotator Test Set: 1.3 Success"
