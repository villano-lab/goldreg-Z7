# goldreg-Z7

The detector registry of the **Z7** analysis (SuperCDMS-type detector Z7, SNOLAB; the MIDAS series such as `24260424_145101`).

It holds the facts about the detectors that the analysis needs and that [goldpan](https://github.com/villano-lab/goldpan) must not contain: a detector's number, type, readout and where each named channel is wired in a given file format. It is **data, not code**: goldpan and [goldsluice](https://github.com/villano-lab/goldsluice) read it (`goldpan.registry`, specification in its docstring) and nothing in them depends on it. Its companion for the Run 76 analysis is [goldreg-R76](https://github.com/villano-lab/goldreg-R76).

| File | What it holds |
|---|---|
| `readouts.toml` | the readouts, with the evidence for each number (`Z7`) |

There are **no detector records yet**. For a MIDAS file, `goldpan.adapters.midas.detectors(path)` returns what the file's ODB says about each detector and `goldpan.adapters.midas.registry_entry(detector)` writes a starting entry from it; add it to a `detectors.toml` here and check it with `goldpan.registry.compare`.

Every entry has a `status` (`confirmed` or `inferred`) and `evidence` that says where it comes from. Write `confirmed` only for what a file or a document says; never write a guess as `confirmed`. A name is defined once.

## Using it

Give the folder to goldpan in one of two ways:

- in a dataset definition: `[dataset] registry = ["../goldreg-Z7"]` (relative to the definition file);
- or set the environment variable `GOLDPAN_REGISTRY` to the folder.

```python
from goldpan import registry

reg = registry.load("~/goldreg-Z7")
config = reg.readout_config("Z7")        # a goldpan.config.PulseConfig
```

## Changing it

Work as in [`CONTRIBUTING.md`](CONTRIBUTING.md): a branch from `develop` and a pull request. Edit the TOML by hand, or let a program add a record (`goldpan.registry.add_record`). Then run `python -m pytest`.

A change to a number that results depend on (a pretrigger window, a sample period) is announced in [`CHANGELOG.md`](CHANGELOG.md): outputs made with the old value differ and should be made again.

## History

Started on 2026-11-06 for the one-registry-per-analysis plan (NSDF-Data task list, item 70). The `Z7` readout was copied from goldreg-R76, where it was the only record of another analysis (its `evidence` says so). A detector is shared between registries by copying its record, with `copied_from = "goldreg-R76@<commit>"` next to its `evidence` once goldpan reads that key.
