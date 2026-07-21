# Product extraction checklist

Create a separate repository; do not deploy this archive.

- Obtain an explicit source license and preserve author/SCM attribution.
- Name product and security owners, users, acceptance criteria, supported JDK/server/Maven versions, and release lifetime.
- Reimplement the intended workflow on supported APIs rather than incrementally trusting Java 6/Servlet 2.5-era code.
- Pin dependencies/plugins, use HTTPS repositories/metadata, generate an SBOM, scan licenses/vulnerabilities, and prevent dependency confusion.
- Add secure identity/input/output/session/error controls appropriate to the real product; remove the sample Greeter/JSP behavior.
- Add unit, integration, end-to-end, migration/failure/security tests, read-only CI permissions, signed artifacts, deployment configuration, observability, backup/restore, rollback, and incident response.
- Complete legal, security, operations, accessibility, and representative-user review before launch.
