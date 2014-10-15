import re


class Team:

    '''
    Team class.
    '''

    name_re = r'(^[A-Za-z][ A-Za-z]*$)+'

    def __init__(self, name, players=None):
        '''
        Constructor
        '''
        if isinstance(name, str) and re.match(self.name_re, name):
            self.__name = name.lower()
        else:
            raise Exception("Invalid team name.")

    @property
    def name(self):
        '''
        Getter for the name attribute.
        '''
        return self.__name

    @name.setter
    def name(self, value):
        '''
        Setter for the name attribute.
        '''
        self.__name = value

    def display(self):
        '''
        Returns a string white the team attributes
        '''
        return self.name
