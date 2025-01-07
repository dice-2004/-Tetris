import dataclasses
from typing import List, Dict


x:int=0
y:int=1

@dataclasses.dataclass
class Field:
    map:List[List[int]] = dataclasses.field(default_factory=lambda:[[0 for _ in range(10)] for _ in range(20)])

    def down(self,possition:List[List[int]],border_y:int) -> None:
        for block in possition:
            self.map[block[y]+border_y][block[x]] = 0
        for block in possition:
            self.map[block[y]+1+border_y][block[x]] = 1

    def right(self,possition:List[List[int]],border_x:int) -> None:
        for block in possition:
            self.map[block[y]][block[x]+border_x] = 0
        border_x+=1
        for block in possition:
            self.map[block[y]][block[x]+border_x] = 1

    def left(self,possition:List[List[int]],border_x:int) -> int:
        for block in possition:
            self.map[block[y]][block[x]+border_x] = 0
        border_x-=1
        for block in possition:
            self.map[block[y]][block[x]+border_x] = 1
        return border_x
