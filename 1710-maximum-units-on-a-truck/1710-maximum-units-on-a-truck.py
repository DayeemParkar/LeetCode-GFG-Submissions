class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans, ptr = 0, 0
        while truckSize > 0 and ptr < len(boxTypes):
            boxes = min(truckSize, boxTypes[ptr][0])
            units = boxes * boxTypes[ptr][1]
            ans += units
            truckSize -= boxes
            ptr += 1
        return ans