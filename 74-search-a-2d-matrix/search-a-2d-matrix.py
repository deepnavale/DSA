class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l=0
        row=len(matrix)
        col=len(matrix[0])
        r=row*col-1

        while l<=r:
            mid = l+(r-l)//2
            mat_row=mid//col
            mat_col=mid%col

            if matrix[mat_row][mat_col]==target:
                return True
            if matrix[mat_row][mat_col]<target:
                l=mid+1
            else: r=mid-1
            
        return False