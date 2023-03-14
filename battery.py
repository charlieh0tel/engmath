#
# Copyright (c) 2023, Christopher Hoover
#
# SPDX-License-Identifier: BSD-3-Clause
#

"""Batteries."""


import dataclasses
import quantities as pq


@dataclasses.dataclass(frozen=True)
class CellChemistry:
    """Cell properties of given chemistry."""

    name: str
    cell_voltage: float = dataclasses.field(repr=False)
    specific_energy: float = dataclasses.field(repr=False)
    energy_density: float = dataclasses.field(repr=False)


@dataclasses.dataclass
class Battery:
    """Battery with single cell."""

    cell_chemistry: CellChemistry
    total_energy: float
    n_cells: int = 1

    @property
    def nominal_voltage(self):
        "Returns the nominal battery voltage."
        if self.n_cells != 1:
            raise ValueError("Use subclass for mutli-cell batteries.")
        return self.cell_chemistry.cell_voltage

    @property
    def mass(self):
        "Returns the mass of the battery."
        return self.total_energy / self.cell_chemistry.specific_energy

    @property
    def volume(self):
        "Returns the volume of the battery without regard to packing or packaging."
        return self.total_energy / self.cell_chemistry.energy_density

    @property
    def capacity(self):
        "Returns the capacity of the battery."
        return (self.total_energy / self.nominal_voltage).rescale(pq.mA * pq.hr)


@dataclasses.dataclass
class SeriesBattery(Battery):
    """Battery with cells in series."""

    @property
    def nominal_voltage(self):
        "Returns the nominal battery voltage."
        return self.n_cells * self.cell_chemistry.cell_voltage


#
# https://en.wikipedia.org/wiki/Comparison_of_commercial_battery_types

LithiumNMC = CellChemistry(
    name="Lithium NMC",
    cell_voltage=3.6 * pq.V,
    specific_energy=0.74 * pq.J / pq.kg,
    energy_density=2.1 * pq.J / pq.L,
)

LithiumFePO4 = CellChemistry(
    name="Lithium FePO4",
    cell_voltage=3.2 * pq.V,
    specific_energy=0.32 * pq.J / pq.kg,  # as high as 0.58
    energy_density=1.20 * pq.J / pq.L,
)

LeadAcid = CellChemistry(
    name="Lead Acid",
    cell_voltage=2.1 * pq.V,
    specific_energy=0.12 * pq.J / pq.kg,
    energy_density=0.23 * pq.J / pq.L,
)
