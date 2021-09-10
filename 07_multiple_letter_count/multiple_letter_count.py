def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    occurrences = {}

    while len(phrase) > 0:
        occurrences[phrase[0]] = phrase.count(phrase[0])
        phrase = phrase.replace(phrase[0], '').strip()
    return occurrences
