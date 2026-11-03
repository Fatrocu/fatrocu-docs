# Vercel OpenWiki publication

The selected platform is [Vercel OpenWiki](https://openwiki.sh/), from [vercel-labs/openwiki](https://github.com/vercel-labs/openwiki). It generates a source-cited wiki from a public GitHub repository. This documentation source needs no second application frontend.

## Publication workflow

1. Run `python scripts/check_docs.py` and review this candidate.
2. Wait for the product accuracy gate and review. A human may then promote the reviewed documentation to main. This work merges no PRs and does not bypass that rule.
3. Run scripts/submit-openwiki.ps1 with -ExpectedMainCommit set to the exact reviewed documentation SHA. -DryRun checks preconditions without submitting.
4. The script verifies public visibility and exact main revision, then submits the documentation repository URL. It returns the wiki URL and indexing metadata; submission alone is not a successfully published wiki.
5. Inspect the generated navigation, citations, setup instructions and pending release gates. Use -Refresh only when deliberately requesting regeneration.

The expected route is https://openwiki.sh/Fatrocu/fatrocu-docs. Do not claim it is published until indexing succeeds.

## Current publication constraint

The hosted API accepts a repository URL without a branch/ref argument, and rejects tree/branch URLs. Indexing the old application default branches would describe superseded code. The reviewed guides therefore stay on the documentation candidate branch until a human promotes them. No index request is sent for an empty or outdated main.

## Self-hosting

The upstream app can be deployed separately on Vercel with Neon Postgres, Vercel Blob and an eve agent. These resources and billing credentials are not provisioned automatically. No database URL, Blob token, provider credential or Vercel linkage file belongs in this repository.

Only public source/documentation URLs go to OpenWiki. Source financial documents, labels, private datasets, taxpayer records and telemetry never do.

Upstream references: [official workflow](https://github.com/vercel-labs/openwiki/blob/main/README.md), [submission schema](https://github.com/vercel-labs/openwiki/blob/main/app/api/repositories/route.ts), [repository URL parser](https://github.com/vercel-labs/openwiki/blob/main/lib/github-repo-url.ts).
