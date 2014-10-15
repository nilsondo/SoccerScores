import unittest
from src.controller.annotator import AnnotatorController
from src.model.annotator import Annotator
from src.model.match import Match


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

    def display(self):
        pass


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - AnnotatorController should be able to create an object instance
    1.1 - AnnotatorController should be able to add a model


    *2* - Functions:
    2.0 - AnnotatorController should be able to add matches to a model
    2.1 - AnnotatorController should be able to get a match to a model
    2.2 - AnnotatorController should be able to remove matches to a model
    2.3 - AnnotatorController should be able to save of a model
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        ctrl = AnnotatorController()
        msg = "AnnotatorController creation fail."
        self.assertIsInstance(ctrl, AnnotatorController, msg)  # 1.0
        print "AnnotatorController Test Set: 1.0 Success"

        model = Annotator.create()
        ctrl.model = model

        msg = "AnnotatorController model addition fail."
        self.assertEquals(ctrl.model, model)  # 1.1
        print "AnnotatorController Test Set: 1.1 Success"

        match = TestMatch(home='Barcelona',
                          away='Bayern Munich',
                          mid='BRAVSBAY15')

        ctrl.add_match(match)

        msg = "AnnotatorController match addition fail."
        self.assertEquals(model.get_match(match.mid), match)  # 2.0
        print "AnnotatorController Test Set: 2.0 Success"

        match_copy = ctrl.get_match(match.mid)

        msg = "AnnotatorController get match fail."
        self.assertEquals(match_copy, match, msg)  # 2.1
        print "AnnotatorController Test Set: 2.1 Success"

        ctrl.remove_match(match.mid)

        msg = "AnnotatorController match deletion fail."
        self.assertTrue(len(model.matches) == 0, msg)  # 2.2
        print "AnnotatorController Test Set: 2.2 Success"

        ctrl.save()
        model = None
        model = Annotator.load()

        msg = "AnnotatorController save state fail."
        self.assertIsInstance(model, Annotator, msg)  # 2.3
        print "AnnotatorController Test Set: 2.3 Success"
