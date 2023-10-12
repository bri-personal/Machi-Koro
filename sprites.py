import pygame
import random
from settings import *
from cards import *
from os import path

#show text on surface with parameters given
def draw_text(surface,text,size,color,x,y,orientation):
    font=pygame.font.Font(pygame.font.match_font(FONT_NAME),size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    if orientation=='topleft':
        text_rect.topleft=(x,y)
    elif orientation=='midtop':
        text_rect.midtop=(x,y)
    elif orientation=='center':
        text_rect.center=(x,y)
    surface.blit(text_surface,text_rect)

#holds game data for cards, money, etc. for each player
class Player():
    def __init__(self,game,is_player):
        self.game=game
        self.card_sprites=pygame.sprite.Group()
        self.card_sprites_list=[] #only property card sprites
        self.is_player=is_player
        
        self.properties_all={"Bakery":0,
                             "General Store":0,
                             "Convenience Store":0,
                             "Flower Shop":0,
                             "Demolition Company":0,
                             "Loan Office":0,
                             
                             "Wheat Field":0,
                             "Ranch":0,
                             "Corn Field":0,
                             "Flower Garden":0,
                             "Forest":0,
                             
                             "Cafe":0,
                             "Sushi Bar":0,
                             "French Restaurant":0,
                             
                             
                             "Cheese Factory":0,
                             "Furniture Factory":0,
                             "Winery":0,
                             "Soda Bottling Plant":0,
                             "Farmer's Market":0,
                             "Food Warehouse":0,
                             "Moving Company":0,
                             
                             "Vineyard":0,
                             "Mackerel Boat":0,
                             "Mine":0,
                             "Apple Orchard":0,
                             "Tuna Boat":0,
                             
                             "Pizza Joint":0,
                             "Hamburger Stand":0,
                             "Family Restaurant":0,
                             "Private Club":0,
                             
                             
                             "TV Station":0,
                             "Stadium":0,
                             "Business Center":0,
                             "Publisher":0,
                             "Renovation Company":0,
                             "Tax Office":0,
                             "Tech Startup":0,
                             "Exhibit Hall":0,
                             "Park":0
                            }
        
        self.properties_16={ "Bakery":0,
                             "General Store":0,
                             "Convenience Store":0,
                             "Flower Shop":0,
                             "Demolition Company":0,
                             "Loan Office":0,
                             
                             "Wheat Field":0,
                             "Ranch":0,
                             "Corn Field":0,
                             "Flower Garden":0,
                             "Forest":0,
                             
                             "Cafe":0,
                             "Sushi Bar":0,
                             "French Restaurant":0
                           }
        
        self.properties_714={"Cheese Factory":0,
                             "Furniture Factory":0,
                             "Winery":0,
                             "Soda Bottling Plant":0,
                             "Farmer's Market":0,
                             "Food Warehouse":0,
                             "Moving Company":0,
                             
                             "Vineyard":0,
                             "Mackerel Boat":0,
                             "Mine":0,
                             "Apple Orchard":0,
                             "Tuna Boat":0,
                             
                             "Pizza Joint":0,
                             "Hamburger Stand":0,
                             "Family Restaurant":0,
                             "Private Club":0,
                            }
        
        self.properties_purple={"TV Station":0,
                                "Stadium":0,
                                "Business Center":0,
                                "Publisher":0,
                                "Renovation Company":0,
                                "Tax Office":0,
                                "Tech Startup":0,
                                "Exhibit Hall":0,
                                "Park":0
                               }
        
        if self.is_player: #should False if object is Market
            self.player_init()
        
    #things to initialize only if this is a Player, not a Market
    def player_init(self):
        #set up inactive landmarks
        self.landmarks_active=0 #counts number of active landmarks for cards that depend on it, 0 b/c city hall doesn't count
        self.landmarks=[]
        for i in range(len(list(LANDMARKS))):
            self.landmarks.append(LandmarkCard(list(LANDMARKS)[i]))
            self.card_sprites.add(CardSprite(self.game,self,BORDER+(CARD_WIDTH+BORDER_BTW)*i,BORDER,self.landmarks[i]))
            
        #activate landmarks for testing/debugging only
#         self.landmarks[0].active=True
#         self.landmarks[1].active=True
#         self.landmarks[2].active=True
#         self.landmarks[3].active=True
#         self.landmarks[4].active=True
#         self.landmarks[5].active=True
        
        for landmark in self.landmarks[0:6]: #not including city hall (index 6) b/c not technically landmark
            if landmark.active:
                self.landmarks_active+=1
        
        #city hall starts activated
        self.landmarks[6].active=True
        
        #set initial position of cards
        self.next_property_x=BORDER
        self.next_property_y=BORDER*2+CARD_HEIGHT
        
        #add starting properties and money
        self.num_properties=0 #counts total properties (not landmarks) owned
        self.add_property(PropertyCard("Wheat Field"))
        self.add_property(PropertyCard("Bakery"))
        
#         self.add_property(PropertyCard("Ranch"))
#         self.add_property(PropertyCard("Forest"))
#         
#         self.add_property(PropertyCard("Moving Company"))
#         
#         self.add_property(PropertyCard("Cafe"))
#         
#         self.add_property(PropertyCard("Mackerel Boat"))
#         
#         self.add_property(PropertyCard("Cheese Factory"))
#         self.add_property(PropertyCard("Farmer's Market"))

#         self.add_property(PropertyCard("Business Center"))
        
        self.money=3 #should be 3
        self.tech_startup_money=0 #money stored in tech startup, starts at 0
        
    #add new property (and corresponding sprite if applicable) to this Player's inventory
    def add_property(self,card): #card is a PropertyCard
        if self.is_player and card.symbol!='tower': #add to total properties (not 'tower') owned if is a player, not necessary for market
            self.num_properties+=1
#             print("added "+card.name)
#             print("num_properties is now "+str(self.num_properties))
            
        self.properties_all[card.name]+=1 #increment count of this card in dictionaries
        
        if card.color==PURPLE:
            self.properties_purple[card.name]+=1 
        else:
            if card.rolls[0]<=6:
                self.properties_16[card.name]+=1
            else:
                self.properties_714[card.name]+=1
        
        if self.properties_all[card.name]<2: #if this is the first time the player gets this card...
            cs=CardSprite(self.game,self,self.next_property_x,self.next_property_y,card)
            self.card_sprites.add(cs)
            self.card_sprites_list.append(cs)
            self.next_card_pos() #add a new sprite and increment the position of the next card
        
    #increment the position where the next CardSprite will be drawn
    def next_card_pos(self):
        self.next_property_x+=CARD_WIDTH+BORDER_BTW
        if self.next_property_x>WIDTH-BORDER-CARD_WIDTH*2-BORDER_BTW:
            self.next_property_x=BORDER
            self.next_property_y+=CARD_HEIGHT+BORDER
    
    def remove_property(self,card_sprite):
        if card_sprite.card.symbol!='tower': #num_properties does not count 'tower' properties
            self.num_properties-=1 #subtract from total properties owned if is a player, not necessary for market
#             print("removed "+card_sprite.card.name)
#             print("num_properties is now "+str(self.num_properties))
        
        self.properties_all[card_sprite.card.name]-=1 #decrement count of this card in dictionaries
        
        if card_sprite.card.color==PURPLE:
            self.properties_purple[card_sprite.card.name]-=1
        else:
            if card_sprite.card.rolls[0]<=6:
                self.properties_16[card_sprite.card.name]-=1
            else:
                self.properties_714[card_sprite.card.name]-=1
                
        if self.properties_all[card_sprite.card.name]<1: #if there is no more of this card...
            x=card_sprite.rect.x
            y=card_sprite.rect.y
            self.card_sprites_list.remove(card_sprite)
            card_sprite.kill()
            for cs in self.card_sprites:
                if cs.card.type!='landmark' and (cs.rect.x>x or cs.rect.y>y):
                    cs.rect.x-=CARD_WIDTH+BORDER_BTW
                if self.next_property_x<BORDER:
                    self.next_property_x=WIDTH-BORDER
                    self.next_property_y-=CARD_HEIGHT+BORDER
                    
            self.next_property_x-=CARD_WIDTH+BORDER_BTW
            if self.next_property_x<BORDER:
                self.next_property_x=WIDTH-BORDER
                self.next_property_y-=CARD_HEIGHT+BORDER
 
            
#subclass of Player, holds the cards to be bought in the center screen
class Market(Player):
    def __init__(self,game):
        Player.__init__(self,game,False)
        
        self.next_property_x=CARD_WIDTH+BORDER+BORDER_BTW
        self.next_property_y=BORDER
        
        self.num_cards_16=0
        self.num_cards_714=0
        self.num_cards_purple=0
        
        #add starting properties of each type to market
        self.add_cards()
        
    def add_cards(self):
        if self.num_cards_16<min(len(PROPERTIES_16),5):
            while self.num_cards_16<min(len(PROPERTIES_16),5):
                name=random.choice(list(PROPERTIES_16))
                self.add_property(PropertyCard(name))
                if self.properties_16[name]<2:
                    self.num_cards_16+=1
            
            #if next card would have been cut off edge, add_property() already made a new line and set x to BORDER
            if self.next_property_x!=BORDER: #if not, a new line needs to be made for the next cards
                self.next_property_y+=CARD_HEIGHT+BORDER
            self.next_property_x=CARD_WIDTH+BORDER+BORDER_BTW #then set x to correct starting value
        
        if self.num_cards_714<min(len(PROPERTIES_714),5):
            while self.num_cards_714<min(len(PROPERTIES_714),5):
                name=random.choice(list(PROPERTIES_714))
                self.add_property(PropertyCard(name))
                if self.properties_714[name]<2:
                    self.num_cards_714+=1
                
            if self.next_property_x!=BORDER:
                self.next_property_y+=CARD_HEIGHT+BORDER
            self.next_property_x=CARD_WIDTH+BORDER+BORDER_BTW
            
        if self.num_cards_purple<min(len(PROPERTIES_PURPLE),5):
            while self.num_cards_purple<min(len(PROPERTIES_PURPLE),2):
                name=random.choice(list(PROPERTIES_PURPLE))
                self.add_property(PropertyCard(name))
                if self.properties_purple[name]<2:
                    self.num_cards_purple+=1
                
    def replace_card(self,card_sprite):
        card=card_sprite.card
        
        self.properties_all[card.name]-=1
        
        if card.color==PURPLE:
            self.properties_purple[card.name]-=1 #increment count of this card in dictionary
            
        elif card.rolls[0]<=6:
            self.properties_16[card.name]-=1
        else:
            self.properties_714[card.name]-=1
        
        if self.properties_all[card.name]<1:
            if card.color==PURPLE:
                self.num_cards_purple-=1
            elif card.rolls[0]<=6:
                self.num_cards_16-=1
            else:
                self.num_cards_714-=1
            
            self.next_property_x=card_sprite.rect.x
            self.next_property_y=card_sprite.rect.y
            
            self.add_cards()
            
            card_sprite.kill()
                
class CardSprite(pygame.sprite.Sprite):
    def __init__(self,game,player,x,y,card):
        self.game=game
        self.groups=self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.player=player
        self.card=card
        
        self.image=pygame.Surface((CARD_WIDTH,CARD_HEIGHT))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        
        self.clicked=False
        
    def update(self):
        if self.card.type=='landmark':
            if self.card.active:
                self.image.fill(GOLD)
            else:
                self.image.fill(GRAY)
        elif self.card.type=='property':
            self.image.fill(self.card.color)
            if len(self.card.rolls)>1:
                draw_text(self.image,str(self.card.rolls[0])+'-'+str(self.card.rolls[len(self.card.rolls)-1]),18,WHITE,CARD_WIDTH//2,CARD_HEIGHT//20,'midtop')
            else:
                draw_text(self.image,str(self.card.rolls[0]),18,WHITE,CARD_WIDTH//2,CARD_HEIGHT//20,'midtop')
            
            #if player has shopping mall, house and cup properties get +1 reward
            if self.card.reward!=0: 
                if self.player.is_player and self.player.landmarks[2].active and (self.card.symbol=='house' or self.card.symbol=='cup'):
                    draw_text(self.image,str(self.card.reward)+" (+1)",18,YELLOW,CARD_WIDTH//2,CARD_HEIGHT-20,'midtop')
                else:
                    draw_text(self.image,str(self.card.reward),18,WHITE,CARD_WIDTH//2,CARD_HEIGHT-20,'midtop')
            else:
                draw_text(self.image,'?',18,WHITE,CARD_WIDTH//2,CARD_HEIGHT-20,'midtop')
            
            if self.player.properties_all[self.card.name]>1:
                draw_text(self.image,'x'+str(self.player.properties_all[self.card.name]),18,YELLOW,CARD_WIDTH*9//10,CARD_HEIGHT//2,'midtop')
                
            if self.card.name=="Tech Startup" and self.player.is_player:
                draw_text(self.image,str(self.player.tech_startup_money),18,YELLOW,CARD_WIDTH//10,CARD_HEIGHT*9//10,'midtop')
                
        pygame.draw.circle(self.image,YELLOW,(CARD_WIDTH//10,CARD_HEIGHT//2),12)
        pygame.draw.circle(self.image,ORANGE,(CARD_WIDTH//10,CARD_HEIGHT//2),12,3)
        if self.card.price>=0:
            draw_text(self.image,str(self.card.price),18,ORANGE,CARD_WIDTH//10,CARD_HEIGHT//2,'center')
        else:
            draw_text(self.image,'0',18,ORANGE,CARD_WIDTH//10,CARD_HEIGHT//2,'center')
                
        draw_text(self.image,self.card.name,18,WHITE,CARD_WIDTH//2,CARD_HEIGHT//20+24,'midtop')
        
        if self.card.type=='property' and self.card.renovating:
            pygame.draw.polygon(self.image,YELLOW,[(self.rect.width//2,self.rect.height//3),(self.rect.width//6,self.rect.height*2//3),(self.rect.width*5//6,self.rect.height*2//3)])
            draw_text(self.image,'!',48,WHITE,self.rect.width//2,self.rect.height//2,'center')
            
        try:
            symbol=pygame.transform.scale(pygame.image.load(path.join(self.game.img_dir,self.card.symbol+".png")).convert(),(self.rect.width//6,self.rect.width//6))
            symbol.set_colorkey(BLACK)
            self.image.blit(symbol,(self.rect.width*5//6-10,10,self.rect.width//6,self.rect.width//6))
        except:
            print("image "+self.game.img_dir,self.card.symbol+".png not found")
        
    def check_clicks(self):
        action=False
        #get mouse pos
        pos=pygame.mouse.get_pos()
        
        #check mouseover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and not self.clicked:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0 and self.clicked:
                self.clicked=False
                
        return action
        
class Button:
    def __init__(self,game,x,y,image):
        self.game=game
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.y=y
        self.clicked=False
    
    def draw(self):
        action=False
        #get mouse pos
        pos=pygame.mouse.get_pos()
        
        #check mouseover and click conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and not self.clicked:
                self.clicked=True
                action=True
            if pygame.mouse.get_pressed()[0]==0 and self.clicked:
                self.clicked=False
        
        self.game.screen.blit(self.image,self.rect)
        return action