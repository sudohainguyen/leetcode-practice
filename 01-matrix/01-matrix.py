import numpy as np

class Solution:
    def updateMatrix(self, mat):
        # Set-Up:
        m, n = len(mat), len(mat[0])
        dm = np.array(mat) * (m + n)

        def rows_columns_scan(dm):
            """Update min distance for rows, then columns"""
            for i in range(1, m):
                dm[i, :] = np.minimum(dm[i - 1, :] + 1, dm[i, :])
            for j in range(1, n):
                dm[:, j] = np.minimum(dm[:, j - 1] + 1, dm[:, j])

        # Scan distane matrix, then scan it rotated 180 degrees:
        rows_columns_scan(dm)
        rows_columns_scan(np.rot90(dm, 2))

        return dm