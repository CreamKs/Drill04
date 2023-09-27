from pico2d import *
from enum import Enum

width = 800
height = 600

open_canvas(width, height)
grass = load_image('grass.png')
charimg = load_image('Zelda.png')

move_speed = 5

class Dir(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Character:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.move = False
        self.Direction = 3
    def move(self):
        if self.Direction == Left:
            if self.x > move_speed:
                self.x = self.x - move_speed
        elif self.Direction == Right:
            if self.x < width - move_speed:
                self.x = self.x + move_speed
        elif self.Direction == Up:
            if self.y > move_speed:
                self.y = self.y + move_speed
        elif self.Direction == Down:
            if self.y < height:
                self.y = self.y - move_speed
    def Draw(self):   
        charimg.clip_draw(0, 0, 100, 100, self.x, self.y)

global character
character = Character()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False  
        elif event.type == SDL_KEYDOWN:
            if event.type == SDLK_ESCAPE:
                running = False;    
            elif event.type == SDLK_LEFT:
                character.move = True
                character.Direction = Left
            elif event.type == SDLK_RIGHT:
                character.move = True
                character.Direction = Right
            elif event.type == SDLK_UP:
                character.move = True
                character.Direction = Up
            elif event.type == SDLK_DOWN:
                character.move = True
                character.Direction = Down
        elif event.type == SDL_KEYUP:
            if event.type == SDLK_LEFT:
                character.move = False
            elif event.type == SDLK_RIGHT:
                character.move = False
            elif event.type == SDLK_UP:
                character.move = False
            elif event.type == SDLK_DOWN:
                character.move = False


running = True
x = 800 // 2
y = 600 // 2
frame = 0

while running:
    update_canvas()
    handle_events()
    if(character.move == True):
        character.move()
    character.Draw()
    delay(0.1)

close_canvas()

