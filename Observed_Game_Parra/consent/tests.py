from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield SubmissionMustFail(pages.Consent, dict(consent=0))
        yield pages.Consent, dict(consent=1)
        yield SubmissionMustFail(pages.Consent2, dict(consent2=0))
        yield pages.Consent2, dict(consent2=1)
