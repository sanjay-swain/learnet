from functools import wraps

from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth import decorators


def user_passes_test(test_func, message='You should be logged in, in order to see this page.'):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                messages.warning(request, message)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def login_required_message(function=None, message='You should be logged in, in order to see this page.'):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        message=message
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# def login_required_message_and_redirect(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None, message='You should be logged in, in order to see this page.'):
#     if function:
#         return login_required_message(
#             login_required(function, redirect_field_name, login_url),
#             message
#         )

#     return lambda deffered_function: login_required_message_and_redirect(deffered_function, redirect_field_name, login_url, message)


# setattr(decorators, 'login_required', login_required_message_and_redirect)
