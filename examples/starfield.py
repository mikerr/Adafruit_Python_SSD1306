import time
from random import randrange

from PIL import Image
from PIL import ImageDraw

# import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

center_x = width  / 2
center_y = height / 2

max_depth = 500
num_stars = 50
speed = 10

# Generate star positions

stars = []
for i in range(num_stars):
    star = [randrange(-25,25), randrange(-25,25), randrange(1, max_depth)]
    stars.append(star)

while 1:

 # Draw a black filled box to clear the image.
 draw.rectangle((0,0,width,height), outline=0, fill=0)
 
 # Move stars

 for star in stars:
    star[2] -= speed

    # If star is behind us, reposition far away in front at random position
    if star[2] <= 0:
                star[0] = randrange(-25,25)
                star[1] = randrange(-25,25)
                star[2] = max_depth

    # Convert the 3D coordinates to 2D 
    
    k = 128.0 / star[2]
    x = int(star[0] * k + center_x)
    y = int(star[1] * k + center_y)

    # Draw the star (if on screen)

    if 0 <= x < width and 0 <= y < height:
                draw.point((x,y),fill=1)

 disp.image(image)
 disp.display()
