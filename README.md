# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [RGB_Neopixel](#RDBNeopixel)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## RGB Neopixel

### Description & Code Snippets
The goal of this assignment was to make a neopixel on a metro express board fade through the rainbow.

 Main part of the code:

```python
def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

```
<a href="https://github.com/amarini3722/engr3/blob/main/Neopixel.py">Neopixel Full Code</a>
 

### Evidence


https://github.com/amarini3722/engr3/assets/143545265/85e68845-ae11-4838-9962-1a6713d2d29a




Video credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>



### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**



## CircuitPython_Servo

### Description & Code Snippets
Get a 180° micro servo to slowly sweep back and forth between 0 and 180°.   
 Spicy part: Now control the servo with 2 buttons. 
 The servo only moves if you are pushing a button.
  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
while True:
    my_servo.throttle = 0.0
    while touch_A4.value:
        my_servo.throttle = 1.0
        time.sleep(.5)
    while touch_A5.value:
        my_servo.throttle = -1.0
        time.sleep(.5)

```

(https://github.com/amarini3722/engr3/blob/main/CompacitiveTouch.py)


### Evidence
![image](https://github.com/amarini3722/engr3/assets/143545265/5d356108-eecc-4d27-a0bc-6a4d88dceb2f)


Image credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>



### Wiring
![image](https://github.com/amarini3722/engr3/assets/143545265/c2e1acbf-5542-4421-9c69-de811ba4d051)

Image credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>
### Reflection
This assignment was easy in that the first code was straight forward. The hard part of this was that it was our first assignment really using Circuit python instead of arduino. The wiring for this was easy because it was basically identical to the assignment like this last year.


## CircuitPython_Distance Sensor

### Description & Code Snippets
Use the HC-SR04 to measure the distance to an object and print that out to your serial monitor or LCD in cm.
 Next, you will get the neopixel to turn red when your object is less than 5cm, and green when its 35cm.  Ignore the blue and 20cm for now, let's just keep it simple.
 For your final version of this code, you'll smoothly shift the color of the onboard neopixel, corresponding to the distance, according to the graphic below.
  (Neopixel should stay red when below 5cm and green when above 35cm)

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255, 0,0)
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()

```

https://github.com/amarini3722/engr3/blob/main/Ultra.py


### Evidence


https://github.com/amarini3722/engr3/assets/143545265/31a06f2c-854a-45c7-a8d0-5f3415e43528



Video credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>



