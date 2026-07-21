#!/usr/bin/env bash
set -euo pipefail
echo "maven-project is a quarantined training archive, not a supported application." >&2
echo "Run 'make check' for non-mutating boundary validation." >&2
exit 78
