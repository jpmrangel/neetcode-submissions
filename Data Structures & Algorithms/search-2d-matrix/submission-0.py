class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        l, r = 0, m
        row, col = 0, 0

        contains=False
        while l <= r:
            row = (l+r)//2
            if target >= matrix[row][0] and target <= matrix[row][n]:
                contains=True
                break;
            elif target < matrix[row][0]:
                r=row-1
            elif target > matrix[row][n]:
                l=row+1
        
        if not contains:
            return False

        l, r = 0, n
        while l <= r:
            col = (r+l)//2
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r=col-1
            elif target > matrix[row][col]:
                l=col+1
        return False