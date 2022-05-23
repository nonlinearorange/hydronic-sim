from thermal.material import Material
from thermal.material_kind import MaterialKind


class MaterialFactory:
    @staticmethod
    def create(kind):
        if kind == MaterialKind.COPPER:
            return Material(kind, 399.0)
        elif kind == MaterialKind.GLASS:
            return Material(kind, 0.81)
        elif kind == MaterialKind.ZIRCONIUM_BRICK:
            return Material(kind, 2.5)
        elif kind == MaterialKind.STEEL:
            return Material(kind, 40.0)
        elif kind == MaterialKind.AIR:
            return Material(kind, 0.026)
        else:
            raise ValueError(kind)
