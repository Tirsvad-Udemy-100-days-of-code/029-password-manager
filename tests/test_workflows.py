"""Static checks of the CI workflows (QC-WF-001): no runner is needed."""

import re
from pathlib import Path
from typing import Any, cast

import pytest
import yaml

WORKFLOW_DIR = Path(__file__).resolve().parents[1] / ".gitea" / "workflows"
WORKFLOW_FILES = sorted(WORKFLOW_DIR.glob("*.yml"))
MAX_INLINE_SCRIPT_LINES = 5
PINNED_ACTION = re.compile(r"^[\w.-]+/[\w.-]+@v\d+\.\d+\.\d+$")


def load(path: Path) -> dict[Any, Any]:
    """Parse a workflow with a safe loader; `on` is read as the key ``True``."""
    return cast("dict[Any, Any]", yaml.safe_load(path.read_text(encoding="utf-8")))


def test_workflows_exist() -> None:
    assert WORKFLOW_FILES, "expected at least one workflow in .gitea/workflows"


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_workflow_declares_required_keys(path: Path) -> None:
    workflow = load(path)
    assert workflow["name"]
    assert True in workflow or "on" in workflow
    assert workflow["jobs"]


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_every_job_has_runner_timeout_and_permissions(path: Path) -> None:
    for job in load(path)["jobs"].values():
        assert job["runs-on"]
        assert job["timeout-minutes"]
        assert "permissions" in job


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_actions_are_pinned_and_scripts_are_short(path: Path) -> None:
    for job in load(path)["jobs"].values():
        for step in job["steps"]:
            assert step["name"]
            if "uses" in step:
                assert PINNED_ACTION.match(step["uses"]), step["uses"]
            if "run" in step:
                lines = step["run"].strip().splitlines()
                assert len(lines) <= MAX_INLINE_SCRIPT_LINES
