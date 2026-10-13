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
PINNED_REUSABLE_WORKFLOW = re.compile(
    r"^[\w.-]+/[\w.-]+/\.gitea/workflows/[\w.-]+\.ya?ml@v\d+\.\d+\.\d+$"
)
SECRET_EXPRESSION = re.compile(r"^\$\{\{\s*secrets\.\w+\s*\}\}$")


def load(path: Path) -> dict[Any, Any]:
    """Parse a workflow with a safe loader; `on` is read as the key ``True``."""
    return cast("dict[Any, Any]", yaml.safe_load(path.read_text(encoding="utf-8")))


def jobs_of(path: Path) -> list[dict[str, Any]]:
    return list(load(path)["jobs"].values())


def is_reusable_call(job: dict[str, Any]) -> bool:
    return "uses" in job


def test_workflows_exist() -> None:
    assert WORKFLOW_FILES, "expected at least one workflow in .gitea/workflows"


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_workflow_declares_required_keys(path: Path) -> None:
    workflow = load(path)
    assert workflow["name"]
    assert True in workflow or "on" in workflow
    assert workflow["jobs"]


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_every_job_has_permissions_and_normal_jobs_have_runner_and_timeout(
    path: Path,
) -> None:
    for job in jobs_of(path):
        assert "permissions" in job
        if not is_reusable_call(job):
            assert job["runs-on"]
            assert job["timeout-minutes"]


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_actions_are_pinned_and_scripts_are_short(path: Path) -> None:
    for job in jobs_of(path):
        if is_reusable_call(job):
            continue
        for step in job["steps"]:
            assert step["name"]
            if "uses" in step:
                assert PINNED_ACTION.match(step["uses"]), step["uses"]
            if "run" in step:
                lines = step["run"].strip().splitlines()
                assert len(lines) <= MAX_INLINE_SCRIPT_LINES


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_reusable_workflow_calls_are_pinned_to_an_exact_release(path: Path) -> None:
    for job in jobs_of(path):
        if is_reusable_call(job):
            assert PINNED_REUSABLE_WORKFLOW.match(job["uses"]), job["uses"]


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_reusable_workflow_tools_ref_equals_the_workflow_release(path: Path) -> None:
    for job in jobs_of(path):
        if is_reusable_call(job) and "tools-ref" in job.get("with", {}):
            release = job["uses"].rsplit("@", 1)[1]
            assert job["with"]["tools-ref"] == release


@pytest.mark.parametrize("path", WORKFLOW_FILES, ids=lambda p: p.name)
def test_reusable_workflow_secrets_are_never_literals(path: Path) -> None:
    for job in jobs_of(path):
        if is_reusable_call(job):
            for name, value in job.get("secrets", {}).items():
                assert SECRET_EXPRESSION.match(str(value)), name
