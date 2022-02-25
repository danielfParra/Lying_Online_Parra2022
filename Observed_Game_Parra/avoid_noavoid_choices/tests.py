from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        random_d1 = random.choice([0,0,0,0,1])
        random_d2 = random.choice([0,0,0,0,1])
        random_r1 = random.choice([True, True, False])


        if self.participant.vars['treat'] == 'noavoid':
            if self.player.id_in_group == 1:
                yield pages.R1_draw, dict(randomDraw1=random_d1)
                yield pages.R1_Choice, dict(report1=random_r1)
                yield pages.Inst_guess
                yield SubmissionMustFail(pages.guess, dict(guess_p1=True, confidence_guess=101))
                yield pages.guess, dict(guess_p1=True, confidence_guess=50)
                yield pages.Results
            else:
                yield pages.R2_draw, dict(randomDraw2=random_d2)
                yield pages.R2_Choice
                yield pages.Results

        print('I have a profit of', self.player.payoff)
