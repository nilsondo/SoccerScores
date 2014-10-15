import os
import sys


class AnnotatorView():

    '''
    Annotator view class.
    '''

    def __init__(self):
        '''
        Constructor
        '''

        self.__ctrl = None

        # flag to stop TUI work flow
        self.__flag = True
        self.__enter_msg = 'press ENTER to continue...'

        self.__str_matches = {}
        self.__str_match = ''
        self.__str_plays = {}
        self.__str_ptype = ''
        self.__str_spec = ''

    @property
    def ctrl(self):
        '''
        Getter for the controller attribute.
        '''
        return self.__ctrl

    @ctrl.setter
    def ctrl(self, value):
        '''
        Setter for the controller attribute.
        '''
        self.__ctrl = value

    def on_anotator_change(self, str_matches):
        '''
        Update view information for the annotator view.
        '''
        self.__str_matches = str_matches

    def on_match_change(self, str_match, str_plays):
        '''
        Update view information for the match view.
        '''
        self.__str_match = str_match
        self.__str_plays = str_plays

    def __prt_opt(self, option):
        '''
        Prints options given a string.
        '''
        print '|' + option.center(77) + '|'

    def __template(self, title, options=None,
                   descrp=None, header=True, footer=True):
        '''
        Prints a TUI template to select options, view matches.
        '''

        up = "*" + '=' * 32 + 'Soccer Scores' + '=' * 32 + "*"
        down = "*" + '=' * 77 + "*"
        mid = '*' + '-' * 77 + '*'
        blanc = '|' + ' ' * 77 + '|'

        if header:
            print up

        print mid
        self.__prt_opt(title)
        print mid

        if descrp:
            self.__prt_opt(descrp)
            print mid

        if options:
            for num, opt in sorted(options.items()):
                self.__prt_opt(str(num) + ' - ' + opt)

        print blanc

        if footer:
            print down

    def __match_view(self, match):
        '''
        Match view.
        '''
        from src.model.play import Play

        options = {0: 'Exit', 1: 'Return to annotator options',
                   2: 'Start match', 3: 'Finish match', 4: 'Add play'}

        while(self.__flag):
            sys.stdin.flush()
            os.system('cls' if os.name == 'nt' else 'clear')

            self.__template(title=self.__str_match.upper(), footer=False)
            self.__template(title='PLAYS', options=self.__str_plays,
                            header=False, footer=False)
            self.__template(title='MATCH OPTIONS', options=options,
                            header=False)

            try:
                opt = int(raw_input('Option: '))
                if opt in options:
                    if opt == 0:
                        self.__flag = False
                        return
                    elif opt == 1:
                        self.ctrl.remove_match_view(match, self)
                        return
                    elif opt == 2:
                        if self.ctrl.start_match(match):
                            print 'Match started'
                            sys.stdin.read(1)
                    elif opt == 3:
                        if self.ctrl.finish_match(match):
                            print 'Match finished'
                            sys.stdin.read(1)
                    elif opt == 4:
                        if self.ctrl.match_started(match):
                            try:
                                time = int(raw_input("Play time [MIN]: "))
                                ptype = int(raw_input("Play type [OPTIONS]:\n"
                                                      + self.__str_ptype))
                                spec = int(raw_input("Play spec [OPTIONS]:\n"
                                                     + self.__str_spec))
                                team = str(
                                    raw_input("Play team [home/away]: ")
                                ).lower()

                                descrip = str(
                                    raw_input("Play description: ")
                                ).lower()

                                if team == match.defined_teams[1]:
                                    team = match.home
                                elif team == match.defined_teams[2]:
                                    team = match.away

                                play = Play(time=time, ptype=ptype, spec=spec,
                                            team=team, descrip=descrip)

                                self.ctrl.add_play(match, play)

                            except:
                                print ('Invalid play argument(s), ' +
                                       self.__enter_msg)
                                sys.stdin.read(1)
                        else:
                            print ('Match is not started or has finished, ' +
                                   self.__enter_msg)
                            sys.stdin.read(1)
                else:
                    print ('Unknown option, '
                           + self.__enter_msg)
                    sys.stdin.read(1)
            except:
                print ('Unknown option, '
                       + self.__enter_msg)
                sys.stdin.read(1)

    def annotator_view(self):
        '''
        Annotator view.
        '''
        from src.model.match import Match
        from src.model.team import Team

        options = {0: 'Exit', 1: 'Create new match', 2: 'View Match',
                   3: 'Remove Match'}

        while(self.__flag):
            sys.stdin.flush()
            os.system('cls' if os.name == 'nt' else 'clear')

            self.__template(title='MATCHES', options=self.__str_matches,
                            footer=False, descrp='ID - DESCRIPTION:')
            self.__template(title='OPTIONS', options=options, header=False)

            try:
                opt = int(raw_input('OPTION: '))

                if opt in options:
                    if opt == 0:
                        self.__flag = False
                    elif opt == 1:
                        home = str(raw_input('Home team name: '))
                        away = str(raw_input('Away team name: '))

                        home = Team(name=home)
                        away = Team(name=away)

                        match = Match(home=home, away=away)

                        self.ctrl.add_match(match)

                    elif opt == 2:
                        mid = str(raw_input('Match ID: ')).upper()
                        match = self.ctrl.get_match(mid, self)

                        if match:
                            self.__match_view(match)
                        else:
                            print 'Unknown ID, ' + self.__enter_msg
                            sys.stdin.read(1)

                    elif opt == 3:
                        mid = str(raw_input('Match ID: ')).upper()

                        if self.ctrl.remove_match(mid):
                            print (mid + ' deleted, ' + self.__enter_msg)
                            sys.stdin.read(1)
                        else:
                            print ('Unknown ID, ' + self.__enter_msg)
                            sys.stdin.read(1)
                else:
                    print ('Unknown option, ' + self.__enter_msg)
                    sys.stdin.read(1)
            except:
                print ('Unknown option, ' + self.__enter_msg)
                sys.stdin.read(1)
