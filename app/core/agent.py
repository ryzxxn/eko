class Agent:
    def __init__(self, name):
        self.name = name
        self.memory = []
        self.permissions = {"tool_access": True}

    def use_tool(self, tool):
        if self.permissions.get("tool_access", False):
            return tool()
        return "Permission denied"

    def remember(self, info):
        self.memory.append(info)
