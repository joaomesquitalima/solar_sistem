import pygame
import math
pygame.init()

WIDTH, HEIGHT = 1210, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema solar")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
fonte = pygame.font.Font(None, 36)

imagem_fundo = pygame.image.load("back.png")  # Substitua pelo caminho da sua imagem
imagem_fundo = pygame.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

class Planet:
    def __init__(self, x, y, radius, color,y_vel,acel_y,x_vel,x_cel,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
       
        self.x_vel = x_vel
        self.y_vel = y_vel

        self.acel_x = x_cel
        self.acel_y = acel_y

        self.pos_x = x
        self.pos_y = y

        self.mass = mass

    def draw(self, win):

        self.x_vel += self.acel_x
        self.y_vel += self.acel_y

        self.pos_x += self.x_vel
        self.pos_y += self.y_vel
        
        pygame.draw.circle(win, self.color, (self.pos_x, self.pos_y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self,sol):
        # fonte = pygame.font.Font(None, 36)
        fx, fy = self.attraction(sol)
            

        self.x_vel += fx 
        self.y_vel += fy 

        self.x += self.x_vel 
        self.y += self.y_vel 
        # texto = fonte.render(f"Velocidade {self.x_vel}", True, WHITE)
        # WIN.blit(texto, (100, 100))



  
def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(WIDTH/2, HEIGHT/2, 60, YELLOW,0,0,0,0,2800)

    terra = Planet(WIDTH/2 - 220,HEIGHT/2 - 200,10,BLUE, 0, 0, 4 ,0,2)
    

    while run:

        clock.tick(60)

        WIN.fill((0, 0, 0))
        WIN.blit(imagem_fundo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

       
        sun.draw(WIN)
        terra.draw(WIN)
        terra.update_position(sun)
        # sun.update_position(terra)


        pygame.display.update()

    pygame.quit()


main()
