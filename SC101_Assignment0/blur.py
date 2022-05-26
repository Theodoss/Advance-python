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

    # Image2_array = np.array(img) #get_pixel函數無法相加，將圖片轉矩陣讀取並相加

    #兩個For遍歷圖片坐標
    for x in range(width):
        for y in range(height):
            print(f'處理至X坐標:{x},y坐標:{y}')
            count_num = 0 #初始周邊元素數量計數
            r_img = 0 #初始RGB_R Value計數
            g_img = 0 #初始RGB_G Value計數
            b_img =0  #初始RGB_B Value計數
            #兩個For遍歷周邊坐標
            for i in (-1,0,1):
                for j in (-1,0,1):
                    if x+i >=0 and x+i <width and y+j >=0 and y+j <height: #避免讀取超出圖片範圍元素
                        count_num += 1 #計算元素總數
                        # 放入RGB
                        img_RGB = img.get_pixel(x+i,y+j)
                        # 分通道取數值
                        r_img += img_RGB.red
                        g_img += img_RGB.green
                        b_img += img_RGB.blue
                        # arr =Image2_array[x+i, y+j]
                        # r_img += arr[0]
                        # g_img += arr[1]
                        # b_img += arr[2]

            r_img=r_img//count_num#除以元素個數
            g_img=g_img//count_num
            b_img=b_img//count_num
            img = img.get_pixel(x, y)
            img.red = r_img #通道整合進圖像
            img.green = g_img
            img.blue = b_img

            # Image2_array[x,y] = [r_img, g_img, b_img]

    return img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    # old_img = Image.open('../images/smiley-face.png') #此數據無法傳入Numpy因此改用Numpy直接讀圖

    old_img.show()
    blurred_img = old_img
    for i in range(4): #額外執行4次
        blurred_img = blur(blurred_img)
    # blurred_img=Image.fromarray(np.uint8(blurred_img))
    # blurred_img= SimpleImage(blurred_img)
    # blurred_img.show()
    new_img = SimpleImage.blank(blurred_img.width,blurred_img.height)
    for x in range(new_img.width):
        for y in range(new_img.height):
            #放入RGB
            blur_RGB = blurred_img.get_pixel(x,y)
            #填入空白
            new_img_RGB = new_img.get_pixel(x,y)
            new_img_RGB.red = blur_RGB.red
            new_img_RGB.green = blur_RGB.green
            new_img_RGB.blue = blur_RGB.blue
    new_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
