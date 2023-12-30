# rotate a matix 90 degrees

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def rotate_matrix_90_CW(mtx):
    print('original ', mtx)
    # get matrix transpose
    for i in range(len(mtx)):
        for j in range(i, len(mtx)):
            mtx[i][j],mtx[j][i] = mtx[j][i],mtx[i][j]
    print('transpose ', mtx)
    # reverse contents of each row
    # for row in mtx:
    #     row.reverse()
    for i in range(len(mtx)):
        for j in range(len(mtx) // 2):
            mtx[i][j],mtx[i][len(mtx)-j-1] = mtx[i][len(mtx)-j-1],mtx[i][j]
    print('90 CW rotation ', mtx)

rotate_matrix_90_CW(matrix)