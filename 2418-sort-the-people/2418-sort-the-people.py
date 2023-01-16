class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash = dict(zip(heights,names))
        final = []
        heights.sort(reverse=True)
        for i in heights:
            final.append(hash[i])
        return final
        