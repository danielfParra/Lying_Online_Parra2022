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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'inst_tnoex'
    players_per_group = None
    num_rounds = 1

    payoff_win = c(2.5)
    payoff_lose = c(0.3)
    completion_fee = c(1.15)
    beliefs_payoff = c(0.3)

    treatments = ['baseline', 'noavoid', 'noext']
    player_roles = [1, 2]
    stages = [1, 2]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1_noext = models.IntegerField(
        choices=[
            [1, 'Both would get {}.'.format(Constants.payoff_lose)],
            [2, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_lose,
                                                                                    Constants.payoff_win)],
            [3, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_win,
                                                                                    Constants.payoff_lose)],
            [4, 'Both would get {}.'.format(Constants.payoff_win)]
        ],
        widget=widgets.RadioSelect,
    )

    def q1_noext_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if the computer reports \"Yes\", then both would get {}.'.format(Constants.payoff_win)

    q2_noext= models.IntegerField(
        choices=[
            [1, 'Both would get {}.'.format(Constants.payoff_lose)],
            [2, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_lose,
                                                                                    Constants.payoff_win)],
            [3, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_win,
                                                                                    Constants.payoff_lose)],
            [4, 'Both would get {}.'.format(Constants.payoff_win)]
        ],
        widget=widgets.RadioSelect,
    )

    def q2_noext_error_message(self, value):
        print('value is', value)
        if not value == 3:
            return 'Recall: Participant B earnings depend only on the computer\'s report.'.format(Constants.payoff_win)

    q3_noext = models.IntegerField(
        choices=[
            [1, 'Both would get {}.'.format(Constants.payoff_lose)],
            [2, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_lose,
                                                                                    Constants.payoff_win)],
            [3, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_win,
                                                                                    Constants.payoff_lose)],
            [4, 'Both would get {}.'.format(Constants.payoff_win)]
        ],
        widget=widgets.RadioSelect,
    )

    def q3_noext_error_message(self, value):
        print('value is', value)
        if not value == 1:
            return 'Recall: if both, Participant A and the computer, report \"No\", then both would get {}.'.format(
                Constants.payoff_lose)

    q4_noext = models.IntegerField(
        choices=[
            [1, 'Both would get {}.'.format(Constants.payoff_lose)],
            [2, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_lose,
                                                                                    Constants.payoff_win)],
            [3, 'Participant A would get {} and Participant B would get {}.'.format(Constants.payoff_win,
                                                                                    Constants.payoff_lose)],
            [4, 'Both would get {}.'.format(Constants.payoff_win)]
        ],
        widget=widgets.RadioSelect,
    )

    def q4_noext_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if both, Participant A and the computer, report \"Yes\", then both would get {}.'.format(
                Constants.payoff_win)

    q5_noext = models.IntegerField(
        choices=[
            [1, 'True'],
            [2, 'False'],
        ],
        widget=widgets.RadioSelect,
    )

    def q5_noext_error_message(self, value):
        print('value is', value)
        if not value == 1:
            return 'Recall: The computer knows the color chosen and the color picked by Participant B. Then, ' \
                   'it reports whether the chosen color and the drawn color by Participant B match using this ' \
                   'information. '
