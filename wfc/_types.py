from dataclasses import dataclass


@dataclass
class Cell:
    modules: set[str]
    propagating: bool = False


Grid = list[list[Cell]]
