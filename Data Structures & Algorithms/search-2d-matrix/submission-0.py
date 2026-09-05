class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_array = []
        for row in matrix:
            for num in row:
                new_array.append(num)
        low = 0
        high = len(new_array) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if new_array[mid] == target:
                return True
            elif new_array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False