# 38
# TC : O()
# SC : O(n)


# iterative
def countAndSay(n: int) -> str:
    memo = ["1"]
    for i in range(1, n):
        s = memo[i-1]
        result = ""
        record = set()
        for i in range(len(s)):
            if i not in record:
                curr, next_ = i, i+1
                cnt = 1
                while next_ < len(s):
                    if s[curr] == s[next_]:
                        cnt += 1
                        record.add(next_)
                        curr += 1
                        next_ += 1
                    else:
                        break
                result += (str(cnt)+s[curr])
        memo.append(result)
    return memo[-1]


# recursive
def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    else:
        s = countAndSay(n-1)
        result = ""
        record = set()
        for i in range(len(s)):
            if i in record:
                continue
            curr, next_ = i, i+1
            cnt = 1
            while next_ < len(s):
                if s[curr] == s[next_]:
                    cnt += 1
                    record.add(next_)
                    curr += 1
                    next_ += 1
                else:
                    break
            result += (str(cnt)+s[curr])
        return result
