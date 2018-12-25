############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #5
#   Instructor: Pei-Yuan Wu
############################################

import sys
import pdb

# **********************************
# *  TODO                          *
# **********************************
def solution(input_K, input_integer_set):
    '''
    Modify this function
    1. Return the minimum difference between maximum and minimum 
       of all possible K-element subsets.
    2. For example, given input_integer_set [13,24,1,44,15], you should return 9.
          input_set        possible_subset     difference        minimum difference 
       [13,24,1,44,15]  =>    [1,13,15]     =>      14       =>     return 11
                              [1,13,24]             23
                              [1,13,44]             43
                              [1,15,24]             23
                              [1,15,44]             43
                              [1,24,44]             43
                              [13,15,24]            11
                              [13,15,44]            31 
                              [13,24,44]            31
                              [15,24,44]            29         
    3. Feel free to add more functions.
    '''
    result = 100000000
    MergeSort(input_integer_set)
    for i in range(0 ,len(input_integer_set)-input_K):
        if input_integer_set[i+input_K-1]-input_integer_set[i] < result:
            result = input_integer_set[i+input_K-1]-input_integer_set[i]
            
    return result

def MergeSort(input_set):
    SortSubvector(input_set, 0 , len(input_set)-1)

def SortSubvector(input_set, low , high):
    if high > low :
        mid = (high+low)//2
        SortSubvector(input_set, low, mid)
        SortSubvector(input_set, mid+1, high)
        Merge(input_set, low, mid, high)

def Merge (input_set, low, mid, high):
    L = input_set[low:mid+1]
    R = input_set[mid+1:high+1]
    L.append(999999999)
    R.append(999999999)
    i = 0
    j = 0
    for k in range(low, high+1):
        if L[i] <= R[j]: 
            input_set[k] = L[i]
            i = i+1
        else:
            input_set[k] = R[j]
            j = j+1

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw5.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()

    # 3. Solve
    input_k = int(input_list[0])
    input_set = input_list[1].split(',')
    input_set = [ int(s) for s in input_set ]
    answer = solution(input_k, input_set) 

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    outFile.write(str(answer))
    outFile.close()
