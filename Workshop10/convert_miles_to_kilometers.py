from kivy.app import App
from kivy.lang import Builder

class ConvertMilesToKilometers (App):
    def build(self):
        self.title = "Covert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_kilometers.kv')
        return self.root

    def handle_calculate (self):
        try:
            miles = float(self.root.ids.input_number.text)
            kms = miles * 1.6
            self.root.ids.output_label.text = str(kms)
        except (ValueError):
            self.root.ids.output_label.text = '0.0'
    def handle_increment (self,num):
        if num > 0:
            try:
                current_num = float(self.root.ids.input_number.text)
            except (ValueError):
                current_num = 0.0
            current_num = current_num + 1
            self.root.ids.input_number.text = str(current_num)
        if num < 0:
            try:
                current_num = float(self.root.ids.input_number.text)
            except (ValueError):
                current_num = 0.0
            current_num = current_num - 1
            self.root.ids.input_number.text = str(current_num)

ConvertMilesToKilometers().run()