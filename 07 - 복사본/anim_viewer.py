from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('Blue Mushmom.png')

x = 0
frame=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*140,580,135,152,x,115)
    update_canvas()
    frame=(frame+1)%4 #1,2,3,4
    x+=5
    delay(0.08)
    get_events()


close_canvas()

