def calculate_average_age(users):
    """Return the average of valid numeric ages across users.

    Ignores users with a missing "age" key or a non-numeric age value
    (e.g. a string). Returns 0.0 if there are no valid ages.
    """
    valid_ages = [
        u["age"] for u in users
        if isinstance(u.get("age"), (int, float)) and not isinstance(u.get("age"), bool)
    ]
    if not valid_ages:
        return 0.0
    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """Return a list of email addresses for active users.

    A user's email is included only if "is_active" is truthy and the
    user has an "email" key. Returns an empty list if none qualify.
    """
    return [u["email"] for u in users if u.get("is_active") and "email" in u]
