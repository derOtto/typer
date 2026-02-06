import pytest
import typer
from typer.testing import CliRunner

runner = CliRunner()


@pytest.mark.parametrize("default", [True, False])
def test_help_displays_default_bool_option(default: bool):
    app = typer.Typer()

    @app.command()
    def cmd(
        dry_run: bool = typer.Option(
            default,
            "--dry-run",
        ),
    ):
        pass

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0, result.output
    assert f"[default: {default}]" in result.output


@pytest.mark.parametrize("default", [True, False])
def test_help_bool_option_without_show_default(default: bool):
    app = typer.Typer()

    @app.command()
    def cmd(dry_run: bool = typer.Option(default, "--dry-run", show_default=False)):
        pass

    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0, result.output
    assert f"[default: {default}]" not in result.output
