
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

    simplegui.Frame._hide_status = True
    simplegui.Frame._keep_timers = False
# define global variables
counter=0
minutes=0
seconds=0
started=False
success=0
tries=0
message='0:00.0'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    global minutes
    global seconds
    global message
    tenths=t
    if t<10:
        message= str(minutes)+':0'+str(seconds)+'.'+str(tenths)
    elif t>=10 and t<100:
        seconds=tenths
        tenths=tenths%10
        seconds=seconds/10
        message= str(minutes)+':0'+str(seconds)+'.'+str(tenths)
    elif t>=100 and t<600:
        seconds=tenths
        tenths=tenths%10
        seconds=seconds/10
        message= str(minutes)+':'+str(seconds)+'.'+str(tenths)
    elif t>=600:
        minutes=tenths/100
        minutes=minutes/6
        seconds=tenths-(minutes*600)
        tenths=seconds%10
        seconds=seconds/10
        if seconds<10:
            message= str(minutes)+':0'+str(seconds)+'.'+str(tenths)
        else:
            message= str(minutes)+':'+str(seconds)+'.'+str(tenths)
        
        
        
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    started=True
    timer.start()
    
def stop():
    timer.stop()
    global started
    global success
    global tries
    if started==True:
        if counter%10==0:
            success=success+1
        tries=tries+1
    started=False
        
def reset():
    global minutes
    global seconds
    global message
    global success
    global tries
    global counter
    success=0
    tries=0
    format(counter)
    timer.stop()
    counter=0
    minutes=0
    seconds=0
    message='0:00.0'
    
    

# define event handler for timer with 0.1 sec interval
def time():
    global counter
    counter=counter+1
    format(counter)
    
        

# define draw handler
def draw(canvas):
    canvas.draw_text(message,[150,150],36,'Red')
    canvas.draw_text(str(success)+"/"+str(tries),[180,100],27,'Green')
    
# create frame
frame=simplegui.create_frame('The StopWatch Game',300,300)

# register event handlers
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,time)
frame.add_button('Start',start)
frame.add_button('Stop', stop)
frame.add_button('Reset',reset)
# start frame
frame.start()
