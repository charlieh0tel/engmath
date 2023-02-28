#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Wearables."""

import quantities as pq

from . import heat_transfer


TOUCH_CONTINUOUS_TEMP_LIMIT = 43. * pq.C


def TouchSurfacePassiveFlux(ambient_temp):
    """The heat flux achievable via passive cooling for the given ambient
    temperature that maintains the surface under continuous touch
    temperature limits.

    """
    dT = TOUCH_CONTINUOUS_TEMP_LIMIT - ambient_temp
    if dT < 0.:
        raise ValueError("Ambient temperature is above the touch limit.")
    # Q = h.A.dT => Q/A = h.dT
    return (heat_transfer.H_PASSIVE * dT).rescale(pq.mW / (pq.mm * pq.mm))
