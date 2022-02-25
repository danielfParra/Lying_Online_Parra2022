from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Daniel Parra'

doc = """
Consent
"""


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(label = '''I have read the data protection
    information and I consent to participation in the experiment and the stated
    processing of data:''',
    choices = [[0, 'No'], [1, 'Yes']])

    consent2 = models.IntegerField(label = '''Can you be in front of the screen for the 
    next 15 minutes?''',
    choices = [[0, 'No'], [1, 'Yes']])
