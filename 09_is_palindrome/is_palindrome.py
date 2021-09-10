def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    phrase_reversed = []
    orig_phrase = []
    for char in list(phrase):
        replaced = (char.replace(' ', '')).lower()
        phrase_reversed.append(replaced)
        orig_phrase.append(replaced)

    phrase_reversed.reverse()

    phrase_reversed = "".join(phrase_reversed)
    orig_phrase = "".join(orig_phrase)

    if orig_phrase == phrase_reversed:
        return True
    else:
        return False
