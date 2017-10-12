import pygame
import time
start = time.time()
pygame.mixer.pre_init(48000, -16, 2, 2048)
pygame.mixer.init()
pygame.mixer.music.load("oldMp3s/attract-2.mp3")
pygame.mixer.music.play()
time.sleep(7)
#pygame.mixer.music.stop()
end = time.time()
totalTime = end-start
print(totalTime)
