from thermal.layer import Layer
from thermal.material_factory import MaterialFactory


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
