# Changelog

All notable changes to the registry. The format follows [Keep a Changelog](https://keepachangelog.com/), the versions follow [semantic versioning](https://semver.org/): a new detector or readout is a minor version, a changed number that results depend on is a minor version too and is called out, a correction of wording is a patch.

## [Unreleased]

### Added

- The repository, started from the setup of goldreg-R76: README, licence, contributing rules, a test of the data (`tests/test_registry.py`) and a workflow that runs it with the released goldpan on Linux, Windows and macOS.
- The `Z7` readout (`readouts.toml`), copied from goldreg-R76 at `3b562a2` with its evidence. It is `inferred` and not checked against a file.
