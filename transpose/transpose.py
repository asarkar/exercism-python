import itertools


# The catch in this problem is to determine whether to
# pad with space or not. Consider the matrix ['ABC', 'DE'].
# There's no padding needed with 'C'. But for ['AB', 'DEF'],
# we need to pad 'F' on the left.
#
# We use zip and fill the missing values with '$'. Since we
# don't want right padding, we later strip the fillers from
# the right.
#
# https://exercism.org/tracks/python/exercises/transpose/solutions/paiv
def transpose(text: str) -> str:
    a = itertools.zip_longest(*text.splitlines(), fillvalue='$')
    return '\n'.join(''.join(w).rstrip('$').replace('$', ' ') for w in a)
