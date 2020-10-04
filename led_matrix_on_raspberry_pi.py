import time

from neopixel import *

LED_1_COUNT      = 30      
LED_1_PIN        = 18      # GPIO-контакт, подкл к пикселям 
LED_1_FREQ_HZ    = 800000  #  800khz
LED_1_DMA        = 10      
LED_1_BRIGHTNESS = 128     
LED_1_INVERT     = False   
LED_1_CHANNEL    = 0       # 0 или 1
LED_1_STRIP      = ws.SK6812_STRIP_GRBW

LED_2_COUNT      = 15      
LED_2_PIN        = 13      
LED_2_FREQ_HZ    = 800000  
LED_2_DMA        = 11      
LED_2_BRIGHTNESS = 128     
LED_2_INVERT     = False   
LED_2_CHANNEL    = 1       
LED_2_STRIP      = ws.WS2811_STRIP_GRB

def multiColorWipe(color1, color2, wait_ms=5):
        global strip1
        global strip2

        for i in range(strip1.numPixels()):
                if i % 2:
                        
                        strip1.setPixelColor(i, color1)
                        strip2.setPixelColor(i / 2, color2)
                        strip1.show()
                        time.sleep(wait_ms/1000.0)
                        strip2.show()
                        time.sleep(wait_ms/1000.0)
                else:

                        strip1.setPixelColor(i, color1)
                        strip1.show()
                        time.sleep(wait_ms/1000.0)
        time.sleep(1)

def blackout(strip):
        for i in range(max(strip1.numPixels(), strip1.numPixels())):
                strip.setPixelColor(i, Color(0,0,0))
                strip.show()


if __name__ == '__main__':
     
        strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)
        strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, LED_2_STRIP)

        
        strip1.begin()
        strip2.begin()
                        
                        strip1.setPixelColor(i, color1)
                        strip2.setPixelColor(i / 2, color2)
                        strip1.show()
                        time.sleep(wait_ms/1000.0)
                        strip2.show()
                        time.sleep(wait_ms/1000.0)
                else:

                        strip1.setPixelColor(i, color1)
                        strip1.show()
                        time.sleep(wait_ms/1000.0)
        time.sleep(1)

def blackout(strip):
        for i in range(max(strip1.numPixels(), strip1.numPixels())):
                strip.setPixelColor(i, Color(0,0,0))
                strip.show()


if __name__ == '__main__':

        strip1 = Adafruit_NeoPixel(LED_1_COUNT, LED_1_PIN, LED_1_FREQ_HZ, LED_1_DMA, LED_1_INVERT, LED_1_BRIGHTNESS, LED_1_CHANNEL, LED_1_STRIP)
        strip2 = Adafruit_NeoPixel(LED_2_COUNT, LED_2_PIN, LED_2_FREQ_HZ, LED_2_DMA, LED_2_INVERT, LED_2_BRIGHTNESS, LED_2_CHANNEL, LED_2_STRIP)

      
        strip1.begin()
        strip2.begin()

        print ('Ctrl-C - stop program')

              blackout(strip1)
        blackout(strip2)

        while True:

                multiColorWipe(Color(255, 0, 0), Color(255, 0, 0))  # Red 
                multiColorWipe(Color(0, 255, 0), Color(0, 255, 0))  # Blue 
                multiColorWipe(Color(0, 0, 255), Color(0, 0, 255))  # Green 
                multiColorWipe(Color(255, 255, 255), Color(255, 255, 255))  
                multiColorWipe(Color(0, 0, 0, 255), Color(0, 0, 0))  
                multiColorWipe(Color(255, 255, 255, 255), Color(0, 0, 0))


