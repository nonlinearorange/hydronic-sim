from dataclasses import dataclass


class MaterialKind:
    COPPER = 1
    ALUMINUM = 2
    CARBON_STEEL = 3
    GLASS = 4,
    PLASTICS = 5,
    WATER = 6,
    AIR = 7,
    WOOD = 8,
    CONCRETE = 9,
    ZIRCONIUM_BRICK = 10,
    STEEL = 40


@dataclass
class Material:
    kind: MaterialKind
    thermal_conductivity: float


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


class Layer:
    def __init__(self, material: Material, thickness):
        self.material = material
        self.thickness = thickness


class Surface:
    def __init__(self):
        self.layers: [Layer] = []
        self.width = 0.0
        self.height = 0.0

    def update_area(self, width, height):
        self.width = width
        self.height = height
        return self.calculate_area()

    def calculate_area(self):
        return self.width * self.height

    def add_layer(self, material_kind, thickness: float):
        material = MaterialFactory.create(material_kind)
        layer = Layer(material, thickness)
        self.layers.append(layer)

    def calculate_thermal_resistance_to_conduction(self):
        area = self.calculate_area()
        total = 0.0
        for layer in self.layers:
            total += layer.thickness / (layer.material.thermal_conductivity * area)

        return total

    # For now, it assumes a series physical model.
    def calculate_total_thermal_conductivity(self):
        return sum(layer.material.thermal_conductivity for layer in self.layers)


def calculate_rate_heat_loss(temp_1, temp_2, thermal_resistance):
    return (temp_1 - temp_2) / thermal_resistance


def main():
    surface = Surface()
    surface.add_layer(MaterialKind.GLASS, 0.004)
    surface.add_layer(MaterialKind.AIR, 0.01)
    surface.add_layer(MaterialKind.GLASS, 0.004)
    surface.update_area(0.8, 1.5)

    conductivity = surface.calculate_total_thermal_conductivity()
    print(f"Wall Total Thermal Conductivity: {conductivity}")

    resistance_to_conduction = surface.calculate_thermal_resistance_to_conduction()
    print(f"Thermal Resistance to Conduction: {resistance_to_conduction}")

    rate = calculate_rate_heat_loss(24.5, 24.0, resistance_to_conduction)
    print(f"Rate of Heat Loss: {rate}")


if __name__ == "__main__":
    main()
