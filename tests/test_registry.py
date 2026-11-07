"""The registry of this repository is valid: goldpan reads it, every record says where it comes from, and the few facts that other
code relies on are stated. It needs the released goldpan (`pip install goldpan pytest`) and nothing else."""
from pathlib import Path

import pytest

registry = pytest.importorskip("goldpan.registry")

FOLDER = Path(__file__).resolve().parents[1]


def reg():
    return registry.load(FOLDER, use_environment=False)


def test_the_folder_is_a_valid_registry_and_every_entry_says_where_it_comes_from():
    r = reg()
    assert r.readouts()
    for rec in list(r.detectors().values()) + list(r.readouts().values()):
        assert rec.status in registry.STATUSES and rec.evidence.strip()
    for rec in r.detectors().values():
        if rec.readout is not None:
            r.readout_config(rec.readout)                                    # the readout it names exists


def test_the_z7_readout_is_1p6_us_per_sample_and_says_it_is_not_checked_against_a_file():
    rec = reg().readouts()["Z7"]
    assert rec.config.sample_period_s == 1.6e-6 and rec.config.glitch_samples == 10 and rec.config.pretrigger_samples > 0
    assert rec.status != "inferred" or "checked" in rec.evidence             # an inferred readout says how far it was checked
