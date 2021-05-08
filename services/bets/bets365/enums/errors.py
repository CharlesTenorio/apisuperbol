from django.db.models import TextChoices

class ErrorApiChoices(TextChoices):
  INTERNAL_SERVER_ERROR = 'INTERNAL_SERVER_ERROR',	'500 Internal Server Error, contact Support if it happens'
  NOT_FOUND = 'NOT_FOUND',	'404 Not Found'
  METHOD_NOT_ALLOWED = 'METHOD_NOT_ALLOWED',	'Method is not allowed, only GET is supported.'
  UNDER_MAINTENANCE = 'UNDER_MAINTENANCE',	"API is under maintenance, we'll annouce it"
  AUTHORIZE_FAILED = 'AUTHORIZE_FAILED',	'Token is not provided or incorrect.'
  TOO_MANY_REQUESTS = 'TOO_MANY_REQUESTS',	'API rate limit exceeded.'
  PERMISSION_DENIED = 'PERMISSION_DENIED',	"You're not allowed, contact Support if it is wrong."
  PARAM_REQUIRED = 'PARAM_REQUIRED',	'Required param is missing, check error_detail for details'
  PARAM_INVALID = 'PARAM_INVALID',	'param is invalid, check error_detail for details'