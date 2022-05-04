"""
File: blur.py
Name: stanCode example answer
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original picture.
    :return new_img: SimpleImage, blurred image.
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):

            # 建立計算平均的變數(variables)
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            count = 0

            # 選取在img(x+i, y+j)的pixels(最多九顆pixels)，並計算RGB平均
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = x + i
                    neighbor_y = y + j

                    # 不要選到超出圖片範圍的座標
                    if 0 <= neighbor_x < img.width and 0 <= neighbor_y < img.height:
                        neighbor_pixel = img.get_pixel(neighbor_x, neighbor_y)
                        sum_red += neighbor_pixel.red
                        sum_green += neighbor_pixel.green
                        sum_blue += neighbor_pixel.blue
                        count += 1

            new_img_pixel = new_img.get_pixel(x, y)     # 選取在new_img(x, y)的pixel,
            new_img_pixel.red = sum_red // count        # 並賦予鄰近pixel的平均RGB值
            new_img_pixel.green = sum_green // count
            new_img_pixel.blue = sum_blue // count

    return new_img


def main():
    """
    This program will produce the blurred image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
