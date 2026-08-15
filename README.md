# Northline Freight — demo repository

The system that prices consignments. Written by a vendor, owned and
governed by Northline.

## Run it locally

    python3 -m app.server
    curl "localhost:8080/quote?from=Kampala&to=Gulu&tonnes=12&km=340"
    curl localhost:8080/version

## Tests

    python3 -m pytest

## How a change reaches production

1. Vendor developer opens a pull request from a feature branch.
   Nobody pushes to `main`. Including the vendor lead.
2. CI runs on Northline's self-hosted runner, on Northline's metal.
   A red build cannot merge.
3. `CODEOWNERS` requires an internal reviewer on the pricing paths.
4. Merge to `main`, then tag a release: `git tag v1.4.0 && git push --tags`.
5. The deploy job pauses for approval from a named person at Northline.
6. `GET /version` reports the commit actually running in production.

Rollback: re-run *Deploy to production* with the previous tag.

<!-- ci smoke test 2026-08-15T10:31:22Z -->
