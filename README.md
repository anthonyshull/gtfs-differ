# GTFS Differ

![GTFS Differ](https://github.com/anthonyshull/gtfs-differ/actions/workflows/gtfs_differ.yml/badge.svg)

[Download the Latest Diff](https://github.com/anthonyshull/gtfs-differ/releases/latest/download/diff.zip)

This repository contains a [GitHub Action](https://github.com/anthonyshull/gtfs-differ/blob/main/.github/workflows/gtfs_differ.yml) that periodically publishes a diff of [GTFS](https://gtfs.org/) changes.

## Instructions

You can point this process at any GTFS feed file with the following steps.

1. Fork this repository.
2. Add an [Actions variable](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables) `GTFS_URL` that points to the zip file you want to process.

This repository is currently set to track changes published by the [MBTA](https://mbta.com) at `https://cdn.mbta.com/MBTA_GTFS.zip`. 