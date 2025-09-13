class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2 * (width + height) - 4
        self.steps = 0
        self.moved = False
        
    def step(self, num: int) -> None:
        if num > 0:
            self.moved = True
        self.steps = (self.steps + num) % self.perimeter


    def getPos(self) -> List[int]:
        s = self.steps
        if s < self.width - 1:
            return [s, 0]
        s -= self.width - 1
        if s < self.height - 1:
            return [self.width - 1, s]
        s -= self.height - 1
        if s < self.width - 1:
            return [self.width - 1 - s, self.height - 1]
        s -= self.width - 1
        return [0, self.height - 1 - s]
        
    def getDir(self) -> str:
        s = self.steps
        if s == 0:
            return "South" if self.moved else "East"
        
        if s <= self.width - 1:
            return "East"
        s -= self.width - 1
        
        if s <= self.height - 1:
            return "North"
        s -= self.height - 1
        
        if s <= self.width - 1:
            return "West"
        s -= self.width - 1
        
        return "South"

