class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        m = len(players)
        n = len(trainers)
        i = j =0
        while i<m and j<n:
            if trainers[j]>= players[i]:
                i+=1
            j+=1
        return i