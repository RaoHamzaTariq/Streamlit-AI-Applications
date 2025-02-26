class Tools:
    def __init__(self) -> None:
        # Base unit: meter
        self.length_units = {
            "m": 1, "meter": 1, "meters": 1,
            "km": 1000, "kilometer": 1000, "kilometers": 1000,
            "cm": 0.01, "centimeter": 0.01, "centimeters": 0.01,
            "mm": 0.001, "millimeter": 0.001, "millimeters": 0.001,
            "inch": 0.0254, "inches": 0.0254,
            "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
            "yard": 0.9144, "yards": 0.9144,
            "mile": 1609.34, "miles": 1609.34
        }
        # Base unit: kilogram
        self.mass_units = {
            "kg": 1, "kilogram": 1, "kilograms": 1,
            "g": 0.001, "gram": 0.001, "grams": 0.001,
            "mg": 0.000001, "milligram": 0.000001, "milligrams": 0.000001,
            "lb": 0.453592, "pound": 0.453592, "pounds": 0.453592,
            "oz": 0.0283495, "ounce": 0.0283495, "ounces": 0.0283495,
            "ton": 1000, "tonne": 1000, "tonnes": 1000
        }
        # Base unit: liter
        self.volume_units = {
            "l": 1, "liter": 1, "liters": 1,
            "ml": 0.001, "milliliter": 0.001, "milliliters": 0.001,
            "gallon": 3.78541, "gallons": 3.78541,
            "cup": 0.236588, "cups": 0.236588
        }
        self.temperature_units = ["celsius", "fahrenheit", "kelvin"]
        # Base unit: square meter
        self.area_units = {
            "sqm": 1, "square meter": 1, "square meters": 1,
            "sqkm": 1e6, "square kilometer": 1e6, "square kilometers": 1e6,
            "sqcm": 0.0001, "square centimeter": 0.0001, "square centimeters": 0.0001,
            "sqft": 0.092903, "square foot": 0.092903, "square feet": 0.092903,
            "acre": 4046.86, "acres": 4046.86
        }
        # Base unit: second
        self.time_units = {
            "sec": 1, "second": 1, "seconds": 1,
            "min": 60, "minute": 60, "minutes": 60,
            "hr": 3600, "hour": 3600, "hours": 3600,
            "day": 86400, "days": 86400
        }
        
    def convert_length(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the length from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.length_units or to_unit not in self.length_units:
            return f"Invalid unit. Please use one of the following: {', '.join(self.length_units.keys())}"
        
        from_unit_value = self.length_units[from_unit]
        to_unit_value = self.length_units[to_unit]
        converted_value = value * from_unit_value / to_unit_value
        return converted_value
    
    def convert_mass(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the mass from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.mass_units or to_unit not in self.mass_units:
            return f"Invalid unit. Please use one of the following: {', '.join(self.mass_units.keys())}"
        
        from_unit_value = self.mass_units[from_unit]
        to_unit_value = self.mass_units[to_unit]
        converted_value = value * from_unit_value / to_unit_value
        return converted_value

    def convert_volume(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the volume from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.volume_units or to_unit not in self.volume_units:
            return f"Invalid unit. Please use one of the following: {', '.join(self.volume_units.keys())}"
        
        from_unit_value = self.volume_units[from_unit]
        to_unit_value = self.volume_units[to_unit]
        converted_value = value * from_unit_value / to_unit_value
        return converted_value
        
    def convert_temperature(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the temperature from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.temperature_units or to_unit not in self.temperature_units: 
            return f"Invalid unit. Please use one of the following: {', '.join(self.temperature_units)}"
        
        if from_unit == "celsius":
            if to_unit == "fahrenheit":
                converted_value = (value * 9/5) + 32
            elif to_unit == "kelvin":
                converted_value = value + 273.15
            else:
                converted_value = value
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                converted_value = (value - 32) * 5/9
            elif to_unit == "kelvin":
                converted_value = (value - 32) * 5/9 + 273.15
            else:
                converted_value = value
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                converted_value = value - 273.15
            elif to_unit == "fahrenheit":
                converted_value = (value - 273.15) * 9/5 + 32
            else:
                converted_value = value

        return converted_value
    
    def convert_area(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the area from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.area_units or to_unit not in self.area_units:
            return f"Invalid unit. Please use one of the following: {', '.join(self.area_units.keys())}"
        
        from_unit_value = self.area_units[from_unit]
        to_unit_value = self.area_units[to_unit]
        converted_value = value * from_unit_value / to_unit_value
        return converted_value
    
    def convert_time(self, value:float, from_unit:str, to_unit:str):
        """
        This is the function which is used to convert the time from one unit to another.
        Args:
            value: The amount which has to converted
            from_unit: The unit of the value which has to converted
            to_unit: The unit to which the value has to converted
        """
        if from_unit not in self.time_units or to_unit not in self.time_units:
            return f"Invalid unit. Please use one of the following: {', '.join(self.time_units.keys())}"
        
        from_unit_value = self.time_units[from_unit]
        to_unit_value = self.time_units[to_unit]
        converted_value = value * from_unit_value / to_unit_value
        return converted_value
