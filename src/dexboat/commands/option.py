class Option:
    def __init__(self, name: str, description: str, required: bool, type: int):
        self.name = name
        self.description = description
        self.type = type
        self.required = required

    def get_json(self) -> dict:
        return {"name": self.name, "description": self.description, "type": self.type, "required": self.required}
