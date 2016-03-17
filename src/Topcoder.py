import functools


class MountainRanges:
    def countPeaks(self, heights):
        # h = list(heights)
        # h.insert(0, 0)
        # h.insert(len(h), 0)
        # cnt = 0
        # print(h)
        # for i in range(1, len(h) - 1):
        #     if h[i] > h[i - 1] and h[i] > h[i + 1]:
        #         cnt += 1
        # return cnt
        h = list((0,) + tuple(heights) + (0,))
        return len(filter(lambda i: h[i] > h[i-1] and h[i] > h[i+1], range(1,len(h)-1)))

print(MountainRanges().countPeaks([1]))
