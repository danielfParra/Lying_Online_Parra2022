from otree.api import Currency as c, currency_range, expect

from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Demographics, dict(age=24, gender=0, education=3, student=1, experiments=2, chosen_role=1, religion=0)


