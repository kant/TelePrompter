# TelePrompter

This is an adaptation of https://github.com/poly451/Tutorials/tree/master/Teleprompter, see also Youtube for Chris's explanation: https://www.youtube.com/watch?v=mkjdlgIwEtc

# Added:
- New filtering of characters, adapted for languages that use umlaut, grave, circumflex and other special characters.
- Different foreground (yellow) and background color (black).
- Borderless window
- Added a OpenFileDialog (using tkinter)
- Prevent program from loading anyhting other than .txt
- Setup new controls

# Controls:
- 1 slow scroll speed
- 2 medium scroll speed
- 3 fast scroll speed
- q pause/start
- e return to top of txt
- w change direction
- s change direction
- a slow down
- d speed up

# Usage
```
pip install pygame
```
Setup a virtual env
```
python -m venv venv
```
Start the virtual environment
```
venv\Scripts\activate
```
Run main.py
```
python main.py
```
Then open a txt (there is an example text file in /data/scripts)
Txt will open in pause mode in a borderless window.

# Important for use:
Position on screen can be changed by changing x and y in myclasses.py. Try to get it as close as possible to your webcam, this way the viewer has the idea you are looking at him or her. Also: keep the screen-width as small as possible (can be changed by self.width in StrangeTelePrompter Class in myclasses.py), that way your eye movement is minimized: the viewer won't see your eyes moving from right to left while you're reading from the screen. If you want to change the width, other important values are font-size (self.font_size) and number of characters per line (self.line_length)
