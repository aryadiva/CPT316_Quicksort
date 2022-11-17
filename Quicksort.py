import os as p
import datetime

# for timing the run time
#start = timeit.default_timer()

# Quick sort in Python

# file processing -------------------------------------------------
def datasrc():
  #reading fromfile
  f = open('Data.txt', 'r')
  data=f.readlines()
  f.close()
  return data

#outputting data
def dataoutput(input):
  #checking if destination file existed or not
  file_status=p.path.exists('Quick_Output.txt')
  if(file_status == True):
    p.remove('Quick_Output.txt')

  #outputting to .txt file
  with open('Quick_Output.txt', 'w') as f1:
    f1.writelines(input)
  f1.close

#creating a variable based on the return value of function
data = datasrc()

#-------------------------------------------------------------------
start = datetime.datetime.now()

def partitioning(arr, start, end):
  pivot = arr[start]
  lowindex = start + 1
  highindex = end

  while True:
    # If the current value is larger than the pivot
    # it's on the right side of the pivot and we can move left, to the next element.
    # We also need to make sure we haven't surpassed the low pointer, since that
    # indicates we have already moved all the elements to the correct side of the pivot
    while lowindex <= highindex and arr[highindex] >= pivot:
      highindex = highindex - 1

    # Opposite process from above
    while lowindex <= highindex and arr[lowindex] <= pivot:
      lowindex = lowindex + 1

    # We will either found a value for both high and low that is out of order
    # or low is higher than high, in which case we ca exit the loop
    if lowindex <= highindex:
      arr[lowindex], arr[highindex] = arr[highindex], arr[lowindex]
      # The loop continues if above conditions persist
    else:
      # We exit the loop
      break

  arr[start], arr[highindex] = arr[highindex], arr[start]
  return highindex;

def quick_sort(arr, start, end):
  if start >= end:
    return

  p = partitioning(arr, start, end)
  quick_sort(arr, start, p-1)
  quick_sort(arr, p+1, end)

#--------------------------------------------------------------------

quick_sort(data, 0, len(data)-1)

# display the runtime
stop = datetime.datetime.now()

dataoutput(data)
time_diff = stop-start
execution_time=time_diff.total_seconds()*1000
print('Run Time(ms): ', execution_time)
