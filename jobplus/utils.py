from flask_login import current_user
from jobplus.models import User


def getCurrentUser() -> User:
    return current_user._get_current_object()
