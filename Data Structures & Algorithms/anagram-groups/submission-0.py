class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) ==1 and strs[0] == "":
            return [[""]]
        d = {}
        for word in strs:
            arr = [0] *26
            for c in word:
                arr[ord(c) - ord("a")] += 1
            t = tuple(arr)
            if t not in d:
                d[t] = [word]
            else:
                d[t].append(word)
                
        return list(d.values())