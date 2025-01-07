import dataclasses
from typing import List, Dict

@dataclasses.dataclass
class Field:
    map:List[List[int]] = dataclasses.field(default_factory=lambda:[[0 for _ in range(10)] for _ in range(20)])

    def down(self,possition:Dict[str,int]) -> None:
        self.map[possition["y"]][possition["x"]] = 0
        self.map[possition["y"]-1][possition["x"]] = 1

    def right(self,possition:Dict[str,int]) -> None:
        self.map[possition["y"]][possition["x"]] = 0
        self.map[possition["y"]][possition["x"]+1] = 1

    def left(self,possition:Dict[str,int]) -> None:
        self.map[possition["y"]][possition["x"]] = 0
        self.map[possition["y"]][possition["x"]-1] = 1
    
