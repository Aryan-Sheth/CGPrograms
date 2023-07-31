import matplotlib.pyplot as plt
import copy

def Bresenham(x1,y1,x2,y2):
    x=x1
    y=y1
    
    #calculate the difference dx and dy
    dx = x2-x1
    dy = y2-y1
    
    if(dx>=dy):
        #calculate decision parameter
        p = 2*dx - dy
        
        prevX = copy.deepcopy(x)
        prevY = copy.deepcopy(y)
        
        #iterate until x = destination x
        while(x<=x2):
            #increment x reguardless of case because x is incremented in any case
            x+=1

            #if p < 0,
                #p = p + 2dy
                #x = x + 1
                #y = y
                
            if p<0:
                p= p + 2*dy
            #else if p>=0,
                #p = p + 2dy - 2dx
                #x = x + 1
                #y = y + 1
            elif p>=0:
                p = p + 2*dy - 2*dx
                y+=1
            print(x,",",y)
            
            #plot the calculated points
            plt.plot([prevX, x], [prevY, y], c='#0099cc')
            # plt.plot([prevX, x], [prevY, y], 'o', c='#0099cc')
            
            prevX = copy.deepcopy(x)
            prevY = copy.deepcopy(y)
            
    else:
        #calculate decision parameter
        p = 2*dy - dx
        
        prevX = copy.deepcopy(x)
        prevY = copy.deepcopy(y)
        
        #iterate until x = destination x
        while(y<=y2):
            #increment x reguardless of case because x is incremented in any case
            y+=1

            #if p < 0,
                #p = p + 2dx
                #x = x
                #y = y + 1
                
            if p<0:
                p= p + 2*dx
            #else if p>=0,
                #p = p + 2dx - 2dy
                #x = x + 1
                #y = y + 1
            elif p>=0:
                p = p + 2*dx - 2*dy
                x+=1
            print(x,",",y)
            
            #plot the calculated points
            plt.plot([prevX, x], [prevY, y], c='#0099cc')
            # plt.plot([prevX, x], [prevY, y], 'o', c='#0099cc')
            
            prevX = copy.deepcopy(x)
            prevY = copy.deepcopy(y)
        
    #show the graph
    plt.show()
    

#Taking input points and converting them to a list of [x,y]
pt1 = list(map(int, input("Enter Source Point: ").split(",")))
pt2 = list(map(int, input("Enter Destination Point: ").split(",")))

Bresenham(pt1[0], pt1[1], pt2[0], pt2[1])

