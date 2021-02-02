class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dict_ = dict()
        lens = len(s)
        lent = len(t)
        for i in range(lent):
            if t[i] in dict_:
                dict_[t[i]].append(i)
            else:
                dict_[t[i]] = [i]
        cur_max_index = lent
        for i in range(lens-1, -1, -1):
            if s[i] not in dict_:
                return False
            if not dict_[s[i]]:
                return False
            if dict_[s[i]][-1] < cur_max_index:
                cur_max_index = dict_[s[i]][-1]
                dict_[s[i]].pop()
            else:
                return False
        return True
