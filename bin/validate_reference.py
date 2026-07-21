#!/usr/bin/env python3
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POMS = (ROOT / "pom.xml", ROOT / "server" / "pom.xml", ROOT / "webapp" / "pom.xml")

def inspect():
    boundary = json.loads((ROOT / "REFERENCE_BOUNDARY.json").read_text())
    issues = []; parsed = []
    for pom in POMS:
        try: parsed.append(ET.parse(pom).getroot())
        except ET.ParseError as error: issues.append(f"{pom.relative_to(ROOT)}: {error}")
    root_text = (ROOT / "pom.xml").read_text()
    for required in ("<module>server</module>", "<module>webapp</module>", "jleetutorial/maven-project"):
        if required not in root_text: issues.append(f"root POM lost provenance/module marker: {required}")
    if boundary.get("application") is not False or boundary.get("executionSupported") is not False or boundary.get("deploymentSupported") is not False: issues.append("boundary must deny execution and deployment")
    license_files = [path.name for path in ROOT.iterdir() if path.is_file() and path.name.lower().startswith(("license", "copying", "notice"))]
    if license_files or boundary["license"]["projectLicenseFound"] is not False: issues.append("license boundary mismatch")
    text = "\n".join(path.read_text(errors="replace") for path in [*POMS, ROOT / "README.md", ROOT / "PROVENANCE.md", ROOT / "start.sh"])
    patterns = [r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", r"AKIA[0-9A-Z]{16}", r"\bsk-[A-Za-z0-9_-]{32,}\b"]
    if any(re.search(pattern, text.encode().decode(), re.ASCII) for pattern in patterns): issues.append("high-confidence secret signature")
    return {"boundary": boundary, "pomCount": len(parsed), "licenseFiles": license_files, "rootPomSha256": hashlib.sha256((ROOT / "pom.xml").read_bytes()).hexdigest(), "issues": issues}

if __name__ == "__main__": result = inspect(); print(json.dumps(result, indent=2, sort_keys=True)); raise SystemExit(bool(result["issues"]))
