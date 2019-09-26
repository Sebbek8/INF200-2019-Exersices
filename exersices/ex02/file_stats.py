def char_counts(textfilename):

    openfile = open(textfilename)
    text = openfile.read()
    openfile.close()

    utf8 = []
    letters = []

    """ split the text into symbols and add to a list """
    for letter in text:
        letters.append(letter.split())

    """ add x for all the values x in letters
        if x has a value, (removes white-spaces) """
    letters2 = [x for x in letters if x]

    """ convert all symbols into UTF-8 format """
    for key in range(len(letters2)):
        utf8.append(ord(letters2[key][0]))

    """ creats empty list, and fill it with how many times
        each number occurs, in acending order """
    result = []
    for number in range(256):
        result.append(utf8.count(number))

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
