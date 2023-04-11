"""CL02"""

def sum(xs: list[int]) -> int:
    sum_total: int = 0
    for idx in xs:
        sum_total += xs[idx]
    return sum_total