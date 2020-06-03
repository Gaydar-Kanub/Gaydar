from typing import List


def workout(sessions: List[int], additional: int) -> int:
    deltas = []
    a = sessions[0]
    for b in sessions:
        deltas.append(b - a)
        a = b
    n = 1
    while additional > 0:
        deltas.sort(reverse=1)
        while deltas[0] / (n + 1) > deltas[1] and additional > n:
            n += 1
        if deltas[0] % (n + 1) == 0:
            deltas = deltas[1:] + [(deltas[0] // (n + 1))] * (n + 1)
        else:
            base_num = (deltas[0] // (n + 1) + 1)
            deltas = deltas[1:] + [base_num] * n + [deltas[0] - base_num * n]
        additional -= n
    deltas.sort(reverse=1)
    return deltas[0]


if __name__ == '__main__':
#     print("Example:")
#     print(workout([100, 200, 230], 1))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert workout([100, 200, 230], 1) == 50, "First"
#     assert workout([10, 13, 15, 16, 17], 2) == 2, "Second"
#     assert workout([9, 10, 20, 26, 30], 6) == 3, "Third"
# print("Coding complete? Click 'Check' to earn cool rewards!")
#     print(workout([10, 13, 15, 16, 17], 2))
#     print(workout([9, 10, 20, 26, 30], 6))
#     print(workout([100, 200, 230], 1))
#     print(workout([18,44,48,92,120,150,191,224,254,282,331,381,395,405,414,428,435,454,483,488,518,568,572,606,639,658,674,704,740,756,798,800,842,858,874,916,941,946,992,1036,1078,1108,1120,1140,1146,1148,1154,1163,1201,1223,1246,1262,1292,1298,1344,1381,1400,1440,1444,1462,1482,1514,1553,1572,1613,1653,1666,1684,1733,1766,1792,1803,1842,1885,1892,1902,1944,1979,2028,2073,2086,2135,2144,2185,2228,2269,2281,2304,2312,2357,2381,2392,2424,2426,2475,2501,2527,2536,2560,2569,2577,2609,2648,2682,2721,2765,2800,2808,2823,2873,2904,2930,2935,2936,2983,3008,3034,3043,3050,3092,3101,3143,3150,3172,3188,3195,3211,3245,3286,3292,3294,3337,3386,3398,3426,3441,3481,3498,3499,3535,3549,3592,3627,3668,3679,3698,3727,3751],424))
    print(workout([100, 200, 230], 5))