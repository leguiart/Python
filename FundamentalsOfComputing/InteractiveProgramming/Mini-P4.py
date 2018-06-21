# Implementation of classic arcade game Pong

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [float(WIDTH/2),float(HEIGHT/2)]
ball_vel = [2.0,4.0]
LEFT = False
RIGHT = True
switch= False
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[float(WIDTH/2),float(HEIGHT/2)]
    if direction==True:
        ball_vel=[ -float(random.randrange(1,4)), float(random.randrange(1,8))]
    else:
        ball_vel=[float(random.randrange(1,4)), float(random.randrange(1,8))]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 , cont # these are ints
    global ball_pos
    paddle1_pos=HEIGHT/2-HALF_PAD_HEIGHT
    paddle2_pos=HEIGHT/2-HALF_PAD_HEIGHT
    paddle1_vel=0.0
    paddle2_vel=0.0
    score1=0
    score2=0
    cont=0
    ball_pos=[float(WIDTH/2),float(HEIGHT/2)]

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_circle([WIDTH/2,HEIGHT/2], 100, 4, 'White', 'Black')    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    acc=0.001
    if cont>0:
        if ball_vel[0]>=0:        
            ball_vel[0]=ball_vel[0]+acc
        else:
            ball_vel[0]=ball_vel[0]-acc
    
        if ball_vel[1]>=0:
            ball_vel[1]=ball_vel[1]+acc
        else:
            ball_vel[1]=ball_vel[1]-acc
        ball_pos[0]=ball_pos[0]+ball_vel[0]
        ball_pos[1]=ball_pos[1]+ball_vel[1]
        if ball_pos[1]>=HEIGHT-BALL_RADIUS:
            ball_vel[1]=-ball_vel[1]
        elif ball_pos[1]<=BALL_RADIUS:
            ball_vel[1]=-ball_vel[1]
    
    #ball collission for right paddle
    if ball_pos[0]+BALL_RADIUS+1>=WIDTH-PAD_WIDTH:
        if ball_pos[1]>=paddle1_pos and ball_pos[1]<=paddle1_pos+PAD_HEIGHT:           
            ball_vel[0]=-ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2=score2+1
    #ball collission for left paddle
    if ball_pos[0]-BALL_RADIUS-1<=PAD_WIDTH:
        if ball_pos[1]>=paddle2_pos and ball_pos[1]<=paddle2_pos+PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0]           
        else:
            spawn_ball(LEFT)
            score1=score1+1
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    # update paddle's vertical position, keep paddle on the screen
    #paddle1
    if paddle1_vel<0:
        if paddle1_pos>0:
            paddle1_pos=paddle1_pos+paddle1_vel
    elif paddle1_vel>0:
        if paddle1_pos < HEIGHT-PAD_HEIGHT:
            paddle1_pos=paddle1_pos+paddle1_vel            
    
    #paddle2
    if paddle2_vel<0:
        if paddle2_pos>0:
            paddle2_pos=paddle2_pos+paddle2_vel
    elif paddle2_vel>0:
        if paddle2_pos < HEIGHT-PAD_HEIGHT:
            paddle2_pos=paddle2_pos+paddle2_vel            
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH,paddle2_pos],[HALF_PAD_WIDTH, paddle2_pos + 2*HALF_PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH, paddle1_pos],[WIDTH - HALF_PAD_WIDTH, paddle1_pos + 2*HALF_PAD_HEIGHT], PAD_WIDTH, 'White')
    # draw scores
    canvas.draw_text(str(score2),[150,50], 30, 'White')
    canvas.draw_text(str(score1),[450,50], 30, 'White')    


def keydown(key):
    global paddle1_vel, paddle2_vel, cont
    global switch, current_key
    current_key=key
    
    if key==simplegui.KEY_MAP["up"]:
        if paddle1_vel>0:
            paddle1_vel=-paddle1_vel           
        paddle1_vel=paddle1_vel-4        
    elif key==simplegui.KEY_MAP["down"]:
        if paddle1_vel<0:
            paddle1_vel=-paddle1_vel            
        paddle1_vel=paddle1_vel+4
    
        
    if key==simplegui.KEY_MAP["w"]:
        if paddle2_vel>0:
            paddle2_vel=-paddle2_vel            
        paddle2_vel=paddle2_vel-4
    elif key==simplegui.KEY_MAP["s"]:
        if paddle2_vel<0:
            paddle2_vel=-paddle2_vel           
        paddle2_vel=paddle2_vel+4 
    if cont==0:    
        if current_key==38 or current_key==40:
            cont=cont+1
        elif current_key==87 or current_key==93:
            cont=cont+1
            ball_vel[0]=-ball_vel[0]
           
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart=frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()