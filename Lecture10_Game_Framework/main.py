import pico2d
#import play_state
import logo_state
state_state = logo_state # 모듈을 변수로 취급

pico2d.open_canvas()
start_state.enter()

# game main loop code
while start_state.running:
    start_state.handle_events()
    start_state.update()
    start_state.draw()

start_state.exit()
# finalization code
pico2d.close_canvas()
