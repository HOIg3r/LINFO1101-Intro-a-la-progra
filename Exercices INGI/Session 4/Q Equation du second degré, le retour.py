def solveur(lst):
    result = []
    for i in lst:
        result.append(solution(i[0],i[1],i[2]))
    return result