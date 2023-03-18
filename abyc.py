#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""ABCY E-11."""

from . import abyc_data

#
# Table 6.


def GetAWGVsCurrentForInsulationTempRating(insulation_temp_rating_C, engine_room=False):
    if insulation_temp_rating_C not in TABLE_VI_B_KNOWN_TEMPS_C:
        raise KeyError(
            f"Unknown insulation temperature rating; known ratings: {TABLE_VI_B_KNOWN_TEMPS_C} C"
        )
    column_name = "current_%dC" % mag_temp_C + ("_engroom" if engine_room else "")
    return TABLE_VI_B[column_name]


#
# Table 9.

_TABLE9 = {
    (12, 3): (abyc_data.TABLE_IX_12V_3PC, abyc_data.TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT),
    (24, 3): (abyc_data.TABLE_IX_24V_3PC, abyc_data.TABLE_IX_24V_3PC_KNOWN_LENGTHS_FT),
    (32, 3): (abyc_data.TABLE_IX_32V_3PC, abyc_data.TABLE_IX_32V_3PC_KNOWN_LENGTHS_FT),
    (12, 10): (
        abyc_data.TABLE_IX_12V_10PC,
        abyc_data.TABLE_IX_12V_10PC_KNOWN_LENGTHS_FT,
    ),
    (24, 10): (
        abyc_data.TABLE_IX_24V_10PC,
        abyc_data.TABLE_IX_24V_10PC_KNOWN_LENGTHS_FT,
    ),
    (32, 10): (
        abyc_data.TABLE_IX_32V_10PC,
        abyc_data.TABLE_IX_32V_10PC_KNOWN_LENGTHS_FT,
    ),
}


def GetAWGForLengthAnd12VCurrent(full_circuit_length_ft, current):
    if full_circuit_length_ft not in TABLE_IX_12V_3PC_KNOWN_LENGTHS:
        raise KeyError(
            f"Unknown length; known lengths: {TABLE_IX_12V_3PC_KNOWN_LENGTHS_FT} FT"
        )
    column_name = "awg_%dft" % full_circuit_length_ft
    current_vs_awg
