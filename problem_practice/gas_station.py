# 134
# TC: O(n)
# SC: O(1)
"""
Can't forget this cuz I solved this in Japan
"""



def canCompleteCircuit(self, gas, cost) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    start_idx = None
    for idx in range(len(gas)):
        start_idx = idx if start_idx is None else start_idx
        total = gas[idx]+total-cost[idx]
        if total < 0:
            total = 0
            start_idx = None
    return start_idx
