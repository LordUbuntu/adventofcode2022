# Jacobus Burger (2022)


class Solution:
    def part1(self, file="day1.txt"):
        # record total calories of each elf inventory
        calories = [
            sum(map(int, inventory.strip().split('\n')))
            for inventory in open(file, 'r').read().split("\n\n")
        ]
        # find the maximum
        return max(calories)


    def part2(self, file="day1.txt"):
        # record total calories of each elf inventory
        calories = [
            sum(map(int, inventories.strip().split('\n')))
            for inventories in open(file, 'r').read().split("\n\n")
        ]
        # reverse sort calores (first 3 are top 3)
        calories.sort(reverse=True)
        # take the first 3 and return their sum
        return sum(calories[:3])
