# Provenance and maintenance record

The configured remote is the `eakarsu` fork. The root POM's SCM metadata identifies `github.com/jleetutorial/maven-project`, the README calls the code source for James Lee's Jenkins course, and reachable history is authored primarily by James Lee. The retained snapshot is commit `0caf6111d5ef4679bf818f99fa448a525566ee69` from 2017-11-18.

No `LICENSE`, `COPYING`, or `NOTICE` file exists in the current tree or reachable history. Repository access and SCM metadata are not a license grant. Public redistribution, derivative release, or incorporation into a product remains blocked until the copyright owner provides a license. The fork custodian is not represented as the upstream author or course operator.

The two-module Maven tree is historical training material: a Greeter JAR/test and a JSP/Servlet WAR. It declares Java 6, Servlet 2.5, JSP 2.2, JUnit 4.10, Mockito 1.8.5, milestone Jetty 8, FindBugs, Maven 3.0.3, HTTP metadata, and obsolete plugin versions. It has no modern runtime, dependency-patching SLA, owner, acceptance contract, or release target. Fetching/building those dependencies is not part of the supported archive check.

The update strategy is replacement, not in-place pseudo-modernization: a named owner must identify a licensed upstream version, document why it is retained, inspect the dependency graph in isolation, update the pinned commit and boundary, and rerun non-executing integrity/security checks. A real application must be extracted into a separate repository.
