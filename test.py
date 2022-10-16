# Julian Angel Murillo
from camera import Camera

HSV_MIN = (160,140,90)
HSV_MAX = (180,210,215)

def main():
    cam = Camera()
    cam.trouver_couleur_image(HSV_MIN, HSV_MAX)

if __name__ == "__main__":
    main()