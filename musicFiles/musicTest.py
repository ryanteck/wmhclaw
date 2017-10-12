import pygame
import time
start = time.time()
pygame.mixer.pre_init(48000, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load(random.choice["attract-1.ogg","attract-2.ogg","attract-3.ogg","attract-4.ogg")
pygame.mixer.music.play()
time.sleep(7)
#pygame.mixer.music.stop()
end = time.time()
totalTime = end-start
print(totalTime)
