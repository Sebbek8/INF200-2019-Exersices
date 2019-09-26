def bubble_sort(data):

    """ Makes list of the data """
    the_list = list(data)

    length = len(the_list)
    """ Iterate from the start to the back,
        then go to back - 1 """
    while length >= 1:
        innerloop(the_list)
        length -= 1

    return the_list


def innerloop(the_list):

    """ Compares values, and changes postions if they
        are in wrong order """
    for index in range(len(the_list)-1):
        if the_list[index] > the_list[index+1]:
            smaller = the_list[index+1]
            bigger = the_list[index]
            the_list[index] = smaller
            the_list[index+1] = bigger

    return tuple(the_list)


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
