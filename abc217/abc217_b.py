from sys import stdin

l = ['ABC', 'ARC', 'AGC', 'AHC']
l.remove(stdin.readline().rstrip())
l.remove(stdin.readline().rstrip())
l.remove(stdin.readline().rstrip())

print(l[0])
