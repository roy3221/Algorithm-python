class NimGame(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 != 0:
            return True
        return False