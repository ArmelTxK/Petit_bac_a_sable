from tkinter import *
from random import *


class App(Frame):
    def __init__(self, master=None):
        self.largeur, self.hauteur = 400, 550
        Frame.__init__(self, master, width=self.largeur, height=self.hauteur, bg="white")
        self.pack()
        
        self.screen = Canvas(self, width=self.largeur - 50, height=self.hauteur - 50, bg="black")
        self.screen.pack(padx=5, pady=5)
        self.screen.bind("<Button-1>", self.changecol)
        
        self.cell_size = 10
        self.grid = []
        for x in range(0, self.largeur - 50, self.cell_size):
            row = []
            for y in range(0, self.hauteur - 50, self.cell_size):
                rect = self.screen.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, outline="white", fill="black")
                row.append(rect)
            self.grid.append(row)

        self.reset_button = Button(self, text="Reset", command=self.reset_grid)
        self.reset_button.pack(pady=5)

        self.animating_elements = set()  
        
    def changecol(self, event):
        eventx, eventy = event.x, event.y
        element = self.screen.find_closest(eventx, eventy)[0]  
        
        # Vérifier si l'élément est déjà en animation
        if element not in self.animating_elements:
            self.animating_elements.add(element)
            self.screen.itemconfig(element, fill="white")
            self.animation(element)  
            print(eventx, eventy)
        
    def animation(self, element):
        # Obtenir les coordonnées de l'élément cliqué
        coords = self.screen.coords(element)
        x1, y1, x2, y2 = coords
        below_y_coord = y1 + self.cell_size

        if below_y_coord < (self.screen.winfo_height() - 10):
            # pour trouver l'élement en dessous
            below_y = self.screen.find_closest((x1 + x2) / 2, below_y_coord)[0]
            below_coords = self.screen.coords(below_y)

            # Vérifiez si le carré en dessous existe et n'est pas déjà colorié
            if below_coords and self.screen.itemcget(below_y, 'fill') == 'black':  
                self.screen.itemconfig(element, fill="black")
                self.screen.itemconfig(below_y, fill="white")
                self.animating_elements.remove(element)
                self.animating_elements.add(below_y)
                self.screen.after(100, lambda: self.animation(below_y))

            else:
                # Si en bas il y'a déja un carré coloré, essayer d'aller à gauche ou à droite
                left_x1 = x1 - self.cell_size
                right_x2 = x2 + self.cell_size
                
                direct = randrange(1,3,1) #choix aléatoire de la direction a prendre 
                print(direct)
                if direct ==1:
                    # vérifier si c'est possible d'aller a gauche et se deplacer vers la gauche
                    if left_x1 >= 0:
                        left_element = self.screen.find_closest((left_x1 + x1) / 2, (y1 + y2) / 2)[0]
                        if self.screen.itemcget(left_element, 'fill') == 'black':  
                            self.screen.itemconfig(element, fill="black")
                            self.screen.itemconfig(left_element, fill="white")
                            self.animating_elements.add(left_element)
                            self.animating_elements.remove(element)
                            self.screen.after(100, lambda: self.animation(left_element))
                            return
                elif direct == 2 :
                    # Vérifier si c'est possible d'aller a droite et aller a droite
                    if right_x2 < self.screen.winfo_width():
                        right_element = self.screen.find_closest((x2 + right_x2) / 2, (y1 + y2) / 2)[0]
                        if self.screen.itemcget(right_element, 'fill') == 'black':
                            self.screen.itemconfig(element, fill="black")
                            self.screen.itemconfig(right_element, fill="white")
                            self.animating_elements.add(right_element)
                            self.animating_elements.remove(element)
                            self.screen.after(100, lambda: self.animation(right_element))
                            return
                
                # Si aucun mouvement possible, terminer
                self.animating_elements.remove(element)
     
                 
    def reset_grid(self):
        # Réinitialiser tous les rectangles à noir et vider les éléments en cours d'animation
        for row in self.grid:
            for rect in row:
                self.screen.itemconfig(rect, fill="black")
        self.animating_elements.clear()

if __name__ == "__main__":
    app = App()
    app.mainloop()
