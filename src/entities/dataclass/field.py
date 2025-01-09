import dataclasses
from typing import List, Dict,Literal
from time import sleep

x=0
y=1

#  0=Enpty 1=active_I   2=active_O   3=active_S   4=active_Z   5=active_J   6=active_L   7=active_T
# 10=wall 11=stacked_I 12=stacked_O 13=stacked_S 14=stacked_Z 15=stacked_J 16=stacked_L 17=stacked_T
@dataclasses.dataclass
class Field:
    rows: int
    cols: int
    map: List[List[int]] = dataclasses.field(init=False)

    def __post_init__(self):
        self.map = [
            [10 if (x == self.rows - 1 or y in {0, self.cols - 1}) else 0 for y in range(self.cols)]
            for x in range(self.rows)
        ]
        self.score:int = 0

    def fall_all(self,possition:List[List[int]],string:Literal["I","O","S","Z","J","L","T"]) -> None:
        for block in possition:
            self.map[block[y]][block[x]] = 0

        while True:
            for block in possition:
                if self.map[block[y]+1][block[x]] >= 10:
                    for block in possition:
                        match(string):
                            case "I":
                                self.map[block[y]][block[x]] = 11
                            case "O":
                                self.map[block[y]][block[x]] = 12
                            case "S":
                                self.map[block[y]][block[x]] = 13
                            case "Z":
                                self.map[block[y]][block[x]] = 14
                            case "J":
                                self.map[block[y]][block[x]] = 15
                            case "L":
                                self.map[block[y]][block[x]] = 16
                            case "T":
                                self.map[block[y]][block[x]] = 17
                                self.delete()
                                return True
                else:
                    block[y]+=1



    def down(self,possition:List[List[int]],string:Literal["I","O","S","Z","J","L","T"]) -> bool:
        for block in possition:
            if self.map[block[y]+1][block[x]] >= 10:
                for block in possition:
                    self.map[block[y]][block[x]] += 10
                self.delete()
                return True
        for block in possition:
            self.map[block[y]][block[x]] = 0
            block[y]+=1
        for block in possition:
            match(string):
                case "I":
                    self.map[block[y]][block[x]] = 1
                case "O":
                    self.map[block[y]][block[x]] = 2
                case "S":
                    self.map[block[y]][block[x]] = 3
                case "Z":
                    self.map[block[y]][block[x]] = 4
                case "J":
                    self.map[block[y]][block[x]] = 5
                case "L":
                    self.map[block[y]][block[x]] = 6
                case "T":
                    self.map[block[y]][block[x]] = 7
        return False

    def right(self,possition:List[List[int]],string:Literal["I","O","S","Z","J","L","T"]) -> None:
        for block in possition:
            if self.map[block[y]][block[x]+1] >= 10:
                return

        for block in possition:
            self.map[block[y]][block[x]] = 0
            block[x]+=1
        for block in possition:
            match(string):
                case "I":
                    self.map[block[y]][block[x]] = 1
                case "O":
                    self.map[block[y]][block[x]] = 2
                case "S":
                    self.map[block[y]][block[x]] = 3
                case "Z":
                    self.map[block[y]][block[x]] = 4
                case "J":
                    self.map[block[y]][block[x]] = 5
                case "L":
                    self.map[block[y]][block[x]] = 6
                case "T":
                    self.map[block[y]][block[x]] = 7
        return

    def left(self,possition:List[List[int]],string:Literal["I","O","S","Z","J","L","T"]) -> None:
        for block in possition:
            if self.map[block[y]][block[x]-1] >= 10:
                return

        for block in possition:
            self.map[block[y]][block[x]] = 0
            block[x]-=1
        for block in possition:
            match(string):
                case "I":
                    self.map[block[y]][block[x]] = 1
                case "O":
                    self.map[block[y]][block[x]] = 2
                case "S":
                    self.map[block[y]][block[x]] = 3
                case "Z":
                    self.map[block[y]][block[x]] = 4
                case "J":
                    self.map[block[y]][block[x]] = 5
                case "L":
                    self.map[block[y]][block[x]] = 6
                case "T":
                    self.map[block[y]][block[x]] = 7
        return



    def delete(self) -> None:
        for i in range(1,self.rows-1):
            if all(self.map[i]):
                self.map.pop(i)
                self.map.insert(0,[10]+[0 for _ in range(self.cols-2)]+[10])
                self.score+=1
                print(self.score)

    # def spin(self,possition:List[List[int]],string:Literal["I","O","S","Z","J","L","T"]) -> None:
    #     if string == "O" or string == "I":
    #         return
    #     else:
