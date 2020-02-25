def jaccard (first, second):
    fcount = 0 
    scount = 0
    for f in first:
        if f in second:
            scount += 1
    fcount = len(first)+len(second)
    score = float(scount) / float(fcount)
    return score
