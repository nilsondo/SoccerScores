from soccerscores.core.team import Team
import datetime as dt


class Match:

    '''
    Match class.
    '''
    __defined_teams = {1: 'home', 2: 'away'}
    __separator = r'VS'

    def __init__(self, home, away):
        '''
        Constructor
        '''

        if isinstance(home, Team) and isinstance(away, Team):
            self.__home = home
            self.__away = away
        else:
            raise Exception('Invalid teams.')

        self.__date = dt.date.today()
        self.__time = None
        self.__state = None
        self.__score = {1: 0, 2: 0}
        self.__plays = []

        # Creating the match id
        self.__mid = (
            home.name[:3].upper() +
            self.__separator +
            away.name[:3].upper() +
            self.__date.strftime('%d'))

    def add_play(self, play):
        '''
        Add a given play to the plays stack of the given Match.
        '''
        if self.__state:
            self.__plays.append(play)
            return True
        return False

    def add_point(self, team):
        '''
        Add one point to a valid team in the score.
        '''
        if self.__state:
            try:
                self.__score[team] = self.__score[team] + 1
            except:
                return False
            return True
        return False

    def start_match(self):
        '''
        Set the state of the match to start.
        '''
        if self.__state is None:
            self.__state = True
            self.__time = None
            return True
        return False

    def finish_match(self):
        '''
        Set the state of the match to finish.
        '''
        if self.__state:
            self.__state = False
            return True
        return False

    def display(self):
        '''
        Return the string format description for the given match.
        '''
        state = None
        if self.__state is True:
            state = 'In progress'
        elif self.__state is False:
            state = 'Finish'
        else:
            state = 'Not started'
        return (
            self.__home.name + ' ' +
            self.__separator + ' ' +
            self.__away.name + ' ' +
            str(self.__score[1]) + ' - ' +
            str(self.__score[2]) + ' |' +
            state + '|')

    @property
    def home(self):
        '''
        Getter for the home team attribute.
        '''
        return self.__home

    @property
    def away(self):
        '''
        Getter for the away team attribute.
        '''
        return self.__away

    @property
    def mid(self):
        '''
        Getter for the match id.
        '''
        return self.__mid

    @property
    def state(self):
        '''
        Getter for the match state.
        '''
        return self.__state

    @property
    def score(self):
        return self.__score

    @property
    def plays(self):
        return self.__plays
