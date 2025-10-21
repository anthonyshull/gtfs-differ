# GTFS Differ

![GTFS Differ](https://github.com/anthonyshull/gtfs-differ/actions/workflows/gtfs_differ.yml/badge.svg)

[Download the Latest Diff](https://github.com/anthonyshull/gtfs-differ/releases/latest/download/diff.zip)

This repository contains a GitHub Action that periodically publishes a diff of GTFS changes.

## Instructions

You can point this process at any GTFS feed file with the following steps.

1. Fork this repository.
2. Add an *action variable* `GTFS_URL` that points to the zip file you want to process.
