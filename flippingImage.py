class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            image[r] = [1 - val for val in image[r][::-1]]
        
        return image