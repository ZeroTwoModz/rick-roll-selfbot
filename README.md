it may slowdown becuz of rate limit XD

also self botting is against the tos so gl lol

i made this shit long time ago so dont expect much

# IMPORTANT (FRAMES)

DOWNLOAD FRAMES:

https://mega.nz/file/7ewmlYiK#tKX5v8nw9PTd8fPH18XLCmkwdmhXpik_XA0y2pUnd0U

but if this doesn't work anymore extract it by urself (follow steps below)


EXTRACTING FRAMES BY URSELF:

First go to this link: https://www.gyan.dev/ffmpeg/builds/

scroll down to `release builds` and install `ffmpeg-release-essentials.7z`

then, clone/download this repo (link: https://github.com/ZeroTwoModz/rick-roll-selfbot)

make folder `frames` in `rick-roll-selfbot`

after you made folder and downloaded build/repo, open `ffmpeg-release-essentials.7z` click `bin` and move ffmpeg to `frames` which you created couple seconds ago

Now, download video of Never Gonna Give You Up (https://www.youtube.com/watch?v=dQw4w9WgXcQ) from youtube downloaders like https://yt1s.com/en25

When you are done downloading it, move mp4 file to frames folder

rename `never gonna give you up`/`mp4` file to `video.mp4`

Open command prompt in frames folder and type this command: `ffmpeg -i video.mp4 frame%01d.jpg -hide_banner`

wait for a bit before it finishes extracting frames

**NOW MOST IMPORTANT PART**

go to latest frame in frames folder and after `frame`, there should be a number on it, something like this: (frame**6000**.jpg), copy numbers. in my case it's **6000** **(it would be something like 1000 and more for you)** (btw it was 5301 for me but i just wanted to show you, what should you do if you have higher frames)

now go to main folder and open `rick_roll.py` with notepad, goto line 50 where it says `while i < 5301:` and change value from 4053 to number you copied in the last step, so in my case it was 6000 and i'm gonna change it like this `while i < 6000:`

after that double click on start.bat (if it doesnt work read **INSTALLATION**)

# INSTALLATION

This requires python3 to work, you can download it from microsoft store or from `https://www.python.org/downloads/`

install libraries using `pip3 install`:
```
PIL
time
json
```

change stuff in config.json and start.bat in main folder

# PREVIEW

<img src="https://cdn.upload.systems/uploads/RLjj5Uhu.gif"/>

