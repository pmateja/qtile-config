import os


class Brightness:
    brightness_dir = "/sys/class/backlight/intel_backlight/"
    br_file = os.path.join(brightness_dir, "brightness")
    max_file = os.path.join(brightness_dir, "max_brightness")
    current_brightness = ""
    max_brightness = ""


    def __init__(self):
        self.max = self.get_max_brightness()

    def get_brightness(self):
        with open(self.br_file) as f:
            return f.read()

    def get_max_brightness(self):
        with open(self.max_file) as f:
            return f.read()

    def set_brightness(self, level):
        if int(self.max) >= level:
            with open(self.br_file, "w") as f:
                f.write(str(level))

    def inc(self, level=10):
        mx = int(self.get_max_brightness())
        cr = int(self.get_brightness())
        if mx >= cr+level and cr+level > 0:
            with open(self.br_file, "w") as f:
                f.write(str(cr + level))

    def dec(self, level=10):
        self.inc(level*-1)
