import math


def letter_freq(txt):
    """ Getting letter_freq and
        change the letter to the UTF8 number """
    liten = txt.lower()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '?', ',',
             '.', '+', '-', '_', '&', '%', '(', ')', '"', ':']

    result = {}
    for i in range(len(alpha)):
        if liten.count(alpha[i]) != 0:
            result[ord(alpha[i])] = liten.count(alpha[i])

    return result


def entropy(message):

    """Defines and uses the function for entropy"""
    n_i = letter_freq(message)
    n = len(message)

    """ Uses the entropy formula and sums up """
    h = 0
    for k in n_i.values():
        p_i = (float(k) / n)
        h += - p_i * math.log(p_i, 2)

    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
