class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        result = ""
        for i in range(len(title)):
            if len(title[i]) < 3:
                result = result + title[i].lower() + " "
            else:
                result = result + title[i].capitalize() + " " 
 
        return result[:-1]
