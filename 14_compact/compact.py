def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    # out_list = []
    # for el in lst:
    #     if bool(el):
    #         out_list.append(el)
    # return out_list

    return [el for el in lst if el]
