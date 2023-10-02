def matrix_chain_multiplication(dims):
    n = len(dims) - 1  
    m = [[0] * n for _ in range(n)] 
    s = [[0] * n for _ in range(n)]  

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return s, m


def print_optimal_parenthesis(s, i, j):
    if i == j:
        print(f'M{str(i)}', end='')
    else:
        print('(', end='')
        print_optimal_parenthesis(s, i, s[i][j])
        print_optimal_parenthesis(s, s[i][j] + 1, j)
        print(')', end='')



matrices = [(2, 3), (3, 4), (4, 2)]
split, min_scalar_mult = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", end=' ')
print_optimal_parenthesis(split, 0, len(matrices) - 2)
print("\nMinimum Scalar Multiplications:", min_scalar_mult[0][-1])
