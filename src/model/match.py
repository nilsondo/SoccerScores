from src.model.team import Team
import datetime


class Match:

    '''
    Match class.
    '''
    defined_teams = {1: 'home', 2: 'away'}
    separator = r'VS'

    def __init__(self, home, away):
        '''
        Constructor
        '''

        if isinstance(home, Team) and isinstance(away, Team):
            self.__home = home
            self.__away = away
        else:
            raise Exception('Invalid teams.')

        self.__score = {self.__home: 0, self.__away: 0}
        self.__plays = []
        self.__state = None

        # Creating the match id
        self.__mid = (
            home.name[:3].upper() +
            self.separator +
            away.name[:3].upper() +
            datetime.date.today().strftime('%d'))

        self.__views = set()

    @property
    def views(self):
        '''
        Getter for the view attribute.
        '''
        return self.__views

    @views.setter
    def views(self, value):
        '''
        Setter for the view attribute.
        '''
        self.__views = value

    def add_view(self, view):
        '''
        Add the given view to the views set.
        '''
        self.views.add(view)
        self.notify_match_change()

    def remove_view(self, view):
        '''
        Remove the given view of the views set.
        '''
        if len(self.view) > 0:
            try:
                self.view.remove(view)
            except:
                return None
        else:
            return None

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

    def add_play(self, play):
        '''
        Add a given play to the plays stack of the Match.
        '''
        if self.state:
            self.__plays.append(play)

            # if the play is a Goal, then a point is added
            if(play.ptype is 0):
                self.add_point(play.team)
                self.notify_match_change()
            return True
        return False

    def add_point(self, team):
        '''
        Add one point to a valid team in the score.
        '''
        if self.state:
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
        if self.state is None:
            self.__state = True
            self.notify_match_change()
            return True
        return False

    def finish_match(self):
        '''
        Set the state of the match to finish.
        '''
        if self.state:
            self.__state = False
            self.notify_match_change()
            return True
        return False

    def __get_str_state(self):
        '''
        Returns the string version of the current state.
        '''
        str_state = None
        if self.state is True:
            str_state = 'In progress'
        elif self.state is False:
            str_state = 'Finish'
        else:
            str_state = 'Not started'

        return str_state

    def display(self):
        '''
        Return the string format description for the given match.
        '''
        return (
            self.__home.name + ' ' +
            self.separator + ' ' +
            self.__away.name + ' ' +
            str(self.__score[self.__home]) + ' - ' +
            str(self.__score[self.__away]) + ' |' +
            self.__get_str_state() + '|')

    def display_plays(self):
        '''
        Return the string format for the plays of the match.
        '''
        str_plays = {}
        i = 1

        for play in self.plays:
            str_plays[i] = play.display()
            i = i + 1

        return str_plays

    def notify_match_change(self):
        '''
        Notify any match change to a listed views
        this views are temporarily listed to the match.
        '''
        str_match = self.display()
        str_plays = self.display_plays()

        for view in self.views:
            view.on_match_change(str_match=str_match,
                                 str_plays=str_plays)