### Wiring
![image](https://github.com/amarini3722/engr3/assets/143545265/a23ca787-6809-4680-9f95-6d824d519601)

Image credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>

### Reflection
The callange of this assingment for me was getting the distance sensor to messure the right distances. At first my distance sensor was backward making the colors go in the worng order. I fixed this by changing the order in which the colors went. I had other minor problems but wiring wise it was pretty easy.





## CircuitPython_Motor Control

### Description & Code Snippets
 Wire up a 6v battery pack to this circuit with a motor.
 Write Python code to make the motor speed up and slow down, based on input from a potentiometer.
  
  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
import board
import analogio

motor=analogio.AnalogOut(board.A0)
pot=analogio.AnalogIn(board.A1)
while True:
    speed=pot.value
    motor.value=speed

```

https://github.com/amarini3722/engr3/blob/main/Motor%20control.py  

### Evidence



https://github.com/amarini3722/engr3/assets/143545265/9e37e78b-ea60-4f6a-99fd-ba818102a3df




Video credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>
### Wiring
![image](https://github.com/amarini3722/engr3/assets/143545265/4862d20c-f2ed-4b43-95a4-555abaf82cd6)

Image credit goes to <a href="https://github.com/Raffi-Chen/engr3/blob/main/README.md">Raffi Chen</a>

### Reflection
This assignment was the hardest wiring assignment but the easiest coding assignment. My code was a total of 6 lines and took maybe 5 minutes to figure out and write. The wireing took my a while to do thought and was dangerous, as I learned when checking Jai's.




## Onshape: The Hanger

### Assignment Description

In this assignment was to create a hanger in onshape. The reason we did this was os when we have the onshape sertification test we will be prepared.

### Evidence
![Part Studio 1 (2)](https://github.com/amarini3722/engr3/assets/143545265/965770fa-3807-485d-82d4-b44f0f9dc913)
![Part Studio 1 (1)](https://github.com/amarini3722/engr3/assets/143545265/f40ed33d-131b-45d6-ba4b-2ebdbc310eaa)
![Part Studio 1](https://github.com/amarini3722/engr3/assets/143545265/7acc1c61-ccbf-4982-91eb-e320d6b764d4)



### Part Link 

https://cvilleschools.onshape.com/documents/a6df4e5b9d7ef08699352238/w/4e10da8a15541707752fd9e0/e/1c74736154ee7dcd285e6183?renderMode=0&uiState=653182becab7294bb8c12488) 


### Reflection
This assignment was used to refesh us on how to mirror a section of a part. During this assignment I was challanged by just using onshape. We hadn't used onshape for 4 months and i was just getting back into the swing of things. The assignment as a whole was easy but remembering all the tools was hard.





## Onshape_swing arm

### Assignment Description

This assignment was to make a part using variables then change the variables and not have to change anything else. This assignment will help with preperation to the onshape certification test.

### Evidence
![Part Studio 1 (3)](https://github.com/amarini3722/engr3/assets/143545265/88170959-766c-4f79-b418-54597182467e)
![Part Studio 1 (4)](https://github.com/amarini3722/engr3/assets/143545265/e9b4c4cd-dfaf-4f1d-bc06-2c765390577c)
![Part Studio 1 (5)](https://github.com/amarini3722/engr3/assets/143545265/750e4fba-b468-4f5c-993a-413fe9418faf)
![Part Studio 1 (6)](https://github.com/amarini3722/engr3/assets/143545265/6f1c9a5c-fbf4-4041-8c92-6444e55d1d6b)


### Part Link 

(https://cvilleschools.onshape.com/documents/e77695125b30882798ee5d92/w/e12ee28b973256b09b71f289/e/1e0d2f184e0db118447975c2?renderMode=0&uiState=653187b0d111681fa4dd1bc8)

### Reflection

This assignment took me a bit of time to complete because of how I constrained things and improperly used variables. The way I improperly constrained thing was I constrained par of it only to a part using a variable making it so that the part constarined to the variable changed when it shouldn't have. With the variables part of messing up, I used variables in place of something that sould have just been 130mm assuming it sould be the variable.

## Single Part

### Assignment Description

In this assignment we made a part in onshape using one part. 

### Evidence
![Part Studio 1 (9)](https://github.com/amarini3722/engr3/assets/143545265/6802c795-dc4c-40b6-b25d-2995c150d582)
![Part Studio 1 (8)](https://github.com/amarini3722/engr3/assets/143545265/b9e1ece6-9463-4703-9a7b-d712b53df740)
![Part Studio 1 (7)](https://github.com/amarini3722/engr3/assets/143545265/85b0a25b-353c-4d5b-82ca-ee00d8544c36)



### Part Link 
https://cvilleschools.onshape.com/documents/11cfd990354aff25bfddd24b/w/f6ff819511c0b150fdb21b5f/e/b370cdbb0ab728283bfd1cdd?renderMode=0&uiState=65b96098889e4819010d44ca 


### Reflection

This assignment was very simple yet for some unknown reason I decided to turn my brain off and struggle. I forgot how to make a slanted cut out around the screw hole. After I found the swich to turn on my brain I helped Jai finish her part.

## Multi-Part Mic Stand 

### Assignment Description

The goal of this assignment is to create a mic stand using multiple parts in one studio. This helped improve the skill of not over complicating one part.

### Evidence

![Assembly 1 (1)](https://github.com/amarini3722/engr3/assets/143545265/a4357d58-9b24-4d34-a1ff-bf7ecc83a849)



### Part Link 
https://cvilleschools.onshape.com/documents/e3c8e4a46bb2b0622bb98b0d/w/1e9719c8c68a330245434468/e/456d2fc448eae0fb06ac3172?renderMode=0&uiState=66048c7802e5fa795f217885 

### Reflection

This assignment brought challanges in that to get the part that holds the mic right we had to do math. The entire holder part had to be one standard length but the challange in that is that there was a curve that needed math to be done to get it right.

## Vice Gripper 

### Assignment Description

The goal of this assignment use mates to create a pair of vice grippers.

### Evidence

![Assembly 1 (2)](https://github.com/amarini3722/engr3/assets/143545265/5bee737e-1ea4-4481-b857-289b223d6413)




### Part Link 
https://cvilleschools.onshape.com/documents/950395349c2f1dc3a4fd068b/w/18f3c684ac0569541f9903ef/e/bda98a0d4ff3c9fb5f7a8a86?renderMode=0&uiState=6604a0d8b5ef12669cf11cb8

### Reflection

This part was challenging because of the use of multipule different mates. Before this assignment I had never used mates to create an actual working tool just stick things together.

## MP Cylinder

### Assignment Description

The goal of this assignment to create a cylinder assembly using multiple parts within one studio. This was important for practicing how to make multiple parts from their shared dimensions

### Evidence

![cylinder parts](https://github.com/amarini3722/engr3/assets/143545265/f2ac4aa4-377e-497f-9b45-28ecd1537317)





### Part Link 
https://cvilleschools.onshape.com/documents/2ef8d220cb8c6486bf08d296/w/81768b571ea41ad76d1646cb/e/357bdec38c70cf79315c586f?renderMode=0&uiState=6604a2f006751e77d445f7a1

### Reflection

This part was over all simple, but it took a good bit of time due to the fact that it was a lot of work and I like to do stuff the hardest way possible. This is a bad habit that needs to change.

## Gripper Claw

### Assignment Description
The goal of this assignment was to create a robot arm that could function with one actuator and could be animated in onshape.
### Evidence

![Assembly 1 (3)](https://github.com/amarini3722/engr3/assets/143545265/e601f40f-649a-41ed-8e80-d5f2b309fa0a)
![Assembly 1 (4)](https://github.com/amarini3722/engr3/assets/143545265/3b859063-1e49-49cb-97ec-55bced766561)
[Drawing 1.pdf](https://github.com/amarini3722/engr3/files/14782006/Drawing.1.pdf)



### Part Link 
https://cvilleschools.onshape.com/documents/94788d94c830d28bb7beaa1e/w/419daf09a373cedad7df4a53/e/213a7ec62ab125b08a097c8d

### Reflection

This assignment wasn't systemically that difficult but me being me I had to make it challenging to automate. Since the claw has three arms, it makes a triangle while fully closed, this makes it extremely hard to constrain and make it not break physics.

## CircuitPython_Rotory Encoder and LCD

### Description
This assignment aimed to create a menu-controlled traffic light using an Arduino, rotary encoder, and the onboard neopixel. The menu needed to have items for stop, go, and caution and be able to switch to the corresponding light color on the neopixel.

### Evidence



https://github.com/amarini3722/engr3/assets/143545265/37182c2b-9212-479e-ad7c-dbc3b2918d7b



### Code

(https://github.com/amarini3722/engr3/blob/main/Rotary.py)

### Wiring
![Rotaryencoder](https://github.com/amarini3722/engr3/assets/143545265/4b1061be-196d-4dd9-ad2d-699a1c209815)




### Reflection
This assignment took a very long time because the way Josh and I did our code and the way I did my wiring took a block period and a normal period to do the code. And my wiring and files may it tough to figure out on my computer.


## CircuitPython_Stepper Motor + Limit Switch

### Description
The goal of this assignment was to program a stepper motor to rotate until it touches the limit switch and then rotate 180 degrees in reverse when it contacts with the motor arm. This assignment was important as it teaches one to use the stepper motor which will come in handy for the robot arm project.

### Evidence

![IMG_2020](https://github.com/amarini3722/engr3/assets/143545265/b9dd283e-325d-46b6-8fc4-c6f52de5188e)



https://github.com/amarini3722/engr3/assets/143545265/b2aab9d1-72cb-45df-8873-b015490497ed


### Code

(https://github.com/amarini3722/engr3/blob/main/Clickythingy.py)

### Wiring
![Steppermotor](https://github.com/amarini3722/engr3/assets/143545265/b5f8a39f-3811-4dc5-a396-729e3f17d46a)

### Reflection
This assignment was fairly simple. The hardest part was waiting for someone to be done with there assignment so I could take their motor and limit switch. I wish for this assignment the slides didn't give us so much of the assignment for free.


## CircuitPython_IR Sensor

### Description
The goal of this assignment was to program a IR sensor to do what it does. 

### Evidence

![IMG_2022](https://github.com/amarini3722/engr3/assets/143545265/b212f9d5-411f-465c-8a49-23e762a78aea)



https://github.com/amarini3722/engr3/assets/143545265/db0d61c6-5820-41dc-ab80-a5032111ae1e


### Code

(https://github.com/amarini3722/engr3/blob/main/irsensor.py)

### Reflection
This assignment was overall simple but made eaiser by the fact that I did a project using IR sensors last year. The wiring was simple and used a total of 3 wires and a ir sensor.
