#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wire."""

import math
import quantities as pq

from . import resistivity


def SolidWireDiameter(awg):
    """The diameter of a solid wire of the specified AWG."""
    if awg == "0000":
        awg = -3
    elif awg == "000":
        awg = -2
    elif awg == "00":
        awg = -1
    elif isinstance(awg, int):
        awg = int(awg)
    else:
        raise ValueError("Expecting awg [-3,40] or '00' or '000' or '0000'")
    if awg < -3 or awg > 40:
        raise ValueError("Expecting awg [-3,40] or '00' or '000' or '0000'")
    #
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
