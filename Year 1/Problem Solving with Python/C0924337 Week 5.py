def doomsday(y):

    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    
    """

    if not 1800 <= y <= 2199:
        answer = -1
        return(answer)
    else:
        if 1800 <= y <= 1899:
            x = 5
        elif 1900 <= y <= 1999:
            x = 3
        elif 2000 <= y <= 2099:
            x = 2
        elif 2100 <= y <= 2199:
            x = 0
        year = str(y)
        decade = year[-2:]
        w = int(decade)
        a = w // 12
        b = w % 12
        c = b // 4
        d = (a + b + c) % 7
        answer = (d + x) % 7
        return(answer)