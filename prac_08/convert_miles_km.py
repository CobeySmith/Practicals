from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.output_text = self.root.ids.output_text.text

    def calculate_conversion(self):
        """Convert miles to km."""
        value = self.get_valid_float()
        result = value * MILES_TO_KM
        self.root.ids.output_text.text = str(result)

    def get_valid_float(self):
        """Get a valid float input."""
        try:
            value = float(self.root.ids.input_text.text)
            return value
        except ValueError:
            return 0

    def go_up(self):
        """Increase value by 1."""
        value = self.get_valid_float() + 1
        self.root.ids.input_text.text = str(value)
        self.calculate_conversion()

    def go_down(self):
        """Decrease value by 1."""
        value = self.get_valid_float() - 1
        self.root.ids.input_text.text = str(value)
        self.calculate_conversion()


MilesConverterApp().run()
