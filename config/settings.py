"""
config/settings.py
All configuration for the framework lives here.
URLs, timeouts, credentials — single source of truth.
"""

BASE_URL = "https://www.saucedemo.com/"

TIMEOUT  = 15000
HEADLESS = False

USERS={
    "valid_user":{"email":"standard_user",
                "password":"secret_sauce"
                }

}