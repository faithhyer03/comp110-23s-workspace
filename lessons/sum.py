"""CL02"""

def sum(xs: list[int]) -> int:
    sum_total: float = 0.0
    for item in xs:
        sum_total += item
    return sum_total