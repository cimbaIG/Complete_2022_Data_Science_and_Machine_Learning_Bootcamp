def test(A, B):
    
    a = A
    b = B
    
    # TODO: Below this comment write your code.
    c = a
    a = b
    b = c
    
    # Leave this line alone as well
    return (a, b)

print(test(2,3))