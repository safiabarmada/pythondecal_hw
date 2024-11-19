import numpy as np

#The Odd Ones Out
arr = np.array([[1,2,3],[5,7,9],[2,4,6], [7,7,7]])
def onlyOdd(arr):
    odd_rows = np.all(arr % 2 != 0, axis=1)
    print(odd_rows)
    return arr[odd_rows]
    #result = np.array([])
    #for row in (arr):
        ##row = np.array([all(x % 2 != 0) for x in row])
        #result = np.append(result, row)
    #return result
    
print(onlyOdd(arr))

#Let's play checkers
#2.1
checkerboard = np.empty((8,8))
#2.2
checkerboard[0:8:2] = [1,0,1,0,1,0,1,0]
#2.3
checkerboard[1:7:2] = [0,1,0,1,0,1,0,1]
print(checkerboard)
#2.4
reverse_checkerboard = np.empty((8,8))
reverse_checkerboard[1:7:2] = [1,0,1,0,1,0,1,0]
reverse_checkerboard[0:8:2] = [0,1,0,1,0,1,0,1]
print(reverse_checkerboard)

#the expanding universe
def expansion(phrase,i):
    array = np.char.join(" "*i, phrase)
    return array

universe = np.array(['galaxy','clusters'])
print(expansion(universe,2))


#4
np.random.seed(42)
planets = np.random.randint(100,1000,(5,5))
print(planets)
def secondLargest(word):
    sorted = np.sort(word)
    result1 = np.array([sorted[:,1]])
    return result1

    
print(secondLargest(planets))