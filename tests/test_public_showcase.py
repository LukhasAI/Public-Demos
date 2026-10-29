"""Real-subprocess smoke tests for the public showcase.

No mocks or synthetic success responses: invoke the shipped entrypoints with
a clean working directory and assert the actual process outputs and exit codes.
These tests do not establish correctness of the research prototypes.
"""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def run_script(filename, *args, input_text=None, cwd=None):
    env = dict(os.environ, TERM="dumb")
    return subprocess.run(
        [sys.executable, str(ROOT / filename), *args],
        input=input_text,
        capture_output=True,
        text=True,
        cwd=cwd,
        env=env,
        timeout=20,
        check=False,
    )


class PublicDemoSmokeTests(unittest.TestCase):
    def test_menu_can_exit_from_outside_repository(self):
        with tempfile.TemporaryDirectory() as temp:
            result = run_script("showcase_interactive.py", input_text="Q\n", cwd=temp)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("INTERACTIVE SHOWCASE PORTAL", result.stdout)

    def test_qrg_menu_routes_to_explicit_preview_from_outside_repository(self):
        with tempfile.TemporaryDirectory() as temp:
            result = run_script("showcase_interactive.py", input_text="3\n\nQ\n", cwd=temp)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("RESEARCH OVERVIEW", result.stdout)
        self.assertIn("QRG showcase", result.stdout)
        self.assertIn("No live capability has been executed", result.stdout)

    def test_unimplemented_agent_menu_is_not_claimed_as_live(self):
        with tempfile.TemporaryDirectory() as temp:
            result = run_script("showcase_interactive.py", input_text="6\n\nQ\n", cwd=temp)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Autonomous agent framework", result.stdout)
        self.assertIn("Conceptual material only", result.stdout)

    def test_unknown_preview_fails_closed(self):
        result = run_script("run_demo_safely.py", "not_a_real_demo")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Unknown research overview", result.stderr)

    def test_preview_requires_exactly_one_name(self):
        result = run_script("run_demo_safely.py")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage:", result.stderr)


if __name__ == "__main__":
    unittest.main()
