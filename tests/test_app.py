from .context import app


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    app.App.hell_world()
    captured = capsys.readouterr()

    assert "Hello World" in captured.out
