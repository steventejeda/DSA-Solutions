from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)

    for s in strs: 
        count = [0] * 26
        for c in s: 
            count[ord(c) - ord("a")] += 1
        result[tuple(count)].append(s)
    return result.values()

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))