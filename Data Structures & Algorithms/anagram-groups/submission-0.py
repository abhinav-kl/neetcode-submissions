class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i in strs:
            count = [0] * 26

            for j in i:
                count[ord(j) - ord("a")] += 1

            hash_map[tuple(count)].append(i)
        return hash_map.values()