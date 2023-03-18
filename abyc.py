#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABCY E-11."""

import quantities as pq
import pandas as pd

from . import abyc_data
from . import wire

#
# TABLE VI – B - AC & DC CIRCUITS – ALLOWABLE AMPERAGE OF CONDUCTORS WHEN UP TO
# THREE CURRENT CARRYING CONDUCTORS ARE BUNDLED, SHEATHED OR IN CONDUIT
def GetWireGaugeUpToThreeConductorBundle(
    current, insulation_temp_rating, engine_room=False
):
    mag_current_A = int(current.rescale("A").magnitude)
    mag_insulation_temp_rating_C = int(insulation_temp_rating.rescale("C").magnitude)
    if mag_insulation_temp_rating_C not in abyc_data.TABLE_VI_B_KNOWN_TEMPS_C:
        raise KeyError(
            f"Unknown insulation temperature rating {insulation_temp_rating}; known ratings: {abyc_data.TABLE_VI_B_KNOWN_TEMPS_C} C"
        )
    column_name = "current_%dC" % mag_insulation_temp_rating_C + (
        "_engroom" if engine_room else ""
    )
    awg_vs_current = abyc_data.TABLE_VI_B[column_name]
    acceptable_awgs = awg_vs_current[awg_vs_current >= mag_current_A]
    if acceptable_awgs.empty:
        raise ValueError("No acceptable wire guage for circuit.")
    return wire.CanonicalizeAWG(acceptable_awgs.keys()[0])


#
# TABLE IX – CONDUCTORS SIZED FOR 3 PERCENT DROP IN VOLTAGE
# TABLE X - CONDUCTORS SIZES FOR 10 PERCENT VOLTAGE DROP
# Length of Conductor from Source of Current to Device and Back to Source

_TABLE_IX_X = {
    (12, 3): abyc_data.TABLE_IX_12V,
    (24, 3): abyc_data.TABLE_IX_24V,
    (32, 3): abyc_data.TABLE_IX_32V,
    (12, 10): abyc_data.TABLE_X_12V,
    (24, 10): abyc_data.TABLE_X_24V,
    (32, 10): abyc_data.TABLE_X_32V,
}
#
_TABLE_IX_X_VOLTAGES = sorted(set((v for (v, drop_pc) in _TABLE_IX_X.keys())))
_TABLE_IX_X_DROP_PCS = sorted(set((drop_pc for (v, drop_pc) in _TABLE_IX_X.keys())))
# All the same
_TABLE_IX_X_KNOWN_LENGTHS_FT = abyc_data.TABLE_IX_12V_KNOWN_LENGTHS_FT


def _list_max(l, minvalue):
    l = sorted(l)
    for v in l:
        if v >= minvalue:
            return v
    raise ValueError("No max value")


def GetAWGForCircuit(voltage, current, full_circuit_length, drop_pc=3):
    mag_current_A = int(current.rescale(pq.A).magnitude)
    mag_voltage_V = int(voltage.rescale(pq.V).magnitude)
    if mag_voltage_V not in _TABLE_IX_X_VOLTAGES:
        raise ValueError("Voltage is not {_TABLE_IX_X_VOLTAGES} V")
    if drop_pc not in _TABLE_IX_X_DROP_PCS:
        raise ValueError("Drop percentage not {_TABLE_IX_X_DROP_PCS}")
    key = (mag_voltage_V, drop_pc)
    table = _TABLE_IX_X[key]
    length_ft = _list_max(
        _TABLE_IX_X_KNOWN_LENGTHS_FT, full_circuit_length.rescale(pq.ft).magnitude
    )
    column_name = "awg_%dft" % length_ft
    current_vs_awg = table[column_name]
    awg_vs_current = pd.Series(current_vs_awg.index, current_vs_awg.values)
    acceptable_awgs = awg_vs_current[awg_vs_current >= mag_current_A]
    if acceptable_awgs.empty:
        raise ValueError("No acceptable wire guage for full circuit.")
    return wire.CanonicalizeAWG(acceptable_awgs.keys()[0])
