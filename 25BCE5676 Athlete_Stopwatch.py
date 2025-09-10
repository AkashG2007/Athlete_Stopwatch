 #stopwatch
l=[]
previous=0
import time
def stopwatch():
    a=input("Enter q to stop the timer:")
    if a=="q":
        m=time.time()
    return m
t=int(input("How many rounds do you wanna run?:"))
for i in range(t):
      b=input(f"Enter q to start the timer for round {i+1} :")
      if b=="q":
          start=time.time()
          end=stopwatch()
      timed=end-start
      print("The time taken is",timed)
      if previous!=False:
          if previous>timed:
              print("Congrates! the time difference between your previous and this run is:",previous-timed)
          else:
              print("Oh no! you took longer,the time difference is",timed-previous)
      previous=timed
      l.append(previous)
o=min(l)
print("wow! your fastest time was",o)

    
