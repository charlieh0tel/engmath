#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire specified by AWG."""

import math
import quantities as pq

from . import abyc
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
    try:
        return int(awg)
    except ValueError:
        raise ValueError(f"{awg} is not a valid AWG specification.")


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


def ABYCWireGaugeUpToThreeConductorBundle(
    current, insulation_temp_rating_C, engine_room=False
):
    awg_vs_current = abyc.GetAWGVsCurrentForInsulationTempRating(
        insulation_temp_rating_C.rescale("C").magnitude, engine_room=engine_room
    )
    mag_current_A = current.rescale("A").magnitude
    acceptable_awgs = awg_vs_current[awg_vs_current >= mag_current_A]
    if acceptable_awgs.empty:
        raise ValueError("No acceptable wire guage for full circuit current.")
    return CanonicalizeAWG(acceptable_awgs.keys()[0])
