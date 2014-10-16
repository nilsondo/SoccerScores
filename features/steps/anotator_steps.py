# -- FILE: features/steps/anotator_steps.py
from behave import given, when, then, step
from src.model.annotator import Annotator
from src.controller.annotator import AnnotatorController
from src.model.match import Match
from src.model.team import Team
from src.model.play import Play


@given('we want to create a new game')
def step_impl(context):
    model = Annotator.create()
    ctrl = AnnotatorController()
    ctrl.model = model
    context.ctrl = ctrl
    context.model = model


@when('{home} is home and {away} is away')
def step_impl(context, home, away):
    home = str(home)
    away = str(away)
    assert len(home) > 0
    assert len(away) > 0
    team_home = Team(home)
    team_away = Team(away)
    match = Match(team_home, team_away)
    context.match_mid = match.mid
    context.ctrl.add_match(match)


@then('a new game with home {home} and away {away} is created')
def step_impl(context, home, away):
    assert context.model.get_match(context.match_mid) is not None


@given('we want to view a game')
def step_impl(context):
    pass


@when('we have a mid {mid}')
def step_impl(context, mid):
    context.execute_steps(u'''
        Given we want to create a new game
        When Dallas is home and NewYork is away
    ''')
    match = context.ctrl.get_match(str(mid))
    context.view_match = match


@then('an instance of the game must be returned')
def step_impl(context):
    assert context.view_match is not None


@given('we want to remove a game')
def step_impl(context):
    pass


@when('having mid {mid}')
def step_impl(context, mid):
    context.execute_steps(u'''
        Given we want to create a new game
        When Dallas is home and NewYork is away
    ''')
    context.ctrl.remove_match(str(mid))


@then('the instance of the game must be removed')
def step_impl(context):
    assert context.ctrl.get_match(context.match_mid) is None


@given('we want to start a game')
def step_impl(context):
    pass


@when('we got a mid {mid}')
def step_impl(context, mid):
    context.execute_steps(u'''
        Given we want to create a new game
        When Dallas is home and NewYork is away
    ''')
    is_started = context.ctrl.get_match(str(mid)).start_match()
    context.is_startedMatch = is_started


@then('the game related should have started')
def step_impl(context):
    assert context.is_startedMatch is True


@given('we want to finish a game')
def step_impl(context):
    pass


@when('got a mid {mid}')
def step_impl(context, mid):
    context.execute_steps(u'''
        Given we want to start a game
        When we got a mid DALVSNEW15
    ''')
    is_finished = context.ctrl.get_match(str(mid)).finish_match()
    context.is_finishedMatch = is_finished


@then('the game related should have finished')
def step_impl(context):
    assert context.is_finishedMatch is True


@given('add a play minute {mins:d} type {ptype:d} spec {spec:d} team {team} and description {desc}')
def step_impl(context, mins, ptype, spec, team, desc):
    context.play_min = mins
    context.play_type = ptype
    context.play_spec = spec
    context.play_team = str(team)
    context.play_desc = str(desc)
    pass


@when('we add all these plays to the match {mid}')
def step_impl(context, mid):
    model = Annotator.create()
    ctrl = AnnotatorController()
    ctrl.model = model
    context.ctrl = ctrl
    context.model = model
    team_home = Team('Dallas')
    team_away = Team('NewYork')
    match = Match(team_home, team_away)
    ctrl.add_match(match)
    ctrl.get_match(str(mid)).start_match()
    if context.play_team == 'home':
        team = team_home
    else:
        team = team_away
    play = Play(ptype=context.play_type, spec=context.play_spec, team=team,
                descrip=context.play_desc, time=context.play_min)
    ctrl.get_match(str(mid)).add_play(play)


@then('all these plays should have been added')
def step_impl(context):
    assert context.failed is False


@given('we want to save the state')
def step_impl(context):
    model = Annotator.create()
    ctrl = AnnotatorController()
    ctrl.model = model
    context.ctrl = ctrl
    context.model = model


@when('we have a model')
def step_impl(context):
    context.ctrl.save()


@then('the model is saved')
def step_impl(context):
    context.model = None
    context.model = Annotator.load()
    assert isinstance(context.model, Annotator)
