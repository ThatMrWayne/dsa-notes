#167


def twoSum(numbers, target: int):
    memo = {}
    for i in range(len(numbers)):
        if target-numbers[i] in memo:
            return [memo[target-numbers[i]]+1 ,i+1]
        else:
            memo[numbers[i]] = i
