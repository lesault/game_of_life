# game_of_life
 Playing with Conway's Game of Life and sha256

Trying to implement the 4 rules of Conway's Game of Life to help me understand working with lists of lists.

Challenges were counting the number of live cells bordering each cell - if the cell is at the edge of the
canvas then cells 'off the edge' shouldn't be counted.

I wanted to stop updating the canvas once the pattern stabilised so I used that as an opportunity to
play with a sha256 hash - totally overkill for this!

Next steps might be to display the canvas differently - a QT maybe? Curses? who knows!