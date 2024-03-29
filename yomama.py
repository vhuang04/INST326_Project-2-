import random
from tkinter import * # see note below
import tkinter as tk

suits = ["Hearts", "Diamonds", "Spades","Clubs"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
card_values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

# creates a custom button that inherits all the features of a tk.Button() and adds card attributes
class Cardbutton(tk.Button):
    def __init__(self, master=None, suit=None, rank=None, value=None): # the arguments on this line are inbound, meaning we pass them when we instantiate the object
        super().__init__(master) # on this line we call the __init__ method of tk.Button and pass the master attribute to it. This gives us all the button attributes and functionality
        self.config(bg = 'green')

        # the rest of the attributes in the main __init__ method are card attributes from our former card class
        self.suit = suit
        self.rank = rank # face rank of the card
        self.value = value # integer value of the card
        self.name = f"{rank}_of_{suit}"
        self.face = f"images/{rank} of {suit}.png" # relative address
        self.back = "images/BackOfCard.png"  # relative address
        self.suit_val = suits.index(suit)
        self.facetk = tk.PhotoImage(file = self.face) # calls the tk.PhotoImage method which creates an image object
        self.backtk = tk.PhotoImage(file = self.back)
        self.display = self.facetk # sets the default display
        self.hand = None # an attribute that allows cards to be assigned to specific hands


        # Bind mouse events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    def on_hover(self, event): # change the background and card image when the cursor hovers over it
        self.config(bg="lightblue")  

    def on_leave(self, event): # change back when not hovering
        self.config(bg="green", image=self.display)  # Restore original color
 
    def ace_toggle(self): # toggle the value of an ace
        if self.rank == 'ace':
            if self.value == 11:
                self.value = 1
            else:
                self.value = 11

### Step 2 ###
class game(): 
    
    
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.player_score = 0 
        self.dealer_score =0
        
    def make_deck(self):
        
        for suit in suits:
            for rank in ranks:
                the_card = Cardbutton(suit=suit, rank=rank, value=card_values[ranks.index(rank)])
                self.deck.append(the_card)
        random.shuffle(self.deck)
        return self.deck
    
    def deal(self):
        self.player_hand.append(self.deck.pop())
        self.player_hand.append(self.deck.pop())
        
        self.dealer_hand.append(self.deck.pop())
        self.dealer_hand.append(self.deck.pop())
        self.dealer_hand[1].display = self.dealer_hand[1].backtk
        
    def score(self):
        self.dealer_score = 0
        self.player_score = 0
        for card in self.player_hand:
            self.player_score += card.value
        for card in self.dealer_hand:
            self.dealer_score += card.value

    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.score()
        
    def stay(self):
        while(self.dealer_score < 17):
            self.dealer_hand.append(self.deck.pop())
            self.score()
  
    def display_dealer_cards(self):
        for card in self.dealer_hand: 
            card.display = card.facetk
    
    
 ### STEP 1 ###
window = Tk() 
window.title("Project 01: BlackJack Game")
window.geometry('1000x800')
window.config(bg='green')


### STEP 2 ###
mygame = game()

### STEP 3 ###
mydeck = mygame.make_deck()

### STEP 4 ###
mygame.deal()

mygame.score()

### STEP 7 ###
name1 = Label(window,
              text="Dealer's Hand \n Score:",
              font=('Gill Sans', 20),
              fg='red',
              bg= '#FFFFFF')
name1.grid(padx=20, pady=20,row= 2, column= 0)


def display_dealer_cards():
    for i in range(len(mygame.dealer_hand)):
        mygame.dealer_hand[i].grid(padx=20,pady=20,row=2, column=i+1)
def display_player_cards():
    for i in range(len(mygame.player_hand)):
        mygame.player_hand[i].grid(padx=20,pady=20,row=1, column=i+1)
name2 = Label(window,text=f"Player's Hand \n Score: {mygame.player_score}",
              font=("Gill Sans", 20),
              fg='red', 
              bg= '#FFFFFF')

name2.grid(padx=20, pady=20,row=1, column=0)

display_dealer_cards()
display_player_cards()

### STEP 8 ###
def hit(): 
    mygame.hit()
    name2.config(text=f"Player's Hand \n Score: {mygame.player_score}")
    display_player_cards()
freaking_hit_me = tk.Button(window, text = "Hit Me", command= hit , font=("Gill Sans",20),fg='red', bg= '#FFFFFF')
freaking_hit_me.grid(padx=20, pady=20, row=3, column=0)


#Stay Function
def stay():
    mygame.stay()
    display_dealer_cards()
stay_btn = tk.Button(window, text = "Stay", command= stay, font=("Gill Sans",20),fg='red', bg= '#FFFFFF')
stay_btn.grid(padx=20,pady=20,row=3, column=1)

#Call Function
def call():
    p = mygame.player_score
    d = mygame.dealer_score
    mygame.score()
    name2.config(text=f"Player's Hand \n Score: {mygame.player_score}")
    name1.config(text=f"Dealer's Hand \n Score: {mygame.dealer_score}")
    mygame.display_dealer_cards()
    if d > 21 and p > 21:
        return
    elif p <= 21 and d < p:
        Label(window,text="Winner, Winner, Chicken Dinner!", font=("Gill Sans",20),fg='red', bg= '#FFFFFF').grid(row=4,column=0,padx=20,pady=20)
    elif d == p:
        return
    else:
        Label(window,text="House Wins", font=("Gill Sans",20),fg='red', bg= '#FFFFFF').grid(row=4,column=0,padx=20,pady=20)
    
call_btn = tk.Button(window, text="Call", command= call, font=("Gill Sans",20),fg='red', bg= '#FFFFFF')
call_btn.grid(padx=20,pady=20,row=3, column=2)

#Quit Function
def quit():
    window.destroy()
    
quit_btn = tk.Button(window, text = 'Quit',command=quit,font=("Gill Sans",20),fg='red', bg= '#FFFFFF')
quit_btn.grid(padx=20,pady=20,row=3, column=3)


window.mainloop()