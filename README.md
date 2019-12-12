# templecarmk3

![car](readmeimages/car.jpg)

## Starting the program

1) 

## Controling the Car

The car uses modified WASD controls to move. See "test.py" below.

W/A moves the car forwards and back

A/S turn the wheels

Q/E turn the wheels and move the car forward simutaneously

## Data Collection

usbwriter.py records speed, steering, and an image every # seconds and stores it in:

```
/templecar/src/{filename}.csv
```

Each line represents a new dataset, and the data is saved in the following format:
```
{speed 1}, {steering 1}, {image 1}
{speed 2}, {steering 2}, {image 2}
…
{speed n}, {steering n}, {image n}
```

## System Architecture

![architecture](readmeimages/SystemArchitecture.JPG)

### test.py

Publishes keyboard inputs from a computer connected to the same network as the Raspberry Pi. Based on keyboard inputs from the user, it publishes speed and steering data to the topic 'driving'.

### drive.py

Subscribes to the 'driving' topic and controls the car using the speed and steering data. This data is converted to a PWM signal for the car to interprite. 

### usb_cam

Streams the image from the USB camera. 
