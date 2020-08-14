import pygame
# works best with error
#  ##
#   ##
#   #
#   wayne w
#colours
black = [ 0, 0, 0 ]
white = [255,255,255]

# init game engine
pygame.init()

# set screen dimensions
size = [ 800, 800 ]

##if size[0] != size[1]: #rem if gets in the way
##    size[1] = size[0]
width = size[0]
height = size[1]

screen = pygame.display.set_mode(size)
#cell dimensions
cellsize = 10
step=int(width/cellsize)

pygame.display.set_caption("the game of life")


# clock for main game loop
clock = pygame.time.Clock()

# main game loop
done = False 

def sqr():
    x = 0 # use for cell loc, 8 neighbours
    rects = []
    for i in range(0, height, cellsize):
        print(x)
        for j in range(0, width, cellsize):
            rects.append([j,i,cellsize, cellsize,False])
            x+=1
        #print x,
    return rects
cells = sqr()

set_cells = True
check_cells = False

def get_neighbours(num):
    i = num
    alive_neighbours = 0
    if cells[i][0] > 0 and cells[i][0] < width - cellsize and cells[i][1] >0 and cells[i][1] < height-cellsize:
        if cells[i-1][-1] == True: # left
            #print "left alive too"
            alive_neighbours += 1
        if cells[i+1][-1] == True: # right
            #print "right alive too"
            alive_neighbours += 1
        if cells[i-step][-1] == True: # top:    step is diff
            #print "top alive too"
            alive_neighbours += 1
        if cells[i-step-1][-1] == True: # top left
            #print "top left alive too"
            alive_neighbours += 1
        if cells[i-step+1][-1] == True: # top right
            #print "top right alive too"
            alive_neighbours += 1
        if cells[i+step][-1] == True: # bottom:    step is diff
            #print "bottom alive too"
            alive_neighbours += 1
        if cells[i+step-1][-1] == True: # bottom left
            #print "bottom left alive too"
            alive_neighbours += 1
        if cells[i+step+1][-1] == True: # bottom right
            #print "bottom right alive too"
            alive_neighbours += 1

    return alive_neighbours

def check_alive_cells():
	#copy = []
	global cells
	test = sqr()
	for i in range( len(cells)):
		if cells[i][-1] == False:

			alive_neighbours = get_neighbours( i)
			if alive_neighbours == 3:
				test[i][-1] = True


		if cells[i][-1] == True: # [-1] is not position it is boolean

			alive_neighbours = get_neighbours( i)
			if alive_neighbours > 3 or alive_neighbours < 2:
				test[i][-1] = False # die of over population or isolation
			if alive_neighbours == 2 or alive_neighbours == 3: # just adding this fixed me
				test[i][-1] = True # 2 or 3 lives on

		#screen.fill( (255, 255, 255) )
	cells = test
	return test
    
    

while done == False:
    # event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                #print "thunderbirds are go"
                set_cells = False
                check_cells = True
                
            if event.key == pygame.K_SPACE: # then press enter again
                print("reset, space pressed")
                cells = sqr()
                set_cells = True
                check_cells = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if set_cells == True:
                x= str( pygame.mouse.get_pos()[0] )
                y = str( pygame.mouse.get_pos()[1] )
                x = int(x[:-1] + "0")
                y = int(y[:-1] + "0")
                #print x,y
                for cell in cells:
                    if [x,y,cellsize, cellsize,False] == cell:
                        #print cell
                        cell[-1] = True
                        print(cell)
                        
    # game logic goes here;
    # if set_cells is now false, call check cells to update each cell before drawing it
    # dont want to check while placing starting cells
    if check_cells == True:
        new_cells = check_alive_cells()
        
    
    screen.fill( (255, 255, 255) )

    # drawing stuff here;
    #for i in range(cellsize, width, cellsize):
    #    pygame.draw.line(screen, black, (0,i),(width,i), 1)
    #    pygame.draw.line(screen, black, (i, 0),(i,width), 1)
    if check_cells == True:
        for cell in new_cells:
            if cell[-1] == True:
                pygame.draw.rect(screen, black, cell[:-1]) # upto but not including bool, for valid rect
            if cell[-1] == False:
                pygame.draw.rect(screen, white, cell[:-1])
    else:
        for cell in cells:
            if cell[-1] == True:
                pygame.draw.rect(screen, black, cell[:-1]) # upto but not including bool, for valid rect
            if cell[-1] == False:
                pygame.draw.rect(screen, white, cell[:-1])
    for i in range(cellsize, width, cellsize):
        pygame.draw.line(screen, black, (0,i),(width,i), 1)
        pygame.draw.line(screen, black, (i, 0),(i,width), 1)
        
    # display the result of drawing operations
    pygame.display.flip()

    # going at  n fps
    clock.tick(50)

# close this stuff

pygame.quit()
