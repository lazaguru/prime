def is_prime(m):
    """Returns True if the  input interger is prime
    else False."""
    if m == 0 or m == 1:
        return False
    for x in range(2, m):
        if m % x == 0:
            return False
    else:
        return True
