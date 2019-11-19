
'''
*****************************************************************************************
*
*        		===============================================
*           		Rapid Rescuer (RR) Theme (eYRC 2019-20)
*        		===============================================
*
*  This script is to implement Task 1A of Rapid Rescuer (RR) Theme (eYRC 2019-20).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''


# Team ID:128			[ Team-ID ]
# Author List: Harshwardhan Tripathi		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a.py
# Functions:		readImage, solveMaze
# 					[ Comma separated list of functions in this file ]
# Global variables:	CELL_SIZE
# 					[ List of global variables defined in this file ]


# Import necessary modules
# Do not import any other modules
import cv2
import numpy as np
import os


# To enhance the maze image
import image_enhancer


# Maze images in task_1a_images folder have cell size of 20 pixels
CELL_SIZE = 20


class Link():
    value = 0
    parent = 0

    def __init__(self, a, b):
        self.value = a
        self.parent = b


# The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
# and returns a stack consisting of all the neighbours of the cell as output.
# Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
# and vertical traversal is allowed.
# You can copy the code you wrote for section1.py here.
def findNeighbours(img, row, column):
    neighbours = []
    #############  Add your Code here   ###############
    i = 0
    while(True):
        if img[i, i] != 0:
            border = i
            break
        i += 1
    i = border
    cell = 0
    while(True):
        if img[i, i] == 0:
            cell = i
            break
        i += 1
    if img[cell - border * 2, cell] == 0 or img[cell, cell - border * 2] == 0:
        cell = cell + border
    row_new = int((2 * row + 1) * (cell / 2))
    col_new = int((2 * column + 1) * (cell / 2))
    top = int(row_new - (cell / 2) + 1)
    bottom = int(row_new + (cell / 2) - 2)
    left = int(col_new - (cell / 2) + 1)
    right = int(col_new + (cell / 2) - 2)
    if img[top, col_new] != 0:
        neighbours.append([row - 1, column])
    if img[bottom, col_new] != 0:
        neighbours.append([row + 1, column])
    if img[row_new, left] != 0:
        neighbours.append([row, column - 1])
    if img[row_new, right] != 0:
        neighbours.append([row, column + 1])
    ###################################################
    return neighbours


# returns the graph of the maze image
def build_graph(img):
    graph = {}
    #############  Add your Code here   ###############
    i = 0
    while(True):
        if img[i, i] != 0:
            border = i
            break
        i += 1
    i = border
    cell = 0
    while(True):
        if img[i, i] == 0:
            cell = i
            break
        i += 1
    if img[cell - border * 2, cell] == 0 or img[cell, cell - border * 2] == 0:
        cell = cell + border
    r = len(img) // cell
    c = len(img) // cell
    for i in range(r):
        for j in range(c):
            graph[(i, j)] = findNeighbours(img, i, j)
    ###################################################

    return graph


def next_num():  # assigning numbers to the cells
    del x[0]
    return x[0]


def numberMaze(graph, initial, new, l):
    c = 0

    for k in graph[initial]:
        if(tuple(k) == (0, 11)):
            break
        if(tuple(k) == (1, 11)):
            break
        if(tuple(k) == (2, 11)):
            break
        if(tuple(k) == (3, 11)):
            break
        if(tuple(k) == (4, 11)):
            break
        if(tuple(k) == (5, 11)):
            break
        if(tuple(k) == (6, 11)):
            break
        if(tuple(k) == (7, 11)):
            break
        if(tuple(k) == (8, 11)):
            break
        if(tuple(k) == (9, 11)):
            break
        if new[tuple(k)] == -1:
            c += 1
    if c == 0:
        return
    elif c == 1:
        for i in range(len(graph[initial])):
            if new[tuple(graph[initial][i])] == -1:
                new[tuple(graph[initial][i])] = new[initial]
                numberMaze(graph, tuple(graph[initial][i]), new, l)
    else:
        for i in range(len(graph[initial])):
            if new[tuple(graph[initial][i])] == -1:
                n = next_num()
                new[tuple(graph[initial][i])] = n
                l.append(Link(n, new[initial]))
                numberMaze(graph, tuple(graph[initial][i]), new, l)


def shortest_path(l, initial, final, path):  # finds the shortest path

    if final == initial:
        return
    else:
        for i in l:
            if i.value == final:
                parent = i.parent
                break
        path.append(parent)
        shortest_path(l, initial, parent, path)
    parent = 0


def readImage(img_file_path):
    """
    Purpose:
    ---
    the function takes file path of original image as argument and returns it's binary form

    Input Arguments:
    ---
    `img_file_path` :		[ str ]
            file path of image

    Returns:
    ---
    `original_binary_img` :	[ numpy array ]
            binary form of the original image at img_file_path

    Example call:
    ---
    original_binary_img = readImage(img_file_path)

    """

    #############	Add your Code here	###############

    mazeImg = cv2.imread(img_file_path, 0)
    ret, binary_img = cv2.threshold(mazeImg, 10, 255, cv2.THRESH_BINARY)

    ###################################################

    return binary_img


def solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width):
    """
    Purpose:
    ---
    the function takes binary form of original image, start and end point coordinates and solves the maze
    to return the list of coordinates of shortest path from initial_point to final_point

    Input Arguments:
    ---
    `original_binary_img` :	[ numpy array ]
            binary form of the original image at img_file_path
    `initial_point` :		[ tuple ]
            start point coordinates
    `final_point` :			[ tuple ]
            end point coordinates
    `no_cells_height` :		[ int ]
            number of cells in height of maze image
    `no_cells_width` :		[ int ]
            number of cells in width of maze image

    Returns:
    ---
    `shortestPath` :		[ list ]
            list of coordinates of shortest path from initial_point to final_point

    Example call:
    ---
    shortestPath = solveMaze(original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

    """

    global shortestPath
    shortestPath = []

    #############	Add your Code here	###############

    shortest = [initial_point]
    visited = [initial_point]
    count = 1

    global new
    new = {}
    global l
    l = []
    breadth = len(original_binary_img)/20
    length = len(original_binary_img[0])/20
    if length == 10:
        initial_point = (0, 0)
        final_point = (9, 9)
    else:
        initial_point = (0, 0)
        final_point = (19, 19)
    graph = build_graph(original_binary_img)
    for k in graph.keys():
        new[k] = -1
        new[initial_point] = 1
    global x
    x = list(range(1, 1000))
    numberMaze(graph, initial_point, new, l)
    shortestPath.append(new[final_point])
    shortest_path(l, new[initial_point], new[final_point], shortestPath)
    shortestPath.reverse()
    current = initial_point
    while(True):
        if (current == final_point):
            return shortest
        for j in graph[current]:
            if not tuple(j) in visited:
                if new[tuple(j)] == new[current]:
                    current = tuple(j)
                    shortest.append(current)
                    visited.append(current)
                    break
                else:
                    if new[tuple(j)] == shortestPath[count]:
                        count += 1
                        shortest.append(tuple(j))
                        current = tuple(j)
                        visited.append(current)
                        break

    ###################################################

    return shortestPath


#############	You can add other helper functions here		#############


#########################################################################


# NOTE:	YOU ARE NOT ALLOWED TO MAKE ANY CHANGE TO THIS FUNCTION
#
# Function Name:	main
# Inputs:			None
# Outputs: 			None
# Purpose: 			the function first takes 'maze00.jpg' as input and solves the maze by calling readImage
# 					and solveMaze functions, it then asks the user whether to repeat the same on all maze images
# 					present in 'task_1a_images' folder or not


if __name__ == '__main__':

    curr_dir_path = os.getcwd()
    # path to directory of 'task_1a_images'
    img_dir_path = curr_dir_path + '/../task_1a_images/'

    file_num = 0
    img_file_path = img_dir_path + 'maze0' + \
        str(file_num) + '.jpg'		# path to 'maze00.jpg' image file

    print('\n============================================')

    print('\nFor maze0' + str(file_num) + '.jpg')

    try:

        original_binary_img = readImage(img_file_path)
        height, width = original_binary_img.shape

    except AttributeError as attr_error:

        print('\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
        exit()

    # number of cells in height of maze image
    no_cells_height = int(height/CELL_SIZE)
    # number of cells in width of maze image
    no_cells_width = int(width/CELL_SIZE)
    initial_point = (0, 0)									# start point coordinates of maze
    final_point = ((no_cells_height-1), (no_cells_width-1)
                   )					# end point coordinates of maze

    try:

        shortestPath = solveMaze(
            original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

        if len(shortestPath) > 2:

            img = image_enhancer.highlightPath(
                original_binary_img, initial_point, final_point, shortestPath)

        else:

            print(
                '\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
            exit()

    except TypeError as type_err:

        print('\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
        exit()

    print('\nShortest Path = %s \n\nLength of Path = %d' %
          (shortestPath, len(shortestPath)))

    print('\n============================================')

    cv2.imshow('canvas0' + str(file_num), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    choice = input(
        '\nWant to run your script on all maze images ? ==>> "y" or "n": ')

    if choice == 'y':

        file_count = len(os.listdir(img_dir_path))

        for file_num in range(1, file_count):

            img_file_path = img_dir_path + 'maze0' + str(file_num) + '.jpg'

            print('\n============================================')

            print('\nFor maze0' + str(file_num) + '.jpg')

            try:

                original_binary_img = readImage(img_file_path)
                height, width = original_binary_img.shape

            except AttributeError as attr_error:

                print(
                    '\n[ERROR] readImage function is not returning binary form of original image in expected format !\n')
                exit()

            # number of cells in height of maze image
            no_cells_height = int(height/CELL_SIZE)
            # number of cells in width of maze image
            no_cells_width = int(width/CELL_SIZE)
            initial_point = (0, 0)											# start point coordinates of maze
            # end point coordinates of maze
            final_point = ((no_cells_height-1), (no_cells_width-1))

            try:

                shortestPath = solveMaze(
                    original_binary_img, initial_point, final_point, no_cells_height, no_cells_width)

                if len(shortestPath) > 2:

                    img = image_enhancer.highlightPath(
                        original_binary_img, initial_point, final_point, shortestPath)

                else:

                    print(
                        '\n[ERROR] shortestPath returned by solveMaze function is not complete !\n')
                    exit()

            except TypeError as type_err:

                print(
                    '\n[ERROR] solveMaze function is not returning shortest path in maze image in expected format !\n')
                exit()

            print('\nShortest Path = %s \n\nLength of Path = %d' %
                  (shortestPath, len(shortestPath)))

            print('\n============================================')

            cv2.imshow('canvas0' + str(file_num), img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    else:

        print('')
