class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
# If I have an even number, I can always pick 1 to hand an odd number to the opponent.
# The opponent can only pick an odd number, thus handing back an even number.
# The first one to hit 1 will lose.
# Thus as long as I start with an even number I can win.
# On the contrary, I lose with an odd number to start.
