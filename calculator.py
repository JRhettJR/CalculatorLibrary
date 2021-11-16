""" 
Calculator library containing basic math operations.
"""


def add(first_term: int,
        second_term: int) -> int:
    """
    add Description here

    Parameters
    ----------
    first_term (int) : Parameter Description
    second_term (int) : Parameter Description

    Returns
    -------
    int : Return Item Description

    Raises
    ------
    ValueError
        If the value of first_term is None

    """
    if first_term is None:
        raise ValueError("first_term cannot be None")

    print(first_term)
    return first_term + second_term


def subtract(first_term: int,
             second_term: int) -> int:
    """
    subtract Description here

    Parameters
    ----------
    first_term (int) : Parameter Description
    second_term (int) : Parameter Description

    Returns
    -------
    int : Return Item Description

    Raises
    ------
    ValueError
        If the value of first_term is None

    """
    if first_term is None:
        raise ValueError("first_term cannot be None")

    print(first_term)
    return first_term + second_term
