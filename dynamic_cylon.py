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
        while True:
            
                    Cylon(strip, 255, 0, 0, 3, .1, .5)
                    Cylon(strip, 0, 255, 0, 3, .1, .5)
                    Cylon(strip, 0, 0, 255, 3, .1, .5)
                    Cylon(strip, 255, 255, 0, 3, .1, .5)
                    Cylon(strip, 128, 0, 128, 3, .1, .5)
                    strip.show()


                        
		        
                    print("========================================")
                    print("Looping")
                    print("========================================")
"""
#List of functions:
		FadeRGB(strip)
		FadeInOut(strip, 255, 255, 255)
		Strobe(strip, 255, 255, 255, 5, .5, 3)
		Cylon(strip, 255, 0, 0, 3, .1, .5)
		Twinkle(strip, 255, 0, 0, 8, .1, False)
		TwinkleRandom(strip, 8, .1, False)
		Sparkle(strip, 255, 255, 255, 0)
		SnowSparkle(strip, 10, 10, 10, .1, random.uniform(0, .5))
		RunningLights(strip, 255, 255, 255, .25)
		ColorWipe(strip, 255, 0, 0, .02)
		ColorWipeReverse(strip, 0, 255, 0, .02)
		Rainbow(strip, 0)
		RainbowCycle(strip, 5, 0)
		ColorChase(strip, 0, 0, 255, .02)
		ColorChaseReverse(strip, 0, 255, 0, .02)
		TheaterChase(strip, 255, 0, 0, .2, 10)
		TheaterChaseRainbow(strip, .1)
		MeteorRain(strip, 255, 0, 0, 5, 64, True, .1)
		NewKitt(strip, 255, 0, 0, 8, .01, .05)
		Fire(strip, Heat, 75, 150, .015)
		BouncingBalls(strip, 255, 0, 0, 3)
		BouncingBallsRGB(strip, 3, [[255, 0, 0], [0, 255, 0], [0, 0, 255]])
		HalloweenEyes(strip, 255, 0, 0, 1, 4, True, random.randint(5, 50), random.uniform(.01, .2), random.randrange(1, 3))
		MorseCode(strip, 255, 255, 255, 'SOS. This is a test.', .15)
		Clock1(strip)
		Clock2(strip, True)
		FillDownRandom(strip, 0, .1, 1, .2)
		RandomColors(strip, .1)
"""


