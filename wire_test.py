#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire test."""

# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

import quantities as pq
import pytest

from . import wire
from .test_utils import isclose

# Diameters from http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/wirega.html


def _checkSolidWireDiameter(awg, expected_value, atol=0.1e-3 * pq.inch):
    diameter = wire.SolidWireDiameter(awg)
    return isclose(diameter, expected_value, atol=atol)


def testSolidWireDiameter_0000():
    assert _checkSolidWireDiameter("0000", 0.46 * pq.inch)


def testSolidWireDiameter_neg3():
    assert _checkSolidWireDiameter(-3, 0.46 * pq.inch)


def testSolidWireDiameter_000():
    assert _checkSolidWireDiameter("000", 0.40965 * pq.inch)


def testSolidWireDiameter_neg2():
    assert _checkSolidWireDiameter(-2, 0.40965 * pq.inch)


def testSolidWireDiameter_00():
    assert _checkSolidWireDiameter("00", 0.3648 * pq.inch)


def testSolidWireDiameter_neg1():
    assert _checkSolidWireDiameter(-1, 0.3648 * pq.inch)


def testSolidWireDiameter_0():
    assert _checkSolidWireDiameter(0, 0.32485 * pq.inch)


def testSolidWireDiameter_21():
    assert _checkSolidWireDiameter(21, 0.02846 * pq.inch)


def testSolidWireDiameter_40():
    assert _checkSolidWireDiameter(40, 0.00314 * pq.inch)


def testSolidWireDiameter_neg4():
    with pytest.raises(ValueError):
        wire.SolidWireDiameter(-4)


def testSolidWireDiameter_41():
    with pytest.raises(ValueError):
        wire.SolidWireDiameter(41)


def testSolidWireDiameter_xxx():
    with pytest.raises(ValueError):
        wire.SolidWireDiameter("xxx")


# Areas from http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/wirega.html


def _checkSolidWireArea(awg, expected_value, atol=4.0 * pq.cmil):
    area = wire.SolidWireCrossSectionalArea(awg)
    return isclose(area, expected_value, atol=atol)


def testSolidWireArea_0000():
    assert _checkSolidWireArea("0000", 211600.0 * pq.cmil)


def testSolidWireArea_0():
    assert _checkSolidWireArea(0, 105530.0 * pq.cmil)


def testSolidWireArea_21():
    assert _checkSolidWireArea(21, 810.1 * pq.cmil)


def testSolidWireArea_40():
    assert _checkSolidWireArea(40, 9.89 * pq.cmil)


# Resistance per unit length from https://en.wikipedia.org/wiki/American_wire_gauge


def _checkSolidWireResistancePerUnitLength(
    awg, expected_value, atol=100e-6 * pq.ohm / pq.m
):
    r_per_unit_length = wire.SolidWireResistancePerUnitLength(awg)
    return isclose(r_per_unit_length, expected_value, atol=atol)


def testSolidWireResistancePerUnitLength_0000():
    assert _checkSolidWireResistancePerUnitLength("0000", 0.1608e-3 * pq.ohm / pq.m)


def testSolidWireResistancePerUnitLength_0():
    assert _checkSolidWireResistancePerUnitLength(0, 0.3224e-3 * pq.ohm / pq.m)


def testSolidWireResistancePerUnitLength_21():
    assert _checkSolidWireResistancePerUnitLength(21, 42.00e-3 * pq.ohm / pq.m)


def testSolidWireResistancePerUnitLength_40():
    assert _checkSolidWireResistancePerUnitLength(40, 3.441 * pq.ohm / pq.m)
