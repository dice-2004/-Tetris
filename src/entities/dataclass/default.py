import dataclasses
from typing import List, Dict

@dataclasses.dataclass
class Tetromino:
    Tetromino: Dict[str, List[List[int]]] = dataclasses.field(default_factory=lambda: {
#ex)    "D": [[x, y], [x, y], [x, y], [x, y]],
        "I": [any],
        "O": [any],
        "S": [any],
        "Z": [any],
        "J": [any],
        "L": [any],
        "T": [any],
    })
