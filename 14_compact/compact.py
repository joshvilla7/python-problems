def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']

        falsey values = 0, '', [], False, (), None
    """

    for item in lst:
        if not(item):
            lst.remove(item)

    return lst 


    