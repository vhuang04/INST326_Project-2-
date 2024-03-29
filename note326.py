import random 
from tkinter import *


window = Tk() 

#class code 
class Cardbutton(tk.Button):
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value 
        self.name = f'{rank} of {suit}' 
        self.face = f'/Users/vanessahuang/Documents/inst326/images/{rank} of {suit}.png'
        self.back = '/Users/vanessahuang/Documents/inst326/images/BackOfCard.png'
        self.state = False 
        self.suit_val = suits.index(suit)
        
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
    
    def facedown(self): 
        self.state = False
        img_file = self.back
        img_out=PhotoImage(file=img_file)
        return img_out

    def faceup(self):
        self.state =True
        img_file = self.face
        img_out = PhotoImage(file=img_file)
        return img_out
    

 

    def on_hover(self, event): # change the background and card image when the cursor hovers over it
        self.config(bg="lightblue")  

    def on_leave(self, event): # change back when not hovering
        self.config(bg="green", image=self.display)  # Restore original color
 
    def ace_toggle(self): # toggle the value of an ace
        if self.rank == 'Ace':
            if self.value == 11:
                self.value = 1
            else:
                self.value = 11

#game class
class game(): 
    uits = ["Hearts", "Diamonds", "Spades","Clubs"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
    card_values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    
    def __init__(self):
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        
    def make_deck(self):
        for suit in suits:
            for rank in ranks:
                the_card = card(suit, rank, card_values[ranks.index(rank)])
                self.deck.append(the_card)
        random.shuffle(self.deck)
        return self.deck
    
    def deal(self):
        
    def stay(self):
    def hit(self):
            
    
#where the logic of the game starts 


#card variables 
suits = ["Hearts", "Diamonds", "Spades","Clubs"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King','Ace']
card_values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

#shuffling the deck 
def deck (suits = suits, ranks = ranks, card_values = card_values):
    deck_of_cards = []
    for suit in suits:
        for rank in ranks:
            the_card = Cardbutton(suit, rank, card_values[ranks.index(rank)])
            deck_of_cards.append(the_card)
    return deck_of_cards
mydeck = deck()
random.shuffle(mydeck)
mycard = mydeck.pop()

print(mydeck)

def dealer(): 
    card_1 = mydeck.pop()
    card_2 = mydeck.pop()
    return [card_1, card_2]
dealer_hand = dealer()
print(dealer_hand)

def player():
    card_1 = mydeck.pop()
    card_2 = mydeck.pop()
    return [card_1, card_2]
player_hand = player()
print(player_hand)  

# def score(hand):
#     value = sum(card['value'] for card in hand)
#     for card in hand:
#         if card['rank']=='Ace' and value > 21:
#             value=- 10 
#         return value
# def blackjack_game():
#      while True:
#          if score(player)>21:
#             dealer_wins = Label(window,
#                                 text="You bust! Dealer wins!",
#                                 font=('Gill Sans', 20),
#                                 fg='red',
#                                 bg= '#FFFFFF')
#             break 
        
        


# the browser               


window.title("Project 01: BlackJack Game")
window.geometry('1000x800')
window.config(bg='green')
frames = Frame(window,bg ='white', bd=5)
frames.pack(pady = 50)
labels = Label(frames,
               text = "BlackJack Game",
               background = "#fcba03",
               fg = '#FFFFFF',
               font = ("Gill Sans", "20"),
               wraplength=200)
labels.pack() 


backOfCard = PhotoImage(file='/Users/vanessahuang/Documents/inst326/images/BackOfCard.png')



name1 = Label(window,
              text="Dealer's Hand \n Score:",
              font=('Gill Sans', 20),
              fg='red',
              bg= '#FFFFFF')
name1.pack()
topButtonsFrame = Frame(window)
topButtonsFrame.pack()

dealer1 = dealer_hand[0].faceup()
dealer2 = dealer_hand[1].facedown()

cardButton1 = Button(topButtonsFrame, image= dealer2, bd = 0 )
cardButton2 = Button(topButtonsFrame, image= dealer1, bd = 0 )
cardButton1.grid(row=1, column=0)
cardButton2.grid(row=1, column=1)

name2 = Label(window,text="Player's Hand \n Score:",font=("Gill Sans", 20),fg='red')
name2.pack()

bottomButtonsFrame = Frame(window)
bottomButtonsFrame.pack()
player1 = player_hand[0].faceup()
player2 = player_hand[1].faceup()

cardButton3 = Button(bottomButtonsFrame, image= player1, bd = 0 )
cardButton4 = Button(bottomButtonsFrame, image= player2, bd = 0 )




cardButton3.grid(row=1, column=0)
cardButton4.grid(row=1, column=1)

#buttons on the websites and their functions 

buttonframe = Frame(window)
def stay():
    dealer_card_1 = dealer_hand[1].faceup()
    cardButton1 = Button(topButtonsFrame, image= dealer_card_1, bd = 0 )
    cardButton1.grid(row=1,column=0)
    
        
stay_card = Button(bottomButtonsFrame, text = "Stay", command= stay, font=("Gill Sans",20),fg='red', bg= '#FFFFFF').grid(row=5,column=0)



def hit_me(): 
    player_hand.append(mydeck.pop())
 
    
    for the_card in player_hand: 
        hit_player_card_img = PhotoImage(file=the_card.face)
        hit_me_card = Button(bottomButtonsFrame, image=hit_player_card_img,bd=0)
        hit_me_card.photo = hit_player_card_img 
        hit_me_card.grid(row=1, column=len(player_hand)-1)
        
        
        
freaking_hit_me = Button(bottomButtonsFrame, text = "Hit Me", command= hit_me , font=("Gill Sans",20),fg='red', bg= '#FFFFFF').grid(row=5, column=1)

def quit():
    window.destroy()
    
quit_button = tk.Button(bottomButtonsFrame, text = 'Quit',command=quit,font=("Gill Sans",20),fg='red', bg= '#FFFFFF')
quit_button.grid(row=5,column= 2 )

def score(hand):
    total = 0
    for card in hand:
        total += card.value 
    name1.config(text=f"Dealer's Hand \n Score:{total}")


                

window.mainloop()




