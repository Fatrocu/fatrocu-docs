---
title: Privacy and retention
nav_order: 7
permalink: /privacy/
---

# Privacy, retention and backups

Originals and work records stay on the device until deletion. SQLite stores profiles, templates, settings and versioned reviews. Managed originals have opaque filenames. Application data lives outside the replaceable installation; the CLI and desktop share the format.

FATROCU_DATA_DIR or --data-dir selects another workspace outside Git. Private storage, backups and financial exports are rejected inside Git checkouts. Backups create a fresh directory with SQLite and retained sources. A source-file lock serializes import, deletion, backup and deletion recovery across sessions. To restore, select the backup directory as the data directory while other sessions are closed.

Deleting a document requires its current revision. Interrupted deletions restore retained sources or finish a committed deletion. A profile used by documents cannot be removed, and changing its taxpayer ID requires a new profile.

## Remote inference

No remote model is configured by default. Non-loopback endpoints require exact-destination disclosure and explicit per-import authorization before content is sent. Requests do not follow redirects or HTTP proxies. Credentials come from a named environment variable and are not persisted in settings.

## Telemetry decision

The saved local preference defaults to enabled and can be disabled. Collection and purge remain deferred until the user decides package contents and disable/delete behavior. No package is created, uploaded or purged. Disabling the preference does not erase an existing package.

## Documentation boundary

OpenWiki receives public code/documentation repository URLs only. Financial originals, ground truth, assets/, taxpayer data, credentials and raw telemetry must never be uploaded to a documentation service or public issue/PR.

Sources: [store and recovery](https://github.com/Fatrocu/fatrocu-cli/blob/f77e87bdb1d12f57f00b4b717f2787d8b3383231/src/storage.rs), [transfer authorization](https://github.com/Fatrocu/fatrocu-cli/blob/f77e87bdb1d12f57f00b4b717f2787d8b3383231/src/inference.rs).
