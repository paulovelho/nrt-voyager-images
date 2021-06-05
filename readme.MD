# Voyager image converter



#### based on
https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html



#### content available
https://drive.google.com/drive/folders/0B0Swx_1rwA6XcFFLc29ncFJSZmM

You can find the .wav from the disc on the drive


#### Audacity
for Linux

```
sudo add-apt-repository ppa:ubuntuhandbook1/audacity
sudo apt update
sudo apt install audacity
```




## building:

for development this can be dockerized to `localhost.com`
`docker-compose --verbose-up`




## python run:
```
python voyager.py [file] [time] [start] [end]
```

example:
```
python3 voyager.py circle.txt 5971 120 4541

python3 voyager.py img2.txt 5901 163 5000
python3 voyager.py img3.txt 5726 128 4940
```
