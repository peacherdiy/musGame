import os
import pygame
import pygame.image
from pygame import display
import sys

def isImageFile(filePath):
    lowerFilePath = filePath.lower()
    if (lowerFilePath.endswith('.jpg') or
        lowerFilePath.endswith('.png') or
        lowerFilePath.endswith('.bmp') or
        lowerFilePath.endswith('.gif') or
        lowerFilePath.endswith('.jpeg')):
        return True

    return False

class ImageFolder:
    def CurrentImage(self):
        if self.index == -1 or len(self.images) == 0:
            return ""
        return self.images[self.index]
    def NextImage(self):
        if 0 == len(self.images) or self.index == len(self.images) - 1:
            return ""
        
        self.index = self.index + 1
        return self.images[self.index]
        
    def PrevImage(self):
        if 0 == len(self.images) or self.index == -1:
            return ""
        
        self.index = self.index - 1
        if self.index >= 0:
            return self.images[self.index]
        pass
    def __init__(self, folderPath):
        self.images = []
        # TODO: add recursive search
        for file in os.listdir(folderPath):
            if (os.path.isfile(os.path.join(folderPath, file))):
                if (isImageFile(file)):
                    self.images.append(os.path.join(folderPath, file))
        self.index = -1
        pass

def ShowImageWithFitScale(screen, imageFilePath, angle=0):
    if (imageFilePath == None or imageFilePath == ""):
        return
    
    image = pygame.image.load(imageFilePath)
    scrWidth, scrHeight = screen.get_size()
    image = pygame.transform.rotate(image, angle)
        
    imgWidth, imgHeight = image.get_size()
    ratio = 1.0 * imgWidth / imgHeight
    if imgWidth > imgHeight:
        if imgWidth > scrWidth:
            imgWidth = scrWidth
            imgHeight = imgWidth / ratio
            if imgHeight > scrHeight:
                imgHeight = scrHeight
                imgWidth = imgHeight * ratio
    else:
        if imgHeight > scrHeight:
            imgHeight = scrHeight
            imgWidth = imgHeight * ratio
            if (imgWidth > scrWidth):
                imgWidth = scrWidth
                imgHeight = imgWidth / ratio

    image = pygame.transform.scale(image, (int(imgWidth), int(imgHeight)))
    posX = (scrWidth - imgWidth) / 2.0
    posY = (scrHeight - imgHeight) / 2.0
    screen.fill((0, 0, 0))
    screen.blit(image, (posX, posY))
    pygame.display.flip()
        
if __name__ == "__main__":
    from sys import argv
    if(len(argv) < 2):
        print "Usage: picView.py "
        sys.exit(1)
    folderPath = argv[1]
    print "Showing pictures in " + folderPath
    imageFolder = ImageFolder(folderPath)
    SCREEN_SIZE = (640, 480)
    
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, True, 32)
    quit = False
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
                    break
                elif event.key in [pygame.K_UP, pygame.K_PAGEUP, pygame.K_F7, pygame.K_BACKSPACE]:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.PrevImage(), angle)
                elif event.key in [pygame.K_DOWN, pygame.K_PAGEDOWN, pygame.K_F8, pygame.K_RETURN, pygame.K_SPACE]:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.NextImage(), angle)
                elif event.key == pygame.K_LEFT:
                    angle = angle + 90
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
                elif event.key == pygame.K_RIGHT:
                    angle = angle - 90
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
                elif event.key == pygame.K_F5:
                    angle = 0
                    ShowImageWithFitScale(screen, imageFolder.CurrentImage(), angle)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ShowImageWithFitScale(screen, imageFolder.NextImage())
        if quit:
            break
    print "Byebye!"
    display.quit()