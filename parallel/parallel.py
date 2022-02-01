from math import sqrt, pow
import Queue
from mpiLib import MPI

import time


def distance(a, b):
  return sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2))



que = Queue.Queue() 


def bruteMin(points, current=float("inf")):
  if len(points) < 2: return current
  else:
    head = points[0]
    del points[0]
    newMin = min([distance(head, x) for x in points])
    newCurrent = min([newMin, current])
    return bruteMin(points, newCurrent)

def divideMin(points):
  half = len(sorted(points))/2
  a = Thread(target=lambda q, arg1: q.put(bruteMin(arg1)), args=(que, points[:half]))
  b = Thread(target=lambda q, arg1: q.put(bruteMin(arg1)), args=(que, points[half:]))
  a.start()
  b.start()
  a.join()
  b.join()

  a = que.get()
  b = que.get()
  minimum = min([a, b])
  nearLine = filter(lambda x: x[0] > half - minimum and x[0] < half + minimum, points)
  return min([bruteMin(nearLine), minimum])




list1 = []

counter = 1500

with open("testcases.txt", "a+") as rfile:
	data = rfile.readlines()

	for i in data[0:counter]:
		aa = i.split(",")
		list1.append((int(aa[0][1:]), int(aa[1][:-2])))

start = time.time()
print("MINIMUM CARTESIAN DISTANCE IS ", divideMin(list1))
end = time.time()

TIME = (end - start)

print("TIME TAKEN TO EXECUTE THE CODE IS ", TIME)
