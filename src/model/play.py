from src.model.team import Team


class Play:

    '''
    Play class.
    '''

    defined_types = {0: 'Goal', 1: 'Red Card', 2: 'Yellow Card', 3: 'Change',
                     4: 'Comment'}
    defined_specs = {0: 'Hand kick', 1: 'Corner kick',
                     2: 'Goal kick', 3: 'Pass', 4: 'Center',
                     5: 'Clearance', 6: 'Ahead position', 7: 'None'}

    def __init__(self, ptype, spec, team, descrip, time=None):
        '''
        Constructor
        '''
        if isinstance(ptype, int) and ptype in self.defined_types.keys():
            self.__ptype = ptype
        else:
            raise Exception('Invalid type.')

        if isinstance(spec, int) and spec in self.defined_specs.keys():
            self.__spec = spec
        else:
            raise Exception('Invalid specialization.')

        if isinstance(team, Team):
            self.__team = team
        else:
            raise Exception('Invalid team.')

        if isinstance(descrip, str):
            self.__descrip = descrip
        else:
            raise Exception('Invalid description.')

        if isinstance(time, int) and time > 0 and time < 120:
            self.__time = time
        else:
            raise Exception('Invalid time.')

    @property
    def ptype(self):
        '''
        Getter for the type attribute.
        '''
        return self.__ptype

    @ptype.setter
    def ptype(self, value):
        '''
        Setter for the type attribute.
        '''
        self.__ptype = value

    @property
    def spec(self):
        '''
        Getter for the spec attribute.
        '''
        return self.__spec

    @spec.setter
    def spec(self, value):
        '''
        Setter for the spec attribute.
        '''
        self.__spec = value

    @property
    def team(self):
        '''
        Getter for the team attribute.
        '''
        return self.__team

    @team.setter
    def team(self, value):
        '''
        Setter for the team attribute.
        '''
        self.__team = value

    @property
    def descrip(self):
        '''
        Getter for the description attribute.
        '''
        return self.__descrip

    @descrip.setter
    def descrip(self, value):
        '''
        Setter for the description attribute.
        '''
        self.__descrip = value

    @property
    def time(self):
        '''
        Getter for the time attribute.
        '''
        return self.__time

    @time.setter
    def time(self, value):
        '''
        Setter for the time attribute.
        '''
        self.__time = value

    def display(self):
        '''
        Returns a string with time, type and description of the play.
        '''
        if self.__spec == 7:
            return (str(self.__time) + "' " +
                    self.defined_types[self.__ptype] +
                    ", " + self.__descrip)
        else:
            return (str(self.__time) + "' " +
                    self.defined_types[self.__ptype] + ", " +
                    self.defined_specs[self.__spec] +
                    ", " + self.__descrip)
