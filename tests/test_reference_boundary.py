import subprocess
import unittest
from pathlib import Path
from bin.validate_reference import inspect

ROOT = Path(__file__).resolve().parents[1]

class ReferenceBoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.result = inspect()
    def test_archive_decision_denies_app_execution(self):
        boundary = self.result["boundary"]; self.assertEqual(boundary["decision"], "retain-pinned-archive"); self.assertFalse(boundary["application"]); self.assertFalse(boundary["executionSupported"])
    def test_upstream_and_snapshot_are_pinned(self):
        snapshot = self.result["boundary"]["snapshot"]; self.assertEqual(snapshot["commit"], "0caf6111d5ef4679bf818f99fa448a525566ee69"); self.assertIn("jleetutorial", snapshot["upstreamFromPomScm"])
    def test_all_three_poms_parse_without_fetching_dependencies(self): self.assertEqual(self.result["pomCount"], 3)
    def test_missing_license_and_owners_fail_closed(self):
        boundary = self.result["boundary"]; self.assertEqual(self.result["licenseFiles"], []); self.assertFalse(boundary["license"]["projectLicenseFound"]); self.assertIsNone(boundary["ownership"]["productOwner"]); self.assertIsNone(boundary["ownership"]["securityPatchOwner"])
    def test_validator_reports_no_boundary_issue(self): self.assertEqual(self.result["issues"], [])
    def test_startup_is_denied(self):
        completed = subprocess.run([str(ROOT / "start.sh")], cwd=ROOT, capture_output=True, text=True, check=False); self.assertEqual(completed.returncode, 78); self.assertIn("not a supported application", completed.stderr)
    def test_extraction_requires_separate_reimplementation(self): self.assertIn("separate repository", (ROOT / "PRODUCT_EXTRACTION_CHECKLIST.md").read_text())

if __name__ == "__main__": unittest.main()
