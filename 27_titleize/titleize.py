def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    listed = []
    index = 0
    for char in phrase:
        if index == 0 or phrase[index - 1] == ' ':
            listed.append(char.upper())
        else:
            listed.append(char.lower())
        index = index + 1
    return "".join(listed)
