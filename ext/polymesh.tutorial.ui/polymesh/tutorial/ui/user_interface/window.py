import omni.ui as ui

import omni.kit.commands
from pxr import Gf

from omni.isaac.ui.ui_utils import *

# Class used to generate the main GUI components. Extension ID is passed.
class WindowExt(ui.Window):
    def __init__(self, title: str, ext_id: str, **kwargs) -> None:
        super().__init__(title=title, **kwargs)
        self._ext_id = ext_id
        
        # Used to store and modify UI models.
        self.task_ui_elements = {}

        self.frame.set_build_fn(self._build_ui)

    # Builds the Extension GUI
    def _build_ui(self):
        with self.frame:
            with ui.ScrollingFrame():
                with ui.VStack(spacing=5, height=10):
                    title = ""
                    doc_link = ""

                    # Builds the Extension header. [omni.isaac.ui]
                    build_header(self._ext_id, __file__, title, doc_link)

                    self._info_panel()

    # Individual Panel to display the group related information. For the example we are simply holding the button here.
    def _info_panel(self):
        frame = ui.CollapsableFrame(
            title="Group Panel",
            height=0,
            collapsed=False,
            style=get_style(),
            style_type_name_override="CollapsableFrame",
            horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_AS_NEEDED,
            vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON,
        )

        with frame:
            with ui.VStack(style=get_style(), spacing=5, height=0):

                # Create a button with a trigger function [omni.isaac.ui].ui_utils.py
                self.task_ui_elements["Prim Path"] = btn_builder(
                    label="", 
                    type="button", 
                    text="button", 
                    tooltip="", 
                    on_clicked_fn=self._create_cube_btn
                )

    def _create_cube_btn(self):
        print("Button Clicked")
        omni.kit.commands.execute(
            'CreateMeshPrimWithDefaultXform',
	        prim_type='Cube',
	        prim_path=None,
	        select_new_prim=True,
	        prepend_default_prim=True
        )

        omni.kit.commands.execute(
            'ChangeProperty',
	        prop_path='/World/Cube.xformOp:translate',
	        value=Gf.Vec3f(-0.02307754009962082, -0.13529472053050995, 0.15837226808071136),
	        prev=None)
        