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
Avoiding the cost of lying - No Avoidance
"""


class Constants(BaseConstants):
    name_in_url = 'exp_tnoav'
    players_per_group = 2
    num_rounds = 1

    payoff_win = c(4)
    payoff_lose = c(0.5)
    completion_fee = c(2.5)
    beliefs_payoff = c(0.5)

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
            [False, 'Black'],
            [True, 'Orange'],
        ],
        widget=widgets.RadioSelect,
        label="The color behind the card I picked was:"

        # only for p2
    )
    report2 = models.BooleanField(
        choices=[
            [False, 'Black'],
            [True, 'Orange'],
        ],
        widget=widgets.RadioSelect,
        label="The color behind the card I picked was:"
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
                use_my_guess = True
            else:
                use_my_guess = False

            if use_my_guess and p1.guess_p1 == self.report2:
                p1.guess_payoff = Constants.beliefs_payoff
            elif  not use_my_guess and p1.random_num <= p1.robot:
                p1.guess_payoff = Constants.beliefs_payoff
            else:
                p1.guess_payoff = 0

            if self.report1:  # It means if report1 == true, I could write if not report1
                p1.payoff = p1.not_a_bot*(Constants.payoff_win + p1.guess_payoff)
            elif self.report2:
                p1.payoff = p1.not_a_bot*(Constants.payoff_win + p1.guess_payoff)
            else:
                p1.payoff = p1.not_a_bot*(Constants.payoff_lose + p1.guess_payoff)

            if self.report1:
                p2.payoff = p2.not_a_bot*(Constants.payoff_win)
            elif self.report2:
                p2.payoff = p2.not_a_bot*(Constants.payoff_win)
            else:
                p2.payoff = p2.not_a_bot*(Constants.payoff_lose)



class Player(BasePlayer):
    def waiting_too_long(self):
        print('in group_by_arrival_time_method')
        import time
        return time.time() - self.participant.vars['wait_page_before_matching'] > 6 * 60

# For beliefs elicitation, p1 choose this
    guess_p1 = models.BooleanField(
        choices=[
            [False, 'Black'],
            [True, 'Orange'],
        ],
        widget=widgets.RadioSelect,
        label="I think that the computer reported that Participant B picked a card with the following color:"
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




