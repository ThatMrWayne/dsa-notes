import random
# 380


class RandomizedSet:

    def __init__(self):
        self.data_dict = dict()
        self.data_arr = [] # for getrandom

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False
        self.data_dict[val] = len(self.data_arr)
        self.data_arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_dict:
            return False
        rm_idx = self.data_dict[val]
        last_item = self.data_arr[-1]
        self.data_arr[rm_idx], self.data_arr[-1] = self.data_arr[-1], self.data_arr[rm_idx]
        self.data_arr.pop()
        self.data_dict[last_item] = rm_idx
        del self.data_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_arr)
