import gd


class EditLevel:
    def __init__(self):
        self.name = "Speed"
        self.description = "Sets the players speed."

        async def run(ctx, speed):
            memory = gd.memory
            memory.WindowsMemory.set_speed()