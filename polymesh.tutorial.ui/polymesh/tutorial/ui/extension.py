import weakref

from .user_interface.window import WindowExt

import omni
from omni.isaac.ui.menu import make_menu_item_description
from omni.kit.menu.utils import MenuItemDescription, add_menu_items, remove_menu_items

EXTENSION_NAME = "Menu and UI Tutorial"

class Extension(omni.ext.IExt):
    def on_startup(self, ext_id: str):
        """Initialize extension and UI elements"""
        self._ext_id = ext_id

        self._add_menu_with_submenu()

        self._window = WindowExt(EXTENSION_NAME, ext_id=self._ext_id, width=700, height=250, visible=False, dockPreference=omni.ui.DockPreference.RIGHT_TOP)

    def _add_menu_with_submenu(self):
        # [omni.isaac.ui].menu.py
        self._menu_items = [
            MenuItemDescription(
                name="Menu",
                sub_menu=[
                    make_menu_item_description(self._ext_id, "Create Item", lambda a=weakref.proxy(self): a._menu_callback())
                ],
            )
        ]
        add_menu_items(self._menu_items, "Tutorial")

    def on_shutdown(self):
        remove_menu_items(self._menu_items, "Tutorial")
        self._window.destroy()
        self._window = None

    def _menu_callback(self):
        self._window.visible = not self._window.visible
