"""Tests for wearable.py"""

import numpy
import quantities as pq

from . import wearable


def test_touch_surface_flux():
    ambient_temp = 25. * pq.C
    flux = wearable.TouchSurfaceFlux(ambient_temp)
    expected_flux = 0.2 * pq.mW / (pq.mm * pq.mm)
    print(f"{flux} {expected_flux}")
    assert numpy.isclose(flux, expected_flux,
                         atol=0.05 * pq.mW / (pq.mm * pq.mm))

