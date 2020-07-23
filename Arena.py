class Arena(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    # checker is game is still running or not
    def is_over(self):
        if self.p1.alive and self.p2.alive:
            return False
        else:
            return True

    # return name of the winner
    def winner(self):
        if self.p1.alive:
            return self.p1.name
        elif self.p2.alive:
            return self.p2.name

    # return name of the looser
    def looser(self):
        if not self.p1.alive:
            return self.p1.name
        else:
            return self.p2.name

    # one decision round
    def round(self, player, p2, loop):
        player.decision(p2, loop)





