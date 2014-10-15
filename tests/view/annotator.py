import unittest
from src.controller.annotator import AnnotatorController
from src.view.annotator import AnnotatorView


class Test(unittest.TestCase):

    '''
    *1* - Instance & Properties:
    1.0 - AnnotatorView should be able to create an object instance
    1.1 - AnnotatorView should be able to add a controller
    '''

    def setUp(self):
        print ""
        print "################################################"

    def tearDown(self):
        print "################################################"

    def testOne(self):
        view = AnnotatorView()

        msg = "AnnotatorView creation fail."
        self.assertIsInstance(view, AnnotatorView, msg)  # 1.0
        print "AnnotatorView Test Set: 1.0 Success"

        ctrl = AnnotatorController()
        view.ctrl = ctrl

        msg = "AnnotatorView controller addition fail."
        self.assertEquals(view.ctrl, ctrl)  # 1.1
        print "AnnotatorView Test Set: 1.1 Success"
