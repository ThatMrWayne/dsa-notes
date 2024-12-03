# 12
# TC: O(1)
# SC: O(1)


def intToRoman(nums: int) -> str:
        d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        r = ""
        # >= 1000
        if nums >= 1000:
            rem = nums//1000
            temp = rem*d[1000]
            r+=temp
            nums = nums%1000
        # 100~900
        if 100 <= nums <= 999:
            rem = nums//100
            if rem == 4:
                temp = d[100]+d[500]
            elif rem == 9:
                temp = d[100]+d[1000]
            elif rem >= 5:
                temp = d[500] + (rem-5)*d[100]
            else:
                temp = rem*d[100]
            r+=temp
            nums = nums%100
        if 10 <= nums <= 99:
            rem = nums//10
            if rem == 4:
                temp = d[10]+d[50]
            elif rem == 9:
                temp = d[10]+d[100]
            elif rem >= 5:
                temp = d[50] + (rem-5)*d[10]
            else:
                temp = rem*d[10]
            r+=temp
            nums = nums%10
        if 1 <= nums <= 9:
            rem = nums
            if rem == 4:
                temp = d[1]+d[5]
            elif rem == 9:
                temp = d[1]+d[10]
            elif rem >= 5:
                temp = d[5] + (rem-5)*d[1]
            else:
                temp = rem*d[1]
            r+=temp

        return r
