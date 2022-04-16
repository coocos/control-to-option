"""Application entry point"""
from remapper import menubar


if __name__ == "__main__":
    app = menubar.create_app()
    app.run()
