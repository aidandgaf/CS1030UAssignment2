""" palindrome checker """
def palichecker(word):
    if(len(word)==1): return True
    if(word[0]==word[len(word)-1]):
        return palichecker(word[1:len(word)-1])
    return False
print (palichecker('tacocat'))
