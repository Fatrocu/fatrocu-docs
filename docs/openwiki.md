---
title: Wiki publication
nav_order: 11
permalink: /publication/
---

# Wiki publication

The public wiki is [Fatrocu Wiki on GitHub Pages](https://fatrocu.github.io/fatrocu-docs/). The user selected this publication target on 2026-11-03 after the hosted Vercel OpenWiki submission API returned HTTP 500. OpenWiki indexing did not succeed and is not claimed.

## Source and build

The wiki is built from the `codex/publish-docs-wiki` branch of [Fatrocu/fatrocu-docs](https://github.com/Fatrocu/fatrocu-docs). The original guide candidate was promoted to main by the repository owner in [PR #1](https://github.com/Fatrocu/fatrocu-docs/pull/1). Publishing from a separate branch preserves main and requires no agent PR merge.

GitHub Pages builds Jekyll with Just the Docs pinned to v0.12.0. The theme supplies responsive navigation, local page search, heading anchors and code-copy controls. Relative Markdown links work both in the repository and on the published site. No runtime database, model provider, API credential or analytics integration is configured.

## Update and verify

1. Start a separate worktree/branch for a documentation change and read the workspace instructions.
2. Update the Markdown sources and retain exact application source citations. Keep beta and unrun benchmark limitations accurate.
3. Run `python scripts/check_docs.py`. The documentation workflow also builds the actual Jekyll site before publication.
4. Commit the reviewed source and publish only the intended revision to the Pages source branch. GitHub Pages source is the repository root of `codex/publish-docs-wiki`; it is separate from the default main branch.
5. Confirm the Pages build/deployment succeeded for that commit. Inspect the home page, all guides, navigation, search results, source links and beta downloads before declaring success.

Financial records, ground truth, credentials, models and raw telemetry never belong in this repository or wiki. Documentation publication does not enable the private accuracy benchmark or establish an extraction pass.

## Optional OpenWiki indexing

The original `scripts/submit-openwiki.ps1` is retained for a future deliberate OpenWiki indexing request. It verifies public visibility and an exact main revision before submitting. The official hosted API accepts a repository URL without a branch/ref argument, so it must not be used to index an unreviewed or outdated default branch. No OpenWiki refresh is required for this GitHub Pages publication.

References: [GitHub Pages branch publication](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [pinned theme source](https://github.com/just-the-docs/just-the-docs/blob/v0.12.0/_config.yml), [OpenWiki submission schema](https://github.com/vercel-labs/openwiki/blob/main/app/api/repositories/route.ts).
