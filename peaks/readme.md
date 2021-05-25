# generate Peaks

Amazing as it is, wavesurfer still has some issues to generate peaks inside google chrome.
So we cheat: we pre-render peaks and send to the application an mp3 file and an array with peaks


to do so, we use audiowaveform to generate peaks:
[https://github.com/bbc/audiowaveform](https://github.com/bbc/audiowaveform)


```
audiowaveform -i audios/v1-1.mp3 -o peaks/v1-1.json --pixels-per-second 20 --bits 8
```

and the result is scalable via a simple python script:
``` 
python peaks/scale-json.py peaks/v1-1.json
```



### based:
https://boingboing.net/2017/09/05/how-to-decode-the-images-on-th.html




