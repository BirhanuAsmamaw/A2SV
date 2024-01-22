class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result=[]
        counter=collections.Counter(s)

        change = set()
        length = 0
        for i,current in enumerate(s):
            length += 1
            change.add(current)
            counter[current] -= 1 
            
            if counter[current]==0:
                change.remove(current)
                if len(change)==0:
                    result.append(length)
                    length=0
        return result
        
