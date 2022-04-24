tracker = 0

def moveForwards():
    global tracker 
    tracker += 1
    print('moved forward by one step.')

def turnRight():
    global tracker
    tracker -= 1
    print('turning right')
    
def move():
    moveForwards()
    for _ in range(3):
        turnRight()
    moveForwards()
    for _ in range(3):
        turnRight()
    moveForwards()
    turnRight()
    for _ in range(2):
        moveForwards()
    return tracker

move()