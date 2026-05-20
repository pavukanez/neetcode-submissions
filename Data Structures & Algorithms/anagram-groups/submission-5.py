class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            cur = seen.get(tuple(arr), [])
            cur.append(s)
            seen[tuple(arr)] = cur

        return list(seen.values())
        
            
        
        

    

    




