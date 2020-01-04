from typing import Any, Callable, Dict


class Reader(Iterator[Dict[str, Any]]):

    def __init__(self, converters: Dict[str, Callable[[Any], Any]]) -> None:
        ...

    def seek_cursor(self, cursor: str) -> None:
        ...

    def close(self) -> None:
        ...
