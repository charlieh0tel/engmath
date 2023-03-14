# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Tests for battery.py"""

# pylint: disable=missing-function-docstring

import quantities as pq
import pytest

from . import battery
from .test_utils import isclose


def test_single_cell_battery():
    chemistry = battery.LithiumNMC
    batteria = battery.Battery(cell_chemistry=chemistry, total_energy=10e3 * pq.J)
    assert isclose(batteria.nominal_voltage, chemistry.cell_voltage, atol=1e-3 * pq.V)
    assert isclose(batteria.capacity, 771.0 * pq.mA * pq.hr, atol=1.0 * pq.mA * pq.hr)


def test_fail_multi_cell_no_confg_battery():
    chemistry = battery.LithiumNMC
    batteria = battery.Battery(
        cell_chemistry=chemistry, total_energy=10e3 * pq.J, n_cells=2
    )
    with pytest.raises(ValueError):
        assert isclose(
            batteria.nominal_voltage, chemistry.cell_voltage, atol=1e-3 * pq.V
        )


def test_series_battery():
    chemistry = battery.LithiumNMC
    n_cells = 2
    batteria = battery.SeriesBattery(
        cell_chemistry=chemistry, total_energy=10e3 * pq.J, n_cells=n_cells
    )
    assert isclose(
        batteria.nominal_voltage, n_cells * chemistry.cell_voltage, atol=1e-3 * pq.V
    )
    assert isclose(batteria.capacity, 385.0 * pq.mA * pq.hr, atol=1.0 * pq.mA * pq.hr)
