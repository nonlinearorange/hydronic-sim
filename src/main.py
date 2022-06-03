from matplotlib import pyplot as plt

from solar.geometry.solar_geometry_predictor import SolarGeometryPredictor
from thermal.material_kind import MaterialKind
from thermal.surface import Surface


def calculate_rate_heat_loss(temp_1, temp_2, thermal_resistance):
    return (temp_1 - temp_2) / thermal_resistance


def execute_thermal_sample():
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


def plot_solar_declination():
    days = [day for day in range(1, 365)]
    solar_declination = [SolarGeometryPredictor.calculate_solar_declination(day) for day in days]
    plt.plot(days, solar_declination)
    plt.title("Solar Declination")
    plt.ylabel("Declination Angle (degrees)")
    plt.xlabel("Day Number")
    plt.show()


def plot_sun_path_diagram():
    pass


def execute_specific_example():
    predictor = SolarGeometryPredictor(40.0, 167, 14)
    predictor.predict()

    print(f'Solar Hour Angle: {predictor.hour_angle}°')
    print(f'Solar Declination: {predictor.solar_declination}°')
    print(f'Solar Altitude: {predictor.solar_altitude}°')
    print(f'Solar Azimuth: {predictor.solar_azimuth}°')


def execute_solar_geometry_sample():
    plot_solar_declination()
    execute_specific_example()


def main():
    # execute_thermal_sample()
    # execute_solar_geometry_sample()
    plot_sun_path_diagram()


if __name__ == "__main__":
    main()
