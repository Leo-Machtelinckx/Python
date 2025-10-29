for i in range(2,1000):
    premier=True
    for j in range(2,i):
        if (i%j)==0:
            premier=False
            break
    if premier==True:
        print(i)