ACCOUNT_APPS = [
  'accounts.users',
  'accounts.benches',
  'accounts.changers',
  'accounts.customers.customers',
  'accounts.customers.transactions',
  'sports.football.leagues',
  'sports.football.match',
  'sports.football.teams',
  'bets.football.odds',
  'bets.football.tickets',
]

MY_APPS = ACCOUNT_APPS

LIB_APPS = [
  'drf_yasg',
  'corsheaders',
  'rest_framework',
  'rest_framework.authtoken',
  'django_rest_passwordreset',
  'whitenoise.runserver_nostatic',
  'django_celery_results',
  'django_celery_beat',
  'django_filters',
  'storages',
  'rangefilter'
]

CONTRIB_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

def get_apps () -> list:
  return CONTRIB_APPS + LIB_APPS + MY_APPS