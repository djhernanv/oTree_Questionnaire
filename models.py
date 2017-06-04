from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Hernan Villamizar'

doc = """
Questionnaire for Skill and Fairness
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    luck = models.PositiveIntegerField(
        choices=[
            [1, 'Not at all'],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, ''],
            [8, ''],
            [9, ''],
            [10, ''],
        ],
        # horizontal radio button instead of selection
        widget=widgets.RadioSelectHorizontal()
    )
    skill = models.PositiveIntegerField(
        choices=[
            [1, '1'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10'],
        ],
        # horizontal radio button instead of selection
        widget=widgets.RadioSelectHorizontal()
    )
    ave = models.PositiveIntegerField()
    bestB = models.PositiveIntegerField()
    bestA = models.PositiveIntegerField()
