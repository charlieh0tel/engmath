#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire test."""

# pylint: disable=missing-function-docstring

import quantities as pq
import pytest

from . import wire
from .test_utils import isclose

# Diameters from http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/wirega.html


def _checkSolidDiameter(awg, expected_diameter, atol=0.1e-3 * pq.inch):
    diameter = wire.SolidAWGDiameter(awg)
    return isclose(diameter, expected_diameter, atol=atol)


def test_wire_dia_awg_0000():
    assert _checkSolidDiameter("0000", 0.46 * pq.inch)


def test_wire_dia_awg_neg3():
    assert _checkSolidDiameter(-3, 0.46 * pq.inch)


def test_wire_dia_awg_000():
    assert _checkSolidDiameter("000", 0.40965 * pq.inch)


def test_wire_dia_awg_neg2():
    assert _checkSolidDiameter(-2, 0.40965 * pq.inch)


def test_wire_dia_awg_00():
    assert _checkSolidDiameter("00", 0.3648 * pq.inch)


def test_wire_dia_awg_neg1():
    assert _checkSolidDiameter(-1, 0.3648 * pq.inch)


def test_wire_dia_awg_0():
    assert _checkSolidDiameter(0, 0.32485 * pq.inch)


def test_wire_dia_awg_21():
    assert _checkSolidDiameter(21, 0.02846 * pq.inch)


def test_wire_dia_awg_40():
    assert _checkSolidDiameter(40, 0.00314 * pq.inch)


def test_wire_dia_awg_neg4():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter(-4)


def test_wire_dia_awg_41():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter(41)


def test_wire_dia_awg_xxx():
    with pytest.raises(ValueError):
        wire.SolidAWGDiameter("xxx")


# Areas from http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/wirega.html


def _checkSolidArea(awg, expected_area, atol=4.0 * pq.cmil):
    area = wire.SolidAWGCrossSectionalArea(awg)
    return isclose(area, expected_area, atol=atol)


def test_wire_area_awg_0000():
    assert _checkSolidArea("0000", 211600.0 * pq.cmil)


def test_wire_area_awg_0():
    assert _checkSolidArea(0, 105530.0 * pq.cmil)


def test_wire_area_awg_21():
    assert _checkSolidArea(21, 810.1 * pq.cmil)


def test_wire_area_awg_40():
    assert _checkSolidArea(40, 9.89 * pq.cmil)
