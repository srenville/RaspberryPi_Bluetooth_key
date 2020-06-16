import bluetooth
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)


target_name = "OneDer V3" #insert device name you want to register.
target_address = None





while(1):
    nearby_devices = bluetooth.discover_devices()
    
    for bdaddr in nearby_devices:
    #print(bluetooth.lookup_name( bdaddr ))
        if target_name == bluetooth.lookup_name( bdaddr ):
            target_address = bdaddr
            break

    if target_address is not None:
        print ("found target bluetooth device with address ", target_address)
        GPIO.setwarnings(False)
        GPIO.output(4,True)
        target_address = None
        
    else:
        print ("could not find target bluetooth device nearby")
        GPIO.output(4,False)
        GPIO.setwarnings(False)
