def solve_koshi(a, b):
    arith_mean = (a + b) / 2
    geom_mean = (a * b) ** 0.5

    if arith_mean > geom_mean:
        return ">"
    elif arith_mean < geom_mean:
        return "<"
    else:
        return "="

a, b = map(int, input().split())
result = solve_koshi(a, b)
print(result)