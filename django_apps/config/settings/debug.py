from .base import *

DEBUG = True
config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']