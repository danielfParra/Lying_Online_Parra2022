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
Instructions - Simultaneous
"""

class Constants(BaseConstants):
    name_in_url = 'inst_tsim'
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

    q1_simult = models.IntegerField(
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

    def q1_simult_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if any of you reports \"Yes\", then both would get {}.'.format(Constants.payoff_win)

    q2_simult = models.IntegerField(
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

    def q2_simult_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if any of you reports \"Yes\", then both would get {}.'.format(Constants.payoff_win)

    q3_simult = models.IntegerField(
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

    def q3_simult_error_message(self, value):
        print('value is', value)
        if not value == 1:
            return 'Recall: if both participants report \"No\", then both would get {}.'.format(
                Constants.payoff_lose)

    q4_simult = models.IntegerField(
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

    def q4_simult_error_message(self, value):
        print('value is', value)
        if not value == 4:
            return 'Recall: if both participants report \"Yes\", then both would get {}.'.format(
                Constants.payoff_win)

    q5_simult = models.IntegerField(
        choices=[
            [1, 'Before Participant B reports her or his own card’s color.'],
            [2, 'After Participant B reports her or his own card’s color.'],
        ],
        widget=widgets.RadioSelect,
    )

    def q5_simult_error_message(self, value):
        print('value is', value)
        if not value == 2:
            return 'Recall: Participants learn the report of the other at the end of the experiment.'
