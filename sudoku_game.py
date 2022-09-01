import pygame

w = 600
WHITE = (255,255,255)
pygame.init()
win = pygame.display.set_mode((w,w))
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_BORDAR = pygame.Color(139,96,19)
COLOR_SET = pygame.Color(0,0,255,255)
FONT = pygame.font.Font(None, 32)
pygame.display.set_caption("sudoku solver.......")

def cp(row,col):
    if (row>=0 and row<3 and col>2 and col<6) or (row>5 and col>2 and col<6):
        return True

class Spot:
    def __init__(self,row,col,width,text='',data=0):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.rect = pygame.Rect(self.x,self.y,width,width)
        self.width = width
        self.data = data
        self.text = ''
        self.color = COLOR_INACTIVE
        self.active = False
        self.text_surface = FONT.render(text,True,self.color)

    def is_Valid(self):
        return self.data != 0
    
    def datac(self):
        return self.data

    def set_data(self,data):
        self.data = data
    
    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                print(event.pos)
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    self.set_data(int(self.text))
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.text_surface = FONT.render(self.text, True, self.color)
                print(self.text)

    def Updraw(self,win):
        self.text_surface = FONT.render(str(self.data),True,self.color)
        win.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(win,self.color,self.rect,2)
    
    def draw(self,win):
        win.blit(self.text_surface, (self.rect.x+5, self.rect.y+5))
        if (cp(self.row,self.col) or cp(self.col,self.row)) and self.active == False:
            pygame.draw.rect(win,COLOR_BORDAR,self.rect,2)
        else:
            pygame.draw.rect(win,self.color,self.rect,2)
    

def make_grid(rows,width):
    gird = []
    print(width/rows)
    gap = width / rows
    for i in range(rows):
        gird.append([])
        for j in range(rows):
            spot = Spot(i,j,gap)
            gird[i].append(spot)
    return gird

#todo
def draw(grid,rows,width):
    win.fill(WHITE)
    for row in grid:
        g =0 #todo

#todo or check
#
# def algo(grid,i,j):
def check(grid ,i,j):
    l = [n for n in range(1,10)] 
    for k in range(9):
        if grid[i][k].data in l:
            l.remove(grid[i][k].data)
        if grid[k][j].data in l:
            l.remove(grid[k][j].data)
    rk = i//3
    rm = j//3
    for k in range(3):
        for m in range(3):
            if grid[(rk*3)+k][(rm*3)+m].data in l:
                l.remove(grid[(rk*3)+k][(rm*3)+m].data)
    return l

def sudo(grid,i=0,j=0):
    if j >= 9:
        j = 0
        i += 1
        if i >= 9:
            return True
    if grid[i][j].data != 0:
        grid[i][j].color = COLOR_SET
        return sudo(grid,i,j+1)
    tem = check(grid,i,j)
    for n in tem:
       # print(i,j)
        grid[i][j].data = n
        if sudo(grid,i,j+1):
            return True
    grid[i][j].data = 0
    return False

def change(g):
    for i in range(9):
        for j in range(9):
            g[i][j].data = 0

def main(win,width):
    rows = 9
    grid = make_grid(rows,width)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if sudo(grid)!=True:
                        print('not possible')
                        change(grid)
                    for grd in grid:
                        for j in grd:
                            j.Updraw(win)
            for spot in grid:
                for box in spot:
                    box.handle_event(event)
            

        for grd in grid:
            for j in grd:
                j.draw(win)

        pygame.display.flip()
    for i in grid:
        for j in i:
            print(j.data,end=' ')
        print()
            
    pygame.quit()
    quit()

main(win,w)
