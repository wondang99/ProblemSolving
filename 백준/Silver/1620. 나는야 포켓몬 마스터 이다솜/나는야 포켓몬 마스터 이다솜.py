import sys
from collections import defaultdict

N, M = list(map(int,sys.stdin.readline().rstrip("\n").split()))

pokemon = defaultdict(str)
for i in range(N) :
    pokemon[i] = sys.stdin.readline().rstrip("\n")
reverse_pokemon = dict(map(reversed,pokemon.items()))

for i in range(M) :
    quiz = sys.stdin.readline().rstrip("\n")
    if quiz.isdigit() :
        print(pokemon[int(quiz)-1])
    else :
        print(reverse_pokemon[quiz]+1)