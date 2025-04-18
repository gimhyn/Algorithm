def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

n, m = map(int, input().split())
truth = list(map(int, input().split()))
truth_people = truth[1:]

parent = [i for i in range(n+1)]
parties = []

for _ in range(m):
    party = list(map(int, input().split()))
    party_people = party[1:]
    parties.append(party_people)
    for i in range(len(party_people) - 1):
        union(party_people[i], party_people[i+1])

# 진실을 아는 사람들의 root를 따로 저장
truth_roots = set(find(person) for person in truth_people)

# 각 파티에서 진실을 아는 사람의 root와 겹치지 않으면 거짓말 가능
count = 0
for party in parties:
    if not any(find(person) in truth_roots for person in party):
        count += 1

print(count)
