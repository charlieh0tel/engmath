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

# References:
#
# https://en.wikipedia.org/wiki/American_wire_gauge
# https://nvlpubs.nist.gov/nistpubs/Legacy/hb/nbshandbook100.pdf
# http://hyperphysics.phy-astr.gsu.edu/hbase/Tables/wirega.html


def testAWGInts():
    for awg in range(0, 40 + 1):
        assert wire.CanonicalizeAWG(awg) == awg
        assert wire.AWGSpecificationToNumber(awg) == awg
        assert wire.AWGSpecificationToNumber(str(awg)) == awg


def testAWGOneZero():
    for awg in [0, "0", "1/0"]:
        assert wire.AWGSpecificationToNumber(awg) == 0
        assert wire.CanonicalizeAWG(awg) == 0


def testAWGTwoZeroes():
    for awg in [-1, "00", "2/0"]:
        assert wire.AWGSpecificationToNumber(awg) == -1
        assert wire.CanonicalizeAWG(awg) == "2/0"


def testAWGThreeZeroes():
    for awg in [-2, "000", "3/0"]:
        assert wire.AWGSpecificationToNumber(awg) == -2
        assert wire.CanonicalizeAWG(awg) == "3/0"


def testAWGFourZeroes():
    for awg in [-3, "0000", "4/0"]:
        assert wire.AWGSpecificationToNumber(awg) == -3
        assert wire.CanonicalizeAWG(awg) == "4/0"

def testAWGXXX():
    with pytest.raises(ValueError):
        wire.AWGSpecificationToNumber("xxx")


#
def _checkSolidWireDiameter(awg, expected_value, atol=0.1e-3 * pq.inch):
    diameter = wire.SolidWireDiameter(awg)
    return isclose(diameter, expected_value, atol=atol)


# AWG 0000 (4/0) is by definition.
def testSolidWireDiameter_0000():
    assert _checkSolidWireDiameter("0000", 0.4600 * pq.inch)


def testSolidWireDiameter_4slash0():
    assert _checkSolidWireDiameter("4/0", 0.46 * pq.inch)


def testSolidWireDiameter_neg3():
    assert _checkSolidWireDiameter(-3, 0.46 * pq.inch)


def testSolidWireDiameter_000():
    assert _checkSolidWireDiameter("000", 0.40965 * pq.inch)


def testSolidWireDiameter_3slash0():
    assert _checkSolidWireDiameter("3/0", 0.40965 * pq.inch)


def testSolidWireDiameter_neg2():
    assert _checkSolidWireDiameter(-2, 0.40965 * pq.inch)


def testSolidWireDiameter_00():
    assert _checkSolidWireDiameter("00", 0.3648 * pq.inch)


def testSolidWireDiameter_2slash0():
    assert _checkSolidWireDiameter("2/0", 0.3648 * pq.inch)


def testSolidWireDiameter_neg1():
    assert _checkSolidWireDiameter(-1, 0.3648 * pq.inch)


def testSolidWireDiameter_str0():
    assert _checkSolidWireDiameter("0", 0.32485 * pq.inch)


def testSolidWireDiameter_1slash0():
    assert _checkSolidWireDiameter("1/0", 0.32485 * pq.inch)


def testSolidWireDiameter_0():
    assert _checkSolidWireDiameter(0, 0.32485 * pq.inch)


def testSolidWireDiameter_21():
    assert _checkSolidWireDiameter(21, 0.02846 * pq.inch)


# AWG 36 is by definition.
def testSolidWireDiameter_36():
    assert _checkSolidWireDiameter(36, 0.0050 * pq.inch)


def testSolidWireDiameter_40():
    assert _checkSolidWireDiameter(40, 0.00314 * pq.inch)


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
