#from zumi.zumi import Zumi
from Graph import Graph

#zumi = Zumi()
#zumi.mpu.calibrate_MPU()

# CONSTANTS
DIV_CONST = 6.0
POWER = 40

heading = 90

def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time


#make zumi go left by 10  inches from point S to point A
# distanceInInches = 10
# timeToTravel = getTimeForTravel(distanceInInches)
# zumi.turn_left(90)
# zumi.forward( POWER, timeToTravel)

#write the code to get Zumi  from point S to point X
#write the code to get Zumi  from point S to point B

#goal is to type in X instead of 10  from point S
#  travel('s', 'x')
#  travel('x', 'a')


def change_heading_to_desired_heading( currAngle, desiredAngle ):
    turn_magnitude =  abs(currAngle - desiredAngle)

    # turning left
    if currAngle < desiredAngle:
        print("Zumi turning LEFT", turn_magnitude)
        #zumi.turn_left(turn_magnitude)
        return desiredAngle
    # turning right
    elif currAngle > desiredAngle :
        print("Zumi turning RIGHT", turn_magnitude)
        #zumi.turn_right(turn_magnitude)
        return desiredAngle
    else:
        return desiredAngle

def main():
    G = Graph()

    G.create_simple()
    #G.create_d_graph()
    #G.create_complex()
    route = G.search('s', 'x')
    #route = G.search('s', 'a')
    #route = G.search('s', 'b')
    #route = G.search('x', 'a')
    #route = G.search('x', 'b')

    print("-----  Final Route: ----- " )
    i = 0
    for item in route:
        print("\t edge name: ", item[0].get_edgeName(), "desired angle", item[1] )
        i+=1

    heading = 90
    print("currHeading", heading)
    while len(route) != 0:
        pair          = route[0]
        desired_angle = pair[1]

        # Step1: change heading to desired heading
        heading = change_heading_to_desired_heading(heading, desired_angle)


        # Step2: get the distance we need to go
        desired_distance = 10
        time = getTimeForTravel(desired_distance)
        #zumi.forward(POWER, time)

        # Step3: deletes the first element in list
        route.pop(0)


if __name__ == "__main__":
    main()