class Solution(object):
    def findAnagrams(self, s, p):
        indices = list()
        l = 0
        r = len(p) - 1
        w_counter = Counter(s[l:r + 1])
        p_counter = Counter(p)
        if w_counter == p_counter:
            indices.append(l)
        while r < len(s) - 1:
            r += 1
            w_counter[s[r]] += 1
            w_counter[s[l]] -= 1
            if w_counter[s[l]] == 0:
                del w_counter[s[l]]
            l += 1
            if w_counter == p_counter :
                indices.append(l)    
        return indices
