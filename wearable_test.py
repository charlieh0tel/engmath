#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Tests for wearable.py"""


import numpy as np
import quantities as pq

from . import wearable


def test_touch_surface_passive_flux():
    ambient_temp = 25.0 * pq.C
    flux = wearable.TouchSurfacePassiveFlux(ambient_temp)
    expected_flux = 0.2 * pq.mW / (pq.mm * pq.mm)
    assert np.isclose(flux, expected_flux, atol=0.05 * pq.mW / (pq.mm * pq.mm))
