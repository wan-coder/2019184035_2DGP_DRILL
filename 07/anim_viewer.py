from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('doraemong_runssss.png')

x = 0
frame=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*136,0,140,180,x,140)
    update_canvas()
    frame=(frame+1)%4 #1 0 1 0 1 0
    x+=5
    delay(0.08)
    get_events()


close_canvas()

