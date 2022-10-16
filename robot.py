# Julian Angel Murillo
from moteur import Moteur
from camera import Camera
import cv2
import numpy as np


# moteur
MIN_VITESSE = 0.1
VITESSE_DEPART= 0.4
MAX_VITESSE = 1

# camera
MIN_X = 106
MAX_X = 212
AIR_MAX = 238 * 78
AIR_MIN = 19 * 16


class Robot:
    def __init__(self):
        self.__camera = Camera()
        self.__moteur_gauche = Moteur(13,6,5)
        self.__moteur_droit = Moteur(18,15,14)
        self.__vitesse = VITESSE_DEPART
    
    def suivre_couleur(self, hsv_min, hsv_max ):
        en_jeu = True
        img = np.zeros((512,512,3),np.uint8)
        cv2.putText(
                img,
                "Pressionner q pour quiter",
                (10, 200),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
               (255, 255, 255),
                2)
        cv2.imshow('directions', img)

        while en_jeu:
            pos_x,air_rectangle  = self.__camera.trouver_couleur(hsv_min, hsv_max)

            if(pos_x != None and air_rectangle != None):
                if(pos_x > MIN_X and pos_x < MAX_X):
                    if(air_rectangle > AIR_MIN and air_rectangle < AIR_MAX):
                        self.avancer()
                    else :
                        self.frein()
                elif(pos_x > MAX_X):
                    self.tourner_droite()
                elif(pos_x < MIN_X):
                    self.tourner_gauche()

            choix = cv2.waitKey(10)
            if  choix == ord('q'):
                en_jeu = False
        
        self.__camera.finir()

                
            

    def augmenter_vitesse(self):
        if self.__vitesse < MAX_VITESSE:
            self.__vitesse += 0.1

    def diminuer_vitesse(self):
        if self.__vitesse > MIN_VITESSE:
            self.__vitesse -= 0.1
    
    def avancer(self):
        self.__moteur_droit.avancer(self.__vitesse)
        self.__moteur_gauche.avancer(self.__vitesse)
    
    def avancer_gauche(self):
        self.__moteur_droit.avancer(self.__vitesse)
        self.__moteur_gauche.avancer(self.__vitesse * 20 / 100)
        
    def avancer_droite(self):
        self.__moteur_droit.avancer(self.__vitesse * 20 / 100)
        self.__moteur_gauche.avancer(self.__vitesse)

    def tourner_gauche(self):
        self.__moteur_droit.avancer(self.__vitesse)
        self.__moteur_gauche.reculer(self.__vitesse)

    def tourner_droite(self):
        self.__moteur_droit.reculer(self.__vitesse)
        self.__moteur_gauche.avancer(self.__vitesse)

    def frein(self):
        self.__moteur_droit.frein()
        self.__moteur_gauche.frein()

    def reculer(self):
        self.__moteur_droit.reculer(self.__vitesse)
        self.__moteur_gauche.reculer(self.__vitesse)

    def augmenter_vitesse(self):
        if self.__vitesse < MAX_VITESSE:
            self.__vitesse += 0.1

    def diminuer_vitesse(self):
        if self.__vitesse > MIN_VITESSE:
            self.__vitesse -= 0.1

    def arreter(self):
        self.__moteur_droit.arreter()
        self.__moteur_gauche.arreter()