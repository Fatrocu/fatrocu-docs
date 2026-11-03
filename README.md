# Fatrocu 3.1 documentation

Product setup, document review and agent automation guides for the Rust Fatrocu applications. Read the published **[Fatrocu Wiki on GitHub Pages](https://fatrocu.github.io/fatrocu-docs/)**.

These guides describe **3.1.0-beta.1**, an unsigned manual-test preview. The private e-Archive and OKC accuracy gates remain **NOT RUN (dataset pending)**. Telemetry package contents/purge and the release publisher identity remain undecided. This candidate is not a verified stable release.

## Read the guides

- [Getting started](docs/getting-started.md)
- [Windows desktop workflow](docs/desktop-workflow.md)
- [CLI and agent automation](docs/cli-automation.md)
- [Model setup and hosting](docs/model-server.md)
- [Schema and human review](docs/schema-review.md)
- [Privacy and retention](docs/privacy-and-data.md)
- [Signed updates](docs/updates.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Private accuracy gate](docs/benchmark-gate.md)
- [Wiki publication](docs/openwiki.md)

Validate with `python scripts/check_docs.py`. This repository contains no financial samples, taxpayer records, ground truth, weights, credentials or telemetry. The static wiki publishes only these public Markdown guides.

The desktop uses the CLI-owned core. The server manages the model runtime. Source citations pin exact reviewed commits: [core/CLI](https://github.com/Fatrocu/fatrocu-cli/tree/f77e87bdb1d12f57f00b4b717f2787d8b3383231), [desktop](https://github.com/Fatrocu/Fatrocu/tree/9d487eda618e68fd1e4ac69b901e89444a1796df), [server](https://github.com/Fatrocu/fatrocu-server/tree/09bd9a9ffa9bf07b58a6a9aad0867c20e7713993).

The repository owner promoted the original guide candidate to main in PR #1. The GitHub Pages site is published from the separate `codex/publish-docs-wiki` branch after source validation and an actual Jekyll build. Main and PR merge settings are not changed. Just the Docs v0.12.0 provides navigation and local search. The user selected GitHub Pages after the hosted OpenWiki API returned HTTP 500; no successful OpenWiki indexing is claimed.
