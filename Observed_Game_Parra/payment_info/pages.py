from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class PaymentInfo(Page):

    def vars_for_template(self):
        payoff = self.participant.payoff
        Prolific_fixed_payoff = Constants.completion_fee
        not_a_bot = self.participant.vars['not_a_bot']
        return dict(
            payoff=payoff,
            Prolific_fixed_payoff = Prolific_fixed_payoff,
            not_a_bot = not_a_bot,
        )

class RedirectProlific(Page):
    pass


page_sequence = [PaymentInfo,
                 RedirectProlific]
