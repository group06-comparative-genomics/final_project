def count_aminoacid(proteomelist):
    f = open(proteomelist, "r").readlines()

    A = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    K = 0
    L = 0
    M = 0
    N = 0
    P = 0
    Q = 0
    R = 0
    S = 0
    T = 0
    V = 0
    W = 0
    Y = 0
    for line in f:
        if line[0] != ">":

            for nucleotide in line:
                if nucleotide == "A":
                    A += 1
                elif nucleotide == "C":
                    C += 1
                elif nucleotide == "G":
                    G += 1
                elif nucleotide == "H":
                    H += 1
                elif nucleotide == "I":
                    I += 1
                elif nucleotide == "K":
                    K += 1
                elif nucleotide == "L":
                    L += 1
                elif nucleotide == "M":
                    M += 1
                elif nucleotide == "N":
                    N += 1
                elif nucleotide == "P":
                    P += 1
                elif nucleotide == "Q":
                    Q += 1
                elif nucleotide == "R":
                    R += 1
                elif nucleotide == "S":
                    S += 1
                elif nucleotide == "T":
                    T += 1
                elif nucleotide == "V":
                    V += 1
                elif nucleotide == "W":
                    W += 1
                elif nucleotide == "Y":
                    Y += 1

    all_nucleotides = A + C + D + E + F + G + H + I + K + M + N + P + Q + R + S + T + V + W + Y

    percentage_A = float(A)/all_nucleotides
    percentage_C = float(C)/all_nucleotides
    percentage_D = float(D)/all_nucleotides
    percentage_E = float(E)/all_nucleotides
    percentage_F = float(F)/all_nucleotides
    percentage_G = float(G)/all_nucleotides
    percentage_H = float(H)/all_nucleotides
    percentage_I = float(I)/all_nucleotides
    percentage_K = float(K)/all_nucleotides
    percentage_L = float(L)/all_nucleotides
    percentage_M = float(M)/all_nucleotides
    percentage_N = float(N)/all_nucleotides
    percentage_P = float(P)/all_nucleotides
    percentage_Q = float(Q)/all_nucleotides

    percentage_R = float(R)/all_nucleotides
    percentage_S = float(S)/all_nucleotides
    percentage_T = float(T)/all_nucleotides
    percentage_V = float(V)/all_nucleotides
    percentage_W = float(W)/all_nucleotides
    percentage_Y = float(Y)/all_nucleotides

    #print (percentage_A)


    return(percentage_A, percentage_C, percentage_D ,percentage_E ,percentage_F ,percentage_G , percentage_H , percentage_I , percentage_K , percentage_L , percentage_M , percentage_N , percentage_P , percentage_Q , percentage_R , percentage_S ,percentage_T ,percentage_V ,percentage_W ,percentage_Y )
#proteomelist ("03.protein.txt", "08.protein.txt", "09.protein.txt", "18.protein.txt","30.fa.txt")
#count_aminoacid("08.protein.txt")
#proteomelist = ["03.protein.txt", "08.protein.txt", "09.protein.txt", "18.protein.txt","30.fa.txt"]
#print (count_aminoacid(proteomelist[1]))
def Distance(proteomelist):
    import numpy as np
    i = 0
    j = 0
    outsidelist1 = []

    #outsidelist2 = []
    while i <= 4:
        insidelist1 = []
        #insidelist2 = []
        for j in range (0,5):
            Distance1 = 0
            for k in range (0, 19):
                Distance = (count_aminoacid(proteomelist[i])[k]-count_aminoacid(proteomelist[j])[k])**2
                Distance1 += Distance
            #print (Distance1)
            insidelist1.append(Distance1)
            #insidelist2.append(Distance2)
            j += 1
        i +=1
        outsidelist1.append(insidelist1)
        #outsidelist2.append(insidelist2)
    print (outsidelist1)
    #print (outsidelist2)


    #return (outsidelist2)

proteomelist = ["03.protein.fa", "08.protein.fa", "09.protein.fa", "18.protein.fa","30.protein.fa"]
Distance(proteomelist)
