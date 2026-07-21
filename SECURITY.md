# Security policy

Do not deploy the WAR, start Jetty, publish Maven artifacts/sites, or load historical dependencies on a shared machine. The sources and POMs are untrusted training reference input. `make check` uses only Python's standard library to parse and inspect repository-owned text; it intentionally does not invoke Maven or download code.

Report credentials, malicious content, dependency confusion, license problems, or private data privately to the fork custodian and relevant upstream owner. Revoke real credentials at their issuer and preserve evidence. There is no security-patching owner or supported runtime until an extracted product assigns both.
