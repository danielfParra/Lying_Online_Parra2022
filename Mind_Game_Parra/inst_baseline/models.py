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


author = 'Daniel Parra '

doc = """
Instructions - Baseline
"""


class Constants(BaseConstants):
    name_in_url = 'inst_t0b'
    players_per_group = None
    num_rounds = 1

    payoff_win = c(2.5)
    payoff_lose = c(0.3)
    completion_fee = c(1.15)
    beliefs_payoff = c(0.3)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1_bas = models.IntegerField(
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

    def q1_bas_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if any of you reports \"Yes\", then both would get {}.'.format(Constants.payoff_win)

    q2_bas = models.IntegerField(
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

    def q2_bas_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if any of you reports \"Yes\", then both would get {}.'.format(Constants.payoff_win)

    q3_bas = models.IntegerField(
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

    def q3_bas_error_message(self, value):
        print('value is', value)
        if not value == 1:
            return 'Recall: if both participants report \"No\", then both would get {}.'.format(
                Constants.payoff_lose)

    q4_bas = models.IntegerField(
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

    def q4_bas_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if both participants report \"Yes\", then both would get {}.'.format(
                Constants.payoff_win)

    q5_bas = models.IntegerField(
        choices=[
            [1, 'Before Participant B reports whether his or her card colors match.'],
            [2, 'After Participant B reports whether his or her card colors match.'],
        ],
        widget=widgets.RadioSelect,
    )

    def q5_bas_error_message(self, value):
        print('value is', value)
        if not value == 1:
            return 'Recall: Participant A\'s report is seen by Participant B before reporting whether their colors ' \
                   'match. '
