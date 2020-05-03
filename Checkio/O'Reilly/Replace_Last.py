def replace_last(roster):
    if len(roster) > 1:
        res = [roster[-1]] + roster[:-1]
    else:
        res = roster
    return res
