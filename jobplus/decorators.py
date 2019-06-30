from flask import abort
from flask_login import current_user
from functools import wraps
from jobplus.models import UserRole


def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role < role or current_user.is_disable is True:
                abort(404)
            return func(*args, **kwargs)

        return wrapper

    return decorator


admin_required = role_required(UserRole.ADMIN.value)
