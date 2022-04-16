"""Hidutil operations for key remapping"""
import json
import subprocess
from typing import List, Final


CONTROL: Final = 0x7000000E4
OPTION: Final = 0x7000000E6
CONTROL_TO_OPTION: Final = {
    "UserKeyMapping": [
        {"HIDKeyboardModifierMappingSrc": CONTROL, "HIDKeyboardModifierMappingDst": OPTION}
    ]
}
CONTROL_TO_CONTROL: Final = {"UserKeyMapping": []}


def _call_hidutil(args: List[str]) -> str:
    """Calls hidutil with the given command and returns the output"""
    process = subprocess.run(["hidutil", *args], capture_output=True)
    process.check_returncode()
    return process.stdout.decode("utf-8")


def is_key_mapping_active() -> bool:
    """Indicates if key mapping is active"""
    key_maps = (
        _call_hidutil(["property", "--get", "UserKeyMapping"])
        .replace("\n", "")
        .replace(" ", "")
    )
    return (
        f"HIDKeyboardModifierMappingSrc={CONTROL}" in key_maps
        and f"HIDKeyboardModifierMappingDst={OPTION}" in key_maps
    )


def enable() -> str:
    """Enables the custom key mapping"""
    return _call_hidutil(["property", "--set", json.dumps(CONTROL_TO_OPTION)])


def disable() -> str:
    """Disables the custom key mapping"""
    return _call_hidutil(["property", "--set", json.dumps(CONTROL_TO_CONTROL)])
