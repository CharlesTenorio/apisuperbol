from decouple import config

TYPE = config('AUTHENTICATION_TYPE', default="token")

AUTHENTICATION_TYPES = { 
  'JWT': 'rest_framework_simplejwt.authentication.JWTAuthentication',
  'TOKEN': 'rest_framework.authentication.TokenAuthentication' 
}

DEFAULT_AUTHENTICATION_CLASSES = AUTHENTICATION_TYPES[TYPE.upper()]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
  'http://localhost:8080',
]

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.AllowAny',
  ],
  'DEFAULT_AUTHENTICATION_CLASSES': [      
    DEFAULT_AUTHENTICATION_CLASSES
  ],
  'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

# Password reset configurations
DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
  "CLASS": "django_rest_passwordreset.tokens.RandomStringTokenGenerator",
  "OPTIONS": {
    "min_length": 40,
    "max_length": 40
  }
}