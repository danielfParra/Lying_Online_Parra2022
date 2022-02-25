from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Inst2_noavoid(Page):
    pass

class Q_noavoid(Page):
    form_model = 'player'

    def get_form_fields(self):
        return ['q1_noavoid', 'q2_noavoid', 'q3_noavoid', 'q4_noavoid', 'q5_noavoid']

    def before_next_page(self):
        import time
        self.participant.vars['wait_page_before_matching'] = time.time()
        print('time now is', self.participant.vars['wait_page_before_matching'])

    def app_after_this_page(self, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        return "mind_noavoid_choices"

page_sequence = [Inst2_noavoid,
                 Q_noavoid,
]
