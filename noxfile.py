import argparse
import shutil
from pathlib import Path

import nox

nox.needs_version = ">=2026.2"


@nox.session
def cibuild_prepare(session: nox.Session) -> None:
    """Clean creedsolo's CMake output folder if it exists"""

    current_file = Path(__file__).resolve()
    project_path = current_file.parent

    build_path = project_path / "build"

    if session.posargs:
        sub_parser = argparse.ArgumentParser(prog="Nox CIBuldWheel environment cleaner")
        sub_parser.add_argument("-o", "--build-path", type=Path)
        sub_namespace = sub_parser.parse_args(session.posargs)

        try:
            if sub_namespace.build_path:
                build_path = Path(sub_namespace.build_path).resolve()
        except (FileNotFoundError, RuntimeError) as exc:
            session.error(f"Encountered an error when trying to resolve a path: {exc}")

        try:
            _ = build_path.relative_to(project_path)
        except ValueError:
            session.error(
                "The provided path is outside the project root. Let's avoid destroying folders for no reason."
            )

    session.log(f"Removing previous build path {build_path}")

    if build_path.exists():
        shutil.rmtree(build_path)
