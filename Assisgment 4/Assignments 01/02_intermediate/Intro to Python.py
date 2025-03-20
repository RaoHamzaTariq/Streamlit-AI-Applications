def calculate_planetary_weight():
    """Calculates a person's weight on another planet."""

    earth_weight = float(input("Enter a weight on Earth: "))

    planet_weights = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.360,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.140,
    }

    planet = input("Enter a planet: ")

    if planet in planet_weights:
        planet_weight_factor = planet_weights[planet]
        planetary_weight = earth_weight * planet_weight_factor
        rounded_weight = round(planetary_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Invalid planet entered.")

calculate_planetary_weight()