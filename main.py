# Julian Angel Murillo
from robot import Robot

HSV_MIN = (160,140,90)
HSV_MAX = (180,210,215)

def main():
    robot = Robot()
    robot.suivre_couleur(HSV_MIN, HSV_MAX)

if __name__ == "__main__":
    main()