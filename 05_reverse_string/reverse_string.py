def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    to_reverse = list(phrase)
    to_reverse.reverse()
    reversed = ''.join(to_reverse)
    return print(reversed)
