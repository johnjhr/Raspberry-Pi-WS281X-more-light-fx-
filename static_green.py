#This is the main.  This meeds to import function_library.py in order to work.

#Import the 'functions_library' which animates the LEDs in various ways.
from function_library import *

#Main program logic:
if __name__ == '__main__':
        #Process arguments
        opt_parse()
        #Create NeoPixel object with appropriate configuration.
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
        #Intialize the library (must be called once before other functions).
        strip.begin()

        print ('Press Ctrl-C to quit.')
        i=1
        
			
        SetAll(strip, Color(0, 255, 0))
        strip.show()


                        
		        
	print("========================================")
	print("Finished")
	print("========================================")


