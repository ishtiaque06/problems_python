"""
>>> hello([2,1,5,2])

"""



def hello(array):
     answer = True
     for i in range(len(array)):
            for j in range(len(array)):
                     if (i!= j) and (array[i] == array[j]):
                             answer = False
     return answer

if __name__=="__main__":
    import doctest
    doctest.testmod()
