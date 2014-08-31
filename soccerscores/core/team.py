class Team:
    '''
    '''

    def __init__(self, name, players):
        '''
        Constructor
        '''
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Invalid team name.")

        if (isinstance(players, dict) and len(players.keys()) > 6
                and len(players.keys()) < 12):
            self.__players = players
        else:
            raise Exception("Invalid players dictionary.")

    @property
    def name(self):
        '''
        Getter for the name attribute.
        '''
        return self.__name

    @property
    def players(self):
        '''
        Getter for the players attribute.
        '''
        return self.__players

    def get_player(self, player_num):
        '''
        Returns a single player name from the players dictionary.
        '''
        return self.__players[player_num]
