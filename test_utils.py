#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Test utilities."""

import numpy as np


def isclose(value, expected, atol):
    """Wrapper for np.isclose() that plays well with quantities."""
    value = value.rescale(expected.units)
    atol = atol.rescale(expected.units)
    return np.isclose(value, expected, atol=atol)
