from django.http import HttpResponseForbidden

def farmer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, "profile") and request.user.profile.is_farmer:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not allowed to access this page (Farmer only).")
    return wrapper


def buyer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, "profile") and request.user.profile.is_buyer:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not allowed to access this page (Buyer only).")
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, "profile") and request.user.profile.is_admin:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not allowed to access this page (Admin only).")
    return wrapper