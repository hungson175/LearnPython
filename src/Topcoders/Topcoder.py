# import functools
#
#
# class MountainRanges:
#     def countPeaks(self, heights):
#         # h = list(heights)
#         # h.insert(0, 0)
#         # h.insert(len(h), 0)
#         # cnt = 0
#         # print(h)
#         # for i in range(1, len(h) - 1):
#         #     if h[i] > h[i - 1] and h[i] > h[i + 1]:
#         #         cnt += 1
#         # return cnt
#         h = list((0,) + tuple(heights) + (0,))
#         peaks = filter(lambda i: h[i] > h[i-1] and h[i] > h[i+1], range(1,len(h)-1))
#         return len(list(peaks))
#
# print(MountainRanges().countPeaks([1,2,1,2]))
#
#
import functools


def maxElem(l: list):
    if l is None or len(l) == 0:
        return None
    return functools.reduce(lambda mx, x: x if x > mx else mx, l, l[0])


class DNASequence:

    def longestDNASequence(self, sequence):
        cnt = 0
        for c in sequence:
            if c in 'ACGT':
                cnt += 1
                rs = max(rs, cnt)
            else:
                cnt = 0
        return rs



print(DNASequence().longestDNASequence('AGT'))
