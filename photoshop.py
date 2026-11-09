"""
File: photoshop.py
Name: Emma Lee
-------------------------------------
This program replaces the green screen
background of Emma.jpeg with Shrek.jpg
"""


from simpleimage import SimpleImage


THRESHOLD = 1.25
BLACK = 115


def main():
    img = SimpleImage('images/Emma.jpeg')
    bg = SimpleImage('images/Shrek.jpg')
    result = combine(img,bg)
    result.show()


def combine(img, bg):
    """
    :param img: SimpleImage, portrait of me
    :param bg: SimpleImage, collage of Shrek
    """
    bg.make_as_big_as(img)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x,y)
            pixel_bg = bg.get_pixel(x,y)
            avg = (pixel.red + pixel.blue + pixel.green) // 3
            total = pixel.green + pixel.blue + pixel.red
            if (pixel.green > avg * THRESHOLD    # This line is to make sure that the shrek bg only replaces the green screen
                and total > BLACK                # This line is to keep black pixels from being replaced
                and not (img.width/3 < x < img.width*2/3 and img.height/2 < y < img.height)):
                                                 # This line is for the code to not replace the green pixels in my shirt
                pixel.red = pixel_bg.red
                pixel.green = pixel_bg.green
                pixel.blue = pixel_bg.blue
    return img


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
