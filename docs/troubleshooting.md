---
title: Troubleshooting
nav_order: 9
permalink: /troubleshooting/
---

# Troubleshooting

| Symptom | Action |
| --- | --- |
| Model unavailable | Run fatrocu-server start, wait for loading, then use connection-check. Verify URL and model alias. |
| PDF preview cannot start | Install trusted Poppler pdftoppm and add its bin directory to PATH. Rust text extraction itself needs no PDF helper. |
| Blank field | Inspect the source, correct it or individually acknowledge an unreadable required value. Never infer missing financial values. |
| Blank direction | Check taxpayer selection and party IDs. Neither or both matching requires review. |
| Approval fails | Read show.issues and correct invalid dates, IDs, decimals and coordinates. These cannot be waived. |
| Stale revision | Reload and preserve the other reviewer's corrections before retrying. |
| Export fails | Select approved records and a new writable file outside Git. |
| Template fails | Retain built-in keys, use a custom ID, ASCII keys and English labels. |
| Remote request refused | Review the destination disclosure and authorize this import only if appropriate. Check the credential environment variable. |
| Update refused | Obtain the matching signed artifact and independently confirmed trust anchor. Do not bypass verification. |
| Download digest mismatch | Discard only the corrupt managed artifact and rerun setup. Never execute mismatched downloads. |

Report a redacted reproduction with OS, version/commit, template and model/runtime revision. Do not attach financial documents, taxpayer values, API keys or telemetry. Prefer synthetic reproductions.

Sources: [CLI usage](https://github.com/Fatrocu/fatrocu-cli/blob/f77e87bdb1d12f57f00b4b717f2787d8b3383231/README.md), [server usage](https://github.com/Fatrocu/fatrocu-server/blob/09bd9a9ffa9bf07b58a6a9aad0867c20e7713993/README.md).
