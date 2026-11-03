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

The desktop uses the CLI-owned core. The server manages the model runtime. Source citations pin exact reviewed commits: [core/CLI](https://github.com/Fatrocu/fatrocu-cli/tree/6eeb108e90cb3f8512780b2f989736b3e5f10f58), [desktop](https://github.com/Fatrocu/Fatrocu/tree/e99518fa4a301d14c2d08eb68574f865c3baa89c), [server](https://github.com/Fatrocu/fatrocu-server/tree/d4aaca0e5977b470308e5fa9a903ac901655df6d).

Documentation stays on its review branch until a human promotes it. This task merges no PRs. OpenWiki submission checks that the default branch equals the reviewed documentation revision before indexing it.
