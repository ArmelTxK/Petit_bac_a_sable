# Petit_bac_a_sable
# petit projet de simulation de grain de sable 2d

This Python project creates a simple falling square animation using `Tkinter`. The application allows users to click on squares in a grid, causing them to fall downward based on gravity-like behavior. The squares will attempt to move down, but if blocked, they can randomly shift left or right.

## Features

- **Grid Generation**: A grid of black squares is drawn on the canvas using `Tkinter`. Each square is clickable and turns white when clicked.
- **Falling Behavior**: After a square is clicked, it begins an animation, attempting to move downward. If a square below is occupied, the current square will randomly attempt to move left or right.
- **Collision Handling**: When a square cannot move further (either due to screen boundaries or other squares), it stops.
- **Reset Button**: Users can reset the grid, turning all squares back to black and stopping all animations.

## Components

### 1. **Grid Creation**:
   The grid is generated by dividing the canvas into small square cells (`cell_size = 10`). Each cell is a rectangle drawn using the `create_rectangle` method from `Tkinter`:

   self.screen.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, outline="white", fill="black")
   

### 2. **Click Event**:
   When the user clicks on a square, the `changecol` method is called. This method identifies which square was clicked and initiates an animation for it if it's not already moving:
   self.screen.bind("<Button-1>", self.changecol)


### 3. **Animation Logic**:
   The `animation` method moves a square downward by checking if the space below is unoccupied (black). If the square can't move down (due to either a boundary or another square), it randomly tries to move left or right using `randrange`.

   - **Move Down**: The square attempts to move down into an empty space.
   - **Random Left/Right Move**: If blocked, the square randomly selects a direction (left or right) and tries to move there:   
   
   direct = randrange(1, 3, 1)  # Randomly chooses 1 (left) or 2 (right)


### 4. **Reset Grid**:
   The `reset_grid` method resets the grid, turning all squares black and stopping any ongoing animations:
   def reset_grid(self):
       for row in self.grid:
           for rect in row:
               self.screen.itemconfig(rect, fill="black")
       self.animating_elements.clear()


## How to Use

1. **Running the Application**:
   Simply run the Python script. The GUI window will open with a grid of black squares.

2. **Interacting with the Grid**:
   - Click on any black square to make it fall.
   - The square will fall vertically unless blocked by another square, in which case it will attempt to move left or right.
   - Click multiple squares to see them animate simultaneously.

3. **Reset**:
   Use the "Reset" button to clear the grid and restart the animation process.

