class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bin search
        start = 0
        end = len(nums)
        prevS = 0
        prevE = 0
        mid = (start + end) // 2
        
        while start <= end:
            if prevS == start and prevE == end:
                break
            else:
                prevS = start
                prevE = end
                if target < nums[mid]:
                    end = mid
                    mid = (start + end) // 2
                elif target > nums[mid]:
                    start = mid
                    mid = (start + end) // 2
                else:
                    break
        if nums[mid] > target:
            if mid == 0:
                return mid
            return mid - 1
        elif nums[mid] < target:
            return mid + 1
        else:
            return mid