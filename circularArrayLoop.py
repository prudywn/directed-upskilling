class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def getNextIndex(current):
            return current + nums[current]

        for i in range(n):
            if nums[i] == 0:
                continue #visited
            
            direction = 1 if nums[i] > 0 else -1
            slow = i
            fast = getNextIndex(i)

            while (nums[fast] * direction > 0 and
                   nums[getNextIndex(fast)] * direction > 0):
                if slow == fast:
                    if slow == getNextIndex(slow):
                        break  #// single-element loop, invalid
                    return True
                
                slow = getNextIndex(slow)
                fast = getNextIndex(getNextIndex(fast))
            
            marker = i
            while direction * nums[marker] > 0:
                next_marker = getNextIndex(marker)
                nums[marker] = 0 # mark as visited
                marker = next_marker
        return False #no valid cycle

        

