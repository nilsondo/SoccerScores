try:
   import cPickle as pickle
except:
   import pickle
import os


class Annotator:
    '''
    '''

    __file = os.path.abspath(os.path.join(os.getcwd(), 'annotator.pickle'))

    def __init__(self):
        '''
        Constructor
        '''
        self.__matches = {}

    @classmethod
    def create(cls):
        '''
        Create a new instance of the class Annotator.
        '''
        print os.getcwd()
        return cls()

    @classmethod
    def load(cls):
        '''
        Load the already created Annotator object.
        '''
        try:
            handle = open(cls.__file, 'rb')
            obj = pickle.load(handle)

            if isinstance(obj, Annotator):
                return obj
            else:
                return cls.create()

            handle.close()
        except IOError:
            return cls.create()

    def save(self):
        '''
        Save the current object in static location.
        '''
        with open(self.__file, 'wb') as handle:
            pickle.dump(self, handle)

    def add_match(self, match):
        '''
        Add the given match to the matches list.
        '''
        self.__matches[match.mid] = match

    def remove_match(self, match):
        '''
        Remove the given match to the matches list.
        '''
        if len(self.__matches) > 0:
            try:
                del self.__matches[match.mid]
            except:
                return None
        else:
            return None

    def get_match(self, mid):
        '''
        Returns the the Match object given a valid mid.
        '''
        if isinstance(mid, str):
            try:
                return self.__matches[mid]
            except:
                return None
        else:
            return None

    @property
    def matches(self):
        '''
        Getter for the matches attribute.
        '''
        return self.__matches
