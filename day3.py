# Jacobus Burger (2022)
from functools import reduce
from string import ascii_letters


class Solution:
    def parse(self, filename="day3.txt"):
        with open(filename, 'r') as file:
            return [
                sack.strip('\n')
                for sack in file.readlines()
            ]


    def part1(self, filename="day3.txt"):
        sacks = self.parse(filename)
        total = 0
        for sack in sacks:
            # find common character (item type) in both compartments
            A = set(sack[:len(sack) // 2])  # compartment 1
            B = set(sack[len(sack) // 2:])  # compartment 2
            item = A.intersection(B).pop()  # common item

            # add common item type priority to total
            total += ascii_letters.index(item) + 1
        return total


    def part2(self, filename="day3.txt"):
        sacks = self.parse(filename)
        total = 0
        # iterate 3 sacks at a time (one group at a time)
        for i in range(0, len(sacks), 3):
            group = sacks[i:i + 3]
            badge = reduce(set.intersection, map(set, group)).pop()
            total += ascii_letters.index(badge) + 1
        return total





day3 = Solution()
solutions = [day3.part1(), day3.part2()]
print(solutions)
