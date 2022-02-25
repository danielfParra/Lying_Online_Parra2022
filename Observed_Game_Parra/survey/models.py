from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Demographics
    age = models.IntegerField(label='Age', min=13, max=125)

    gender = models.IntegerField(
        label='Gender',
        choices=[[0, 'Male'], [1, 'Female'], [2, 'Rather not say'], [3, 'Other']]
    )
    gender_add = models.StringField(blank=True, label='')
    education = models.IntegerField(
        choices=[[0, 'Less than High School'],
                 [1, 'High School'],
                 [2, 'Some College'],
                 [3, 'Associate Degree'],
                 [4, 'Bachelor\'s Degree'],
                 [5, 'Advanced or Professional Degree']
                 ],
        label='What is your highest level of education?'
    )
    student = models.IntegerField(
        label='Are you currently enrolled in college?',
        choices=[[0, 'No'], [1, 'Yes']]
    )
    experiments = models.IntegerField(
        label='Please give a rough estimate about the number of experiments you have participated in before',
        blank=True
    )

    reasoning = models.LongStringField(
        label='Please give a concise explanation of how you took your decisions in the experiment',
        blank=True
    )

    charity_PG = models.IntegerField(
        label='From the four organizations, which one do you think provides a better service for people living in the UK?',
        choices=[[1, 'Keep Britain Tidy'], [2, 'RNLI Lifeboats'], [3, 'British Red Cross'], [4, 'National Trust']],
        widget=widgets.RadioSelect
    )


    charity_taxes = models.IntegerField(
        label='If you had to vote for one of the four organizations to receive government funding (i.e. from taxes), which one would you vote for?',
        choices=[[1, 'Keep Britain Tidy'], [2, 'RNLI Lifeboats'], [3, 'British Red Cross'], [4, 'National Trust']],
        widget=widgets.RadioSelect
    )

