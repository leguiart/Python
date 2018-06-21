# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
import random

WIDTH=800
HEIGHT=100
DIST=50
HALF_DIST=DIST/2
LINE='Red'
HALF_HEIGHT=HEIGHT/2
CARD_COLOR='Green'


# helper function to initialize globals
def new_game():
    global lst1, exposed, none_turned, position, state, x, y, turn
    x=[]
    y=[]
    turn=0
    state=0
    position=0
    none_turned=True
    exposed=[False]*16
    lst1=range(0,8)
    lst2=range(0,8)
    lst1.extend(lst2)
    random.shuffle(lst1)


     
# define event handlers
def mouseclick(pos):
    global position, none_turned, state, turn
    if False in exposed:
        if state==0:
            state=1
        elif state==1:
            state=2
        elif state==2:
            if x[0]==y[0]:
                exposed[x[1]]=True
                exposed[y[1]]=True
            else:
                exposed[x[1]]=False
                exposed[y[1]]=False
            turn=turn+1
            state=1
    position=list(pos)
    position=position[0]
    none_turned=False
    label.set_text('Turns= '+str(turn))
           
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global x, y
    dist=0
    half_dist=25
    n=0
    for element in lst1:
        canvas.draw_line([dist, 0],[dist,HEIGHT],1,LINE)                        
        canvas.draw_text(str(element), (half_dist-10, HALF_HEIGHT+10), 40, 'Red')        
        if position>= dist+1 and position<= dist+DIST-1 and none_turned is False:
            exposed[n]=True
            if state==1:
                a=element
                c=n
                x=[a,c]               
            if state==2:
                b=element
                d=n
                y=[b,d]
        dist=DIST+dist
        half_dist=HALF_DIST+dist
        n=n+1
    dist=DIST    
    for element in exposed:
        if element is False:
            canvas.draw_polygon([(dist-DIST+3, 1), (dist-1, 1), (dist-1, HEIGHT-1), (dist-DIST+3, HEIGHT-1)], 1, CARD_COLOR, CARD_COLOR)
        dist=DIST+dist
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns= 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric