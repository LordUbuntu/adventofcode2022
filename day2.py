# Jacobus Burger (2022)



class Solution:
    def parse(self, filename):
        with open(filename, 'r') as f:
            strategies = [
                line.strip('\n').split()
                for line in f.readlines()
            ]
            return strategies


    def part1(self, filename="day2.txt"):
        strategies = self.parse(filename)
        total_score = 0
        for strategy in strategies:
            # get values for shapes (A = 1, B = 2, C = 3. X = 1, Y = 2, Z = 3)
            opponent = ord(strategy[0]) - ord('A') + 1
            shape = ord(strategy[1]) - ord('X') + 1

            # score game
            if opponent - shape == -1 or opponent - shape == 2:
                total_score += shape + 6  # win
            if opponent == shape:
                total_score += shape + 3  # tie
            if opponent - shape == 1 or opponent - shape == -2:
                total_score += shape + 0  # lose
        return total_score


    def part2(self, filename="day2.txt"):
        strategies = self.parse(filename)
        total_score = 0
        for strategy in strategies:
            # get opponent move and play of round
            opponent = ord(strategy[0]) - ord('A') + 1
            play = strategy[1]

            if play == 'X':
                # lose
                shape = (opponent - 1) if opponent > 1 else 3
                total_score += shape + 0
            if play == 'Y':
                # draw
                total_score += opponent + 3
            if play == 'Z':
                # win
                shape = (opponent + 1) if opponent < 3 else 1
                total_score += shape + 6
        return total_score


day2 = Solution()
solutions = [day2.part1(), day2.part2()]
print(solutions)
