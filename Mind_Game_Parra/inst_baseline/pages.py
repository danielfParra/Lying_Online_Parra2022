from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Inst2_bas(Page):
    pass

class Q_bas(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['q1_bas', 'q2_bas', 'q3_bas', 'q4_bas', 'q5_bas']

    def before_next_page(self):
        import time
        self.participant.vars['wait_page_before_matching'] = time.time()
        print('time now is', self.participant.vars['wait_page_before_matching'])

    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        return "mind_baseline_choices"

page_sequence = [Inst2_bas,
                 Q_bas,
]
