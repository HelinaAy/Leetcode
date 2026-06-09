class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = ""
        for num in digits:
            i+= str(num)
        number = int(i)+1
        
        return list(map(int,str(number)))