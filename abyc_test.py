#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABYC test."""

# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

import quantities as pq
import pytest

from . import abyc


def testGetWireGaugeUpToThreeCounductorBundle11A60C():
    assert (
        abyc.GetWireGaugeUpToThreeConductorBundle(
            11 * pq.A, 60 * pq.C, engine_room=False
        )
        == 14
    )


def testGetWireGaugeUpToThreeCounductorBundleT11A60CEng():
    with pytest.raises(ValueError):
        abyc.GetWireGaugeUpToThreeConductorBundle(
            11 * pq.A, 60 * pq.C, engine_room=True
        )


def testGetWireGaugeUpToThreeCounductorBundle150NotEngine():
    assert (
        abyc.GetWireGaugeUpToThreeConductorBundle(
            150 * pq.A, 105 * pq.C, engine_room=False
        )
        == 1
    )


def testGetWireGaugeUpToThreeCounductorBundle150Engine():
    assert (
        abyc.GetWireGaugeUpToThreeConductorBundle(
            150 * pq.A, 105 * pq.C, engine_room=True
        )
        == 0
    )


def testGetWireGaugeUpToThreeCounductorBundleHighest():
    assert (
        abyc.GetWireGaugeUpToThreeConductorBundle(
            357 * pq.A, 200 * pq.C, engine_room=False
        )
        == "4/0"
    )


def testGetWireGaugeUpToThreeCounductorBundleTooHigh():
    with pytest.raises(ValueError):
        abyc.GetWireGaugeUpToThreeConductorBundle(
            357 * pq.A, 200 * pq.C, engine_room=True
        )


########################################################################


def testGetAWGForCircuitTest_12V_4A_9FT():
    assert abyc.GetAWGForCircuit(12.0 * pq.V, 4.0 * pq.A, 9.0 * pq.ft) == 18


def testGetAWGForCircuitTest_24V_24A_71FT():
    assert abyc.GetAWGForCircuit(24.0 * pq.V, 24.0 * pq.A, 71.0 * pq.ft) == 4


def testGetAWGForCircuitTest_12V_80A_100FT_Fail():
    with pytest.raises(ValueError):
        abyc.GetAWGForCircuit(12.0 * pq.V, 80.0 * pq.A, 100.0 * pq.ft)


def testGetAWGForCircuitTest4_32V_25A_70FT():
    assert abyc.GetAWGForCircuit(32.0 * pq.V, 25.0 * pq.A, 70.0 * pq.ft) == 6


def testGetAWGForCircuitTest5_32V_25A_70FT_10PC():
    assert (
        abyc.GetAWGForCircuit(32.0 * pq.V, 25.0 * pq.A, 70.0 * pq.ft, drop_pc=10) == 10
    )


def testGetAWGForCircuitTest5_32V_2A_12FT_10PC():
    assert (
        abyc.GetAWGForCircuit(32.0 * pq.V, 2.0 * pq.A, 12.0 * pq.ft, drop_pc=10) == 18
    )
