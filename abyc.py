#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABCY E-11."""

from . import abyc_data
from . import wire

#
# TABLE VI – B - AC & DC CIRCUITS – ALLOWABLE AMPERAGE OF CONDUCTORS WHEN UP TO
# THREE CURRENT CARRYING CONDUCTORS ARE BUNDLED, SHEATHED OR IN CONDUIT
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
# TABLE IX – CONDUCTORS SIZED FOR 3 PERCENT DROP IN VOLTAGE
# Length of Conductor from Source of Current to Device and Back to Source

_TABLE_IX = {
    12: abyc_data.TABLE_IX_12V,
    24: abyc_data.TABLE_IX_24V,
    32: abyc_data.TABLE_IX_32V,
}
_TABLE_IX_VOLTAGES=sorted(_TABLE_IX.keys())
_TABLE_IX_KNOWN_LENGTHS_FT=abyc_data.TABLE_IX_12V_KNOWN_LENGTHS_FT


#
# TABLE X – CONDUCTORS SIZED FOR 3 PERCENT DROP IN VOLTAGE
# Length of Conductor from Source of Current to Device and Back to Source

_TABLE_X = {
    12: abyc_data.TABLE_X_12V,
    24: abyc_data.TABLE_X_24V,
    32: abyc_data.TABLE_X_32V,
}
_TABLE_X_VOLTAGES=sorted(_TABLE_X.keys())
_TABLE_X_KNOWN_LENGTHS_FT=abyc_data.TABLE_X_12V_KNOWN_LENGTHS_FT


"""
def GetAWGForLength(voltage_V, full_circuit_length_ft, ):, 
    if full_circuit_length_ft not in TABLE_IX_12V_3PC_KNOWN_LENGTHS:
        raise KeyError(
            f"Unknown length; known lengths: {TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT} FT"
        )
    column_name = "awg_%dft" % full_circuit_length_ft
    current_vs_awg

"""
