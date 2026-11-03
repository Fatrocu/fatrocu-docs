---
title: Getting started
nav_order: 2
permalink: /getting-started/
---

# Getting started

Fatrocu processes e-Archive invoices, OKC Z reports and UTTS fuel slips. The workflow is import, extract, inspect/correct, approve each document, then export. Excel is the initial default; CSV and JSON are available.

The desktop supports Windows. The CLI and model tool support Windows/Linux. The baseline target is a CPU-only computer with 16 GB RAM. PDF previews and scanned-PDF inference require Poppler pdftoppm on PATH; PDF text extraction is built into Rust. PNG/JPEG need no PDF helper.

For development, keep Fatrocu, fatrocu-cli and fatrocu-server as sibling checkouts. Match the pinned dependency revisions. Build with cargo build --locked. These instructions apply to 3.1.0-beta.1; older stable releases may not include this behavior. [Download the beta packages](../index.md#download-the-beta) and extract them to a new directory before following the steps below. The Windows desktop ZIP includes the server and updater companions.

1. Run `fatrocu-server setup`. Standard downloads and verifies the CPU runtime, default model and visual projector, then starts a loopback-only API.
2. Open the Windows desktop. In Settings / About, create a taxpayer profile with a legal name and VKN/TCKN.
3. On Upload, choose the taxpayer and e-Archive or OKC template. Choose Z report or UTTS for OKC documents.
4. Add files, inspect the actual source and extracted fields, correct errors, and approve individually.
5. Select approved records and export to a fresh path outside Git.

On later sessions, use `fatrocu-server start`. If inference is unavailable, deterministic/manual imports preserve missing values for review. Never guess a blank field.

Sources: [CLI usage](https://github.com/Fatrocu/fatrocu-cli/blob/f77e87bdb1d12f57f00b4b717f2787d8b3383231/README.md), [setup implementation](https://github.com/Fatrocu/fatrocu-server/blob/09bd9a9ffa9bf07b58a6a9aad0867c20e7713993/src/main.rs).
