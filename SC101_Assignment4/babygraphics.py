"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_width = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)

    return GRAPH_MARGIN_SIZE + line_width * year_index


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        line_x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(line_x, 0, line_x, CANVAS_HEIGHT)
        canvas.create_text(line_x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plot
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # ----- Ver1 ----- #
    # color_num = 0
    # for names in lookup_names:
    #     i = 0
    #     for year in YEARS:
    #         # 畫到結束前一年
    #         if i < len(YEARS) - 1:
    #             # 判斷第一點是否有值，如果沒值
    #             if str(year) not in name_data[names]:
    #                 line_x_beg = get_x_coordinate(CANVAS_WIDTH, i)
    #                 line_x_end = get_x_coordinate(CANVAS_WIDTH, i + 1)
    #                 # 判斷一點沒值, 第二點有值
    #                 if str(YEARS[i + 1]) in name_data[names]:
    #                     rank = get_rank(name_data, names, YEARS, i + 1)
    #                     canvas.create_line(line_x_beg, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, line_x_end,
    #                                        GRAPH_MARGIN_SIZE + rank[1], width=LINE_WIDTH, fill=COLORS[color_num])
    #                 # 判斷一點沒值, 第二點無值
    #                 else:
    #                     canvas.create_line(line_x_beg, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, line_x_end,
    #                                        CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=COLORS[color_num])
    #                 draw_text(canvas, line_x_beg, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, names, 1001, COLORS[color_num])
    #                 i += 1
    #             # 判斷第一點是否有值，如果有值
    #             else:
    #                 rank1 = get_rank(name_data, names, YEARS, i)
    #                 line_x_beg = get_x_coordinate(CANVAS_WIDTH, i)
    #                 line_x_end = get_x_coordinate(CANVAS_WIDTH, i + 1)
    #                 # 判斷一點有值, 第二點有值
    #                 if str(YEARS[i + 1]) in name_data[names]:
    #                     rank2 = get_rank(name_data, names, YEARS, i + 1)
    #                     canvas.create_line(line_x_beg, GRAPH_MARGIN_SIZE + rank1[1], line_x_end,
    #                                        GRAPH_MARGIN_SIZE + rank2[1], width=LINE_WIDTH, fill=COLORS[color_num])
    #                 # 判斷一點有值, 第二點無值
    #                 else:
    #                     canvas.create_line(line_x_beg, GRAPH_MARGIN_SIZE + rank1[1], line_x_end,
    #                                        CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill=COLORS[color_num])
    #                 draw_text(canvas, line_x_beg, GRAPH_MARGIN_SIZE + rank1[1], names, rank1[0], COLORS[color_num])
    #                 i += 1
    #         # 畫最後一個點的名稱
    #         else:
    #             line_x_end_graph = get_x_coordinate(CANVAS_WIDTH, i)
    #             rank_end_graph = get_rank(name_data, names, YEARS, i)
    #             draw_text(canvas, line_x_end_graph, GRAPH_MARGIN_SIZE + rank_end_graph[1], names, rank_end_graph[0],
    #                       COLORS[color_num])
    #
    #     if color_num <= len(COLORS):
    #         color_num += 1
    #     else:
    #         color_num = 0

    # ----- Ver2 ----- #
    color_num = 0
    for names in lookup_names:
        for i in range(len(YEARS)):
            # 畫到結束前一年
            if i < len(YEARS) - 1:
                # 判斷第一點是否有值，如果沒值
                line_x_beg = get_x_coordinate(CANVAS_WIDTH, i)
                line_x_end = get_x_coordinate(CANVAS_WIDTH, i + 1)
                rank1 = get_rank(name_data, names, YEARS, i)
                rank2 = get_rank(name_data, names, YEARS, i + 1)
                canvas.create_line(line_x_beg, GRAPH_MARGIN_SIZE + rank1[1], line_x_end,
                                   GRAPH_MARGIN_SIZE + rank2[1], width=LINE_WIDTH, fill=COLORS[color_num])
                draw_text(canvas, line_x_beg, GRAPH_MARGIN_SIZE + rank1[1], names, rank1[0],
                          COLORS[color_num])
            # 畫最後一個點的名稱
            else:
                line_x_end_graph = get_x_coordinate(CANVAS_WIDTH, i)
                rank_end_graph = get_rank(name_data, names, YEARS, i)
                draw_text(canvas, line_x_end_graph, GRAPH_MARGIN_SIZE + rank_end_graph[1], names, rank_end_graph[0],
                          COLORS[color_num])

        if color_num <= len(COLORS):
            color_num += 1
        else:
            color_num = 0


# 獲得rank值，與rank高度
def get_rank(name_data, names, year_lst, i):
    year = str(year_lst[i])
    if year in name_data[names]:
        # 設定Rank1 條件
        rank = int(name_data[names][year])
        # 標準化Rank1長度, 拉伸到1-1000區間
        rank_h = int(rank / 1000 * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2))
        if rank > 1000:
            rank_h = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2
        rank = [rank, rank_h]
    else:
        rank = [1001, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2]
    return rank


# 繪製名稱
def draw_text(canvas, x, y, name, rank, color):
    if rank > 1000:
        canvas.create_text(x + TEXT_DX, y, text=f'{name} *', anchor=tkinter.SW, fill=color)
    else:
        canvas.create_text(x + TEXT_DX, y, text=f'{name} {str(rank)}', anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
