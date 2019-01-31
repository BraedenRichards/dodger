# Dodger

## Purpose
Created as a short project to get a basic understanding of Pygame and decide if it's a library I wanted to use for future projects. This project has its fair share of issues, as described under the 'Important Notes' section down below. 

Dodger is a basic dodging game where the player is a cube that must dodge other cubes moving across the screen from right to left. As the score rises, so does the speed of the incoming 'projectile' cubes. To keep the same density of projectiles, the frequency that the cubes are created increases proportionately to the speed.

## Controls
```
w - move up
s - move down
a - move left
d - move right
```

## Important Notes
This program is more of a testing of the Pygame library more than anything else. Therefore, measures were not put into place to ensure consistent gameplay between different computers/operating systems/etc. This was intended to only run on the computer that it was created on, which is a late 2016 Macbook Pro 13. On faster computers the game runs at a much faster rate, and on slower computers the game slows down tremendoulsy.

I would like to add framecaps, proper timing, etc. in the future, but as this program was never meant to be more than a testing of Pygame it is solely dependent on free time and the priorities of future me. 

## Requirements
```
Python3
Pygame
```

## To Do
Refactoring, proper timing (taking advantage of dt in the movements and whatnot), better commenting, optimizations.
