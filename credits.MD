# Voyager image converter


## developed by
Paulo Henrique Martins
@paulovelho

#### with a HUGE help of
Luiz Carlos Vieira
Ron Barry

## based on
https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html
by Ron Barry

### content available
https://drive.google.com/drive/folders/0B0Swx_1rwA6XcFFLc29ncFJSZmM
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


## To Do:
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
