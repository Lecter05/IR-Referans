from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "deploy.yml"
REQUIREMENTS_PATH = REPO_ROOT / "requirements-dev.txt"
GITIGNORE_PATH = REPO_ROOT / ".gitignore"


def workflow_text() -> str:
    return WORKFLOW_PATH.read_text(encoding="utf-8")


def test_pages_workflow_uses_the_official_pinned_artifact_pipeline() -> None:
    workflow = workflow_text()

    for action in (
        "actions/checkout@v7",
        "actions/setup-python@v6",
        "actions/configure-pages@v6",
        "actions/upload-pages-artifact@v5",
        "actions/deploy-pages@v5",
    ):
        assert action in workflow

    assert "pages: write" in workflow
    assert "id-token: write" in workflow
    assert "environment:" in workflow
    assert "name: github-pages" in workflow
    assert "needs: build" in workflow


def test_generator_failures_are_not_masked_or_committed_by_the_workflow() -> None:
    workflow = workflow_text()

    assert "python generate_index.py" in workflow
    assert "set +e" not in workflow
    assert "slug_collision" not in workflow
    assert "exit 0" not in workflow
    assert "git add" not in workflow
    assert "git commit" not in workflow
    assert "git push" not in workflow
    assert "contents: write" not in workflow


def test_workflow_installs_pinned_tests_and_runs_all_validation_gates() -> None:
    workflow = workflow_text()

    assert "python-version: '3.13'" in workflow
    assert "cache: 'pip'" in workflow
    assert "cache-dependency-path: requirements-dev.txt" in workflow
    assert "python -m pip install -r requirements-dev.txt" in workflow
    assert "python -m pytest -p no:cacheprovider -q" in workflow
    assert "node --check app.js" in workflow
    assert "node --check analytics.js" in workflow
    assert "python -m json.tool index.json" in workflow
    assert "python -m json.tool search-index.json" in workflow
    assert "PYTHONDONTWRITEBYTECODE: '1'" in workflow


def test_pages_deployments_are_serialized_and_pull_requests_only_build() -> None:
    workflow = workflow_text()

    assert "pull_request:" in workflow
    assert "group: pages" in workflow
    assert "cancel-in-progress: false" in workflow
    assert workflow.count("if: github.event_name != 'pull_request'") == 3


def test_dev_requirements_are_explicitly_pinned() -> None:
    assert REQUIREMENTS_PATH.is_file(), "requirements-dev.txt eksik"
    requirements = set(REQUIREMENTS_PATH.read_text(encoding="utf-8").splitlines())

    assert "pytest==8.4.1" in requirements
    assert "beautifulsoup4==4.13.4" in requirements


def test_python_test_caches_are_ignored() -> None:
    assert GITIGNORE_PATH.is_file(), ".gitignore eksik"
    ignored = set(GITIGNORE_PATH.read_text(encoding="utf-8").splitlines())

    assert "__pycache__/" in ignored
    assert "*.py[cod]" in ignored
    assert ".pytest_cache/" in ignored
