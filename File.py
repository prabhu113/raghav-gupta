import pygame

class File():
    
    def LoadFile(self):
        file = open("objects.txt")
        data = file.readlines()
        objects = []

        for line in data:
            objects.append(line.strip().split(","))

        return objects
