# created by sidhanshu monga
# 08 may, 2018

#Problem statement :  find permutations of particular word

def permute(strr,k,m):
    if(k == m):
        print "".join(strr), 
    else:
        for a in range(k,m):
            strr[k],strr[a] = strr[a],strr[k] 
            permute(strr, k+1, m)
            strr[k],strr[a] = strr[a],strr[k]
            
input = 'sam'
i =  list(input)
permute(i,0,len(i))