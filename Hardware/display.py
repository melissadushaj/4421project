from Config.settings import FACE_COLS, FACE_ROWS, BRIGHTNESS

try:
    # When you download Waveshare's demo and copy the "lib" folder into your project,
    # this import should work. Their Python examples use "from lib import LCD_2inch".
    # :contentReference[oaicite:3]{index=3}
    from lib import LCD_2inch
except ImportError:
    LCD_2inch = None
    print("[Display] WARNING: Waveshare LCD_2inch driver not found. Running in console-only mode.")

from PIL import Image, ImageDraw

class DisplayManager:
    def __init__(self):
        self.lcd = None

        if LCD_2inch is not None:
            try:
                self.lcd = LCD_2inch.LCD_2inch()
                self.lcd.Init()
                self.lcd.clear()

                # Most Waveshare drivers expose width/height attributes
                self.width = self.lcd.width
                self.height = self.lcd.height

                # Set backlight brightness if function exists :contentReference[oaicite:4]{index=4}
                if hasattr(self.lcd, "bl_DutyCycle"):
                    self.lcd.bl_DutyCycle(BRIGHTNESS)
                print(f"[Display] LCD initialized ({self.width}x{self.height}), brightness={BRIGHTNESS}%")
            except Exception as e:
                print(f"[Display] ERROR initializing LCD_2inch: {e}")
                self.lcd = None

        # Fallback values when running on your Mac without the screen
        if not getattr(self, "width", None):
            self.width = 240
            self.height = 320
            print("[Display] Using virtual resolution 240x320 (no hardware attached)")

        # precompute scale factor from logical face grid to physical LCD
        self.block_w = self.width // FACE_COLS
        self.block_h = self.height // FACE_ROWS

    def _face_to_image(self, face_grid):
        """
        Convert a logical face grid (FACE_ROWS x FACE_COLS, 0/1 values)
        into a full 240x320 RGB image.
        """
        img = Image.new("RGB", (self.width, self.height), "black")
        draw = ImageDraw.Draw(img)

        on_color = (255, 255, 255)  # white
        off_color = (0, 0, 0)       # black

        for row in range(FACE_ROWS):
            for col in range(FACE_COLS):
                value = face_grid[row][col]
                color = on_color if value else off_color

                x0 = col * self.block_w
                y0 = row * self.block_h
                x1 = x0 + self.block_w
                y1 = y0 + self.block_h

                draw.rectangle([x0, y0, x1, y1], fill=color)

        return img

    def show_face(self, face_grid):
        """
        Public API: take a logical face pattern and show it on the LCD.
        """
        img = self._face_to_image(face_grid)

        if self.lcd is not None:
            self.lcd.ShowImage(img)   # standard Waveshare API :contentReference[oaicite:5]{index=5}
        else:
            # Debug mode on your laptop: print ASCII face instead of erroring
            print("[Display] (debug) Showing face grid:")
            for row in face_grid:
                print("".join("#" if c else "." for c in row))

    def clear(self):
        if self.lcd is not None:
            self.lcd.clear()
        else:
            print("[Display] (debug) Clear screen")
