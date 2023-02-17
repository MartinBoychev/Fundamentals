# You are a mad scientist, and you have decided to play with electron distribution among atom shells. The basic idea
# of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons. You
# will receive a single integer - the number of electrons. Your task is to fill shells until there are no more
# electrons left. The rules for electron distribution are as follows: The maximum number of electrons in a shell can
# be 2n2, where n is the position of a shell (starting from 1). For example, the maximum number of electrons in the
# 3rd shield can be 2*32 = 18. You should start filling the shells from the first one at the first position. If the
# electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so
# on. In the end, print a list with the filled shells.

num_electrons = int(input())
shells = []
n = 1

while num_electrons > 0:
    max_electrons = 2 * n ** 2
    if num_electrons >= max_electrons:
        shells.append(max_electrons)
        num_electrons -= max_electrons
    else:
        shells.append(num_electrons)
        num_electrons = 0
    n += 1

print(shells)
