class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = goat = 0
        for i in range(len(gas)):
            goat += gas[i] - cost[i]

            if goat < 0:
                goat = 0
                start = i + 1
        return start