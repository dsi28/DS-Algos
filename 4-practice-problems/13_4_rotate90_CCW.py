#  rotate matrix 90 CCW

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def rotate_matrix_90_CCW(mtx):
    print('original ', mtx)
    # get transpose
    for i in range(len(mtx)):
        for j in range(i, len(mtx)): # with first i = 0 iteration, the j=0 column will be populated. so set the start of the range equal to i 
            mtx[i][j],mtx[j][i] = mtx[j][i],mtx[i][j]
    print('transpose ', mtx)
    # reverse columns
    for j in range(len(mtx)):
        for i in range(len(mtx) // 2):
            mtx[i][j],mtx[len(mtx)-i-1][j] = mtx[len(mtx)-i-1][j],mtx[i][j]
    print('90 CCW rotations ', mtx)

rotate_matrix_90_CCW(matrix)