# 867. Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        c_new = len(matrix)
        r_new = len(matrix[0])
        
        matrix_return = []
        for i in range(0, r_new):
            row = []
            for j in range(0, c_new):      
                row.append(matrix[j][i])
            matrix_return.append(row)
        return matrix_return