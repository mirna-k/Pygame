from os import walk
import pygame

def import_images_from_folder(path):
	images = []

	for __,__,fileNames in walk(path):
		for image in fileNames:
			full_path = path + '/' + image
			image_surface = pygame.image.load(full_path).convert_alpha()
			images.append(image_surface)

	return images