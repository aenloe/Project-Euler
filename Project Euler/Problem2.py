'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''
def fibonacci_even_sum():
    
    #generate list of fibonacci numbers under 4 million
    L1 = [1,2]
    x = 2
    y = 3
    z = 3
    while True:
        if z > 4000000:
            break
        L1.append(z)
        z = y + x
        x = y
        y = z

    #generate list of even fibonacci numbers out of L1
    L2 = []
    for e in L1:
        if e % 2 == 0:
            L2.append(e)
    #sum list L2
    y = 0
    for e in L2:
        y += e
    
    print(y)
    return None

fibonacci_even_sum()