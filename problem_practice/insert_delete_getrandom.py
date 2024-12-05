import random
# 274


class RandomizedSet:

    def __init__(self):
        self.data_dict = dict()
        self.idx_dict = dict() # for getrandom
        self.curr_idx = None

    def insert(self, val: int) -> bool:
        if val in self.data_dict:
            return False
        temp_idx = self.curr_idx+1 if self.curr_idx is not None else 0
        self.data_dict[val] = temp_idx
        self.idx_dict[temp_idx] = val
        self.curr_idx = temp_idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_dict:
            return False
        temp_idx = self.data_dict[val]
        del self.data_dict[val]
        del self.idx_dict[temp_idx]
        return True

    def getRandom(self) -> int:
        random_idx = random.choice(list(self.idx_dict.keys()))
        return self.idx_dict[random_idx]
