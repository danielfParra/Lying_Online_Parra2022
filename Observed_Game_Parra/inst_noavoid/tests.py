from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        if self.participant.vars['treat'] == 'noavoid':
            yield pages.Inst2_noavoid
            yield SubmissionMustFail(pages.Q_noavoid, dict(q1_noavoid=1,q2_noavoid=1,q3_noavoid=1,q4_noavoid=1,q5_noavoid=2))
            yield pages.Q_noavoid, dict(q1_noavoid=4, q2_noavoid=4, q3_noavoid=1, q4_noavoid=4, q5_noavoid=1)