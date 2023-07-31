import matplotlib.pyplot as plt
import copy

def Midpoint(x1,y1,x2,y2):
    x=x1
    y=y1
    
    #calculate the difference dx and dy
    dx = x2-x1
    dy = y2-y1
    
    prevX = copy.deepcopy(x)
    prevY = copy.deepcopy(y)
    
    #difference in x is greater iterate through x and decide based on y   
    if dy<=dx:
        d = dy - (dx/2)
        x = x1 
        y = y1
    
        prevX = copy.deepcopy(x)
        prevY = copy.deepcopy(y)

        print(x,",",y)
        plt.plot([prevX, x], [prevY, y], c='#0099cc')
        # plt.plot([prevX, x], [prevY, y], 'o', c='#0099cc')
        
        #iterate until x = destination x
        while x<x2:
            x+=1
            
            #if d < 0,
                #d = d + dy
                #x = x + 1
                #y = y
            if (d < 0):
                d = d + dy
                
            #if d >= 0,
                #d = d + dy - dx
                #x = x + 1
                #y = y + 1
            else:
                d = d + dy - dx
                y = y+1
            
            print(x,",",y)
            plt.plot([prevX, x], [prevY, y], c='#0099cc')
            # plt.plot([prevX, x], [prevY, y], 'o', c='#0099cc')
            
            prevX = copy.deepcopy(x)
            prevY = copy.deepcopy(y)
    
    #if difference in y is greater iterate through y and decide based on x   
    elif dx<=dy:
        d = dx - (dy/2)
        x = x1
        y = y1
        
        #iterate until y = destination y
        while y< y2:
            y= y+1
            
            #if d < 0,
                #since iteration is based on y change x and y
                #d = d + dx 
                #y = y + 1
                #x = x
            if (d < 0):
                d = d + dx
                
            #if d >= 0,
                #since iteration is based on y change x and y
                #d = d + dx - dy
                #y = y + 1
                #x = x + 1
            else:
                d = d + dx - dy
                x = x+1
                
            print(x,",",y)
            plt.plot([prevX, x], [prevY, y], c='#0099cc')
            # plt.plot([prevX, x], [prevY, y], 'o', c='#0099cc')
        
    plt.show()
    
#Taking input points and converting them to a list of [x,y]
pt1 = list(map(int, input("Enter Source Point: ").split(",")))
pt2 = list(map(int, input("Enter Destination Point: ").split(",")))

Midpoint(pt1[0], pt1[1], pt2[0], pt2[1])

