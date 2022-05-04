"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
from PIL import Image as Image



def blur(img):
    """
    :param img:
    :return:img:
    """
    width = 300
    height = 300
    new_img = SimpleImage.blank(img.width, img.height)
    # 兩個For遍歷圖片坐標
    for x in range(img.width):
        for y in range(img.height):
            print(f'處理至X坐標:{x},y坐標:{y}')
            count_num = 0  # 初始周邊元素數量計數
            r_img = 0  # 初始RGB_R Value計數
            g_img = 0  # 初始RGB_G Value計數
            b_img = 0  # 初始RGB_B Value計數
            # 兩個For遍歷周邊坐標
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if x + i >= 0 and x + i < width and y + j >= 0 and y + j < height:  # 避免讀取超出圖片範圍元素
                        count_num += 1  # 計算元素總數
                        # 放入RGB
                        img_RGB = img.get_pixel(x + i, y + j)
                        # 分通道取數值
                        r_img += img_RGB.red
                        g_img += img_RGB.green
                        b_img += img_RGB.blue

            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = r_img // count_num  # 除以元素個數
            new_img_pixel.green = g_img // count_num
            new_img_pixel.blue = b_img // count_num

    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(4):  # 額外執行4次
        blurred_img = blur(blurred_img)

    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
