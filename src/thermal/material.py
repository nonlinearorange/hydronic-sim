from dataclasses import dataclass

from thermal.material_kind import MaterialKind


@dataclass
class Material:
    kind: MaterialKind
    thermal_conductivity: float
