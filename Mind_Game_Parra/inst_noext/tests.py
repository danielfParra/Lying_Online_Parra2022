from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        if self.participant.vars['treat'] == 'noext':
            yield pages.Inst2_noext
            yield SubmissionMustFail(pages.Q_noext, dict(q1_noext=1,q2_noext=1,q3_noext=1,q4_noext=1,q5_noext=2))
            yield pages.Q_noext, dict(q1_noext=4, q2_noext=3, q3_noext=1, q4_noext=4, q5_noext=1)