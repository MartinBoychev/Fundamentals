# Calculate how many courses will be needed to elevate N persons by using
# an elevator with a capacity of P persons.
# The input holds two lines: the number of the people N and the capacity P of the
# if elevator is None:

N = int(input())
P = int(input())

if N % P == 0:
    print(int(N/P))
else:
    print(int(N/P) + 1)
