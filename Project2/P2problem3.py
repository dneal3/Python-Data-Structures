#problem3
#shared psuedocode on the process I went through to solve this with Mariah McRae and Daniel Loyd
import sys
#python3 problem3.py input
def rCycle():
    q = [] # set 
    start = 0 # it
    sum_e = 0 # up
    nextr = 0 # lets go
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip()) # get that n range tho
        for _ in range(n): # will be n time, so O(n) linear time
            in_data = f.readline().strip().split() # the numbers... what do they mean (energy obtained and lost)
            e_delta = int(in_data[0]) - int(in_data[1]) # difference of energy from eating and energy lost from leaving
            q.append(e_delta) # slap that difference into a list for safekeeping (and indexing later)
            sum_e += q[start + nextr] # compute that sum
            nextr+=1 # increase that index for reasons (computes next index counts how many restaurants you have been to)
            if sum_e < 0: # you died en route to the next restaurant :'(
                sum_e = 0 # reset that sum ur ded it cant help you now
                start = (start + nextr) # increase start point by rests past, the last two places cant be starters on this team
                nextr = 0 # reset the amount of restaurants you have passed cuz you died and respawned
        print(start) # straight to the STDOUT we outta here
        return start # saves the first starting point that was possible

if __name__ == '__main__':
    rCycle()
