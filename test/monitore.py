from screeninfo import get_monitors
a = 0
b = 0
for monitor in get_monitors():
    a = monitor.width
    b = monitor.height
    
    
print (a,b)
