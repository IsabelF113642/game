blob=Actor('characterman')
blob.topright= 0,10

WIDTH=500
HEIGHT=blob.height+20

def draw():
    screen.fill((128, 0,0))
    blob.draw()

def update():
    blob.left = blob.left + 2
    if blob.left>WIDTH:
        blob.right=0

def on_mouse_down(pos):
    if blob.collidepoint(pos):
        print("Ahhh!")
        sounds.clicked.play()
        blob.image='blob_hurt'
    else:
        print("Haha you missed!")
