from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Inst2_simult(Page):
    pass

class Q_simult(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['q1_simult', 'q2_simult', 'q3_simult', 'q4_simult', 'q5_simult']

    def before_next_page(self):
        import time
        self.participant.vars['wait_page_before_matching'] = time.time()
        print('time now is', self.participant.vars['wait_page_before_matching'])

    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        return "avoid_simult_choices"

page_sequence = [Inst2_simult,
                 Q_simult,
]
