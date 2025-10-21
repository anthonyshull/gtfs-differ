# GTFS Differ

![GTFS Differ](https://github.com/anthonyshull/gtfs-differ/actions/workflows/gtfs_differ.yml/badge.svg)

This repository contains a GitHub Action that periodically publishes a diff of GTFS changes.

## Instructions

You can point this process at any GTFS feed file with the following steps.

1. Fork this repository.
2. Add an *action variable* `GTFS_URL` that points to the zip file you want to process.
3. Create a personal access token and give it access to repository content. [See more](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
4. Add an *action secret* `GH_PAT` with the personal access token created above.