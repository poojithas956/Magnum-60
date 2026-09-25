---
title: "Magnum60"
author: "poojithas536"
description: "A compact 60% mechanical keyboard designed for minimal desk space."
created_at: "2026-09-25"
---

# 2026-09-25: BOM

**Total time spent: 1 hr 10min**


| Name | Purpose | Quantity | Total Cost (USD) | Distributor | Link |
|---|---|---:|---:|---|---|
| 3D printed Case | 3D printing | 1 | x | Hack Club | https://printlegion.hackclub.com |
| PCB fabrication | PCB | 1 | 39.20 | Robu.in | https://robu.in/product/online-pcb-manufacturing-service/ |
| RP2040-zero | Microcontroller | 1 | 6.05 | Robu.in | https://robu.in/product/waveshare-rp2040-zero-raspberry-pi-mcu-with-presoldered-header/ |
| Cherry PBT Keycaps | Keycaps | 1 | 17.47 | Curiosity Caps | https://curiositycaps.in/products/counter-strike-printstream-decal-collectio-n-cherry-pbt-keycaps |
| Durock Smokey Screw-In Stabilizers V2 | Stabilizers | 1 | 17.00 | StacksKB | https://stackskb.com/store/durock-smokey-screw-in-stabilizers-v2/ |
| Akko V5 Creamy Blue Pro Switch (Pack of 45) | For typing I guess ? | 1 | 13.14 | StacksKB | https://stackskb.com/store/akko-v5-creamy-blue-pro-switch-pack-of-45/ |

**Total BOM cost:** 92.86 USD

