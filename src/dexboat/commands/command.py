from collections.abc import Callable

from dexboat.commands.option import Option


class Command:
    def __init__(self, name: str, description: str, function: Callable[..., object], options: list[Option] | None = None, contexts: list[int] | None = None ):
        self.name: str = name
        self.description: str = description
        self.function: Callable = function
        self.options: list[Option] = options if options is not None else []
        self.contexts: list[int] = contexts if contexts is not None else [0, 1, 2]

    def get_json(self) -> dict:
        options_json = []
        for option in self.options:
            options_json.append(option.get_json())

        return {"name": self.name, "description": self.description, "options": options_json, "contexts": self.contexts}

    def get_name(self) -> str:
        return self.name

    def execute(self, *args, **kwargs):
        return self.function(*args, **kwargs)
