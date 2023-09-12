
def pattern_search(P, I):
    width_I = len(I[0])
    height_I = len(I)

    # Rotate function rotates the pattern 90 degrees to the right. 
    # In order the achieve that, it takes the zeroth indices starting from the last row(=last string in the pattern) and appends them to the "new_l".
    # It joins the elements in the "new_l" after every loop because they create the first row (first string) in the new pattern.
    # Every string that is created is appended to the list "new". It is our new rotated pattern.
    def rotate(P): 
        new = []
        reverse_lenght = range(len(P))[::-1]
        for n in range(len(P[0])):
            new_l = []
            for m in reverse_lenght:
                new_l.append(P[m][n])
            new_chr = "".join(new_l)
            new.append(new_chr)
        return new

    def helper(i, a, I, P):
        for j in range(height_P):  # this is not starting from 1 bc when we increment n by 1, in the count greater than 1 situation, if the first row doesn't match no need to look for the second.
            b = (I[i + j].find(P[j], a, a + width_P) == a)
            # if the current b is True, then it will continue with the for loop. if the current b is False, then it will return False and exit the function.
            if not b:
                return False
        return True


    for z in range(4):
        if z != 0:
            P = rotate(P)
        degree = 90*z
        width_P = len(P[0])
        height_P = len(P)

    #For image's all rows (indices of the list I)
    #for degree 0, when looking for P[0], in order not the be out of range, range should be range(height_I - height_P + 1)
    #find gives -1 when what we are looking for isn't there
    #if there are more than 1 match, it will give the first match's index. so if there is a match we need a recursion.

        for i in range(height_I - height_P + 1):

            if I[i].find(P[0]) != -1 :

                for n in range(width_I - width_P + 1):
                    a = I[i].find(P[0]) + n
                    if a > (width_I - width_P):
                        break    
                    if helper(i,a,I,P):
                        return (i,a,degree)

    return False

