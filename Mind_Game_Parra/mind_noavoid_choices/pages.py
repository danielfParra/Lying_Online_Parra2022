from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Matching(WaitPage):
    group_by_arrival_time = True


class pick_colorA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):

        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
        print(self.player.waiting_too_long())

class R1_draw(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'group'

    def get_form_fields(self):
        return ['randomDraw1']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60


    def before_next_page(self):

        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True

        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

class R1_Choice(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'group'
    form_fields = ['report1']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.report1 = False
        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

class WaitForP1(WaitPage):
    pass

class Inst_guess(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['times_clicked_info']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 6*60

    def before_next_page(self):
        import random
        self.player.robot = random.randint(1, 100)
        self.player.random_num = random.randint(1, 100)

        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

class guess(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'

    def get_form_fields(self):
        return ['guess_p1', 'confidence_guess']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.guess_p1 = 1
            self.player.confidence_guess = 1
        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

        self.player.players_in_group = len(self.player.get_others_in_group()) + 1

class pick_colorB(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'

    def get_form_fields(self):
        return ['selected_card_p2']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True

class R2_draw(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'

    def get_form_fields(self):
        return ['randomDraw2']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):

        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.randomDraw2 = 0

        if self.group.randomDraw2 == self.group.selected_card_p2:
            self.group.report2 = True
        else:
            self.group.report2 = False

        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

class R2_Choice(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5*60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        return "survey"

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):
        self.player.players_in_group = len(self.player.get_others_in_group()) + 1

        if self.player.players_in_group==2:
            self.group.p1_is_a_human = self.group.get_player_by_id(1).not_a_bot
            self.group.p2_is_a_human = self.group.get_player_by_id(2).not_a_bot
        else:
            self.group.p1_is_a_human = self.group.get_player_by_id(1).not_a_bot

        self.participant.vars['report1'] = self.group.get_report1_display
        self.participant.vars['report2'] = self.group.get_report2_display
        self.participant.vars['randomDraw1'] = self.group.randomDraw1
        self.participant.vars['randomDraw2'] = self.group.randomDraw2
        self.participant.vars['guess_payoff'] = self.player.guess_payoff
        self.participant.vars['payoff'] = self.player.payoff
        self.participant.vars['player_id'] = self.player.id_in_group
        self.participant.vars['not_a_bot'] = self.player.not_a_bot
        self.participant.vars['players_in_group'] = self.player.players_in_group

page_sequence = [
    Matching,
    pick_colorA,
    R1_draw,
    R1_Choice,
    WaitForP1,
    Inst_guess,
    guess,
    pick_colorB,
    R2_draw,
    R2_Choice,
    ResultsWaitPage,
    Results,
]
