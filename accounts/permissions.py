from accounts.models import User



def is_admin(user):
    return user.is_authenticated and user.is_superuser


def is_vendor(user):
    return ( user.is_authenticated and user.role == User.VENDOR )


def is_rider(user):
    return (  user.is_authenticated and user.role == User.RIDER )




