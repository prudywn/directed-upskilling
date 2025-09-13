class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            #flip and invert
            image[r] = [1 - val for val in image[r][::-1]]
            """ 
        [::-1] flips row.
        1 - val inverts each element (1 → 0, 0 → 1). """
        
        return image