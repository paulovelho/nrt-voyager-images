# Voyager image converter


## Introduction

In 1977 NASA send two probes to space: Voyagers 1 and 2.
Both were destinated to leave the solar system and reach the unknown.

At the time, NASA asked Carl Sagan to create a message from Earth for whatever or whoever get it. Sagan built a golden disc with some Earthian music such as Beethoven and Johnny B. Goode and sent some images encoded as sounds.

The cover of the disc is an auxiliar message, to help to decode the hidden images inside it:

![alt text](./images/voayager-disc.png "Voyager disc")

Well, it seems tough. Let's find out how to get those images out of here.


## Diving in

My first idea was to build something in Javascript. As this project's goal was not only to extract images for myself but to create a visual demonstration of how this process work, I imagined that I could do this whole process via browser - or at least simulating it in a browser.

Oh god, how naïve!

Supposing that each image has `512` pixels width and `384` pixels height, this would be `512 * 384 = 196.608` points to manage individually. That means I would have to iterate and manipulate an array of around 200.000 items. That would be not viable at all for running inside a browser.

At least I was smart enough to give up this idea quickly.

So, I would need another programming language. Something that would deal good with huge lists of numbers, something that could easily plot images and something light enough to run from any terminal (because I'm too lazy to create an interface, despite my ambicious plans).

I chose `python`. Only because I believed it would satisfy all the requirements, despite, honestly, I never had touched any python project that worthed mentioning, so this would be the first.

Hands on!


## Viewing the sound

Ron Barry built something like this in the past and made the .wav file public available (you can find it in the [about section](credits.MD)). I owe him a lot.  
Apart from that huge 1,5GB and roughly 8 minutes wav file, I could only find soundcloud and youtube samples of the audio and, honestly: they are useless. The data on the video was too compressed to extract anything from it.

That raw .wav is also not included in this project because it's fucking 1,5GB, I don't want to push github that much.

Opening the .wav in Audacity, we can find the file:

![alt text](./images/wav_full.png "Wav File")

Do you see each one of those peaks? In every interval between them you have an image. If you are smarter than I am (and a bet you are, believe me), you will be much faster to notice that the left channel (top) and the right channel (bottom) are not synchronized: each channel have different images at different times.

Ok, let's check what the disc cover can tell us:

![alt text](./images/voyager_disc-detail.png "How to read")

The first box represents how to read the data: it should be read from top to bottom, left to right, plotting the points in the sequence it displays.  
The second image could be read as the Brazil's flag without the diamond shape, and is the closest Brazil got to really go to space. But it's the calibration image, a simple shape for alien researchers to use as base to build their algorithms.  
They don't have ways to find that out, it's honestly not too obvious.

Ok. Now I have the sound wave and I have a sample result. Let's dig deeper.


## Extracting the sample

Here it goes, a 5-second extraction from the first piece of wave of the left channel:

![alt text](./images/wav-circle.png "Circle in the wave")

Hey, look at that! You can see the circle over there. Can you see it? Are you excited? Oh boy, I was singing Disney songs and drinking beer alone all night long after I saw that (although I don't think it was related to this project).

Let's see what the disc cover has to say about that:

![alt text](./images/wav_read.png "Disc cover waves")

Ok... Does that mean I should read every three waves to build a column of pixels? That was my initial thought. But no, this would give me too few columns to make a decent image by my accounts.

Let's zoom the .wav:

![alt text](./images/wav-circle_opening.png "Circle in the wave (zoom)")

Ok, looking closely we can see that the shape between the peaks start as a single wave and splits in two... exploring further, it gets closer again after merging in a single wave once more. If we think on every column of pixels required to build a circle, we could assume that every interval between peaks can represent a column of pixels.

Let's divide the amount of time in the wav by the amount of columns and...

![alt text](./images/nothing.jpeg "Nothing!")

Shit, this does not look good.  
Time to drink whisky and cry all night long listening to Coldplay (although I don't think it was related to this project).

What if instead of a fixed time for each wave, I made a dynamic way to calculate how long each column will take. Looking back at our .wav wave, we can, maybe, count the points between every deep valley and every top peak and plot the points in between.

![alt text](./images/almost.jpeg "Almost!")

Great!  
I mean, not great, but look there, you can kind of see the circle if you get drunk in the same syntony.

I used a value for the alghoritm to find out when a wave is in its peak and another value for the alghoritm to find out when it reached the bottom (no, it's not smart enough to find it by itself). Tweaking a little bit there and back and...

![alt text](./images/circle-1.jpeg "The circle")

YES! I am a genius!  
Look at that! an almost-perfect egg. I am so excited that I post it to Instagram, can you believe how excited this is?

Do you see that the egg ends abruptly? Well.. the reason for that is because I am exporting the points from the wav using Audacity and the application only allows me to plot the first million points in a .txt. A million points for a sound wave is a hell lot of things for any 3 minute-music, but not much when you are trying to build an image plotting out the points of every 9 milisseconds wave in an y-axis.

Shit!
Well, Let's take a look what we have here in the second piece of audio.  
Pure gibberish.

I got the calibration image but failed to get everything else.  
Will aliens face this same issue when finding the voyager?







## Using the script
[list of available commands](commands.MD)



## About and setup
I have a lot to thank during the small period of time that I worked with this.  
[Thank you, everyone!](credits.MD)




