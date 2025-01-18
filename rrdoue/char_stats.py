"""The char_stats module, with one function, when given a mandatory string, returns a count of each character in the string.  An optional argument limits the function to counting only the specified characters.
One can run the module's function interactively from the command line. """


def count_characters(text, lookfor=None):
    """
    :param text: Mandatory, a string whose characters will be counted
    :param lookfor: Optional, a string that specifies what characters to count; otherwise, all characters are counted
    :return: dictionary of characters and their respective counts
    """

    if lookfor:
        output = dict.fromkeys(lookfor, 0)
    else:
        output = dict.fromkeys(text, 0)

    for one_character in text:
        if one_character in output:
            output[one_character] += 1

    return output


if __name__ == "__main__":
    user_text = input('Enter some text: ').strip()
    look_for_values = input('Restrict to the following characters (optional): ') # strip was omitted to allow for
    # counting only characters

    if look_for_values:
        print(count_characters(user_text, look_for_values))
    else:
        print(count_characters(user_text))
