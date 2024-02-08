def pascaltri(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
def pascaltriangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1])*2 - 1))
triangle_5_steps = pascaltri(5)
pascaltriangle(triangle_5_steps)

print("AdarshAgrawal")
