from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('doraemong_runssss.png')

x = 0
frame=0
while(x<800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*90,0,140,280,x,170)
    update_canvas()
    frame=(frame+8)%16
    x+=5
    delay(0.08)
    get_events()


close_canvas()

