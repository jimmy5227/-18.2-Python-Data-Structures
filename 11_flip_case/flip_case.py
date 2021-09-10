def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_phrase = ""
    uppercase = to_swap.upper()
    lowercased = to_swap.lower()
    for char in phrase:
        if char == uppercase:
            swapped_phrase = swapped_phrase + lowercased
        elif char == lowercased:
            swapped_phrase = swapped_phrase + uppercase
        else:
            swapped_phrase = swapped_phrase + char
    return swapped_phrase
