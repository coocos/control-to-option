import rumps

from . import hidutil


class RemapperApp(rumps.App):
    """Menu bar app for remapping right ctrl"""

    @rumps.clicked("Enabled")
    def enable(self, sender):
        """Toggles the key remapping on or off"""
        if hidutil.is_key_mapping_active():
            hidutil.disable()
        else:
            hidutil.enable()
        sender.state = not sender.state


def create_app() -> RemapperApp:
    """Configures and returns the app"""

    enabled_item = rumps.MenuItem("Enabled")
    enabled_item.state = bool(hidutil.is_key_mapping_active())
    return RemapperApp("Remapper", menu=[enabled_item])
