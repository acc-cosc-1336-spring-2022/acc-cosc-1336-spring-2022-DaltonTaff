def get_p_distance(list1, list2):
    i = 0
    di = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            di += 1
        i += 1
    p_dist = di / len(list1)
    return p_dist

def get_p_distance_matrix(list1):
    p_distance_matrix = []
    for r in list1:
        row = []
        for c in list1:
            row.append(get_p_distance(r,c))
        p_distance_matrix.append(row)
    return p_distance_matrix
