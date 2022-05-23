from thermal.material import Material


class Layer:
    def __init__(self, material: Material, thickness):
        self.material = material
        self.thickness = thickness
