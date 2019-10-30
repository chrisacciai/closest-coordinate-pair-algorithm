import math

class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distance
    # and return that value from this method
    #
    # @return the distance between the closest pair 
    def compute(self, file_data):
        pairs = self.coordStrToArr(file_data)
        sortedPairs = self.quickSortX(pairs)
        return  self.findClosestPair(sortedPairs)[0]

    # Converts the input list of strings into a list of tuples that contain
    # the coordinate points as a pair of floats.
    #
    # @return the list of coordinate tuples.
    def coordStrToArr(self, file_data):
        coordArr = []
        for i in range(0, len(file_data)):
            coords = file_data[i].split()
            coordArr.append([float(coords[0]),float(coords[1])])
        return coordArr

    # Recursively executes the closest pair algorithm
    #
    # @return minimum distance between any points in the list and the sorted list
    def findClosestPair(self, pairs):
        n = len(pairs)
        midpoint = n/2

        if (n <= 3):
            return self.baseCase(pairs)

        leftPairs = pairs[0:midpoint]
        rightPairs = pairs[midpoint:]

        left = self.findClosestPair(leftPairs)
        right = self.findClosestPair(rightPairs)

        leftMin = left[0]
        leftSorted = left[1]

        rightMin = right[0]
        rightSorted = right[1]

        minDist = min(leftMin, rightMin)

        mergeSorted = []
        runwayPoints = []

        i = 0
        j = 0
        while (i < len(leftSorted) and j < len(rightSorted)):
            if (min(leftSorted[i][1], rightSorted[j][1]) == leftSorted[i][1]):
                mergeSorted.append(leftSorted[i])
                if ((midpoint) - minDist <= leftSorted[i][0] <= midpoint + minDist):
                    runwayPoints.append(leftSorted[i])
                i+=1
            else:
                mergeSorted.append(rightSorted[j])
                if ((midpoint) - minDist <= rightSorted[j][0] <= midpoint + minDist):
                    runwayPoints.append(rightSorted[j])
                j+=1

        if (j < len(rightSorted)):
            for t in range(j, len(rightSorted)):
                mergeSorted.append(rightSorted[t])
        else:
            for t in range(i, len(leftSorted)):
                mergeSorted.append(leftSorted[t])

        runwayMin = leftMin
        for i in range(0, len(runwayPoints)):
            for j in range(1, 16):
                if ((i + j) < len(runwayPoints)):
                    distance = self.distance(runwayPoints[i], runwayPoints[i + j])
                    if (distance < runwayMin):
                        runwayMin = distance

        return (min(runwayMin, minDist), mergeSorted)

    # Performs a quick sort algorithm based on the value of the x
    # coordinates of the pairs.
    #
    # @return the list of coordinates sorted by x value
    def quickSortX(self, arr):
        p = 0 
        if len(arr) <= 1:
            return arr

        for i in range(1, len(arr)):
            if arr[i][0] <= arr[0][0]:
                p += 1
                temp = arr[i]
                arr[i] = arr[p]
                arr[p] = temp

        temp = arr[0]
        arr[0] = arr[p]
        arr[p] = temp
        
        leftArr = self.quickSortX(arr[0:p])
        rightArr = self.quickSortX(arr[p+1:len(arr)])

        arr = leftArr + [arr[p]] + rightArr
        
        return arr

    # Performs a quick sort algorithm based on the value of the y
    # coordinates of the pairs.
    #
    # @return the list of coordinates sorted by y value
    def quickSortY(self, arr):
        p = 0 
        if len(arr) <= 1:
            return arr

        for i in range(1, len(arr)):
            if arr[i][1] <= arr[0][1]:
                p += 1
                temp = arr[i]
                arr[i] = arr[p]
                arr[p] = temp

        temp = arr[0]
        arr[0] = arr[p]
        arr[p] = temp
        
        leftArr = self.quickSortY(arr[0:p])
        rightArr = self.quickSortY(arr[p+1:len(arr)])

        arr = leftArr + [arr[p]] + rightArr
        
        return arr

    # Computes the distance between two coordinate points
    #
    # @return the float value of the distance between two coordinates
    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    # This base case method is called when the findClosestPair algorithm
    # recurses to 2 or 3 pairs left in the list. It then sorts the pairs 
    # by y value and finds the mininum distance between the points.
    #
    # @return a tuple containing the minimum distance between the points and the sorted list
    def baseCase(self, basePairs):
        ySorted = self.quickSortY(basePairs) 
        minDist = 9999999999999
        for i in range(len(basePairs)):
            for t in range(i + 1, len(basePairs)):
                tempDist = self.distance(basePairs[i], basePairs[t])
                if (tempDist < minDist):
                    minDist = tempDist
        
        return minDist, ySorted
                    
