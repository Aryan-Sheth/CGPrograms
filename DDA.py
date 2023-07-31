import matplotlib.pyplot as plt
import copy

#Taking input points and converting them to a list of [x,y]
pt1 = list(map(int, input("Enter Source Point: ").split(",")))
pt2 = list(map(int, input("Enter Destination Point: ").split(",")))

print(pt1)
print(pt2)

print(pt1[0],",",pt1[1])

#iterate until either x or y axis is equal to the destination
while pt1[0]!=pt2[0] and pt1[1]!=pt2[1]:
    #calculate slope
    slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
    prevpt = copy.deepcopy(pt1)
    #Case 1: m<1
        #x = x + 1
        #y = y + m
    if slope<1:
        pt1[0] = pt1[0] + 1
        pt1[1] = round(pt1[1] + slope)
    #Case 2: m>1
        #x = x + 1/m
        #y = y + 1
    elif slope>1:
        pt1[0] = round(pt1[0] + 1/slope)
        pt1[1] = pt1[1] + 1
    #Case 3: m=1
        #x = x + 1
        #y = y + 1
    else:
        pt1[0] += 1
        pt1[1] += 1

    print(pt1[0],",",pt1[1])
    
    #plot the calculated point
    plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]])
    # plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]], 'o', c="#0099cc")

prevpt = copy.deepcopy(pt1)

if pt1[0]<pt1[1]:
    pt1[1] += 1
    plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]])
    # plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]], 'o', c="#0099cc")
    print(pt1[0],",",pt1[1])
elif pt1[0]>pt1[1]:
    pt1[0] += 1
    plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]])
    # plt.plot([prevpt[0], pt1[0]], [prevpt[1], pt1[1]], 'o', c="#0099cc")
    print(pt1[0],",",pt1[1])
    
    
#displaying the plot
plt.show()