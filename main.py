import sys
import time
from closest_pair import ClosestPair

fp = open("test1.txt", 'r')
lines = fp.readlines()


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
cp = ClosestPair()
print(cp.compute(lines))
end = time.time()
print("time: "+ str(end-start))