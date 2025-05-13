API_PREFIX = "api"

# apps:
CREW = "crew"
ROLES = "roles"
ACCOUNTS = "accounts"
SIGNUP = "signup"
LOGIN = "login"
REFRESH_TOKEN = "token/refresh"

# app urls:
CREW_URL = f"{API_PREFIX}/{CREW}/"
ROLES_URL = f"{API_PREFIX}/{ROLES}/"
SIGNUP_URL = f"{API_PREFIX}/{ACCOUNTS}/{SIGNUP}/"
LOGIN_URL = f"{API_PREFIX}/{ACCOUNTS}/{LOGIN}/"
REFRESH_TOKEN_URL = f"{API_PREFIX}/{REFRESH_TOKEN}/"
