# Getting started

Fatrocu processes e-Archive invoices, OKC Z reports and UTTS fuel slips. The workflow is import, extract, inspect/correct, approve each document, then export. Excel is the initial default; CSV and JSON are available.

The desktop supports Windows. The CLI and model tool support Windows/Linux. The baseline target is a CPU-only computer with 16 GB RAM. PDF previews and scanned-PDF inference require Poppler pdftoppm on PATH; PDF text extraction is built into Rust. PNG/JPEG need no PDF helper.

For development, keep Fatrocu, fatrocu-cli and fatrocu-server as sibling checkouts. Match the pinned dependency revisions. Build with cargo build --locked. These instructions apply to candidate sources; superseded stable releases may not include this behavior.

1. Run `fatrocu-server setup`. Standard downloads and verifies the CPU runtime, default model and visual projector, then starts a loopback-only API.
2. Open the Windows desktop. In Settings / About, create a taxpayer profile with a legal name and VKN/TCKN.
3. On Upload, choose the taxpayer and e-Archive or OKC template. Choose Z report or UTTS for OKC documents.
4. Add files, inspect the actual source and extracted fields, correct errors, and approve individually.
5. Select approved records and export to a fresh path outside Git.

On later sessions, use `fatrocu-server start`. If inference is unavailable, deterministic/manual imports preserve missing values for review. Never guess a blank field.

Sources: [CLI usage](https://github.com/Fatrocu/fatrocu-cli/blob/90e3a225eaa58c9e83789b71f5b624d0fd63a058/README.md), [setup implementation](https://github.com/Fatrocu/fatrocu-server/blob/7ab0bd24631d6272481a6df1d2458280c80cd0ce/src/main.rs).
