# get matrix transpose

matrix = [[1,2,3],[4,5,6],[7,8,9]]

def transpose_matrix(mtx):
    for i in range(len(mtx)):
        for j in range(i, len(mtx)):
            mtx[i][j],mtx[j][i] = mtx[j][i],mtx[i][j]

print('original ', matrix)
transpose_matrix(matrix)
print('transpose ', matrix)