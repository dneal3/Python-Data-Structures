#Problem 1
import sys
#Worked with Daniel Loyd and Mariah McRae we may have similar ideas 
#on how to deal with this
#python3 problem1.py input
def collage():
    #this function takes in two sets of words and returns YES if the words
    #are present in the first set
    with open(sys.argv[1]) as f:
        inputDict = {}
        l0 = f.readline().strip().split() # input ints
        l1 = f.readline().strip().split() # initial word collage
        l2 = f.readline().strip().split() # words to check for
        for i in range(int(l0[0])-1): #x time
            if l1[i] not in inputDict.keys():
                inputDict[l1[i]] = 1 # basically counts occurances
            else:
                inputDict[l1[i]] += 1 # increase occurance counter
        for j in range(int(l0[1])-1): #y time
            if l2[j] in inputDict.keys():
                inputDict[l2[j]] -= 1# subtract an occurance from that key
                if inputDict.get(l2[j]) < 0: # if less than 0 it didnt exist in the list or there are no more remaining
                    print("NO")
                    return "NO"
            else:
                print("NO")
                return "NO"
        print("YES")
        return "YES" #should run in at most x+y complexity

if __name__ == "__main__":
    collage()


