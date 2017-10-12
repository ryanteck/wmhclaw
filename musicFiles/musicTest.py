import pygame
import time
start = time.time()
pygame.mixer.pre_init(22050, -8, 2, 512)
pygame.mixer.init()
pygame.mixer.music.load("movement.ogg")
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()
end = time.time()
totalTime = end-start
print(totalTime)
