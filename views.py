from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class questionnaire(Page):
    form_model = models.Player
    form_fields = ['luck', 'skill']

class Results(Page):
    pass


page_sequence = [
    questionnaire
]
