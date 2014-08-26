import cPickle as pickle
import os


class Annotator:
    '''
    '''

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
        return cls()

    @classmethod
    def load(cls):
        '''
        Load the already created Annotator object.
        '''
        pass

    def save(self):
        '''
        Save the current object in static location.
        '''
        pass

    def add_match(self, match):
        '''
        Add the given match to the matches list.
        '''
        self.__matches[match.mid] = match

    def remove_match(self, match):
        '''
        Remove the given match to the matches list.
        '''
        del self.__matches[match.mid]

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
    @matches.setter
    def matches(self, value):
        '''
        Setter for the matches attribute.
        '''
        self.__matches = value
