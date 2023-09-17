from talemate.emit import Emitter, AbortCommand


class Manager(Emitter):
    """
    TaleMateCommand class to handle user command
    """

    command_classes = []

    @classmethod
    def register(cls, command_cls):
        cls.command_classes.append(command_cls)

    @classmethod
    def is_command(cls, message):
        return message.startswith("!")

    def __init__(self, scene):
        self.scene = scene
        self.aliases = self.build_aliases()
        self.processing_command = False
        self.setup_emitter(scene)

    def build_aliases(self):
        aliases = {}
        for name, method in Manager.__dict__.items():
            if hasattr(method, "aliases"):
                for alias in method.aliases:
                    aliases[alias] = name.replace("cmd_", "")
        return aliases

    async def execute(self, cmd):
        # commands start with ! and are followed by a command name
        cmd = cmd.strip()
        cmd_args = ""
        if not self.is_command(cmd):
            return False
        
        if ":" in cmd:
            # split command name and args which are separated by a colon
            cmd_name, cmd_args = cmd[1:].split(":", 1)
            cmd_args = cmd_args.split(":")
        else:
            cmd_name = cmd[1:]
            cmd_args = []
            
        for command_cls in self.command_classes:
            if command_cls.is_command(cmd_name):
                command = command_cls(self, *cmd_args)
                try:
                    self.processing_command = True
                    command.command_start()
                    await command.run()
                except AbortCommand:
                    self.system_message(f"Action `{command.verbose_name}` ended")
                except Exception:
                    raise
                finally:
                    command.command_end()
                    self.processing_command = False
                return True

        self.system_message(f"Unknown command: {cmd_name}")

        return True


def register(command_cls):
    Manager.command_classes.append(command_cls)

    setattr(Manager, f"cmd_{command_cls.name}", command_cls.run)

    return command_cls