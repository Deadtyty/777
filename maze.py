#создай игру "Лабиринт"!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y+=self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x+=self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x-=self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 230:
            self.direction = "right"
        if self.rect.x >= 600:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width,self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
      
window = display.set_mode((700,500))
display.set_caption('Лабиринт ')
background = transform.scale(image.load('background.jpg'),(700,500))

wall1 = Wall(0,255,0,200,0,25,300) 
wall2 = Wall(0,255,0,310,300,25,300)
wall3 = Wall(0,255,0,410,120,25,400)

game_hero = Player("hero.png",100,100,5)
game_enemy = Enemy("cyborg.png",470,25,5)

treasure = GameSprite('treasure.png',600,300,0)


game = True
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
finish = False
font.init()
font = font.SysFont('Arial',40)
win = font.render('Победа!',True,(255,215,0))
lose = font.render('Поражение!',True,(255,215,0))
n = 0
while game:
    events = event.get()
    for i in events:
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        wall1.draw_wall() 
        wall2.draw_wall()
        wall3.draw_wall()
        game_hero.reset()
        game_hero.update()
        game_enemy.reset()
        game_enemy.update()
        treasure.update()
        treasure.reset()
        window.blit(font.render(str(n),True,(255,215,0)),(0,400))
        if sprite.collide_rect(game_hero,wall1) or sprite.collide_rect(game_hero,wall2) or sprite.collide_rect(game_hero,wall3) or sprite.collide_rect(game_hero,game_enemy):
            finish = True
            window.blit(lose,(200,200))
            n+=1
            kick.play()
        if sprite.collide_rect(game_hero,treasure):
            finish = True
            window.blit(win,(200,200))
            
            money.play()
    else:
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            finish = False
            game_hero.rect.x = 100
            game_hero.rect.y = 100
    clock.tick(FPS)
    display.update()