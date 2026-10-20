import sys
import random
from config import *

def load_high_score():
    with open("highscore.txt", "r") as f:
        return int(f.read())

def save_high_score(new_high_score):
    with open("highscore.txt", "w") as f:
        f.write(str(new_high_score))

#USTAWIENIE na ekranie
#player
player_rect = rocket_img.get_rect()
player_rect.x = 50
player_rect.y = 300
player_speed = 6

bg_x = 0
bg_speed = 2
enemy_speed = 4
star_speed = 4

lives = 3
max_lives = 3
score = 0
high_score = load_high_score()
game_active = True

game_state = "menu"

#TWORZENIE OBJEKTOW
def create_enemy():
    rect = enemy_img.get_rect()
    rect.x = random.randint(1000,1500)
    rect.y = random.randint(120,500)
    return rect

def create_star():
    rect = star_img.get_rect()
    rect.x = random.randint(1000, 2000)
    rect.y = random.randint(120, 500)
    return rect

def reset_game():
    global lives, score, player_rect, bg_x, enemy_speed, star_speed, bg_speed, enemies_list, stars_list
    lives = 3
    score = 0
    player_rect.y = 300
    bg_x = 0
    enemy_speed = 4
    star_speed = 4
    bg_speed = 2
    enemies_list = []
    for i in range(4):
        enemies_list.append(create_enemy())
    stars_list = []
    for i in range(3):
        stars_list.append(create_star())

def draw_button(image, rect):
    clicked = False
    pos = pygame.mouse.get_pos() #aktualizuje pozycje myszki, przekazuje X oraz Y

    if rect.collidepoint(pos): #sprawdza czy kursor jest w "pudelku" buttona
        if pygame.mouse.get_pressed()[0] == 1: #sprawdza czy byl wcisniety lewy przycisk. [0] - lewy, [2] - prawy
            clicked = True

    screen.blit(image, rect)
    return clicked

enemies_list = []
for i in range(4): enemies_list.append(create_enemy())
stars_list = []
for i in range(3): stars_list.append(create_star())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(bg_img, (bg_x, 0))
    screen.blit(bg_img, (bg_x + 1000, 0))

    if game_state == "menu":
        title_text = font_title.render("Android Attack", True, (128, 0, 128))
        title_rect = title_text.get_rect(center=(500, 200))
        screen.blit(title_text, title_rect)

        if draw_button(play_btn_img, play_button_rect):
            reset_game()
            game_state = "playing"

        if draw_button(exit_btn_img, exit_button_rect):
            running = False

    if game_state == "playing":
        #Bg animation
        bg_x -= bg_speed
        if bg_x <= -1000:
            bg_x = 0
        #KIEROWNAIE
        #rakieta
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_rect.top > 80:
            player_rect.y -= player_speed
        if keys[pygame.K_s] and player_rect.bottom < 600:
            player_rect.y += player_speed

        rocket_hitbox = player_rect.inflate(-60, -105) #zmniejszenie hitboxa
        #androidki
        for enemy in enemies_list:
            enemy.x -= enemy_speed
            if enemy.right < 0:  #sprawdza czy wrog zalkowicie zniknal z ekranu
                enemy.x = random.randint(1000, 1500)
                enemy.y = random.randint(120, 500)
        #KOLIZJA
        #hitboxy
        #enemy
            enemy_hitbox = enemy.inflate(-60, -80)
            enemy_hitbox.y -= 11

            if rocket_hitbox.colliderect(enemy_hitbox):  #jesli hitbox rakiety pokryje sie z hitboxem wroga
                lives -= 1
                enemy.x = random.randint(1000, 1500)
                enemy.y = random.randint(100, 500)
                if lives <= 0:
                    print("Game Over")
                    if score > high_score:
                        high_score = score
                        save_high_score(score)
                    game_state = "game_over"
        #star
        for star in stars_list:
            star.x -= star_speed
            if star.right < 0:
                star.x = random.randint(1000, 2000)
                star.y = random.randint(120, 500)
            star_hitbox = star.inflate(-60, -60)
            star_hitbox.y -= 15

            if rocket_hitbox.colliderect(star_hitbox):
                score += 10

                if enemy_speed < 15:
                    enemy_speed += 0.2
                    star_speed += 0.2
                    bg_speed += 0.1

                star.x = random.randint(1000, 2000)
                star.y = random.randint(120, 500)

    #WYSWIETLENIE
        screen.blit(rocket_img, player_rect)

        for enemy in enemies_list:
            screen.blit(enemy_img, enemy)
        for star in stars_list:
            screen.blit(star_img, star)

        for i in range(max_lives):
            heart_x = 10 + i * 50
            heart_y = 90
            if i < lives:
                screen.blit(heart_full, (heart_x, heart_y))
            else:
                screen.blit(heart_empty, (heart_x, heart_y))

        score_text = font.render(f"Score: {score}",True,(255,255,255))
        screen.blit(score_text,(370,130))

    elif game_state == "game_over":

        final_score = font_restart.render(f"Final Score: {score}",True,(128,0,128))
        final_score_rect = final_score.get_rect(center=(500,200))
        screen.blit(final_score,final_score_rect)

        high_score_print = font_restart.render(f"High Score: {high_score}",True,(255,215,0))
        high_score_rect = high_score_print.get_rect(center=(500,250))
        screen.blit(high_score_print,high_score_rect)

        if draw_button(play_btn_img, play_button_rect):
            reset_game()
            game_state = "playing"
        if draw_button(exit_btn_img, exit_button_rect):
            running = False

    screen.blit(frame_img, (0,0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
