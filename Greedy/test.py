from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 3개 뽑음, 순열
print(result)

result = list(combinations(data, 2)) # 2개 뽑음, 조합
print(result)

result = list(product(data, repeat=2)) # 2개 뽑음, 중복 순열
print(result)

result = list(combinations_with_replacement(data, 2)) # 2개 뽑음, 중복 조합
print(result)
