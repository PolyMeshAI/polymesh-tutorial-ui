import omni.kit.commands

# this command is used to create each REB prim, it also handles undo so that each individual prim command doesn't have to
class TutorialTestCommand(omni.kit.commands.Command):
    def __init__(
        self,
        text: str = ""
    ):
        # condensed way to copy all input arguments into self with an underscore prefix: text = self._text
        for name, value in vars().items():
            if name != "self":
                setattr(self, f"_{name}", value)
        self._prim_path = None
        pass

    def do(self):
        print("Tutorial Test Command Do Triggered")
        return "Received"

    def undo(self):
        print("Tutorial Test Command Undo Triggered")
        return "Removed"
    
omni.kit.commands.register_all_commands_in_module(__name__)