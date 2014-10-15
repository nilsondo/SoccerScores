from src.model.annotator import Annotator


class AnotatorController():

    '''
    Anotator controller class.
    '''
    __model = None

    def __init__(self):
        pass

    @property
    def model(self):
        '''
        Getter for the model attribute.
        '''
        return self.__model

    @model.setter
    def model(self, value):
        '''
        Setter for the model attribute.
        '''
        if isinstance(value, Annotator):
            self.__model = value
        else:
            raise Exception('Invalid model.')

    def add_match(self, match):
        '''
        Add the given match to the model.
        '''
        self.model.add_match(match)

    def get_match(self, mid, view):
        '''
        Returns the the Match object given a valid mid.
        '''
        match = self.model.get_match(mid)
        match.add_view(view)

        return match

    def remove_match(self, mid):
        '''
        Remove the given match of the model.
        '''
        match = self.model.get_match(mid)

        if match:
            self.model.remove_match(match)
            return True
        else:
            return False

    def remove_match_view(self, match, view):
        '''
        Remove the current match listener.
        '''
        match.remove_view(view)

    def add_play(self, match, play):
        '''
        Add a given play to the plays stack of the given Match.
        '''
        print('HERE')
        match.add_play(play)

    def start_match(self, match):
        '''
        Set the state of the given match to start.
        '''
        return match.start_match()

    def finish_match(self, match):
        '''
        Set the state of the given match to finish.
        '''
        return match.finish_match()

    def match_started(self, match):
        '''
        '''
        return match.state
