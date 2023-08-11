class Solution(object):
    def minWindow(self, s, t):
        # keeps track of elements in t
        t_counter = Counter(t)
        # keeps track of relevant elements in current window
        window = Counter()
        # keeps track of shortest substring
        shortest = s
        # index pointers
        start = 0
        end = 0

        if (not self.containsLetters(s, t) or len(t) > len(s)) :
            return ""
        
        while end < len(s) :
            if s[end] in t_counter :
                window[s[end]] += 1
            end += 1
            current = s[start:end]

            while all(window[t] >= t_counter[t] for t in t_counter) and start < end : 
                if len(current) < len(shortest) : 
                    shortest = current
                if s[start] in t_counter: 
                    window[s[start]] -= 1
                start += 1
                current = s[start:end]

        return shortest

    def containsLetters(self, s, t):
            s_counter = Counter(s)
            t_counter = Counter(t)
            for t in t_counter : 
                if t not in s_counter or t_counter[t] > s_counter[t]:
                    return False
            return True
