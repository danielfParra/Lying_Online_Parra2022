from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    def consent_error_message(self, value):
        if value != 1:
            return '''If you do not agree, you cannot participate in today\'s
            experiment. In this case, you can close the window and contact the
            experimenters.'''

class Consent2(Page):
    form_model = 'player'
    form_fields = ['consent2']

    def consent2_error_message(self, value):
        if value != 1:
            return '''If you do not have the time now, you cannot participate in today\'s
            experiment. In this case, you can close the window and contact the
            experimenters.'''


page_sequence = [Consent, Consent2]
