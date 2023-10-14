import xml.etree.ElementTree as ET


class TemperatureConverter():

    def __init__(self) -> None:
        pass

    @staticmethod
    def convert_celsius_to_fahrenheit(temp_celcius):
        return round(9/5 * temp_celcius + 32)
    


class ForecastXmlParse():

    def __init__(self, file) -> None:
        self.tree = ET.parse(file)
        self.root = self.tree.getroot()

    def parseAndPrint(self):

        for item in self.root :
            day = item.find("day").text
            temp_celcius = int(item.find("temperature_in_celsius").text)
            temp_fahrenheit = TemperatureConverter.convert_celsius_to_fahrenheit(temp_celcius)
            
            print(f"{day} : {temp_celcius}°C = {temp_fahrenheit}°F")
            
            


            
           

# appel
forecastToXml = ForecastXmlParse('forecast.xml')
forecastToXml.parseAndPrint()



# Monday: 28 Celsius, 82.4 Fahrenheit