a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

for i in a:
    print ("\n" + str(i))
    for j in b:
        print ("  " + str(j))
        if j == 6:
            break
