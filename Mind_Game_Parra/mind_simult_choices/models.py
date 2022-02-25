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
Mind Game- Simultaneous
"""


class Constants(BaseConstants):
    name_in_url = 'exp_tsimul'
    players_per_group = 2
    num_rounds = 1

    payoff_win = c(2.5)
    payoff_lose = c(0.3)
    completion_fee = c(1.15)
    beliefs_payoff = c(0.3)

class Subsession(BaseSubsession):
    def group_by_arrival_time_method(self, waiting_players):
        if len(waiting_players) >= 2:
            return waiting_players[:2]
        for p in waiting_players:
            if p.waiting_too_long():
                # [p] means a single-player group.
                return [p]

class Group(BaseGroup):
    # only for p1
    report1 = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect,
        label="Please indicate whether the color behind the card you picked is the color that you thought of:"

        # only for p2
    )
    report2 = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect,
        label="Please indicate whether the color behind the card you picked is the color that you thought of:"
    )

    randomDraw1 = models.IntegerField()
    randomDraw2 = models.IntegerField()
    p1_is_a_human = models.IntegerField()
    p2_is_a_human = models.IntegerField()

    # Calculating payoffs

    def set_payoffs(self):
        players = self.get_players()
        print('players in group', players)
        num_players_in_group = len(players)
        print('number of players', num_players_in_group)

        p1 = self.get_player_by_id(1)

        if num_players_in_group == 2:
            self.p1_is_a_human = self.get_player_by_id(1).not_a_bot
            self.p2_is_a_human = self.get_player_by_id(2).not_a_bot
        else:
            self.p1_is_a_human = self.get_player_by_id(1).not_a_bot

        if num_players_in_group == 1 or self.p2_is_a_human == 0:
            p1.payoff = Constants.payoff_win + Constants.beliefs_payoff
        elif self.p1_is_a_human == 0:
            self.get_player_by_id(2).payoff = Constants.payoff_win + Constants.beliefs_payoff
        else:
            p2 = self.get_player_by_id(2)

            if p1.confidence_guess > p1.robot:
                use_my_guess_p1 = True
            else:
                use_my_guess_p1 = False

            if p2.confidence_guess > p2.robot:
                use_my_guess_p2 = True
            else:
                use_my_guess_p2 = False

            if use_my_guess_p1 and p1.guess_p1 == self.report2:
                p1.guess_payoff = Constants.beliefs_payoff
            elif not use_my_guess_p1 and p1.random_num <= p1.robot:
                p1.guess_payoff = Constants.beliefs_payoff
            else:
                p1.guess_payoff = 0

            if use_my_guess_p2 and p2.guess_p1 == self.report1:
                p2.guess_payoff = Constants.beliefs_payoff
            elif not use_my_guess_p2 and p2.random_num <= p2.robot:
                p2.guess_payoff = Constants.beliefs_payoff
            else:
                p2.guess_payoff = 0

            if self.report1:  # It means if report1 == true, I could write if not report1
                p1.payoff = p1.not_a_bot*(Constants.payoff_win + p1.guess_payoff)
            elif self.report2:
                p1.payoff = p1.not_a_bot*(Constants.payoff_win + p1.guess_payoff)
            else:
                p1.payoff = p1.not_a_bot*(Constants.payoff_lose + p1.guess_payoff)

            if self.report1:
                p2.payoff = p2.not_a_bot*(Constants.payoff_win + p2.guess_payoff)
            elif self.report2:
                p2.payoff = p2.not_a_bot*(Constants.payoff_win + p2.guess_payoff)
            else:
                p2.payoff = p2.not_a_bot*(Constants.payoff_lose + p2.guess_payoff)


class Player(BasePlayer):
    def waiting_too_long(self):
        print('in group_by_arrival_time_method')
        import time
        return time.time() - self.participant.vars['wait_page_before_matching'] > 6 * 60

# For beliefs elicitation, p1 and p2 choose this. Then it will store for both in this treatment
    guess_p1 = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect,
        label="When Participant B was asked whether the color she/he picked is the color she/he thought of, I think Participant B reported:"
    )

    confidence_guess = models.IntegerField(min=0, max=100,
            label="I think the chance that my answer is correct is (write a number between 0 and 100):"
    )


# Gets whether a player clicked in more information
    times_clicked_info = models.StringField(blank = True)

# For beliefs elicitation, needed for compute payoffs

    robot = models.IntegerField()
    guess_payoff = models.CurrencyField()
    random_num = models.IntegerField()
    not_a_bot = models.IntegerField()
    players_in_group = models.IntegerField()


