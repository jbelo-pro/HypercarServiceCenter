gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())

print(set.union(*[gryffindor, ravenclaw, slytherin, hufflepuff]))
