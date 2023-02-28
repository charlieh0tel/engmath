#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

import dataclasses
import quantities as pq

@dataclasses.dataclass
class Battery:
    """Battery properties."""
    name: str
    cell_voltage: float
    specific_energy: float
    energy_density: float

    def mass(self, energy):
        return energy / self.specific_energy

    def volume(self, energy):
        return energy / self.energy_density

    def capacity(self, energy):
        return (energy / self.cell_voltage).rescale(pq.mA * pq.hr)


LithiumNMC = Battery(
     name="Lithium NMC",
     cell_voltage=3.6 * pq.V,                # [3.60 - 3.85] V
     specific_energy=0.600e6 * pq.J / pq.kg, # 0.360–0.954 MJ/kg
     energy_density=1.70e6 * pq.J / pq.L     # 0.90–2.49 MJ/L
     )
