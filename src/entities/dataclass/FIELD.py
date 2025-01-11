import dataclasses
from typing import List, Dict, Literal
from time import sleep

x = 0
y = 1

@dataclasses.dataclass
class Field:
    rows: int
    cols: int
    map: List[List[int]] = dataclasses.field(init=False)
    score: int = dataclasses.field(default=0)
    level: int = dataclasses.field(default=1)
    lines_cleared: int = dataclasses.field(default=0)
    combo: int = dataclasses.field(default=0)

    def __post_init__(self):
        self.map = [
            [20 if y == 0 else 30 if y == self.cols - 1 else 10 if x == self.rows - 1 else 0 for y in range(self.cols)]
            for x in range(self.rows)
        ]

    def calculate_score(self, lines_cleared: int) -> int:
        base_points = {
            1: 100,
            2: 300,
            3: 500,
            4: 800
        }
        combo_bonus = self.combo * 50 if self.combo >= 1 else 0
        score = int(base_points.get(lines_cleared, 0) + combo_bonus)
        print(f"Base: {base_points.get(lines_cleared, 0)} | Combo: {combo_bonus}")
        return score

    def update_level(self) -> None:
        old_level = self.level
        self.level = (self.lines_cleared // 10) + 1
        if old_level != self.level:
            print(f"Level Up! Now at level {self.level}")

    def delete(self) -> None:
        lines_deleted = 0
        for i in range(1, self.rows-1):
            if all(cell >= 10 for cell in self.map[i][1:-1]):
                self.map.pop(i)
                self.map.insert(0, [10]+[0 for _ in range(self.cols-2)]+[10])
                lines_deleted += 1
        
        if lines_deleted > 0:
            self.combo += 1
            self.lines_cleared += lines_deleted
            score_gain = self.calculate_score(lines_deleted)
            self.score += score_gain
            self.update_level()
            print(f"Lines: {lines_deleted} | Score: +{score_gain} (Total: {self.score}) | Level: {self.level} | Combo: {self.combo}")
        else:
            self.combo = 0

    def fall_all(self, possition: List[List[int]], string: Literal["I","O","S","Z","J","L","T"]) -> None:
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

    def down(self, possition: List[List[int]], string: Literal["I","O","S","Z","J","L","T"]) -> bool:
        print(possition)
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

    def right(self, possition: List[List[int]], string: Literal["I","O","S","Z","J","L","T"]) -> None:
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

    def left(self, possition: List[List[int]], string: Literal["I","O","S","Z","J","L","T"]) -> None:
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

    def L_spin(self, possition: Dict[str,List[List[int]]], string: Literal["I","O","S","Z","J","L","T"]) -> None:
        for block in possition["tetro"]:
            self.map[block[y]][block[x]] = 0
        for block in possition["tetro"]:
            block[x] = block[x]-possition["shaft"][x]
            block[y] = block[y]-possition["shaft"][y]
        for block in possition["tetro"]:
            block[x],block[y] = -block[y],block[x]
        for block in possition["tetro"]:
            block[x] = block[x]+possition["shaft"][x]
            block[y] = block[y]+possition["shaft"][y]
        while any(self.map[block[y]][block[x]] == 20 for block in possition["tetro"]):
            for block in possition["tetro"]:
                block[x]+=1
            possition["shaft"][x]+=1
        while any(self.map[block[y]][block[x]] == 30 for block in possition["tetro"]):
            for block in possition["tetro"]:
                block[x]-=1
            possition["shaft"][x]-=1

        for block in possition["tetro"]:
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

    def R_spin(self, possition: Dict[str,List[List[int]]], string: Literal["I","O","S","Z","J","L","T"]) -> None:
        for block in possition["tetro"]:
            self.map[block[y]][block[x]] = 0
        for block in possition["tetro"]:
            block[x] = block[x]-possition["shaft"][x]
            block[y] = block[y]-possition["shaft"][y]
        for block in possition["tetro"]:
            block[x],block[y] = block[y],-block[x]
        for block in possition["tetro"]:
            block[x] = block[x]+possition["shaft"][x]
            block[y] = block[y]+possition["shaft"][y]

        while any(self.map[block[y]][block[x]] == 20 for block in possition["tetro"]):
            for block in possition["tetro"]:
                block[x]+=1
            possition["shaft"][x]+=1
        while any(self.map[block[y]][block[x]] == 30 for block in possition["tetro"]):
            for block in possition["tetro"]:
                block[x]-=1
            possition["shaft"][x]-=1
        for block in possition["tetro"]:
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

    def is_game_over(self) -> bool:
        return any(self.map[1][x] >= 10 for x in range(1,self.cols-1))