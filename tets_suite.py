import unittest
from tests.access import annotator
import sys


def suite():
    '''
    Gather all the tests in a test suite.
    '''
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(annotator.Test))
    return test_suite

if __name__ == "__main__":
    test_suite = suite()

    runner = unittest.TextTestRunner(descriptions=True, verbosity=1)
    result = runner.run(test_suite)
    ran_test_msg = "Tests ran: {count}".format(count=result.testsRun)
    print ran_test_msg

    if not result.wasSuccessful():
        sys.exit(1)
