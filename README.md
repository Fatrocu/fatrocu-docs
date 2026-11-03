# Fatrocu 3.1 documentation

Product setup, document review and agent automation guides for the Rust Fatrocu applications. The selected publication platform is **Vercel OpenWiki (openwiki.sh)**.

These guides describe candidate branches. The private e-Archive and OKC accuracy gates remain **NOT RUN (dataset pending)**. Telemetry package contents/purge and the release publisher identity remain undecided. This candidate is not a verified stable release.

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
- [Vercel OpenWiki publication](docs/openwiki.md)

Validate with `python scripts/check_docs.py`. This repository contains no financial samples, taxpayer records, ground truth, weights, credentials or telemetry. Only public code/documentation repository URLs may be submitted to OpenWiki.

The desktop uses the CLI-owned core. The server manages the model runtime. Source citations pin exact reviewed commits: [core/CLI](https://github.com/Fatrocu/fatrocu-cli/tree/90e3a225eaa58c9e83789b71f5b624d0fd63a058), [desktop](https://github.com/Fatrocu/Fatrocu/tree/df4e9546e456a088cec43bf7490f7f57d050e698), [server](https://github.com/Fatrocu/fatrocu-server/tree/7ab0bd24631d6272481a6df1d2458280c80cd0ce).

Documentation stays on its review branch until a human promotes it. This task merges no PRs. OpenWiki submission checks that the default branch equals the reviewed documentation revision before indexing it.
