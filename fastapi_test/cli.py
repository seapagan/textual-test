"""Test code for the CLI."""
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Static, TextLog


class ControlButtons(Static):
    def compose(self) -> ComposeResult:
        yield Button("Start Server", id="start", variant="success")
        yield Button("Stop Server", id="stop", variant="error")


class FastaAPIRunner(App):
    """A textual app to run a FastAPI app.

    This app is used to run a FastAPI from a Textual app.
    """

    CSS_PATH = "cli.styles"

    def compose(self) -> ComposeResult:
        yield ControlButtons()


if __name__ == "__main__":
    app = FastaAPIRunner()
    app.run()
