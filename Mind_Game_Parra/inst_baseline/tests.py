from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        if self.participant.vars['treat'] == 'baseline':
            yield pages.Inst2_bas
            yield SubmissionMustFail(pages.Q_bas, dict(q1_bas=1,q2_bas=1,q3_bas=1,q4_bas=1,q5_bas=2))
            yield pages.Q_bas, dict(q1_bas=4, q2_bas=4, q3_bas=1, q4_bas=4, q5_bas=1)