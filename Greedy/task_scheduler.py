"""
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.


"""
from typing import List
import collections

"""
1- Greedy

Example 
    have following tasks : 3 A, 2 B, 1 C. and we have n = 2. 
    We should first arrange A, and then B and C. Imagine there are "slots" and we need to arrange tasks by putting them into "slots". Then A should be put into slot 0, 3, 6 since we need to have at least n = 2 other
    tasks between two A. After A put into slots, it looks like this:

    A ? ? A ? ? A
    "?" is "empty" slots.

    Now we can use the same way to arrange B and C. The finished schedule should look like this:

    A B C A B # A
    "#" is idle
    
    let's call this process, `slot_filling`

NOTE: Building such list needs more space and complexity, but that way should be purpose of an interview.

here is the shorter solution:
    the most frequent tasks occurs `most_freq` times
    and there are `most_freq_count` of them.
    
    by doing `slot_filling` for first one:
        
        number_of_idle = (most_freq - 1) * n
        total_slots_for_most_freq = most_freq + number_of_idle
    
    if we have several tasks with same `most_freq` time, you can image we need to do the `slot_filling` but by shifting 1 to the right, then we need 1 more slot per each
    
        total_slots = total_slots_for_most_freq + (most_freq_count - 1)
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(collections.Counter(tasks).values())

        most_freq = max(task_counts)
        most_freq_count = task_counts.count(most_freq)
        number_of_idle = (most_freq - 1) * n
        total_slots_for_most_freq = most_freq + number_of_idle

        total_slots = total_slots_for_most_freq + (most_freq_count - 1)

        # e.g total_slots for ["A","A","B","C","D","E","F","G"] is 4, then we need max(len(task), total_slots)
        return max(len(tasks), total_slots)
