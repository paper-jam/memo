# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
# 1 décorateur permet d'étendre les capacités d'une fonction
import functools

user_name = "Jason"

def check_user(username):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            """
                le wrapper
            """
            if username == user_name:
                return func()
            else:
                print("utilisateur inconnu")
        return wrapper
    return decorator


@check_user("Jason")
def profile():
    """
    Page accès profil 
    """
    print("le profile membre est ...")


profile()
