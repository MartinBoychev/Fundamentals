# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what,
# and that is exactly what you are called to do for this problem. On the first line, you will be given the population
# (numbers separated by comma and space ", "). On the second line, you will be given the minimum wealth. You should
# distribute the wealth so that no part of the population has less than the minimum wealth. To do that, you should
# always take wealth from the wealthiest part of the population. There will be cases where the distribution will not
# be possible. In that case, print: "No equal distribution possible".

population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)

if total_wealth < min_wealth * len(population):
    print("No equal distribution possible")
else:
    sorted_population = sorted(population, reverse=True)
    for i in range(len(sorted_population)):
        if sorted_population[i] >= min_wealth:
            break
        wealth_diff = min_wealth - sorted_population[i]
        wealth_to_transfer = min(wealth_diff, (total_wealth - min_wealth * len(population)) / i)
        sorted_population[i] += wealth_to_transfer
        total_wealth += wealth_to_transfer

    print(sorted_population)
