class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        v = {
            1 : [], 
            2 : ["a", "b", "c"], 
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"], 
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"], 
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"], 
            9 : ["w", "x", "y", "z"] 
        }
        if not digits:
            return []

        def recurse(i, path, combinations, v):
            if i == len(digits):
                combinations.append("".join(path))
                return
            for l in v[int(digits[i])]:
                path.append(l)
                recurse(i + 1, path, combinations, v)
                path.pop()

        combinations = []
        recurse(0, [], combinations, v)
        return combinations
