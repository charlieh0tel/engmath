#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABCY E-11."""

from . import abyc_data
from . import wire

#
# Table 6.

def GetWireGaugeUpToThreeConductorBundle(
        current, insulation_temp_rating_C, engine_room=False):
    mag_current_A = current.rescale("A").magnitude
    mag_insulation_temp_rating_C = insulation_temp_rating_C.rescale('C').magnitude
    if mag_insulation_temp_rating_C not in abyc_data.TABLE_VI_B_KNOWN_TEMPS_C:
        raise KeyError(
            f"Unknown insulation temperature rating; known ratings: {TABLE_VI_B_KNOWN_TEMPS_C} C"
        )
    column_name = ("current_%dC" % mag_insulation_temp_rating_C +
                   ("_engroom" if engine_room else ""))
    awg_vs_current = abyc_data.TABLE_VI_B[column_name]
    acceptable_awgs = awg_vs_current[awg_vs_current >= mag_current_A]
    if acceptable_awgs.empty:
        raise ValueError("No acceptable wire guage for full circuit current.")
    return wire.CanonicalizeAWG(acceptable_awgs.keys()[0])



#
# Table 9.

_TABLE9 = {
    (12, 3): abyc_data.TABLE_IX_12V_3PC,
    (24, 3): abyc_data.TABLE_IX_24V_3PC,
    (32, 3): abyc_data.TABLE_IX_32V_3PC,
    (12, 10): abyc_data.TABLE_IX_12V_10PC,
    (24, 10): abyc_data.TABLE_IX_24V_10PC,
    (32, 10): abyc_data.TABLE_IX_32V_10PC
}
_TABLE9_VOLTAGES=sorted(set([v for (v, pc) in _TABLE9.keys()]))
_TABLE9_PC_DROPS=sorted(set([pc for (v, pc) in _TABLE9.keys()]))
# All of the tables are the same.
_TABLE9_KNOWN_LENGTHS_FT=abyc_data.TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT

"""
def GetAWGForLength(voltage_V, full_circuit_length_ft):, 
    if full_circuit_length_ft not in TABLE_IX_12V_3PC_KNOWN_LENGTHS:
        raise KeyError(
            f"Unknown length; known lengths: {TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT} FT"
        )
    column_name = "awg_%dft" % full_circuit_length_ft
    current_vs_awg
"""
