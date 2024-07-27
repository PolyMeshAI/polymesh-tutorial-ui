import weakref

from .user_interface.window import WindowExt

import omni
from omni.isaac.ui.menu import make_menu_item_description
from omni.kit.menu.utils import MenuItemDescription, add_menu_items, remove_menu_items

EXTENSION_NAME = "Menu and UI Tutorial"

# This extension is a simple example extension that shows how a user can get started creating their own UI while leveraging existing Isaac Systems.
class Extension(omni.ext.IExt):
    def on_startup(self, ext_id: str):
        """Initialize extension and UI elements"""
        self._ext_id = ext_id

        # This method is used to create just the menu drop down on the top with no other submenus. Perfect for a core extension
        #self._add_menu_without_subfolder()

        # This method is used to create the menu with a submenu selection.
        self._add_menu_with_submenu()

        # Initialize your window for the extension and pass along the Extension ID for the Header information.
        self._window = WindowExt(EXTENSION_NAME, ext_id=self._ext_id, width=700, height=250, visible=False, dockPreference=omni.ui.DockPreference.RIGHT_TOP)

    # Method used to create Menu on the top navbar
    def _add_menu_without_subfolder(self):
        self._menu_items_1 = [MenuItemDescription()]
        add_menu_items(self._menu_items_1, "Tutorial")

    # Method used to create a Menu with a Submenu in the top navbar
    def _add_menu_with_submenu(self):
        # Used to add a new section to the above code.
        self._menu_items_2 = [
            MenuItemDescription(
                name="Menu",
                sub_menu=[
                    make_menu_item_description(self._ext_id, "Create Cube", lambda a=weakref.proxy(self): a._menu_callback())
                ],
            )
        ]
        add_menu_items(self._menu_items_2, "Tutorial")

    # Destroy window on shutdown
    def on_shutdown(self):
        #remove_menu_items(self._menu_items_1, "Menu")
        remove_menu_items(self._menu_items_2, "Tutorial")
        self._window.destroy()
        self._window = None

    # Callback method that toggles the visibility for the extension GUI. Will save its existing states.
    def _menu_callback(self):
        self._window.visible = not self._window.visible