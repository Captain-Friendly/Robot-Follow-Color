# Julian Angel Murillo
import gpiozero
# self.__ENA = gpiozero.PWMOutputDevice(13)
        # self.__IN1 = gpiozero.DigitalOutputDevice(6)
        # self.__IN2 = gpiozero.DigitalOutputDevice(5)


class Moteur:
    def __init__(self, enx, inx, iny):
        self.__ENX = gpiozero.PWMOutputDevice(enx)
        self.__INX = gpiozero.DigitalOutputDevice(inx)
        self.__INY = gpiozero.DigitalOutputDevice(iny)

    def avancer(self, vitesse):
        self.__ENX.value = vitesse
        self.__INX.on()
        self.__INY.off()


    def reculer(self, vitesse):
        self.__ENX.value = vitesse
        self.__INX.off()
        self.__INY.on()
    
    def frein(self):
        self.__ENX.on()
        self.__INX.on()
        self.__INY.on()

    def arreter(self):
        self.__ENX.off()

    def rien(self):
        self.__ENX.on()
        self.__INX.off()
        self.__INY.off()

    

