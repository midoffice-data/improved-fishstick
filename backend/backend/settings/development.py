from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cx8&=ho5h7_(0i_g&(j%@^0)3)(*lw7xq^2a2&v=4sder2gwaj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "django", "localhost", "127.0.0.1", "0.0.0.0",
    ".github.dev", ".app.github.dev", ".githubpreview.dev"
]

# Allow Codespaces forwarded hosts (e.g., *.github.dev) in dev
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://*.github.dev",
    "https://*.app.github.dev",
    "https://*.githubpreview.dev",
]

# Extra apps for development
INSTALLED_APPS += [
    'django_extensions',
    'corsheaders',
]

# Insert CORS middleware early
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    *MIDDLEWARE,
]

# Allow all origins in development to simplify Codespaces usage
CORS_ALLOW_ALL_ORIGINS = True
