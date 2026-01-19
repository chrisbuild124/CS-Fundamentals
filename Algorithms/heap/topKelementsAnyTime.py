# This is not a leetcode problem
# This was on an interview OA that I did not solve
# but I figured it out after some time. 

# Basically, the situation is - there are multiple roles in
# the company (engineer, HR, manager, etc). For each role, the
# amount of time for each employee was given per day. However, each
# employee can get additional time, so the amounts per day change. 

# Goal: To find the top k elements in a role at any given time.
# Keep in mind each person's time can change, so keeping a heap
# cannot work the entire time.

from collections import defaultdict
import heapq

class Employees:
  """
  All employees for the company. 
  Keeps track of max k times for each employee. 
  """
  def __init__(self):
    self.id_to_time = defaultdict(int) # Maps employee's id to the time
    self.id_to_role = {} # Maps employee's id to role
    self.role_to_heap = defaultdict(list)

  def add_employee(self, role, id):
    self.id_to_role[id] = role

  def add_time(self, id, time):
    self.id_to_time[id] -= time
    heapq.heappush(self.role_to_heap[self.id_to_role[id]], (self.id_to_time[id], id))

  def top_k_employees(self, role, k):
    heap = self.role_to_heap[role]
    tmp = []
    res = []

    while heap and k:
      time, id = heapq.heappop(heap)
      if self.id_to_time[id] != time: # Invalidates incorrect times in the heap
        continue
      tmp.append((id, time))
      res.append(str(time * -1) + '(' + f'{id}' + ')') # Each id is lexigraphically ordered
      k -= 1

    while tmp:
      time, id = tmp.pop()
      heapq.heappush(heap, (time, id))
      
    return res  
