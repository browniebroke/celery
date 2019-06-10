import pytest
from celery.bin.celery import CeleryCommand


@pytest.mark.usefixtures("depends_on_current_app")
def test_celery_ping():
    """Check that the command we use for monitoring our celery workers is working."""
    cmd = CeleryCommand()
    with pytest.raises(SystemExit) as exc:
        cmd.execute_from_commandline(
            ["celery", "inspect", "ping", "-A", "celery.tests"]
        )
    assert exc.value.code == 0
