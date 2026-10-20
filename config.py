import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Android Attack")
clock = pygame.time.Clock()
retro_font = os.path.join("assets", 'retro_font.ttf')
pixel_font = os.path.join("assets", 'pixel_font.ttf')

font = pygame.font.Font(pixel_font, 30)
font_title = pygame.font.Font(pixel_font, 50)
font_restart = pygame.font.Font(pixel_font, 30)
font_highscore = pygame.font.Font(pixel_font, 60)

#GRAFIKA
#player
rocket_img_original = pygame.image.load(os.path.join("assets", "rocket.png"))
rocket_img = pygame.transform.scale(rocket_img_original, (140, 150))
rocket_img = pygame.transform.rotate(rocket_img, -90)

#enemy
android_img_original = pygame.image.load(os.path.join("assets", "android.png"))
enemy_img = pygame.transform.scale(android_img_original, (110, 110))

#stars
star_orig = pygame.image.load(os.path.join("assets", "star.png"))
star_img = pygame.transform.scale(star_orig, (100, 100))

#serca
heart_full = pygame.image.load(os.path.join("assets", "heart_full.png"))
heart_full = pygame.transform.scale(heart_full, (120, 120))

heart_empty = pygame.image.load(os.path.join("assets", "heart_empty.png"))
heart_empty = pygame.transform.scale(heart_empty, (120, 120))

#background
bg_img_orig = pygame.image.load(os.path.join("assets", "bg2.jpg"))
bg_img = pygame.transform.scale(bg_img_orig, (1000, 600))

#frame
frame_img_orig = pygame.image.load(os.path.join("assets", "frame.png"))
frame_img = pygame.transform.scale(frame_img_orig, (1000, 600))

#buttons
play_btn_img = pygame.image.load(os.path.join("assets", "btn_start.png"))
play_btn_img = pygame.transform.scale(play_btn_img, (220, 200))
play_button_rect = play_btn_img.get_rect(center=(500, 350))

exit_btn_img = pygame.image.load(os.path.join("assets", "btn_exit.png"))
exit_btn_img = pygame.transform.scale(exit_btn_img, (220, 200))
exit_button_rect = exit_btn_img.get_rect(center=(500, 450))
