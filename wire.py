#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire specified by AWG."""

import math
import io
import pandas as pd
import quantities as pq

from . import resistivity


def AWGSpecificationToNumber(awg):
    if awg == "0000" or awg == "4/0":
        return -3
    if awg == "000" or awg == "3/0":
        return -2
    if awg == "00" or awg == "2/0":
        return -1
    if awg == "0" or awg == "1/0":
        return 0
    return int(awg)


def CanonicalizeAWG(awg):
    awg = AWGSpecificationToNumber(awg)
    if awg < 0:
        return "%d/0" % (-awg + 1)
    else:
        return awg


def SolidWireDiameter(awg):
    """The diameter of a solid wire of the specified AWG."""
    awg = AWGSpecificationToNumber(awg)
    # https://en.wikipedia.org/wiki/American_wire_gauge
    return 0.005 * 92.0 ** ((36.0 - awg) / 39.0) * pq.inch


def SolidWireCrossSectionalArea(awg):
    """The cross-sectional area of a solid wire of the specified AWG."""
    radius = SolidWireDiameter(awg) / 2.0
    return math.pi * radius ** 2


def SolidWireResistancePerUnitLength(awg, p=resistivity.p_Cu):
    """Returns the resistance per unit length for the specified AWG and resistivity."""
    area = SolidWireCrossSectionalArea(awg)
    return (p / area).rescale(pq.ohm / pq.m)


# ABYC E-11 2008
# TABLE VI – B - AC & DC CIRCUITS – ALLOWABLE AMPERAGE OF CONDUCTORS WHEN UP TO
# THREE CURRENT CARRYING CONDUCTORS ARE BUNDLED, SHEATHED OR IN CONDUIT
_ABYC_TABLE_VI_B_CSV = """
awg,current_60C,current_60C_eng,current_75C,current_75C_eng,current_80C,current_80C_eng,current_90C,current_90C_eng,current_105C,current_105C_eng,current_125C,current_125C_eng,current_200C,current_200C_eng
18,7.0,0,7.0,5.3,10.5,8.2,14.0,11.5,14.0,11.9,17.5,15.6,17.5
16,10.5,0,10.5,7.9,14.0,10.9,17.5,14.4,17.5,14.9,21.0,18.7,24.5
14,14.0,0,14.0,10.5,17.5,13.7,21.0,17.2,24.5,20.8,28.0,24.9,31.5
12,17.5,0,17.5,13.1,24.5,19.1,28.0,23.0,31.5,26.8,35.0,31.2,38.5
10,28.0,0,28.0,21.0,35.0,27.3,38.5,31.6,42.0,35.7,49.0,43.6,49.0
8,38.5,0,45.5,34.1,49.0,38.2,49.0,40.2,56.0,47.6,63.0,56.1,70.0
6,56.0,0,66.5,49.9,70.0,54.6,70.0,57.4,84.0,71.4,87.5,77.9,94.5
4,73.5,0,87.5,65.6,91.0,71.0,94.5,77.5,112.0,95.2,119.0,105.9,126.0
3,84.0,0,101.5,76.1,105.0,81.9,108.5,89.0,126.0,107.1,136.5,121.5,147.0
2,98.0,0,119.0,89.3,122.5,95.6,126.0,103.3,147.0,125.0,157.5,140.2,168.0
1,115.5,0,136.5,102.4,147.0,114.7,147.0,120.5,171.5,145.8,185.5,165.1,196.0
0,136.5,0,161.0,120.8,171.5,133.8,171.5,140.6,199.5,169.6,213.5,190.0,227.5
2/0,157.5,0,185.5,139.1,199.5,155.6,199.5,163.6,231.0,196.4,248.5,221.2,259.0
3/0,182.0,0,217.0,162.8,231.0,180.2,231.0,189.4,269.5,229.1,287.0,255.4,301.0
4/0,210.0,0,252.0,189.0,269.5,210.2,269.5,221.0,311.5,264.8,332.5,295.9,357.0
"""

_ABYC_TABLE_VI_B = pd.read_csv(io.StringIO(_ABYC_TABLE_VI_B_CSV)).set_index("awg")
_ABYC_TABLE_VI_B_KNOWN_TEMPS_C = [60, 75, 80, 90, 105, 125, 200]


def AmericanBoatAndYachtCouncilWireGaugeUpToThreeConductorBundle(
    current, insulation_temp_rating_C, engine_room=False
):
    mag_temp_C = insulation_temp_rating_C.rescale("C").magnitude
    mag_current_A = current.rescale("A").magnitude
    if mag_temp_C not in _ABYC_TABLE_VI_B_KNOWN_TEMPS_C:
        raise KeyError(
            f"Unknown insulation temperature rating; known ratings: {_ABYC_TABLE_VI_B_KNOWN_TEMPS_C} C"
        )
    column_name = "current_%dC" % mag_temp_C + ("_eng" if engine_room else "")
    awg_vs_current = _ABYC_TABLE_VI_B[column_name]
    acceptable_awgs = awg_vs_current[awg_vs_current >= mag_current_A]
    if acceptable_awgs.empty:
        raise ValueError("No acceptable wire guage for full circuit current.")
    return CanonicalizeAWG(acceptable_awgs.keys()[0])
