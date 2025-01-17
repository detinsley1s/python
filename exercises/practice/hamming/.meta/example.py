def distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strands must be of equal length.")

    return sum(a != b for a, b in zip(s1, s2))
