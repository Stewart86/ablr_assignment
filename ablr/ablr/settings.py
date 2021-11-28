"""
Django settings for ablr project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from textwrap import dedent
from typing import Final

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Final = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: Final = "django-insecure-!$)_l70b2-1uswhkn2m=2)9)eq@5yk)ajq681@ppfo$9l^ae$&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: Final = True
TEST: Final = True

ALLOWED_HOSTS: Final[list[str]] = ["localhost", "localhost:3000", "127.0.0.1"]

CORS_ORIGIN_ALLOW_ALL: Final = True
# CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:3001"]

# Application definition

INSTALLED_APPS: Final = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "myinfo",
]

MIDDLEWARE: Final = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF: Final = "ablr.urls"

TEMPLATES: Final = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "frontend"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: Final = "ablr.wsgi.application"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES: Final = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: Final = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE: Final = "en-us"

TIME_ZONE: Final = "Asia/Singapore"

USE_I18N: Final = True

USE_L10N: Final = True

USE_TZ: Final = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/dist/"
# Extra places for collectstatic to find static files.
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "frontend/build",
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: Final = "django.db.models.BigAutoField"

# MYINFO
CERT_VERIFY: Final = False

MYINFO_ROOT: str = os.environ.get("MYINFO_ROOT", "")
MYINFO_CLIENT_ID: str = os.environ.get("MYINFO_CLIENT_ID", "")
MYINFO_SECRET: str = os.environ.get("MYINFO_SECRET", "")
MYINFO_PRIVATE_KEY: str = os.environ.get("MYINFO_PRIVATE_KEY", "")
MYINFO_PUBLIC_CERT: str = os.environ.get("MYINFO_PUBLIC_CERT", "")

if TEST:
    # SECURITY WARNING: Constants use for test only, for production set `TEST = False` above
    # These are test credentials so they can live in the git commit

    MYINFO_ROOT = "https://test.api.myinfo.gov.sg/com/v3"
    MYINFO_CLIENT_ID = "STG2-MYINFO-SELF-TEST"
    MYINFO_SECRET = "44d953c796cccebcec9bdc826852857ab412fbe2"

    # this is MyInfo private key that is used:
    # - to sign our requests to MyInfo, and
    # - to decrypt personal data returned back
    MYINFO_PRIVATE_KEY = dedent(
        """
    -----BEGIN PRIVATE KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDGBRdsiDqKPGyH
    gOpzxmSU2EQkm+zYZLvlPlwkwyfFWLndFLZ3saxJS+LIixsFhunrrUT9ZZ0x+bB6
    MV55o70z4ABOJRFNWx1wbMGqdiC0Fyfpwad3iYpRVjZO+5etHA9JEoaTPoFxv+kt
    d8kVAL9P5I7/Pi6g1R+B2t2lsaE2bMSwtZqgs55gb7fsCR3Z4nQi7BddYR7MZ2lA
    MWf7h7Dkm6uRlGhl2RvtmYa6dXFnK3RhIpdQOUT3quyhweMGspowC/tYSG+BNhy1
    WukbwhIP5vTAvv1WbHTg+WaUUV+pP0TjPQcY73clHxNpI5zrNqDmwD2rogNfePKR
    UI63yBUfAgMBAAECggEAGy/7xVT25J/jLr+OcRLeIGmJAZW+8P7zpUfoksuQnFHQ
    QwBjBRAJ3Y5jtrESprGdUFRb0oavDHuBtWUt2XmXspWgtRn1xC8sXZExDdxmJRPA
    0SFbgtgJe51gm3uDmarullPK0lCUqS92Ll3x58ZQfgGdeIHrGP3p84Q/Rk6bGcOb
    cPhDYWSOYKm4i2DPM01bnZG2z4BcrWSseOmeWUxqZcMlGz9GAyepUU/EoqRIHxw/
    2Y+TGus1JSy5DdhPE0HAEWKZH729ZdoyikOZCMxApQglUkRwkwhtXzVAemm6OSoy
    3BEWvSEJh/F82tFrmquUoe/xd5JastlBHyD78RAakQKBgQDkHAzo1fowRI19tk7V
    CPn0zMdF/UTRghtLywc/4xnw1Nd13m+orArOdVzPlQokLVNL81dIVKXnId0Hw/kX
    8CRyRYz8tkL81spc39DfalZW7QI7Fschfq1Htgkxd/QEjBlIaqjkOjGSbX9xYjYU
    1Db8PuGoGXWOsYiv9PCsKR056wKBgQDeOzfZSpV5kX8SECJXRA+emyCnO9S29p0W
    +5BCTQp3OPnmbL7b/mGqBVJ0DC+IiN67Lu8xxzejswqLZqaRvmQuioqH+8mOGpXY
    ZwhShAif2AuixxvL7OK6dvDmMqoKhBI9nZ9+XI60Cd/LjnWgyFO04uq4otnTukmY
    sSP+fp6wnQKBgEopYH0WjFfDAelcKzcRywouxZ7Yn9Ypoaw7nujDcfydhktY/R5u
    iLjk6T7H6tsmLU2lGLx4YNPLa6wJp+ODfKX2PMcwjojbYEFftu3cCaQLPE1vs2AN
    alLFOSnvINOVpOapXq2Mye8cUHHRh1mwQQwzeXQIivLQf2sNjG28lDbvAoGACsh8
    0UJZNmjk7Y9y2yEmUN/eGb9Bdw9IWBEk0tLCKz7MgW3NZQdW3dUcRx1AQTPC+vow
    CQ5NmNfbLyBv/KpsWgXG6wpAoXCQzMtTEA3wDTGCfweCRcbcyYdz8PeMYK4/5FV9
    o7gCBKJmBY6IDqEpzqEkGolsYGWtpIcT5Alo0dECgYEA3hzC9NLwumi/1JWm+ASS
    ADTO3rrGo9hicG/WKGzSHD5l1f+IO1SfmUN/6i2JjcnE07eYArNrCfbMgkFavj50
    2ne2fSaYM4p0o147O9Ty8jCyY9vuh/ZGid6qUe3TBI6/okWfmYw6FVbRpNfVEeG7
    kPfkDW/JdH7qkWTFbh3eH1k=
    -----END PRIVATE KEY-----
    """
    ).strip()

    # this is MyInfo X.509 Public Key Certificate
    MYINFO_PUBLIC_CERT = dedent(
        """
    -----BEGIN CERTIFICATE-----
    MIIGtTCCBJ2gAwIBAgINAMqXqT4AAAAAV8nKdjANBgkqhkiG9w0BAQsFADBoMQsw
    CQYDVQQGEwJTRzEYMBYGA1UEChMPTmV0cnVzdCBQdGUgTHRkMSYwJAYDVQQLEx1O
    ZXRydXN0IENlcnRpZmljYXRlIEF1dGhvcml0eTEXMBUGA1UEAxMOTmV0cnVzdCBD
    QSAyLTEwHhcNMTkxMTA3MDcyNTAwWhcNMjQxMTA3MDc1NTAwWjCBzDELMAkGA1UE
    BhMCU0cxGDAWBgNVBAoTD05ldHJ1c3QgUHRlIEx0ZDEmMCQGA1UECxMdTmV0cnVz
    dCBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkxIDAeBgNVBAsTF05ldHJ1c3QgQ0EgMi0x
    IChTZXJ2ZXIpMQ8wDQYDVQQLEwZNeUluZm8xJDAiBgNVBAsTG0dvdmVubWVudCBU
    ZWNobm9sb2d5IEFnZW5jeTEiMCAGA1UEAxMZc3RnLmNvbnNlbnQubXlpbmZvLmdv
    di5zZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALBgTSLOJ7IhzXy6
    qEeNIdOlntSL1lWhiErxExypSQE1iFEXfcMdW6h2erXrFZi2Kik+++pIMV8FQ/DT
    9Fbvk4fAviBfvXzDTmvP03qML3Kg4iEYy+0SHfJJqXJo7SEthvjKJX0mx+wkVlUZ
    KOKvPCzGyVAJYJUpxaaX0IbBFWJcC7WZRwGMvXJfD3LMT5hVMwlB+BXn8qu+wQVD
    zKc22Sy45QI/e6xdaEkCShzOkQS3LyPgGrkaSnt+DtxkfWwgk25IRE1Xq1rHprRV
    M56/ZqDkmg5BDCBgOcA8rddpIyir225vpNmOUzKtSCEF34YoRgG07bVaZmS2MCXW
    tJ3pi+ECAwEAAaOCAfcwggHzMAsGA1UdDwQEAwIFoDAdBgNVHSUEFjAUBggrBgEF
    BQcDAQYIKwYBBQUHAwIwSAYDVR0gBEEwPzA9BggqhT4Ah2oGATAxMC8GCCsGAQUF
    BwIBFiNodHRwOi8vd3d3Lm5ldHJ1c3QubmV0L291cnByYWN0aWNlczBDBggrBgEF
    BQcBAQQ3MDUwMwYIKwYBBQUHMAKGJ2h0dHA6Ly9haWEubmV0cnVzdC5uZXQvbmV0
    cnVzdGNhMi0xLmNlcjCBvQYDVR0fBIG1MIGyMC2gK6AphidodHRwOi8vY3JsLm5l
    dHJ1c3QubmV0L25ldHJ1c3RjYTItMS5jcmwwgYCgfqB8pHoweDELMAkGA1UEBhMC
    U0cxGDAWBgNVBAoTD05ldHJ1c3QgUHRlIEx0ZDEmMCQGA1UECxMdTmV0cnVzdCBD
    ZXJ0aWZpY2F0ZSBBdXRob3JpdHkxFzAVBgNVBAMTDk5ldHJ1c3QgQ0EgMi0xMQ4w
    DAYDVQQDEwVDUkwxNTArBgNVHRAEJDAigA8yMDE5MTEwNzA3MjUwMFqBDzIwMjQx
    MTA3MDc1NTAwWjAfBgNVHSMEGDAWgBQXSyZLlHkKX9+a8Qg3w0g3g7vX+jAdBgNV
    HQ4EFgQUb/y4gDv05wxdNMIxNBevaxx/0cUwCQYDVR0TBAIwADANBgkqhkiG9w0B
    AQsFAAOCAgEAsUJ8u0vooWCeadOO3280dGnCWNYPpGKeWrZo7GYU3jTyvpVSinvY
    INEEqaxjC5EPpWf6L1RC306bjm0EmcalxnhFeQuopSWmZdfttltfcCdAb8x6FJtv
    +n2idHwjRGX4pkR5Txxteu7YpYXU2ltx/WK5xdeCKWPPDnmuZxnfV9R0tw4TQy3M
    ZmImrDV0q4FGOKr1vddHrPml5ud9gLP8pb55ogEApV3bPJJW6J4HoAbF/+8KMEcP
    /3ayYmL37AXWwYTzkQzSQGjl02bumHvY8M1lOeTnUUfeufvPx2FqGJfJfwmMjVKd
    hxISCEEvGPtJnN/20psEFOgbOA4s5y/WwGjWbX665up3AXIBxGb0hMpXsIi5pV1z
    WcXaNlYREb98L8Rm5r/rHoCFudZM1yu//+XyUTBG9hRl0Cconj6GB4aq10KGd7SH
    i7lf1Hx2K6UaAZdgPKbg5AhdZ0Yuxl6Jb6ZjFJ9lwLpd7dQlqh6ylvKsY1hoXvZf
    GKoBraTIydUscYXJkubGUfu6Y13H4TNnR1OZx7oX1sX94M3/QDyStmLvg/5R/oJB
    BKTTdZkGqGLQE9LMDYPNsH8BaeXb9U98W9XeXG6eKAX2gkEWzPgC1ebb7ZBEmLXb
    GR2PyiNqvibfB7US70IBQik7J2WU9XvM9z+YiQlpVWMwQb2TDb2FCNk=
    -----END CERTIFICATE-----
    """
    ).strip()

MYINFO_ATTRS: Final = (
    "uinfin,name,sex,race,nationality,dob,email,mobileno,regadd,housingtype,hdbtype,marital,edulevel,"
    "ownerprivate,cpfcontributions,cpfbalances,"
    "birthcountry,residentialstatus,"
    "aliasname,marriedname,passtype,employmentsector,noahistory"
)
