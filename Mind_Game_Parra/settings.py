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
       name='Mind_MAIN',
       app_sequence=['consent', 'welcome', 'inst_baseline', 'inst_simult', 'inst_noavoid', 'inst_noext',
                     'mind_baseline_choices', 'mind_noavoid_choices', 'mind_noext_choices', 'mind_simult_choices',
                     'survey', 'payment_info'],
       num_demo_participants=8,

    ),
   dict(
        name='Bots_Avoidance_Main',
        app_sequence=['consent', 'welcome', 'inst_baseline','inst_simult', 'inst_noavoid','inst_noext',
                      'mind_baseline_choices', 'mind_noavoid_choices', 'mind_noext_choices', 'mind_simult_choices', 'survey','payment_info'],
        num_demo_participants=8,
        use_browser_bots=True,
    ),
   dict(
        name='testing',
        app_sequence=['welcome','inst_simult', 'mind_simult_choices', 'survey', 'payment_info'],
        num_demo_participants=8,
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
        name='t_15feb',
        display_name='Test MG',
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
