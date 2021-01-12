import cv2
import numpy as np
from sudoku import Sudoku

path = "test_images/1.png"
gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# edges = cv2.Canny(gray,150, 200, (3,3))
# lines = cv2.HoughLines(edges, 3, np.pi/4 , 200, None, 0, 0)
cells = []
cols, rows = gray.shape

for i in range(1,10):
    l = []
    row = gray[int((cols/9)*(i-1)) : int((cols/9)*i), 0 : rows]
    for j in range(1,10):
        cell = row[:,int((rows/9)*(j-1)) : int((rows/9)*j)]
        l.append(cell)
    cells.append(l)
cells = np.array(cells)

table = np.zeros((9,9))
thresh = 0.75
for row in range(0,9):
    for col in range(0,9):
        for i in range(1,10):
            cell = cells[row][col]
            template = cv2.imread("templates/" + str(i) + ".png", cv2.IMREAD_GRAYSCALE)
            loc = cv2.matchTemplate(cell, template, cv2.TM_CCOEFF_NORMED )
            if len(np.where(loc > thresh)[0])!= 0:
                    table[row][col] = i
                    biggest_prob = np.max(loc[np.where(loc > thresh)])
table = table.tolist()
table = [[int(t) for t in row] for row in table]
puzzle = Sudoku(3, 3, board=table)
print(puzzle)
puzzle.solve().show_full()

# cv2.imshow('image', template[:])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
