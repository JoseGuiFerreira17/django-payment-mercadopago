import contextlib

from django.contrib.auth import get_user_model

from apps.core.middlewares import current_request


def get_request_user():
    with contextlib.suppress(Exception):
        user = current_request().user
        if isinstance(user, get_user_model()):
            return current_request().user
    return None
