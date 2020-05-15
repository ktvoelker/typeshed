import logging
from typing import Any, Callable, Dict


class JournalHandler(logging.Handler):

    def __init__(self) -> None:
        ...


class Reader(Iterator[Dict[str, Any]]):

    def __init__(self, converters: Dict[str, Callable[[Any], Any]]) -> None:
        ...

    def seek_cursor(self, cursor: str) -> None:
        ...

    def close(self) -> None:
        ...
