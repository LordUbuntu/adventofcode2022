# Jacobus Burger (2022)



class Solution:
    def __doc__(self):
        return """
        # Advent of code, day 2 solutions.

        I realized that I could map each move (rock, paper, scissors) to an
        accompanying value (1, 2, 3) and then use some basic arithmetic to
        determine the score.



        ## Part 1

        ### Explanation

        We win when the opponent move is "behind" our move by 1 or by 2. In
        principle, the moves Rock, Paper, and Scissors can be seen as a cyclic
        directed graph with R < P < S < R as the relation between each move.
        Arithmetically, if opponent chooses Rock (1), then subtracting that
        from the winning move Paper (2) would result in a 1. This follows along
        the entire chain except when they play Scissors (3) and we play
        rock (1) in which case we get -2 instead.

        As a consequence, the three states (win, tie, lose) are determined
        by if `opponent - shape is -1 or 2`, `opponent is shape`, or
        if `opponent - shape is 1 or -2`.

        ### Pseudocode

        ```
        foreach round
            opponent = ascii value of opponent move offset by 'A'
            shape = ascii value of our move offset by 'X'

            if opponent - shape is -1 or 2 then
                score = shape + 6
            if opponent is shape then
                score = shape + 3
            if opponent - shape is 1 or -2 then
                score = shape + 0
        ```



        ## Part 2

        ### Explanation

        The same logic applies but this time in reverse. We know the value of
        the opponent and we know the strategy we want to play, so to find the
        shape for each condition we:
        * lose: shape = opponent - 1 if opponent is > 1 otherwise 3
        * tie: shape = opponent
        * win: shape = opponent + 1 if opponent is < 3 otherwise 1

        ### Pseudocode

        ```
        foreach round
            opponent = ascii value of opponent move offset by 'A'

            if move is 'X' then
                shape = opponent - 1 if opponent is > 1 otherwise 3
                score = shape + 0
            if move is 'Y' then
                shape = opponent
                score = shape + 3
            if move is 'Z' then
                shape = opponent + 1 if opponent is < 3 otherwise 1
                score = shape + 6
        ```
    """
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
