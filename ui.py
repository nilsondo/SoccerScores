import os
import sys


# global flag to stop TUI work flow
flag = True


def template(title, options=None, descrp=None, header=True, footer=True):
    '''
    Prints a TUI template to select options, view matches.
    title -> str
    options -> dict
    '''

    up = "*" + '=' * 32 + 'Soccer Scores' + '=' * 32 + "*"
    down = "*" + '=' * 77 + "*"
    mid = '*' + '-' * 77 + '*'
    blanc = '|' + ' ' * 77 + '|'

    if header:
        print up

    print mid
    prt_opt(title + ":")
    print mid

    if descrp:
        prt_opt(descrp)
        print mid

    if options:
        for num, opt in sorted(options.items()):
            prt_opt(str(num) + ' - ' + opt)

    print blanc

    if footer:
        print down


def prt_opt(option):
    '''
    Prints options given a string.
    '''
    print '|' + option.center(77) + '|'


def view_annotator():
    '''
    Main function for TUI.
    '''
    from soccerscores.access.annotator import Annotator
    from soccerscores.core.match import Match
    from soccerscores.core.team import Team

    global flag
    annotator = Annotator.create()

    options = {1: 'View matches', 2: 'Create new match', 0: 'Exit'}

    while(flag):
        sys.stdin.flush()
        os.system('cls' if os.name == 'nt' else 'clear')

        template('OPTIONS', options)

        try:
            opt = int(raw_input('Option: '))

            if opt in options:
                if opt == 0:
                    flag = False
                elif opt == 1:
                    view_matches(annotator)
                elif opt == 2:
                    home = Team(name=str(raw_input('Home team name: ')))
                    away = Team(name=str(raw_input('Away team name: ')))

                    match = Match(home=home, away=away)

                    annotator.add_match(match)
            else:
                print 'Unknown option, press ENTER to continue...'
                sys.stdin.read(1)
        except:
            print 'Unknown option, press ENTER to continue...'
            sys.stdin.read(1)


def view_matches(annotator):
    from soccerscores.core.play import Play

    global flag
    options = {1: 'Return to main options', 0: 'Exit', 2: 'View Match',
               3: 'Remove Match'}

    while(flag):
        str_matches = {}
        for mid, match in sorted(annotator.matches.items()):
            str_matches[mid] = match.display()

        sys.stdin.flush()
        os.system('cls' if os.name == 'nt' else 'clear')

        template('MATCHES', options=str_matches, footer=False,
                 descrp='ID - DESCRIPTION:')
        template('MATCHES OPTIONS', options, header=False)

        try:
            opt = int(raw_input('Option: '))

            if opt in options:
                if opt == 0:
                    flag = False
                    return
                elif opt == 1:
                    return
                elif opt == 2:
                    mid = str(raw_input('Match ID: ')).upper()
                    match = annotator.get_match(mid)

                    if match:
                        view_match(match)
                    else:
                        print 'Unknown ID, press ENTER to continue...'
                        sys.stdin.read(1)
                elif opt == 3:
                    mid = str(raw_input('Match ID: ')).upper()
                    match = annotator.get_match(mid)

                    if match:
                        annotator.remove_match(match)
                        print match.mid + ' deleted'
                        sys.stdin.read(1)
                    else:
                        print 'Unknown ID, press ENTER to continue...'
                        sys.stdin.read(1)
            else:
                print 'Unknown option, press ENTER to continue...'
                sys.stdin.read(1)
        except:
            print 'Unknown option, press ENTER to continue...'
            sys.stdin.read(1)


def view_match(match):
    from soccerscores.core.play import Play

    global flag
    options = {1: 'Return to matches options', 0: 'Exit',
               3: 'Start match', 4: 'Finish match', 5: 'Add play'}

    while(flag):
        sys.stdin.flush()
        os.system('cls' if os.name == 'nt' else 'clear')

        template(match.display().upper(), footer=False)
        template('PLAYS', {}, header=False, footer=False)
        template('MATCH OPTIONS', options, header=False)

        try:
            opt = int(raw_input('Option: '))

            if opt in options:
                if opt == 0:
                    flag = False
                    return
                elif opt == 1:
                    return
                elif opt == 2:
                    pass
                elif opt == 3:
                    if match.start_match():
                        print 'Match started'
                        sys.stdin.read(1)
                elif opt == 4:
                    if match.finish_match():
                        print 'Match finished'
                        sys.stdin.read(1)
                elif opt == 5:
                    pass
            else:
                print 'Unknown option, press ENTER to continue...'
                sys.stdin.read(1)
        except:
            print 'Unknown option, press ENTER to continue...'
            sys.stdin.read(1)

view_annotator()