![image.png](https://cdn.hackclub.com/01a0d86c-eba7-7666-9f1f-fcecf5adbb05/image.png)
![image.png](https://cdn.hackclub.com/01a0d86d-0a76-71f7-b14b-9c15f3bbc892/image.png)
![image.png](https://cdn.hackclub.com/01a0d86d-3c05-7d0a-8643-acc848aafb57/image.png)
![image.png](https://cdn.hackclub.com/01a0d86d-6165-7e9e-9cc4-782e8da99a3c/image.png)
![image.png](https://cdn.hackclub.com/01a0d86d-865b-7486-88eb-9c96df883747/image.png)
![image.png](https://cdn.hackclub.com/01a0d86d-a916-7c61-a5e6-4dcdb437b2d5/image.png)

* If the grant is short of the required amount, I will paying it out of my own pocket.

# 2026-09-25: September 24, 2026: Keyboard Case Optimization

**Total time spent: 3 hr**

After a thorough examination, including checking the error and accuracy of my measurements, I realized that the case was too tight for the components. Because of this, I had to add a deep cutout for the MCU so it could fit properly and have some space for airflow.

However, this cutout affected the overall look and aesthetics of the case. As a last resort, I decided to add rubber pads for support—although in reality, they’re just made of PLA : / 

![image.png](https://cdn.hackclub.com/01a0d86a-36cb-7ea2-bda3-e160d8fe153e/image.png)
![image.png](https://cdn.hackclub.com/01a0d86a-6148-7d38-8104-94b4a24490f0/image.png)

# 2026-09-25: September 22, 2026: Improvising the Case

**Total time spent: 4 hr**

Yea this was loooooonnnnnnnnnggggggg and ttuffff!!!!

## Phase I
 As I recently modified the pcb with the added 4pin UART extension and some routing changes and the type c breakout board, I made a revisied version of the   Case. Once done I added final touch ups like Fillet and Chamber giving it a finished look.

## Phase II
 This was probably the most stupidist and most time pass part of my project,  Drawing the Keyboard Plate . Since I wanted this to be more of a Product based and not some random prototype, I spent hours trying to perfect the plate. And ended up deleting that and using default plate generator and modifying it. 
*Could have saved an hours work : /

I modified the plate by adjusting its lenght and width according to the case and added a Fillet. Also added screw holes for securing it tightly to the case!

## Phase III
Gave it a final touch up and bit of basic rendering !

## Result
![image.png](https://cdn.hackclub.com/01a0d867-6b91-76a5-88c3-d7ad58101b45/image.png)
![image.png](https://cdn.hackclub.com/01a0d867-85ba-714f-ba01-129133c232cc/image.png)
![image.png](https://cdn.hackclub.com/01a0d867-d768-7c50-8389-dd721aad7860/image.png)
![image.png](https://cdn.hackclub.com/01a0d867-a0f2-70dd-bf29-abb647ec8e1f/image.png)
![image.png](https://cdn.hackclub.com/01a0d868-1ad7-7833-8c1b-1e66c9e135ef/image.png)
![image.png](https://cdn.hackclub.com/01a0d868-3974-7ea0-926a-96e77c0a631b/image.png)
![image.png](https://cdn.hackclub.com/01a0d868-739f-7056-b53f-13eb5fd5c95f/image.png)

# 2026-09-25: September 20, 2026: Improvising the PCB

**Total time spent: 2hr 19min**


 So I spent the next 10-15ins on researching about the communications between two RP2040-zero's via UART, and if it could be used has an extension port ?

### Why ?
 Well cuz, I decided on building a small cute wired/wireless macropad which could be directly connected to this keyboard, so that i don't need a bunch of cables or a dongle to connect various accessories &lt;3: 

### MODs


- Do to the recent modifications, that's a 4pin (5v, D+, D-, GND) (UART), I can now connect another keeb or macropad or anything else via this UART extension without the need of an extra port or dongle.

- I also added a extrude for the USB C breakout board with slightly leaning towards the left of the keyboard. 

- Also due to constraint of avaliable GPIO pins, i resorted to using the GPIO 0 &amp; 1 for UART and shifted the ROW 1 &amp; 2 to the unsoldered GPIO pin which can be accessed on the back of the PCB.

### Result
![image.png](https://cdn.hackclub.com/01a0d865-b0e8-704e-bc93-6c5f5269c873/image.png)

![image.png](https://cdn.hackclub.com/01a0d865-ccf3-7598-8ab1-344ce9c3436f/image.png)

# 2026-09-25: September 18, 2026: CADDING: Bottom Case

**Total time spent: 3hr 47min**


## Designing the Case

Designing the case was probably the **most challenging and brainstorming-heavy** part of building this keyboard. It wasn’t my first time working on something like this, but it still took a lot of thinking.
***
I spent about **half an hour researching DIY custom keyboard cases** to understand how different designs work. One thing I quickly noticed was how **expensive many custom keyboard cases are**, which made me even more motivated to design my own.

Eventually, I settled on the style I wanted: **minimalistic, clean, and professional**. I added a few **fillets and curved edges** to make the case look softer and more aesthetic instead of just a plain rectangular box.

I started by designing the **bottom case** first. One important thing I considered was clearance for the electronics. I left around **2 mm of space under the PCB** to accommodate the **through-hole solder joints** from the switches, along with a thin layer of **foam** between the PCB and the case for cushioning and sound dampening.

![image.png](https://cdn.hackclub.com/01a0d863-7de5-71ce-9eda-960cf5822309/image.png)

![image.png](https://cdn.hackclub.com/01a0d863-9ebf-7552-903b-9918ee767897/image.png)

![image.png](https://cdn.hackclub.com/01a0d863-c7e7-773a-aa95-9ae64f473b3c/image.png)

Software:  Onshape
***
Happy Cadding !!!

# 2026-09-25: September 15, 2026: PCB Designing

**Total time spent: 4 hr**

After finishing the schematic, I moved on to designing the PCB in **KiCad**. This part was a bit more challenging because I wanted the keyboard to stay compact while still looking *clean* and *ergonomic*.

The first step was placing all the *Cherry MX switch* footprints in the proper **60% layout**. Once the switches were aligned, I started thinking about the overall board shape. Instead of keeping the edges completely straight, I experimented with slightly curved outlines to give the PCB a more cute and soft aesthetic rather than a rigid rectangular look.

One of the trickier parts was figuring out where to place the MCU. Since I’m using the *RP2040-Zero*, its small size actually helped a lot. After trying a few different placements, I realized it could fit nicely in the empty space to the left of the 6.25u spacebar. That spot had just enough room for the board while keeping the layout clean and avoiding interference with switches and stabilizers.

Keeping everything compact without making the routing messy took some trial and error. I had to carefully arrange the diodes and traces so the matrix stayed organized while still fitting within the board’s shape.

Once the main components were placed, I began routing the traces for the matrix and connecting everything back to the MCU. After routing, I ran a few DRC checks in KiCad again to make sure there were no clearance or connectivity issues.

![image.png](https://cdn.hackclub.com/01a0d862-3cf7-7ae1-8884-427ccffe8b00/image.png)

![image.png](https://cdn.hackclub.com/01a0d862-62cf-7531-95f7-102afa94ffaf/image.png)

# 2026-09-25: September 12, 2026: Sketched the Schematic

**Total time spent: 2 hr**

After doing some research and installing the footprints for the Cherry MX switches and the RP2040-Zero, I started working on the schematic for the 60% mechanical keyboard.

It took me about an hour to sketch out the full schematic. I connected all the switches in a matrix and added the required diodes for proper key scanning. After the main circuit was done, I organized everything to make the schematic easier to read by grouping components into sections like the Matrix grid, MCU, stabilized keys, and the status LEDs.

Once everything looked good, I reviewed the schematic to check for mistakes. I also ran a few DRC (Design Rule Checks) in KiCad and fixed the small issues that popped up. After that, the schematic was clean and ready for the PCB layout stage.

![image.png](https://cdn.hackclub.com/01a0d860-bee8-7c38-a9e8-80ac700eeb5f/image.png)
![image.png](https://cdn.hackclub.com/01a0d860-f874-7962-897f-4a0b985c0102/image.png)

# 2026-09-25: September 7, 2026: Planning the layout

**Total time spent: 45 min**

I spent around 25 minutes thinking about the keyboard layout because I wanted it to be **lightweight**, **portable**, and **efficient** in terms of usability.

For the next 20 minutes, I looked at different keyboards available in the market to find a design that had a *clean outer look*, *compact form factor*, and *good overall layout*.

After finalizing the layout and the outer case design, I drew a rough sketch of the keyboard matrix.

Based on the number of GPIO pins required, I started looking at different MCUs — from Arduinos to Raspberry Pi boards to Waveshare modules — and eventually decided to go with the ***RP2040-Zero***.

***

![image.png](https://cdn.hackclub.com/01a0d85f-30da-7a88-a410-5c51fc729e06/image.png)
![image.png](https://cdn.hackclub.com/01a0d85f-8d7c-79d7-a069-af25f758f011/image.png)

60% Mechanical Keyboard ANSI layout


