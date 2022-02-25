from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)


SESSION_CONFIGS = [
   dict(
       name='Avoidance_MAIN',
       app_sequence=['consent', 'welcome', 'inst_baseline', 'inst_simult', 'inst_noavoid', 'inst_noext',
                     'avoid_baseline_choices', 'avoid_noavoid_choices', 'avoid_noext_choices', 'avoid_simult_choices',
                     'survey', 'payment_info'],
       num_demo_participants=8,

    ),
    dict(
        name='Bots_Avoidance_Main',
        app_sequence=['consent', 'welcome', 'inst_baseline','inst_simult', 'inst_noavoid','inst_noext',
                      'avoid_baseline_choices', 'avoid_noavoid_choices', 'avoid_noext_choices', 'avoid_simult_choices', 'survey','payment_info'],
        num_demo_participants=8,
        use_browser_bots=True,
    ),
   dict(
        name='testing',
        app_sequence=['welcome','inst_baseline', 'avoid_baseline_choices', 'survey', 'payment_info'],
        num_demo_participants=4,
   )
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='test_avoid',
        display_name='Test Avoid',
    ),
    dict(
        name='s1',
        display_name='S1_21dec',
    ),
    dict(
        name='s2',
        display_name='S2_21dec',
    ),
    dict(
        name='s3',
        display_name='S3_21dec',
    ),
    dict(
        name='s4',
        display_name='S4_21dec',
    ),
    dict(
        name='s5',
        display_name='S5_21dec',
    )
]

ADMIN_USERNAME = 'daniel'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '_0@1s^4rtuh=yev^agvo66(*ubf&i)1(u$2^0do#fjw&h6nxln'

INSTALLED_APPS = ['otree']

# inactive session configs
# dict(name='trust', display_name="Trust Game", num_demo_participants=2, app_sequence=['trust', 'payment_info']),
# dict(name='prisoner', display_name="Prisoner's Dilemma", num_demo_participants=2,
#      app_sequence=['prisoner', 'payment_info']),
# dict(name='volunteer_dilemma', display_name="Volunteer's Dilemma", num_demo_participants=3,
#      app_sequence=['volunteer_dilemma', 'payment_info']),
# dict(name='cournot', display_name="Cournot Competition", num_demo_participants=2, app_sequence=[
#     'cournot', 'payment_info'
# ]),
# dict(name='dictator', display_name="Dictator Game", num_demo_participants=2,
#      app_sequence=['dictator', 'payment_info']),
# dict(name='matching_pennies', display_name="Matching Pennies", num_demo_participants=2, app_sequence=[
#     'matching_pennies',
# ]),
# dict(name='traveler_dilemma', display_name="Traveler's Dilemma", num_demo_participants=2,
#      app_sequence=['traveler_dilemma', 'payment_info']),
# dict(name='bargaining', display_name="Bargaining Game", num_demo_participants=2,
#      app_sequence=['bargaining', 'payment_info']),
# dict(name='common_value_auction', display_name="Common Value Auction", num_demo_participants=3,
#      app_sequence=['common_value_auction', 'payment_info']),
# dict(name='bertrand', display_name="Bertrand Competition", num_demo_participants=2, app_sequence=[
#     'bertrand', 'payment_info'
# ]),
# dict(name='public_goods_simple', display_name="Public Goods (simple version from tutorial)",
#      num_demo_participants=3, app_sequence=['public_goods_simple', 'payment_info']),
# dict(name='trust_simple', display_name="Trust Game (simple version from tutorial)", num_demo_participants=2,
#      app_sequence=['trust_simple']),
