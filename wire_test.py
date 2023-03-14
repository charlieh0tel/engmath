#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire test."""

# pylint: disable=missing-function-docstring

import numpy as np
import quantities as pq
import pytest

from . import wire


def _checkSolidDiameter(awg, expected_dia, atol=1e-3 * pq.inch):
    return np.isclose(wire.SolidAWGDiameter(awg), expected_dia, atol=atol)


def test_wire_awg_0000():
    assert _checkSolidDiameter("0000", 0.46 * pq.inch)


def test_wire_awg_neg3():
    assert _checkSolidDiameter(-3, 0.46 * pq.inch)


def test_wire_awg_000():
    assert _checkSolidDiameter("000", 0.4096 * pq.inch)


def test_wire_awg_neg2():
    assert _checkSolidDiameter(-2, 0.4096 * pq.inch)


def test_wire_awg_00():
    assert _checkSolidDiameter("00", 0.3648 * pq.inch)


def test_wire_awg_neg1():
    assert _checkSolidDiameter(-1, 0.3648 * pq.inch)


def test_wire_awg_0():
    assert _checkSolidDiameter(0, 0.3249 * pq.inch)


def test_wire_awg_21():
    assert _checkSolidDiameter(21, 0.0285 * pq.inch)


def test_wire_awg_40():
    assert _checkSolidDiameter(40, 0.0031 * pq.inch)


def test_wire_awg_neg4():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter(-4)


def test_wire_awg_41():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter(41)


def test_wire_awg_xxx():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter("xxx")
