import rumps

from . import hidutil


class RemapApp(rumps.App):
    """UI"""

    @rumps.clicked("Enabled")
    def enable(self, sender: rumps.MenuItem) -> None:
        """Toggles the key remapping on or off"""
        if hidutil.is_key_mapping_active():
            hidutil.disable()
        else:
            hidutil.enable()
        sender.state = not sender.state


def create_app() -> RemapApp:
    """Configures and returns the app"""

    enabled_item = rumps.MenuItem("Enabled")
    enabled_item.state = bool(hidutil.is_key_mapping_active())
    return RemapApp("Remap", menu=[enabled_item])
