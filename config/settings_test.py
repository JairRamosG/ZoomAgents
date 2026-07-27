from config.settings import *  # noqa: F401, F403

DEBUG = True
SECRET_KEY = "test-secret-key-not-for-production"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

TASKS = {
    "default": {
        "backend": "django.tasks.backends.immediate.ImmediateBackend",
    },
}
