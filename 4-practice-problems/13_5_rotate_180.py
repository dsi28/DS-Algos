# rotate matrix 180 degrees
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate_matrix_180(mtx):
    print('original ', mtx)
    # reverse row
    for i in range(len(mtx)):
        for j in range(len(mtx) // 2):
            mtx[i][j],mtx[i][len(mtx) - j - 1] = mtx[i][len(mtx) - j - 1],mtx[i][j]
    print('reverse rows ', mtx)
    # reverse columns
    for j in range(len(mtx)):
        for i in range(len(mtx) // 2):
            mtx[i][j],mtx[len(mtx) - i - 1][j] = mtx[len(mtx) - i - 1][j],mtx[i][j]
    print('180 degree rotation ', mtx)   

rotate_matrix_180(matrix) 