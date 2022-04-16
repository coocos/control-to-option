from setuptools import setup

APPS = ["Remap.py"]
OPTIONS = {
    "argv_emulation": True,
    "plist": {
        "LSUIElement": True,
    },
    "packages": ["rumps"]
}

setup(
    app=APPS,
    data_files=[],
    options= {
        "py2app": OPTIONS
    },
    setup_requires=["py2app"],
)