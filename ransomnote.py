"""
>>> checkMagazine(['two', 'times', 'three', 'is', 'not', 'four'], ['two', 'times', 'two', 'is', 'four'])

"""


def dictBuilder(list):
    dict = {}
    for item in list:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict

def checkMagazine(magazine, note):
    magazine_vocab = dictBuilder(magazine)
    for key in note:
        if key not in magazine_vocab:
            print ("No")
            return
        if magazine_vocab[key] == 0:
            print ("No")
            return
        else:
            print (magazine_vocab[key])
            magazine_vocab[key] -= 1
            print (magazine_vocab)
    print ("Yes")
    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()