import sys
input = sys.stdin.readline

N, M = map(int, input().strip('\n').split())
pokemons = {}

for i in range(1, N+1):
    name = input().strip('\n')
    pokemons[i] = name
    pokemons[name] = i

for j in range(M):
    quiz = input().strip('\n')
    if quiz.isdigit():
        quiz = int(quiz)
    print(pokemons[quiz])