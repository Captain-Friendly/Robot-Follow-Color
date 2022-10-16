# from robot import Robot
# julian Angel Murillo
import cv2




# HSV_MIN = (160,140,90)
# HSV_MAX = (180,210,215)
# AIR_MAX = 238 * 78
# AIR_MIN = 19 * 16

# MIN_X = 106
# MAX_X = 212
    

class Camera:
    def __init__(self):
        self.__capteur = cv2.VideoCapture(0)
        self.__capteur.set(cv2.CAP_PROP_FRAME_WIDTH, 320) 
        self.__capteur.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)   


    def trouver_couleur_image(self, hsv_min, hsv_max):
        fini = False

        while fini == False:
            ok, image = self.__capteur.read() 
            if(ok):
                image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                image_bin = cv2.inRange(image_hsv, hsv_min, hsv_max)
                contours, _ = cv2.findContours(image_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                image_contour = cv2.drawContours(image, contours, -1, (179, 0, 30), 2)
            
                image_afficher = image
                if len(contours) > 0:
                    plus_grand_contour = cv2.boundingRect(contours[0])
                    for countour in contours:
                        x, y, l, h = cv2.boundingRect(countour)
                        air_contour = l * h
                        air_plus_grand_contour =  plus_grand_contour[2] * plus_grand_contour[3]
                        if  air_contour > air_plus_grand_contour:
                            plus_grand_contour = x, y, l, h

                    # ajouter rectangle
                    x, y, l, h = plus_grand_contour
                    cv2.rectangle(image_contour, (x,y), (x+l,y+h), (172,255,89), 2)

                    # ajoute un markeur
                    pos_x = int(x + (l/2))
                    pos_y = int(y + (h/2))
                    image_afficher = cv2.drawMarker(image_contour, 
                                                    (pos_x,pos_y), 
                                                    (255, 255, 255), 
                                                    cv2.MARKER_TILTED_CROSS, 
                                                    20, 
                                                    3)
            cv2.imshow("Image", image_afficher)  
            key = cv2.waitKey(1)
            if key==ord('q'): 
                fini = True




          
    
    def trouver_couleur(self,hsv_min,hsv_max):
        ok, image = self.__capteur.read() 
        # on fait rien si l'image n'est pas ok
        if(ok):
            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image_bin = cv2.inRange(image_hsv, hsv_min, hsv_max)
            contours, _ = cv2.findContours(image_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            image_contour = cv2.drawContours(image, contours, -1, (179, 0, 30), 2)
        
            # image_afficher = image
            # trouve plus grans contours
            if len(contours) > 0:
                plus_grand_contour = cv2.boundingRect(contours[0])
                for countour in contours:
                    x, y, l, h = cv2.boundingRect(countour)
                    air_contour = l * h
                    air_plus_grand_contour =  plus_grand_contour[2] * plus_grand_contour[3]
                    if  air_contour > air_plus_grand_contour:
                        plus_grand_contour = x, y, l, h

                # ajouter rectangle
                x, y, l, h = plus_grand_contour
                cv2.rectangle(image_contour, (x,y), (x+l,y+h), (172,255,89), 2)

                # ajoute un markeur
                pos_x = int(x + (l/2))
                # pos_y = int(y + (h/2))
                # if(afficher_image == True):
                #     image_afficher = cv2.drawMarker(image_contour, (pos_x,pos_y), (255, 255, 255), cv2.MARKER_TILTED_CROSS, 20, 3)

                    

                air_rectangle = l * h

                return pos_x,air_rectangle
            else:       
                return None,None
            
            

        
    def finir(self):
        self.__capteur.release()
        cv2.destroyAllWindows()

        