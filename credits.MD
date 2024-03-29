# Voyager image converter


## developed by
Paulo Henrique Martins  
[@paulovelho](https://twitter.com/paulovelho)

#### with a HUGE help of
Luiz Carlos Vieira [@luigivieira](https://github.com/luigivieira)  
...and Ron Barry  

## based on
[https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html](https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html)
by Ron Barry

### content available
[https://drive.google.com/drive/folders/0B0Swx_1rwA6XcFFLc29ncFJSZmM](https://drive.google.com/drive/folders/0B0Swx_1rwA6XcFFLc29ncFJSZmM)  
Ron Barry kindly let available all the images and the raw wav file in high quality.  
I can't imagine who he had to bribe to get access to that wav but I only could build this because he has done this job before.   
You can find the .wav from the disc on the drive.  


## Setup:
### Wav examined and trimmed with Audacity
installation for Linux:
```
sudo add-apt-repository ppa:ubuntuhandbook1/audacity
sudo apt update
sudo apt install audacity
```

### code built in python 3
packages used:
- numpy
- pprint
- scipy.io
- math
- matplotlib


## Thank You!
First to Luiz Carlos Vieira. Without him, I would not be able to make this. Thanks, Luiz, you were of a huge help and support.

Also Galvão Chucruts - that I will always thank in any nRT project.


## TO DO:
### Right channel images
I am not really good using Audacity, so I could only export wavs from the left channel of the sound file.  
I know. Shame on me. This might be a really simple thing to do, but I am not that smart despite of what you might think for what I achieved in this repo. It was mostly lucky, believe me.

### Improve code quality
Once my ignorance is already exposed, let's play it real: Probably it was not the best solution.  
Some images are barely visible and some couldn't be extracted at all.  
Everyone is invited to find new and better solutions that capture the image using better wave points.

### Colored images
There are colored images hidden in the middle of the code.  
Those can be obtained by mixing three images from three different waves, but I will be terribly honest and admit that I don't understand how to do it.

### amplitude x decibels
The wave is being captured and analyized as the default measurement system from the `scipy.io` package: amplitude.  
I believe that if we get the wave with the points in decibels values, I can improve the alghoritm and the final quality of the images.

