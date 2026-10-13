"""Validates the CI workflow files with actionlint."""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _find_actionlint() -> str | None:
    found = shutil.which("actionlint")
    if found:
        return found
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        links = Path(local_app_data) / "Microsoft" / "WinGet" / "Links"
        return shutil.which("actionlint", path=str(links))
    return None


def test_workflows_pass_actionlint() -> None:
    executable = _find_actionlint()
    if executable is None:
        pytest.skip("actionlint is not installed")

    config = REPO_ROOT / ".gitea" / "actionlint.yaml"
    workflows = sorted((REPO_ROOT / ".gitea" / "workflows").glob("*.yml"))

    result = subprocess.run(
        [executable, "-config-file", str(config), *map(str, workflows)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, f"{result.stdout}\n{result.stderr}"
