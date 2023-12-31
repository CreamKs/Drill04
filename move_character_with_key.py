from pico2d import *
from enum import Enum

width = 800
height = 600

open_canvas(width, height)
grass = load_image('grass.png')
charimg = load_image('Zelda.png')
back = load_image('TUK_GROUND.png')

move_speed = 10

class Dir(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

class Character:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.moveOn = False
        self.Direction = Dir.Right
    def move(self):
        if self.Direction == Dir.Left:
            if self.x > 30:
                self.x = self.x - move_speed
        elif self.Direction == Dir.Right:
            if self.x < width - 30:
                self.x = self.x + move_speed
        elif self.Direction == Dir.Up:
            if self.y < height - 30:
                self.y = self.y + move_speed
        elif self.Direction == Dir.Down:
            if self.y > 30:
                self.y = self.y - move_speed
    def Draw(self, frame):  
        if self.moveOn == True:
            if self.Direction == Dir.Right:
                charimg.clip_draw(frame * 120, 0, 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Left:
                charimg.clip_draw(frame * 120, 260, 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Up:
                charimg.clip_draw(frame * 120, 130, 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Down:
                charimg.clip_draw(frame * 120, 390, 120, 130, self.x, self.y, 60, 60)
        else:
            if(frame < 7):
                frame_stop = 0
            elif frame < 8:
                frame_stop = 1
            else:
                frame_stop = 2
            if self.Direction == Dir.Right:
                charimg.clip_draw(frame_stop * 120, 0 + 520, 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Left:
                charimg.clip_draw(frame_stop * 120, 260 + 520 , 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Up:
                charimg.clip_draw(frame_stop * 120, 130 + 520, 120, 130, self.x, self.y, 60, 60)
            elif self.Direction == Dir.Down:
                charimg.clip_draw(frame_stop * 120, 390 + 520, 120, 130, self.x, self.y, 60, 60)
            

global character
character = Character()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False  
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False    
            elif event.key == SDLK_LEFT:
                character.moveOn = True
                character.Direction = Dir.Left
            elif event.key == SDLK_RIGHT:
                character.moveOn = True
                character.Direction = Dir.Right
            elif event.key == SDLK_UP:
                character.moveOn = True
                character.Direction = Dir.Up
            elif event.key == SDLK_DOWN:
                character.moveOn = True
                character.Direction = Dir.Down
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                character.moveOn = False
            elif event.key == SDLK_RIGHT:
                character.moveOn = False
            elif event.key == SDLK_UP:
                character.moveOn = False
            elif event.key == SDLK_DOWN:
                character.moveOn = False


running = True
x = 800 // 2
y = 600 // 2
frame = 0

while running:
    clear_canvas()     
    back.draw(400, 300)
    handle_events()
    if(character.moveOn == True):
        character.move()
    character.Draw(frame)
    if character.moveOn == True:
        delay(0.1)
    elif character.moveOn == False:
        delay(0.4)
    frame = (frame + 1) % 10
    update_canvas()

close_canvas()

