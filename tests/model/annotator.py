import unittest
from src.model.annotator import Annotator
from src.model.match import Match
from src.model.team import Team


class TestMatch(Match):

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
    *1* - Instance & Properties:
    1.0 - Annotator should be able to create an object instance
    1.1 - Annotator should be able to add matches
    1.2 - Annotator should be able to remove matches
    1.3 - Annotator should be able to get an specifix match
    1.4 - Annotator should be able to save and load from an static file

    *2* - Functions:
    2.0 - Annotator must be able to return its own information.
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

        home = Team(name='Barcelona')
        away = Team(name='Bayern Munich')

        match = Match(home=home,
                      away=away)

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

        annotator.save()
        annotator = None
        annotator = Annotator.load()

        msg = "Annotator persistance fail."
        self.assertIsInstance(annotator, Annotator, msg)  # 1.4
        print "Annotator Test Set: 1.4 Success"

        msg = "Annotator display information fail"
        self.assertIsInstance(annotator.display(), str)  # 2.0
        print "Annotator Test Set: 2.0 Success"
