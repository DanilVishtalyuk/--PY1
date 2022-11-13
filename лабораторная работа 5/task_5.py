import random
import string


def get_random_password(len_=8) -> str:
    return "".join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, len_))


print(get_random_password())
