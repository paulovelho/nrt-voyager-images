# Voyager image converter


## Introduction

In 1977 NASA send two probes to space: Voyagers 1 and 2.
Both were destinated to leave the solar system and reach the unknown.

NASA asked Carl Sagan to create a message from Earth for whatever or whoever get it. Sagan built a golden disc with some Earthian music such as Beethoven and Johnny B. Goode and sent some images encoded as sounds.

The cover of the disc is an auxiliar message, to help to decode the hidden images inside it:

![alt text](./images/voayager-disc.png "Voyager disc")

Well, it seems tough. Let's find out how to get those images out of here.

## Diving in
My first idea was to build something in Javascript. As this project's goal was not only to extract images for myself but to create a visual demonstration of how this process work, I imagined that I could do this whole process via browser - or at least simulating it in a browser.

Oh god, how naïve!

Supposing that each image has 512 pixels width and 384 pixels height, this would be 196.608 to manage individually. That means I would have to iterate and manipulate an array of around 200.000 items. That would be not viable at all for running inside a browser.

At least I was smart enough to give up this idea quickly.

So, I would need another programming language. Something that would deal good with huge lists of numbers, something that could easily plot images and something light enough to run from any terminal (because I'm too lazy to create an interface, despite my ambicious plans).

I chose `python`. Only because I believed it would satisfy all the requirements, because, honestly, I never had touched any python project that worthed mentioning, so this would be the first.

Hands on!



