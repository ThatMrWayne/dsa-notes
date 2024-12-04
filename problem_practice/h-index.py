# 274


def hIndex(citations) -> int:
    citations.sort(reverse=True)
    h=len(citations)
    cnt = 0
    for num in citations:
        while num < h and h > cnt:
            h-=1
        if h == cnt:
            return h
        cnt+=1
        if cnt >= h:
            return h
