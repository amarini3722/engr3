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




Video credit goes to [Raffi Chen]



### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**



## CircuitPython_Servo

### Description & Code Snippets
Get a 180° micro servo to slowly sweep back and forth between 0 and 180°.   
 Spicy part: Now control the servo with 2 buttons. 
 The servo only moves if you are pushing a button.
  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  


### Evidence
![image](https://github.com/amarini3722/engr3/assets/143545265/5d356108-eecc-4d27-a0bc-6a4d88dceb2f)


GIF credit goes to [Raffi Chen]



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

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
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  


### Evidence


https://github.com/amarini3722/engr3/assets/143545265/31a06f2c-854a-45c7-a8d0-5f3415e43528



Video credit goes to [Raffi Chen]



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


### Reflection
The callange of this assingment for me was getting the distance sensor to messure the right distances. At first my distance sensor was backward making the colors go in the worng order. I fixed this by changing the order in which the colors went. I had other minor problems but wiring wise it was pretty easy.





## CircuitPython_Motor Control

### Description & Code Snippets
 Wire up a 6v battery pack to this circuit with a motor.
 Write Python code to make the motor speed up and slow down, based on input from a potentiometer.
  
  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence



https://github.com/amarini3722/engr3/assets/143545265/9e37e78b-ea60-4f6a-99fd-ba818102a3df




Video credit goes to [Raffi Chen]
### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.


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





## Onshape_Assignment_Template

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
