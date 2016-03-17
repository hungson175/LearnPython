
def count(s, i, j):
    length = j - i + 1
    cnt = 0
    for k in range(j + 1, len(s)):
        if k + length <= len(s):
            if s[i:j + 1] == s[k:k + length]:
                cnt += 1
    return cnt


class EqualSubstrings2:
    def get(self, s):
        cnt = 0
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                cnt += count(s,i,j)

        return cnt

print(EqualSubstrings2().get("abab"))
