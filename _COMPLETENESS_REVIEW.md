# Completeness Review: maven-project

**Review date:** 2026-07-18

## Assessment basis

Static inspection of project-owned source and configuration only; no dependency installation, build, database migration, external-service call, or runtime launch was performed. The scan considered 11 project files (2 source files), 3 manifest(s), 1 test-like file(s), and 0 CI workflow(s), excluding dependency/generated directories.

## Classification

**Not an app**

This folder is best treated as source material, a library/tool, generated workspace, dependency cache, or portfolio container—not as an independently complete application workflow app. App-completeness criteria therefore do not apply until a supported executable product boundary is defined.

## Why it is not a complete app

- No clear, independently supported end-user application boundary was identified in the inspected source/configuration.
- Ownership, release target, supported entry point, and acceptance criteria are absent or belong to an upstream/reference project.

## Needed features

1. Decide whether to retain this as an upstream/reference dependency, internal tool, archive, or source for extraction.
2. Document provenance, license, owner, supported version, update strategy, and security-patching responsibility.
3. If an app is intended, create a separate product boundary with an explicit entry point, user journey, configuration contract, tests, and release process.

## Risks or launch blockers

- Accidental deployment or unsupported modification could create security, licensing, and maintenance obligations.
- Treating this folder as an original product may obscure upstream provenance and update responsibility.

## Evidence inspected

- `README.md`
- `server/src/main/java/com/example/Greeter.java:15`
- `server/src/main/java/com/example/Greeter.java`
- `server/src/test/java/com/example/TestGreeter.java`
- `pom.xml`

## Recommended next action

Record an explicit retain/extract/archive decision; only create an app roadmap if a supported product boundary and owner are assigned.

## Implementation progress — 2026-07-19

The review is implemented as a non-application archive boundary; the obsolete training sample was not misrepresented as a production app.

1. `REFERENCE_BOUNDARY.json` records the explicit `retain-pinned-archive` decision at commit `0caf6111d5ef4679bf818f99fa448a525566ee69`. The two-module Greeter/JSP Maven tree is supported only as historical training reference; application execution and deployment are denied, the README leads with that warning, and `start.sh` always exits `78`.
2. `PROVENANCE.md` distinguishes the configured `eakarsu` fork from the `jleetutorial/maven-project` upstream named by the POM SCM metadata and James Lee course README/history. It documents the 2017 snapshot, Java 6/Servlet 2.5/JSP 2.2 and obsolete Maven/plugin/dependency constraints, the replacement-only update policy, and the absence of any license in the tree or reachable history. Redistribution remains blocked, and product/security-patching owners remain explicitly unassigned rather than inferred.
3. No app is intended here. `PRODUCT_EXTRACTION_CHECKLIST.md` requires a separately owned repository, explicit license and attribution, a supported toolchain and user journey, clean pinned dependencies/SBOM, secure product controls, tests/CI/release, operations/recovery, and launch review. `SECURITY.md` treats the archive and its POMs as untrusted input and deliberately forbids downloading/building the historical dependency graph during boundary validation.

Validation completed with only Python standard-library and shell checks: all three POMs parse; the parent retains the two declared modules and upstream SCM marker; the no-license and no-owner boundary fails closed; seven provenance/boundary/POM/startup/extraction tests pass; the validator reports no issues; launcher denial, `bash -n start.sh`, `git diff --check`, and Gitleaks also pass with no findings. Read-only CI repeats these checks and never invokes Maven, Jetty, artifact/site publication, or deployment.

External decisions remain: the copyright owner must provide a license before redistribution, governance must assign product and security-patching owners before extraction, and any new product must independently reimplement and validate its runtime rather than treating these 2016–2017 course dependencies as supported.

## Runtime and login acceptance — 2026-07-20

- **Status:** NOT_APPLICABLE
- **Startup safety:** the obsolete training-archive boundary and fail-closed launcher were inspected.
- **Startup, readiness, login, and primary journey:** N/A; the historical course dependencies are deliberately not an independently supported application runtime.
- **Browser/server evidence:** N/A; Maven/Jetty and application dependencies were not executed.
- **Cleanup:** no runtime or disposable service was created.
- **Residual issue:** a future product must be separately owned, licensed, reimplemented, and independently validated.
