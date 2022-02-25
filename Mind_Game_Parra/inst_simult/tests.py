from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        if self.participant.vars['treat'] == 'simult':
            yield pages.Inst2_simult
            yield SubmissionMustFail(pages.Q_simult, dict(q1_simult=1,q2_simult=1,q3_simult=1,q4_simult=1,q5_simult=2))
            yield pages.Q_simult, dict(q1_simult=4, q2_simult=4, q3_simult=1, q4_simult=4, q5_simult=2)