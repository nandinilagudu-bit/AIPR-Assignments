def find_common(a, b):
    return list(set(a) & set(b))
print(find_common([10, 20, 30, 40, 50], [40, 50, 60, 70, 80]))