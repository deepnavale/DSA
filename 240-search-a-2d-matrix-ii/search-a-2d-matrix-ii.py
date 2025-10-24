class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        r=0
        c = len(matrix[0])-1

        while r<row and c>=0: 
            ele = matrix[r][c]
            if ele == target: 
                return True
            if ele>target:
                c-=1
            else: r+=1
        return False

                 

    