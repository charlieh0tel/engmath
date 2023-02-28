#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

import quantities as pq

from . import heat_transfer


TOUCH_CONTINUOUS_TEMP_LIMIT = 43. * pq.C


def TouchSurfaceFlux(ambient_temp):
    dT = TOUCH_CONTINUOUS_TEMP_LIMIT - ambient_temp
    # Q = h.A.dT => Q/A = h.dT
    return (heat_transfer.H_PASSIVE * dT).rescale(pq.mW / (pq.mm * pq.mm))
