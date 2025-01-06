import dataclasses
from typing import List, Dict


@dataclasses.dataclass
class Kakin:
    Tetromino:Dict[str,List[List[int]]] = {
#ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
        "I":[any]
    }
