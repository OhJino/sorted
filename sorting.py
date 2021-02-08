import pygame
import sys
import random
from time import sleep
from pygame.locals import *

screen_width = 1000
screen_height = 1000
purple = (150, 0, 200)
red = (200, 0, 0)
blue = (0, 0, 200)
green = (0, 200, 0)

pygame.init()
surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Merge Sort")
surface.fill(purple)


def bubbleSort(array):
    arr_length = len(array)
    for i in range (arr_length-1):
        for l in range (0, arr_length-i-1):
            if array[l] > array[l+1]:
                array[l], array[l+1] = array[l+1], array[l]

def selectSort(array):
    array_length = len(array)
    for i in range(array_length):
        min_index = i
        for k in range(i+1, array_length):
            if array[min_index] > array[k]:
                min_index = k
        array[i], array[min_index] = array[min_index], array[i]
            




def mergeSort(array):
    if(len(array) > 1):
        length = int(len(array)/2)
        left_array = []
        right_array = []
        for x in range(length):
            left_array.append(array[x])
        mergeSort(left_array)

        for y in range(length, len(array)):
            right_array.append(array[y])
        mergeSort(right_array)

        i = x = y = 0
        while i < len(left_array) and y < len(right_array):
            if (left_array[i] < right_array[y]):
                array[x] = left_array[i]
                i += 1
            else:
                array[x] = right_array[y]
                y += 1
            x += 1    
        
        while i < len(left_array):
            array[x] = left_array[i]
            i += 1
            x += 1
        while y < len(right_array):
            array[x] = right_array[y]
            y += 1
            x += 1

array1 = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit
        if event.type == pygame.MOUSEBUTTONUP:
            posx, posy = pygame.mouse.get_pos()
            print(posx, posy)
        if event.type == KEYDOWN and event.key == K_m:
            for x in range(len(array1)):
                pygame.draw.line(surface, purple, (x, 0), (x, array1[x]))
            mergeSort(array1)
            x = 0
            for x in range(len(array1)):
                pygame.draw.line(surface, green, (x, 0), (x, array1[x]))
        if event.type == KEYDOWN and event.key == K_b:
            for x in range(len(array1)):
                pygame.draw.line(surface, purple, (x, 0), (x, array1[x]))
            bubbleSort(array1)
            x = 0
            for x in range(len(array1)):
                pygame.draw.line(surface, green, (x, 0), (x, array1[x]))
        if event.type == KEYDOWN and event.key == K_s:
            for x in range(len(array1)):
                pygame.draw.line(surface, purple, (x, 0), (x, array1[x]))
            selectSort(array1)
            x = 0
            for x in range(len(array1)):
                pygame.draw.line(surface, green, (x, 0), (x, array1[x]))
        if event.type == KEYDOWN and event.key == K_r:
            x = 0
            for x in range(len(array1)):
                pygame.draw.line(surface, purple, (x, 0), (x, array1[x]))
            x = 0
            array1 = []
            for x in range(screen_width):
                array1.append(random.randint(0, screen_height))
            x = 0
            for x in range(len(array1)):
                pygame.draw.line(surface, green, (x, 0), (x, array1[x]))
    pygame.display.update()