def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWELS = 'aeiou'
    phrase = phrase.lower()
    initialier = {vowels: 0 for vowels in phrase if vowels in VOWELS}
    for vowel_count in phrase:
        if vowel_count in VOWELS:
            initialier[vowel_count] = initialier[vowel_count] + 1
    return initialier
