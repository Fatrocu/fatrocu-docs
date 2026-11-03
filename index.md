---
title: Home
nav_order: 1
permalink: /
---

# Fatrocu Wiki

Set up Fatrocu, review source documents and automate approved exports. Fatrocu 3.1 processes **e-Archive invoices, OKC Z reports and UTTS fuel slips** with a shared Rust core, a Windows desktop and Windows/Linux command-line tools.

> **3.1.0-beta.1 preview.** Private extraction accuracy is **NOT RUN (dataset pending)**. Neither document-family gate has passed. Downloads are unsigned manual-test builds. Review every extracted value before approving a document; unreadable values stay blank/null. Stable 3.1.0 follows successful accuracy validation and the remaining release checks, with no confirmed date.

## Start with your workflow

| What you want to do | Read this guide |
| --- | --- |
| Install the tools and process your first document | [Getting started](docs/getting-started.md) |
| Review and correct documents on Windows | [Desktop workflow](docs/desktop-workflow.md) |
| Run repeatable CLI or agent workflows | [CLI and automation](docs/cli-automation.md) |
| Install a local model or configure hosting | [Model setup and hosting](docs/model-server.md) |
| Understand fields, tax rows and approval rules | [Schema and human review](docs/schema-review.md) |
| Manage retained originals, credentials and telemetry preferences | [Privacy and retention](docs/privacy-and-data.md) |
| Understand signed updates and current limitations | [Updates](docs/updates.md) |
| Diagnose setup, preview or extraction problems | [Troubleshooting](docs/troubleshooting.md) |
| Understand the private acceptance gate | [Benchmark status](docs/benchmark-gate.md) |
| Maintain or republish this wiki | [Wiki publication](docs/openwiki.md) |

## Download the beta

| Application | Platforms | Release |
| --- | --- | --- |
| Fatrocu Desktop | Windows x86_64 | [3.1.0-beta.1](https://github.com/Fatrocu/Fatrocu/releases/tag/3.1.0-beta.1) |
| Fatrocu CLI | Windows/Linux x86_64 | [3.1.0-beta.1](https://github.com/Fatrocu/fatrocu-cli/releases/tag/3.1.0-beta.1) |
| Fatrocu Server | Windows/Linux x86_64 | [3.1.0-beta.1](https://github.com/Fatrocu/fatrocu-server/releases/tag/3.1.0-beta.1) |

Each release provides ZIP downloads and SHA-256 files. Extract all files into a new directory. Publisher signing is pending; these previews are separate from verified stable updates. Model setup downloads llama.cpp, Qwen3.5-4B and its visual projector separately. PDF previews and scanned-PDF inference require Poppler `pdftoppm` on PATH.

## The document workflow

1. Choose a taxpayer profile and document template.
2. Import one or more documents and extract source-grounded fields.
3. Inspect the source, correct mistakes and resolve review flags.
4. Approve each document individually.
5. Export approved records to Excel, CSV or JSON.

Original documents and work records remain on your device. Local inference is the default; optional non-loopback inference requires disclosure and consent before document contents are sent. Telemetry package collection and purge await the user decision. This public wiki receives no financial documents, labels, credentials or raw telemetry.

## Find an answer

Use the search field for commands, field names or setup topics, or browse the guide menu. Source citations in each guide pin the application revisions used by this beta.
