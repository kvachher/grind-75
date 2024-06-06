class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        st = deque(s)

        def recurse(st):
            num = 0
            sum = 0
            sign = 1

            while st:
                val = st.popleft()

                if val.isdigit() :
                    num = num * 10 + int(val)

                elif val == '-' : 
                    sum += num*sign
                    num = 0
                    sign = -1

                elif val == '+' : 
                    sum += num*sign
                    num = 0
                    sign = 1

                elif val == '(':
                    num = recurse(st)
                    sum += num * sign
                    num = 0

                elif val == ')':
                    sum += sign*num
                    return sum

            sum += sign*num
            return sum
        return recurse(st)
