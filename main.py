import pygame
import random
from os import path
from settings import *
from sprites import *
from cards import *

class Game:
    def __init__(self):
        #initialize pygame and create window
        pygame.init()
        pygame.mixer.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock=pygame.time.Clock()
        self.load_data()
        self.running=True
        
    def load_data(self):
        #load images, sounds, etc.
        self.dir=path.dirname(__file__)
        self.img_dir=path.join(self.dir,'img')
        self.snd_dir=path.join(self.dir,'snd')
    
    def new(self):
        #start a new game
        self.all_sprites=pygame.sprite.Group()
        
        #market holds cards in center
        self.market=Market(self)
        self.players=[Player(self,True),Player(self,True)]#,Player(self,True)]#,Player(self,True),Player(self,True)]
        
        #create button to roll 1 die
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"ROLL 1",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.roll_button_1=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT,img)
        
        #create button to roll 2 dice
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"ROLL 2",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.roll_button_2=Button(self,WIDTH-BORDER-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT,img)
        
        #create button to pass turn without building after rolling
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"PASS",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.pass_button=Button(self,WIDTH-(CARD_WIDTH+BORDER),HEIGHT//2-CARD_HEIGHT//8,img)
        
        #create button to pass turn without building after rolling and get 10 coins if player owns airport
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"PASS",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        draw_text(img,"+10 coins!",14,RED,CARD_WIDTH//2,CARD_HEIGHT//4+15,'midtop')
        self.pass_button_2=Button(self,WIDTH-(CARD_WIDTH+BORDER),HEIGHT//2-CARD_HEIGHT//8,img)
        
        #next buttons are all in the same position but show up for different times
        
        #create button to buy card after rolling
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"BUY",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.buy_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to demolish landmark when demolition company is activated
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"DEMOLISH",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.demolish_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to move property when demolition company is activated
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"MOVE",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.move_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to activate property when exhibit hall is activated
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"ACTIVATE",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.activate_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to activate property when business center is activated
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"EXCHANGE",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.exchange_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to renovate property when renovation company is activated
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"RENOVATE",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.renovate_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        ############################################
        
        #create button to go back from card screen
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"BACK",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.back_button=Button(self,WIDTH-BORDER-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*5//2-BORDER_BTW*3,img)
        
        #create button to add 2 to dice roll if at least 10 and player has harbor
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"ADD 2",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.add_2_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*3//2-BORDER_BTW,img)
        
        #create button to choose NOT to add 2 to dice roll if at least 10 and player has harbor
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"KEEP ROLL",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.keep_roll_button=Button(self,WIDTH-BORDER-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*3//2-BORDER_BTW,img)
        
        #create button to add reroll dice if player has radio tower
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"REROLL",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.reroll_button=Button(self,WIDTH-BORDER-CARD_WIDTH-BORDER_BTW-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*2-BORDER_BTW*2,img)
        
        #create button to choose NOT to reroll if player has radio tower
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"KEEP ROLL",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.no_reroll_button=Button(self,WIDTH-BORDER-CARD_WIDTH//2,HEIGHT-BORDER-CARD_HEIGHT*2-BORDER_BTW*2,img)
        
        #create button to reset game after game is over
        img=pygame.Surface((CARD_WIDTH,CARD_HEIGHT//2))
        img.fill(WHITE)
        draw_text(img,"NEW GAME",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.new_game_button=Button(self,WIDTH//2,HEIGHT*2//3,img)

        #create buttons to select player in select screen
        self.select_buttons=[]
        for _ in range(len(self.players)):
            img=pygame.Surface(( (SIDE-BORDER*2)//2-BORDER_BTW,(SIDE-BORDER*2-50)//2-BORDER_BTW ))
            #all positions set to (0,0) and no graphics b/c rearrange_buttons() will change position and set graphics when needed
            self.select_buttons.append(Button(self,0,0,img))
            
        #create buttons for yes/no in select_screen
        x=BORDER+(SIDE-BORDER*2)//8+((SIDE-BORDER*2)//2-BORDER_BTW)//2
        y=BORDER+50 #under text at top of screen    
        
        img=pygame.Surface(( (SIDE-BORDER*2)//2-BORDER_BTW,(SIDE-BORDER*2-50)//2-BORDER_BTW ))
        img.fill(WHITE)
        draw_text(img,"YES",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.yes_button=Button(self,x,y,img)
        
        x+=(SIDE-BORDER*2)//2
        
        img=pygame.Surface(( (SIDE-BORDER*2)//2-BORDER_BTW,(SIDE-BORDER*2-50)//2-BORDER_BTW ))
        img.fill(WHITE)
        draw_text(img,"NO",18,BLACK,CARD_WIDTH//2,CARD_HEIGHT//4,'center')
        self.no_button=Button(self,x,y,img)
        
        ############################################
        
        self.view_timer=0 #track time to start for viewing income and building in each turn
        self.income_num=len(self.players) #track player to be shown for gaining income, corresponds to indices of self.players and -1 for center
        self.card_num=-1 #track card in player.card_sprites_list to be activated
        self.income_color=[RED]
        self.checking_city_hall=False #track if income screen is showing gain for city hall pity money or demo/moving co result
        self.turn=0 #corresponds to indices of self.players
        self.has_rolled=False
        self.has_added=False #if player has harbor, this flag checks if button to add 2 or not has been pressed
        self.has_rerolled=False #if player has radio tower, this flag checks if button to reroll or not has been pressed
        self.has_bought=False
        self.is_demolishing=0 #tag for when demolition company is activated, number is how many demolitions are left
        self.is_moving=0 #tag for when moving company is activated, number is how many moves are left
        self.is_activating=0 #tag for when exhibit hall is activated, number is how many activations are left
        self.is_choosing_tv_station=0 #tag for when tv station is activated, number of how many times player can take 5 coins left
        self.is_exchanging=0 #tag for when business center is activated, number of how many exchanges are left
        self.is_rolling_tuna_boat=False #tag for when tuna boat is activated and active player must roll for income
        self.is_choosing_tech_startup=0 #tag for end of turn if player needs to choose to add 1 to tech startup or not
        self.is_renovating=0 #tag for when renovation company is activated, number of how many cards can be renovated
        self.exchange_properties=[] #list contains which properties are being exchanged when business center is activated
        
        self.selected_card_sprite=None #CardSprite for card screen
        self.selected_exhibit_hall=None #if player activates a card using exhibit hall, this tracks the exhibit hall so it can be removed
        self.roll=0
        self.doubles=False
        self.page='start'
        self.last_page='player 1'
        self.run()

    def run(self):
        self.playing=True
        while self.playing:
            #keep loop running at correct speed
            self.clock.tick(FPS)
            if self.page=='start':
                self.start_screen()
            elif self.page=='center':
                self.center_screen()
            elif self.page=='player 1':
                self.player_screen(0)
            elif self.page=='player 2' and len(self.players)>=2:
                self.player_screen(1)
            elif self.page=='player 3' and len(self.players)>=3:
                self.player_screen(2)
            elif self.page=='player 4' and len(self.players)>=4:
                self.player_screen(3)
            elif self.page=='player 5' and len(self.players)>=5:
                self.player_screen(4)
            elif self.page=='card':
                self.card_screen()
            elif self.page=='income':
                self.income_screen()
            elif self.page=='build':
                self.build_screen()
            elif self.page=='select':
                self.select_screen()
            elif self.page=='end':
                self.end_screen()
            else:
                print("page not found or player selected out of bounds!")
                self.page='center'
            
    #central screen with market cards and rolling dice
    def center_screen(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
            if self.page=='center' and event.type==pygame.KEYUP: #don't want to do this during income screen
                if event.key==pygame.K_1:
                    self.page='player 1' #go to player 1's cards
                elif event.key==pygame.K_2 and len(self.players)>=2:
                    self.page='player 2' #go to player 2's cards
                elif event.key==pygame.K_3 and len(self.players)>=3:
                    self.page='player 3' #go to player 2's cards
                elif event.key==pygame.K_4 and len(self.players)>=4:
                    self.page='player 4' #go to player 2's cards
                elif event.key==pygame.K_5 and len(self.players)>=5:
                    self.page='player 5' #go to player 2's cards
                    
        self.market.card_sprites.update()
        
        self.screen.fill(BLACK)
        
        #draw face down cards to show deck next to market cards
        pygame.draw.rect(self.screen,WHITE,(BORDER,BORDER,CARD_WIDTH,CARD_HEIGHT))
        pygame.draw.rect(self.screen,WHITE,(BORDER,BORDER+(CARD_HEIGHT+BORDER),CARD_WIDTH,CARD_HEIGHT))
        pygame.draw.rect(self.screen,WHITE,(BORDER,BORDER+(CARD_HEIGHT+BORDER)*2,CARD_WIDTH,CARD_HEIGHT))
        
        #show player's turn and if they have to demolish/move properties, etc.
        draw_text(self.screen,self.bottom_text(),24,WHITE,WIDTH//2,HEIGHT-BORDER-30,'midtop')
            
        self.market.card_sprites.draw(self.screen)
        
        #show buttons to roll when player hasn't rolled yet
        if not self.has_rolled:
            #don't show this option when rolling for tuna boat, 2 dice must be rolled
            if (not self.is_rolling_tuna_boat) and self.roll_button_1.draw():
                self.roll=3#random.randint(1,6)
                self.doubles=False
                self.has_rolled=True
                            
            #roll 2 dice button only shown if player has train station active or if rolling for tuna boat
            #don't show button in income screen, etc.
            if self.page=='center' and (self.players[self.turn].landmarks[1].active or self.is_rolling_tuna_boat) and self.roll_button_2.draw():
                roll1=random.randint(1,6)
                roll2=random.randint(1,6)
                self.roll=10#roll1+roll2
                self.doubles=(roll1==roll2)
                self.has_rolled=True
                
                #if rolling for tuna boat, give players money and go to income screen again
                if self.is_rolling_tuna_boat:
                    self.has_added=True
                    self.has_rerolled=True
                    self.is_rolling_tuna_boat=False
                    
                    for p in self.players:
                        p.money+=p.properties_all["Tuna Boat"]*self.roll
                    
                    self.view_timer=pygame.time.get_ticks()
                    self.income_num=len(self.players)
                    self.card_num=-1
                    self.income_color=[RED]
                    self.page='income' #make it so the center screen is shown first before going to income screen
                
        elif not self.has_added: #if player has harbor and 10+ roll, show buttons to add 2 or keep roll
            draw_text(self.screen,"Roll: "+str(self.roll),24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT,'midtop')
            if self.doubles:
                if self.players[self.turn].landmarks[3].active:
                    draw_text(self.screen,"DOUBLES! (Take another turn)",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
                else:
                    draw_text(self.screen,"DOUBLES!",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
            
            if self.players[self.turn].landmarks[0].active and self.roll>=10:
                if self.add_2_button.draw():
                    self.roll+=2
                    self.has_added=True
                    if self.has_rerolled:
                        self.give_income()
                if self.keep_roll_button.draw():
                    self.has_added=True
                    if self.has_rerolled:
                        self.give_income()
            else: #otherwise, skip this step and go straight to income screen
                self.has_added=True
                if self.has_rerolled:
                    self.give_income()
        
        elif not self.has_rerolled: #if player has radio tower, show buttons to reroll or keep roll
            draw_text(self.screen,"Roll: "+str(self.roll),24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT,'midtop')
            if self.doubles:
                if self.players[self.turn].landmarks[3].active:
                    draw_text(self.screen,"DOUBLES! (Take another turn)",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
                else:
                    draw_text(self.screen,"DOUBLES!",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
            
            if self.players[self.turn].landmarks[4].active:
                if self.reroll_button.draw():
                    self.has_rolled=False
                    self.has_added=False
                    self.has_rerolled=True
                if self.no_reroll_button.draw():
                    self.has_rerolled=True
                    self.give_income()
            else: #otherwise, skip this step and go straight to income screen
                self.has_rerolled=True
                self.give_income()
        
        elif self.has_rerolled: #if player has rolled, show result
            draw_text(self.screen,"Roll: "+str(self.roll),24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT,'midtop')
            if self.doubles:
                if self.players[self.turn].landmarks[3].active:
                    draw_text(self.screen,"DOUBLES! (Take another turn)",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
                else:
                    draw_text(self.screen,"DOUBLES!",24,WHITE,WIDTH-(CARD_WIDTH+BORDER)*3//2,HEIGHT-BORDER-CARD_HEIGHT+30,'midtop')
            
            if self.page=='center' and self.is_demolishing<=0 and self.is_moving<=0 and self.is_exchanging<=0 and self.is_renovating<=0 and not self.is_rolling_tuna_boat: #click this button to pass turn without building (not in income page or when demolishing)
                #is_activating not checked here b/c it is optional, while demo and moving (etc.) are not
                if self.players[self.turn].landmarks[5].active:
                    if self.pass_button_2.draw():
                        self.players[self.turn].money+=10 #give money for airport if owned and player does not build
                        #if player has tech startup(s), set count to go to selection screen after build screen
                        self.is_choosing_tech_startup=self.players[self.turn].properties_all["Tech Startup"]
                        self.has_bought=True
                        self.view_timer=pygame.time.get_ticks()
                        self.page='build'
                    
                elif self.pass_button.draw():
                    #if player has tech startup(s), set count to go to selection screen after build screen
                    self.is_choosing_tech_startup=self.players[self.turn].properties_all["Tech Startup"]
                    self.has_bought=True
                    self.view_timer=pygame.time.get_ticks()
                    self.page='build'
            
        if self.page=='center': #don't want to do this in income page
            for card_sprite in self.market.card_sprites: #check if any market cards are clicked and display on card screen
                if card_sprite.check_clicks():
                    self.last_page='center'
                    self.page='card'
                    self.selected_card_sprite=card_sprite
                    break
            
        pygame.display.flip()
            
    #shows cards, money, etc. for certain player, index given by n
    def player_screen(self,n):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
            if event.type==pygame.KEYUP:
                if self.page[0:6]=='player' and event.key==pygame.K_SPACE:
                    self.page='center'
        self.players[n].card_sprites.update()
        self.screen.fill(BLACK)
        draw_text(self.screen,"Player "+str(n+1)+"'s Cards",24,WHITE,BORDER,HEIGHT-BORDER-30*2,'topleft')
        draw_text(self.screen,"Money: "+str(self.players[n].money),24,YELLOW,BORDER,HEIGHT-BORDER-30,'topleft')
        
        #show player's turn and if they have to demolish/move properties, etc.
        draw_text(self.screen,self.bottom_text(),24,WHITE,WIDTH//2,HEIGHT-BORDER-30,'midtop')
        
        #mark property to be exchanged when one has been chosen
        for card_sprite in self.exchange_properties:
            pygame.draw.circle(card_sprite.image,RED,(card_sprite.rect.width//2,card_sprite.rect.height//2),card_sprite.rect.width//4,10)
        self.players[n].card_sprites.draw(self.screen)
        
        if self.page[0:6]=='player': #don't want to do this during income or build pages
            for card_sprite in self.players[n].card_sprites: #check if any market cards are clicked and display on card screen
                if card_sprite.check_clicks():
                    temp=self.page
                    self.page='card'
                    self.last_page=temp
                    self.selected_card_sprite=card_sprite
                    break
                
#         if self.page=='income' and self.card_num>=0:
#             print(self.players[self.income_num].card_sprites_list[self.card_num].card.name)
        
        pygame.display.flip()
        
    #displays single card in larger detail and shows buttons to buy card (if applicable) and go back to previous screen
    def card_screen(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
                
        self.screen.fill(BLACK)
        
        #show player's turn and if they have to demolish/move properties, etc.
        draw_text(self.screen,self.bottom_text(),24,WHITE,WIDTH//2,HEIGHT-BORDER-30,'midtop')
        
        #img is bigger card image
        img=pygame.Surface((SIDE//2,SIDE*2//3))
        img_rect=img.get_rect()
        img_rect.x=SIDE//4
        img_rect.y=SIDE//6
        
        #most of this is very similar to update() in CardSprite class
        #if card is landmark, show if it is active
        if self.selected_card_sprite.card.type=='landmark':
            if self.selected_card_sprite.card.active:
                img.fill(GOLD)
            else:
                img.fill(GRAY)
        else: #otherwise, show property details
            img.fill(self.selected_card_sprite.card.color)
            if len(self.selected_card_sprite.card.rolls)>1:
                draw_text(img,str(self.selected_card_sprite.card.rolls[0])+'-'+str(self.selected_card_sprite.card.rolls[len(self.selected_card_sprite.card.rolls)-1]),18,WHITE,img_rect.width//2,img_rect.height//20,'midtop')
            else:
                draw_text(img,str(self.selected_card_sprite.card.rolls[0]),18,WHITE,img_rect.width//2,img_rect.height//20,'midtop')
            
            if self.selected_card_sprite.card.reward!=0: 
                #if player has shopping mall, house and cup properties get +1 reward
                if self.selected_card_sprite.player.is_player and self.selected_card_sprite.player.landmarks[2].active and (self.selected_card_sprite.card.symbol=='house' or self.selected_card_sprite.card.symbol=='cup'):
                    draw_text(img,str(self.selected_card_sprite.card.reward)+" (+1)",18,YELLOW,img_rect.width//2,img_rect.height-20,'midtop')
                else:
                    draw_text(img,str(self.selected_card_sprite.card.reward),18,WHITE,img_rect.width//2,img_rect.height-20,'midtop')
            else:
                draw_text(img,'?',18,WHITE,img_rect.width//2,img_rect.height-20,'midtop')
                
            if self.selected_card_sprite.player.properties_all[self.selected_card_sprite.card.name]>1:
                draw_text(img,'x'+str(self.selected_card_sprite.player.properties_all[self.selected_card_sprite.card.name]),18,YELLOW,img_rect.width*9//10,img_rect.height//2,'midtop')
                
            if self.selected_card_sprite.card.name=="Tech Startup" and self.selected_card_sprite.player.is_player:
                draw_text(img,str(self.selected_card_sprite.player.tech_startup_money),18,YELLOW,img_rect.width//10,img_rect.height-20,'midtop')
                
        #all cards show name and price and desc.
        draw_text(img,str(self.selected_card_sprite.card.price),18,WHITE,img_rect.width//10,img_rect.height//2,'midtop')        
        draw_text(img,self.selected_card_sprite.card.name,18,WHITE,img_rect.width//2,img_rect.height//20+24,'midtop')
        
        #description may go on multiple lines of text
        i=0
        y=img_rect.height*2//3
        while i<len(self.selected_card_sprite.card.description):
            j=i+1
            for j in range(j,len(self.selected_card_sprite.card.description)+1):
                if j>=len(self.selected_card_sprite.card.description) or self.selected_card_sprite.card.description[j]=='(' or (j>i+36 and self.selected_card_sprite.card.description[j]==' ' and j+1<len(self.selected_card_sprite.card.description) and self.selected_card_sprite.card.description[j+1]!='('):
                    break #end current line if reach end of string, open parentheses, or space over 36 characters from start
                
            text=self.selected_card_sprite.card.description[i:j]
            draw_text(img,text,18,WHITE,img_rect.width//2,y,'midtop')
            i=j
            y+=24
            
        try:
            symbol=pygame.transform.scale(pygame.image.load(path.join(self.img_dir,self.selected_card_sprite.card.symbol+".png")).convert(),(img_rect.width//8,img_rect.width//8))
            symbol.set_colorkey(BLACK)
            img.blit(symbol,(img_rect.width*7//8-10,10,img_rect.width//8,img_rect.width//8))
        except:
            print("image "+self.img_dir,self.selected_card_sprite.card.symbol+".png not found")
        
        self.screen.blit(img,img_rect)
        
        #if last page was center, player can buy if they have rolled and can afford it
        if self.last_page=='center':
            #is_activating not checked here b/c it is optional, while demo and moving and exchanging and rolling for tuna boat and renovating are not
            #player can only have 1 of each purple property
            if self.has_rolled and self.has_added and self.has_rerolled and not self.has_bought and self.is_demolishing<=0 and self.is_moving<=0 and self.is_exchanging<=0 and self.is_renovating<=0 and not self.is_rolling_tuna_boat and self.players[self.turn].money>=self.selected_card_sprite.card.price and (self.selected_card_sprite.card.color!=PURPLE or (self.selected_card_sprite.card.color==PURPLE and self.players[self.turn].properties_all[self.selected_card_sprite.card.name]<1)) and self.buy_button.draw():
                #can only buy one card per turn (no hold clicking) AFTER rolling and must have enough money to buy card
                self.has_bought=True
                self.players[self.turn].add_property(self.selected_card_sprite.card)
                self.players[self.turn].money-=self.selected_card_sprite.card.price
                self.market.replace_card(self.selected_card_sprite)
                
                #if player has tech startup(s), set count to go to selection screen after build screen
                self.is_choosing_tech_startup=self.players[self.turn].properties_all["Tech Startup"]
                self.view_timer=pygame.time.get_ticks()
                self.page='build'
                
        
        elif self.last_page[0:6]=='player':
            if self.has_rolled and self.has_added and self.has_rerolled and not self.has_bought:
                if int(self.last_page[len(self.last_page)-1])==self.turn+1:
                    #if last page was player page and it is this player's turn, player can buy if they have rolled and can afford it
                    if self.selected_card_sprite.card.type=='landmark':
                        #is_activating not checked here b/c it is optional, while demo and moving are not
                        if self.is_demolishing<=0 and self.is_moving<=0 and self.is_exchanging<=0 and self.is_renovating<=0 and not self.is_rolling_tuna_boat and not self.selected_card_sprite.card.active and self.players[self.turn].money>=self.selected_card_sprite.card.price and self.buy_button.draw():
                            #can only buy one card per turn (no hold clicking) AFTER rolling and must have enough money to buy card
                            self.has_bought=True
                            self.selected_card_sprite.card.active=True
                            self.players[self.turn].money-=self.selected_card_sprite.card.price
                            self.players[self.turn].landmarks_active+=1
                            
                            #if player has tech startup(s), set count to go to selection screen after build screen
                            self.is_choosing_tech_startup=self.players[self.turn].properties_all["Tech Startup"]
                            self.view_timer=pygame.time.get_ticks()
                            self.page='build'
                        #if last page was player page and this player must demolish a landmark, show button to demolish if landmark is active but not city hall
                        elif self.is_demolishing>0 and self.selected_card_sprite.card.active and self.selected_card_sprite.card.name!="City Hall" and self.demolish_button.draw():
                            self.is_demolishing-=1 #decrement count to show landmark has been demolished
                            self.selected_card_sprite.card.active=False #deactivate demolished landmark
                            self.players[self.turn].landmarks_active-=1
                            self.players[self.turn].money+=PROPERTIES_ALL["Demolition Company"][3] #give money as reward
                            self.checking_city_hall=True #shows demolition company is being checked so not all players are shown
                            
                            #if player could activate property before but can't after demolishing, set is_activating to 0
                            if self.is_activating>0:
                                #player can activate if they have properties other than demo co or enough landmarks to demolish
                                if self.players[self.turn].properties_all["Demolition Company"]==self.players[self.turn].num_properties:
                                    #if player only has demo co and less landmarks left than activations, set activations to # of landmarks
                                    self.is_activating=min(self.is_activating,self.players[self.turn].landmarks_active)
                            
                            #show player's screen again with demolished card
                            self.checking_city_hall=True #shows exhibit hall is being checked so not all players are shown
                            #MAYBE DELETE THIS? ^^^^ TEST IT
                            self.view_timer=pygame.time.get_ticks()
                            self.income_num=self.turn #reset player shown to active player
                            self.card_num=-1 #no card is being activated
                            self.page='income'
                            
                    #if last page was player page and this player must move a property, show button to move it if not a 'tower' property and not a moving co if only 1 left
                    elif self.selected_card_sprite.card.type=='property':
                        if self.is_moving>0 and self.selected_card_sprite.card.symbol!='tower' and (self.selected_card_sprite.card.name!="Moving Company" or (self.selected_card_sprite.card.name=="Moving Company" and self.players[self.turn].properties_all["Moving Company"]>1)):
                            if self.move_button.draw():
                                self.rearrange_buttons()
                                self.page='select'
                        #elif b/c we don't want activate button shown if move button is already shown (i.e. if player activates moving co but still has another activation to do)
                        #is_moving must be 0 b/c moving co and exhibit hall have same roll but moving company must be done first
                        elif self.is_activating>0 and self.is_moving<=0 and not self.is_rolling_tuna_boat and self.selected_card_sprite.card.symbol!='tower' and self.selected_card_sprite.card.color!=RED and (self.selected_card_sprite.card.name!="Demolition Company" or (self.selected_card_sprite.card.name=="Demolition Company" and self.players[self.turn].landmarks_active>0)):
                            #don't show activate button on demo co if no landmarks to demolish!
                            if self.activate_button.draw():
                                self.is_activating-=1 #decrement count to show property has been moved
                                
                                #activate card and remove exhibit hall
                                self.players[self.turn].remove_property(self.selected_exhibit_hall)
                                
                                #give reward for property activated - no purple b/c all 'tower' and no red b/c this is active player
                                if self.selected_card_sprite.card.color==GREEN:
                                    self.green_income(self.players[self.turn],self.selected_card_sprite)
                                elif self.selected_card_sprite.card.color==BLUE:
                                    self.blue_income(self.players[self.turn],self.selected_card_sprite)
                                    
                                #show player's screen again with moved card
                                self.checking_city_hall=True #shows exhibit hall is being checked so not all players are shown
                                self.view_timer=pygame.time.get_ticks()
                                self.income_num=self.turn #reset player shown to active player
                                self.card_num=-1 #no card is being activated
                                self.page='income'
                                
                        #show exchange button for active player        
                        elif self.is_exchanging>0 and self.is_activating<=0 and self.is_moving<=0 and not self.is_rolling_tuna_boat and self.selected_card_sprite.card.symbol!='tower':
                            if len(self.exchange_properties)==0 or (len(self.exchange_properties)==1 and self.players.index(self.exchange_properties[0].player)+1!=int(self.last_page[len(self.last_page)-1])):
                                if self.exchange_button.draw():
                                    self.business_center_move()
                        
                        #show renovate button for active player
                        elif self.is_renovating>0 and self.is_moving<=0 and self.is_activating<=0 and self.is_exchanging<=0 and not self.is_rolling_tuna_boat and not self.selected_card_sprite.card.renovating:
                            if self.renovate_button.draw():
                                self.renovate_properties()
                                    
                #show exchange button even if player screen isn't for active player 
                elif self.selected_card_sprite.card.type=='property':
                    if self.is_exchanging>0 and self.is_activating<=0 and self.is_moving<=0 and not self.is_rolling_tuna_boat and self.selected_card_sprite.card.symbol!='tower':
                        if len(self.exchange_properties)==0 or (len(self.exchange_properties)==1 and self.players.index(self.exchange_properties[0].player)+1!=int(self.last_page[len(self.last_page)-1])):
                                if self.exchange_button.draw():
                                    self.business_center_move()
                        
                    #show renovate button even if player screen isn't for active player
                    elif self.is_renovating>0 and self.is_moving<=0 and self.is_activating<=0 and self.is_exchanging<=0 and not self.is_rolling_tuna_boat and not self.selected_card_sprite.card.renovating:
                        if self.renovate_button.draw():
                            self.renovate_properties()
                    
        #always show back button
        if self.back_button.draw():
            self.page=self.last_page
        
        pygame.display.flip()
        
    #select player to give card from moving company, choose who to take from with TV station, etc.
    def select_screen(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
        
        self.screen.fill(BLACK)
        
        #show text to tell player what they are selecting
        if self.is_choosing_tech_startup:
            text="Add 1 coin to tech startup? You have "+str(self.players[self.turn].money)+" coins"
        else:
            text="Choose a player to "
            if self.is_moving>0:
                text+="give your property!"
            elif self.is_choosing_tv_station>0:
                text+="take 5 coins from!"
        
        draw_text(self.screen,text,36,WHITE,WIDTH//2,BORDER,'midtop')
        
        if self.is_choosing_tech_startup>0:
            if self.yes_button.draw():
                self.is_choosing_tech_startup-=1
                self.players[self.turn].money-=1
                self.players[self.turn].tech_startup_money+=1
                
                self.view_timer=pygame.time.get_ticks()
                self.page='build'
            if self.no_button.draw():
                self.is_choosing_tech_startup-=1
                
                self.view_timer=pygame.time.get_ticks()
                self.page='build'
                
        else:
            #show buttons for each player whose turn it is not
            for i in range(len(self.select_buttons)): #buttons are created for each player in new() so it is impossible for there to be out of bounds selection
                if self.turn!=i and self.select_buttons[i].draw(): #if not this player's turn and this player is selected...
                    if self.is_choosing_tv_station>0:
                        self.is_choosing_tv_station-=1
                        
                        payment=min(PROPERTIES_ALL["TV Station"][3],self.players[i].money)
                        
                        #active player loses money for each red card and this player gets the same amount
                        self.players[self.turn].money+=payment
                        self.players[i].money-=payment
                        
                        #show player's screen again with new money
                        self.checking_city_hall=True #shows moving company is being checked so not all players are shown
                        self.view_timer=pygame.time.get_ticks()
                        self.income_num=self.turn #reset player shown to active player
                        self.card_num=-1 #no card is being activated
                        self.page='income'
                                    
                    elif self.is_moving>0: #if selecting for moving company...
                        self.is_moving-=1 #decrement count to show property has been moved
                        
                        #move card
                        self.players[i].add_property(self.selected_card_sprite.card)
                        self.players[self.turn].remove_property(self.selected_card_sprite)
                        
                        self.players[self.turn].money+=PROPERTIES_ALL["Moving Company"][3] #give money as reward
                        
                        #if player could activate property before but can't after moving, set is_activating to 0
                        if self.is_activating>0:
                            #player can activate if they have properties other than moving co or more than one moving co
                            if self.players[self.turn].num_properties<=1 and self.players[self.turn].properties_all["Moving Company"]==self.players[self.turn].num_properties:
                                self.is_activating=0
                            elif self.players[self.turn].properties_all["Moving Company"]==self.players[self.turn].num_properties:
                                self.is_activating=self.players[self.turn].properties_all["Moving Company"]-1
                        
                        #show player's screen again with moved card
                        self.checking_city_hall=True #shows moving company is being checked so not all players are shown
                        self.view_timer=pygame.time.get_ticks()
                        self.income_num=self.turn #reset player shown to active player
                        self.card_num=-1 #no card is being activated
                        self.page='income'
                        
                        #show back button
                        if self.back_button.draw():
                            self.page=self.last_page
        
        pygame.display.flip()
    
    #start screen shown when game is first opened
    def start_screen(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
            if event.type==pygame.KEYUP:
                self.page='player 1'
        self.screen.fill(BLACK)
        draw_text(self.screen,TITLE,48,WHITE,WIDTH/2,HEIGHT/4,'midtop')
        pygame.display.flip()
        
    #end screen shown when game is over to show winner
    def end_screen(self): #winner is index of winning player in self.players
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
                self.running=False
        self.screen.fill(BLACK)
        draw_text(self.screen,"Player "+str(self.turn+1)+" wins!",48,WHITE,WIDTH/2,HEIGHT/4,'midtop')
        if self.new_game_button.draw():
            self.playing=False
        pygame.display.flip()
        
    def income_screen(self):
#         print(self.card_num)
        show=False
        if self.income_num<len(self.players) and self.card_num>=0: #if indices are in range to show card, check if card should be shown
            if self.income_num>=0 and self.players[self.income_num].card_sprites_list[self.card_num].card.color in self.income_color and self.roll in self.players[self.income_num].card_sprites_list[self.card_num].card.rolls:
                if self.players[self.income_num].card_sprites_list[self.card_num].card.color==RED and self.turn!=self.income_num:
                    show=True
                elif self.players[self.income_num].card_sprites_list[self.card_num].card.color==BLUE:
                    show=True
                elif (self.players[self.income_num].card_sprites_list[self.card_num].card.color==GREEN or self.players[self.income_num].card_sprites_list[self.card_num].card.color==PURPLE) and self.turn==self.income_num:
                    show=True
        else: #otherwise, show=True b/c either showing center or showing no specific card on player screen
            show=True
        now=pygame.time.get_ticks()
        
        if not show: #if not show, go to next card to check
            self.card_num+=1
            if self.card_num>=len(self.players[self.income_num].card_sprites_list):
                self.income_num-=1 #if no more cards, go to next player (backward in list)
                if self.income_color==RED:
                    self.card_num=-1 #show player screen with no specific card first
                else:
                    self.card_num=0 #in later colors, just show activated cards
            if self.income_num<0:
                self.next_color()
                
        else: #if show, check timer
            if now-self.view_timer<=1500:
                if self.income_num>=len(self.players): #show center screen first
                    self.center_screen()
                else: #then each player screen
                    self.player_screen(self.income_num) #income num --> index of player in self.players shown
                    
            else: #when timer ends...
                if not self.checking_city_hall: #in normal income cycle (not giving city hall money)
                    if self.income_num>=0 and self.income_num<len(self.players):
                        self.card_num+=1 #go to next card
                        if self.card_num>=len(self.players[self.income_num].card_sprites_list):
                            self.income_num-=1 #if no more cards, go to next player (backward in list)
                            self.card_num=-1
                    elif self.income_num>=len(self.players): #if center screen, go to last player for red card income
                        self.income_num=len(self.players)-1
                    
                    #go to next color if applicable
                    if self.income_num<0: # if all players have been shown, go to next color
                        self.next_color() 
                    else:
                        self.view_timer=pygame.time.get_ticks()
                else: #if checking city hall, deal with special cases and go back to other screen
                    self.checking_city_hall=False
                    if self.is_choosing_tv_station>0:
                        self.rearrange_buttons()
                        self.page='select'
                    elif self.is_demolishing>0 or self.is_moving>0 or self.is_activating>0 or self.is_exchanging>0 or self.is_renovating>0:
                        self.page='player '+str(self.turn+1) #if still demolishing/moving, go back to player screen
                    else:
                        self.page='center' #otherwise, once city hall has been checked, go back to center screen
            
    def build_screen(self):
        now=pygame.time.get_ticks()
        if now-self.view_timer<=1500:
            self.player_screen(self.turn)
        else: #after time ends for showing active player, end turn
            if self.is_choosing_tech_startup>0 and self.players[self.turn].money>0:
                #don't need to rearrange buttons b/c using yes and no buttons here
                self.page='select'
            else:
                self.end_turn()
        
    #increments each player's money based on cards that match the current roll
    def give_income(self):
        #red cards are checked first
        for i in range(len(self.players)-1,-1,-1): #red income is determined counterclockwise in case multiple people need to take money
            if self.turn!=i: #red cards are only activated if it is NOT this player's turn
                player=self.players[i]
                for card_sprite in player.card_sprites:
                    if card_sprite.card.type=='property' and card_sprite.card.color==RED and self.roll in card_sprite.card.rolls:
                        if not card_sprite.card.renovating: #if card not under renovation, pay as normal
                            #sushi bar only activated when player has harbor
                            if card_sprite.card.name=="Sushi Bar" and player.landmarks[0].active:
                                self.red_income(player,card_sprite)
                            #french restaurant only activated when active player has at least 2 landmarks
                            elif card_sprite.card.name=="French Restaurant" and self.players[self.turn].landmarks_active>=2:
                                self.red_income(player,card_sprite)
                            #otherwise do normal red income
                            elif card_sprite.card.name!="Sushi Bar" and card_sprite.card.name!="French Restaurant":
                                self.red_income(player,card_sprite)
                        else: #if under renovation, make it not under renovation anymore
                            card_sprite.card.renovating=False
                            
        #blue/green cards are checked second
        for i in range(len(self.players)):
            player=self.players[i]
            for card_sprite in player.card_sprites:
                if card_sprite.card.type=='property' and self.roll in card_sprite.card.rolls:
                    #blue cards are activated on anyone's turn
                    if card_sprite.card.color==BLUE:
                        if not card_sprite.card.renovating: #if card not under renovation, pay as normal
                            #corn field only activated when player has <2 landmarks
                            if card_sprite.card.name=="Corn Field" and player.landmarks_active<2:
                                self.blue_income(player,card_sprite)
                            #mackerel/tuna boat only activated when player has harbor
                            elif (card_sprite.card.name=="Mackerel Boat" or card_sprite.card.name=="Tuna Boat") and player.landmarks[0].active:
                                self.blue_income(player,card_sprite)
                            #otherwise do normal blue income
                            elif card_sprite.card.name!="Corn Field" and card_sprite.card.name!="Mackerel Boat" and card_sprite.card.name!="Tuna Boat":
                                self.blue_income(player,card_sprite)
                        else: #if under renovation, make it not under renovation anymore
                            card_sprite.card.renovating=False
                            
                    #green cards are activated only if it is this player's turn
                    elif self.turn==i and card_sprite.card.color==GREEN:
                        if not card_sprite.card.renovating: #if card not under renovation, pay as normal
                            #general store only activated when player has <2 landmarks
                            if card_sprite.card.name=="General Store" and player.landmarks_active<2:
                                self.green_income(player,card_sprite)
                            #otherwise do normal green income
                            elif card_sprite.card.name!="General Store":
                                self.green_income(player,card_sprite)
                        else: #if under renovation, make it not under renovation anymore
                            card_sprite.card.renovating=False
                            
        #purple cards are checked last
        for i in range(len(self.players)):
            if self.turn==i: #purple cards are activated only if it is this player's turn
                player=self.players[i]
                for card_sprite in player.card_sprites:
                    if card_sprite.card.type=='property' and card_sprite.card.color==PURPLE and self.roll in card_sprite.card.rolls:
                        if not card_sprite.card.renovating: #if card not under renovation, pay as normal
                            self.purple_income(player,card_sprite)
                        else: #if under renovation, make it not under renovation anymore
                            card_sprite.card.renovating=False
                        
        self.view_timer=pygame.time.get_ticks()
        self.income_num=len(self.players)
        self.card_num=-1
        self.income_color=[RED]
        self.page='income' #make it so the center screen is shown first before going to income screen
        
    def red_income(self,player,card_sprite):
        #check for special cases first, otherwise use default payment method
        if card_sprite.card.name=="Private Club" and self.players[self.turn].landmarks_active>=3:
            payment=self.players[self.turn].money
        else:
            payment=min(card_sprite.card.reward*player.properties_all[card_sprite.card.name],self.players[self.turn].money)
        
        #if player has shopping mall, house and cup properties get +1 reward
        if player.landmarks[2].active and card_sprite.card.symbol=='cup':
            payment=min(payment+(1*player.properties_all[card_sprite.card.name]),self.players[self.turn].money)
        
        #active player loses money for each red card and this player gets the same amount
        player.money+=payment
        self.players[self.turn].money-=payment
        #print("player "+str(i+1)+" gets "+str(payment)+" and  player "+str(self.turn+1)+" loses "+str(payment))

    def blue_income(self,player,card_sprite):
        if card_sprite.card.name=="Tuna Boat":
            self.is_rolling_tuna_boat=True
            self.has_rolled=False
        else:
            player.money+=card_sprite.card.reward*player.properties_all[card_sprite.card.name]
    
    def green_income(self,player,card_sprite):
        #check for special cases first, otherwise use default payment method
        payment=0
        if card_sprite.card.name=="Flower Shop": #income based on number of flower gardens owned
            payment=(card_sprite.card.reward*player.properties_all["Flower Garden"])*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Demolition Company":
            #demolishes set to number of demo companies, or total number of active landmarks if it is less
            self.is_demolishing=min(player.properties_all["Demolition Company"],player.landmarks_active)
        elif card_sprite.card.name=="Cheese Factory":
            count=0
            for name in PROPERTIES_COW: #income based on number of 'cow' properties owned
                count+=player.properties_all[name]
            payment=(card_sprite.card.reward*count)*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Furniture Factory":
            count=0
            for name in PROPERTIES_SUN: #income based on number of 'sun' properties owned
                count+=player.properties_all[name]
            payment=(card_sprite.card.reward*count)*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Winery":
            payment=(card_sprite.card.reward*player.properties_all["Vineyard"])*player.properties_all[card_sprite.card.name]
            card_sprite.card.renovating=True
        elif card_sprite.card.name=="Soda Bottling Plant":
            count=0
            for p in self.players: #"p" b/c "player" is already used as an argument for this method
                for name in PROPERTIES_CUP: #income based on number of 'grain' properties owned by ALL players
                    count+=p.properties_all[name]
            payment=(card_sprite.card.reward*count)*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Farmer's Market":
            count=0
            for name in PROPERTIES_GRAIN: #income based on number of 'grain' properties owned
                count+=player.properties_all[name]
            payment=(card_sprite.card.reward*count)*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Food Warehouse":
            count=0
            for name in PROPERTIES_CUP: #income based on number of 'cup' properties owned
                count+=player.properties_all[name]
            payment=(card_sprite.card.reward*count)*player.properties_all[card_sprite.card.name]
        elif card_sprite.card.name=="Moving Company":
            #number of moves set to either number of moving cos, or total # of properties-1 if it is less (-1 b/c cannot move Moving Co if only one is owned)
            self.is_moving=max(min(player.properties_all["Moving Company"],player.num_properties-1),0) #but shouldn't be <0
        else:
            payment=card_sprite.card.reward*player.properties_all[card_sprite.card.name]
        
        #if player has shopping mall, house and cup properties get +1 reward
        if player.landmarks[2].active and card_sprite.card.symbol=='house':
            payment+=1*player.properties_all[card_sprite.card.name]
            
        player.money+=payment
        #print("player "+str(i+1)+" gets "+str(payment))
    
    def purple_income(self,player,card_sprite):
        if card_sprite.card.name=="TV Station":
            #find max number of times player could take 5 coins
            count=0
            for i in range(len(self.players)):
                if i!=self.turn and self.players[i].money>0:
                    count+=-(-self.players[i].money//5) #round up to ceiling b/c extra coins can be taken even if <5
            self.is_choosing_tv_station=min(count,player.properties_all["TV Station"])
            self.rearrange_buttons()
        
        elif card_sprite.card.name=="Stadium": #income taken from all players
            for i in range(len(self.players)):
                if i!=self.turn:
                    payment=min(card_sprite.card.reward,self.players[i].money)
                    #active player loses money for each red card and this player gets the same amount
                    player.money+=payment
                    self.players[i].money-=payment
                    
        elif card_sprite.card.name=="Business Center": #exchange your property with someone else's
            if player.num_properties>0: #active player and at least one other player must have at least 1 property to exchange
                for i in range(len(self.players)):
                    if i!=self.turn and self.players[i].num_properties>0:
                        self.is_exchanging=player.properties_all["Business Center"]
                        break
            
        elif card_sprite.card.name=="Publisher": #income paid based on # of 'cup' and 'house' properties each player owns
            for i in range(len(self.players)):
                if i!=self.turn:
                    count=0
                    for name in PROPERTIES_HOUSE: #income based on number of 'house' properties owned
                        count+=player.properties_all[name]
                    for name in PROPERTIES_CUP: #income based on number of 'cup' properties owned
                        count+=player.properties_all[name]
                    
                    payment=min(card_sprite.card.reward*count,self.players[i].money)
                    #active player loses money for each card and this player gets the same amount
                    player.money+=payment
                    self.players[i].money-=payment
                    
        elif card_sprite.card.name=="Renovation Company":
            self.is_renovating=player.properties_all["Renovation Company"]
                    
        elif card_sprite.card.name=="Tax Office":
            for i in range(len(self.players)):
                if i!=self.turn and self.players[i].money>=10:
                    payment=self.players[i].money//2
                    #active player loses money for each card and this player gets the same amount
                    player.money+=payment
                    self.players[i].money-=payment
                    
        elif card_sprite.card.name=="Tech Startup":
            for i in range(len(self.players)):
                if i!=self.turn:
                    payment=min(player.tech_startup_money,self.players[i].money)
                    #active player loses money for each red card and this player gets the same amount
                    player.money+=payment
                    self.players[i].money-=payment
            
        elif card_sprite.card.name=="Exhibit Hall":
            #number of activations set to number of exhibit halls as long as player has properties other than single moving co
            if player.num_properties>=1:
                #player can activate if they have properties other than moving co or more than one moving co
                if player.properties_all["Moving Company"]<player.num_properties:
                    #player can activate if they have properties other than demo co or enough landmarks to demolish
                    if player.properties_all["Demolition Company"]<player.num_properties:
                        self.is_activating=player.properties_all["Exhibit Hall"]
                        self.selected_exhibit_hall=card_sprite
                    elif player.properties_all["Demolition Company"]==player.num_properties:
                        self.is_activating=player.landmarks_active
                        self.selected_exhibit_hall=card_sprite
                #if all properties are moving co, must have >1 to activate, and demo co doesn't matter
                elif player.properties_all["Moving Company"]==player.num_properties:
                    self.is_activating=player.properties_all["Moving Company"]-1
                    self.selected_exhibit_hall=card_sprite
            
        elif card_sprite.card.name=="Park":
            total=0
            for p in self.players: #"p" b/c "player" is already used as an argument for this method
                total+=p.money
            for p in self.players: #all players money set to evenly divided number from total amount, rounding up
                p.money=-(-total//len(self.players)) #this formula gives ceiling (decimal always rounded up)
        else:
            player.money+=card_sprite.card.reward*player.properties_all[card_sprite.card.name]
    
    #called when button for business center is pressed, exhcanges chosen properties between players
    def business_center_move(self):
        #add chosen property to exchange list
        self.exchange_properties.append(self.selected_card_sprite)
        
        if len(self.exchange_properties)==2: #both properties have been chosen
            if int(self.last_page[len(self.last_page)-1])==self.turn+1: #if active player chose their property second
                i=self.players.index(self.exchange_properties[0].player)
                
                self.players[i].add_property(self.exchange_properties[1].card)
    #                         print("giving player "+str(i+1)+" "+self.exchange_properties[1].card.name)
                
                self.players[self.turn].add_property(self.exchange_properties[0].card)
    #                         print("giving player "+str(self.turn+1)+" "+self.exchange_properties[0].card.name)
                
                self.players[i].remove_property(self.exchange_properties[0])
    #                         print("removing player "+str(i+1)+" "+self.exchange_properties[0].card.name)
                
                self.players[self.turn].remove_property(self.exchange_properties[1])
    #                         print("removing player "+str(self.turn+1)+" "+self.exchange_properties[1].card.name)
                
            else: #active player chose their card first
                i=self.players.index(self.exchange_properties[1].player)
                
                self.players[i].add_property(self.exchange_properties[0].card)
    #                         print("giving player "+str(i+1)+" "+self.exchange_properties[0].card.name)
                
                self.players[self.turn].add_property(self.exchange_properties[1].card)
    #                         print("giving player "+str(self.turn+1)+" "+self.exchange_properties[1].card.name)
                
                self.players[i].remove_property(self.exchange_properties[1])
    #                         print("removing player "+str(i+1)+" "+self.exchange_properties[1].card.name)
                
                self.players[self.turn].remove_property(self.exchange_properties[0])
    #                         print("removing player "+str(self.turn+1)+" "+self.exchange_properties[0].card.name)
                
            self.exchange_properties.clear()
            self.is_exchanging-=1
            
        #show player's screen again with exchanged cards
        self.checking_city_hall=True #shows moving company is being checked so not all players are shown
        self.view_timer=pygame.time.get_ticks()
        self.income_num=self.turn #reset player shown to active player
        self.card_num=-1 #no card is being activated
        self.page='income'
                
    #called when button for renovation company is pressed, renovates properties and pays money accordingly
    def renovate_properties(self):
        self.is_renovating-=1
        renovate_name=self.selected_card_sprite.card.name
        for i in range(len(self.players)):
            count=0
            for cs in self.players[i].card_sprites:
                if cs.card.name==renovate_name:
                    cs.card.renovating=True
                    count+=self.players[i].properties_all[cs.card.name]
                    
            if i!=self.turn:
                payment=min(PROPERTIES_ALL["Renovation Company"][3]*count,self.players[i].money)
                    
                #active player loses money for each red card and this player gets the same amount
                self.players[self.turn].money+=payment
                self.players[i].money-=payment
                
        self.view_timer=pygame.time.get_ticks()
        self.income_num=len(self.players)-1 #set to 0 to cycle through all players to show properties under renovation
        self.card_num=-1 #no card is being activated
        self.page='income' #make it so the center screen is shown first before going to income screen
        
    def next_color(self):
        #go to next color if applicable
        if self.income_color==[RED]:
            self.income_color=[GREEN,BLUE]
            self.income_num=len(self.players)-1 #go back to first player to check
            self.card_num=0 #go back to first card to check
        elif self.income_color==[GREEN,BLUE]:
            self.income_color=PURPLE
            self.income_num=len(self.players)-1
            self.card_num=0
        else:
            #handle special cases to be dealt with after income
            if self.is_choosing_tv_station>0:
                self.rearrange_buttons()
                self.page='select'
            elif self.is_demolishing>0 or self.is_moving>0 or self.is_activating>0 or self.is_exchanging>0 or self.is_renovating>0:
                self.page='player '+str(self.turn+1) #if demolishing/moving, go back to player screen
            else:
                self.page='center' #otherwise, after all players, go back to center screen
            
            #if active player has 0 money after income, give city hall money
            if self.players[self.turn].landmarks[6].active and self.players[self.turn].money==0:
                self.players[self.turn].money+=1
                self.checking_city_hall=True #shows city hall is being checked so not all players are shown
                self.view_timer=pygame.time.get_ticks()
                self.income_num=self.turn #reset player shown to active player
                self.card_num=-1 #no card is being activated
                self.page='income'

    #gets text for middle bottom of screen showing player turn number and if they have to demolish/move cards
    def bottom_text(self):
        text="Player "+str(self.turn+1)+"'s Turn"
        if self.is_demolishing==1:
            text+=" - demolishing "+str(self.is_demolishing)+" landmark"
        elif self.is_demolishing>1:
            text+=" - demolishing "+str(self.is_demolishing)+" landmarks"
        if self.is_moving==1:
            text+=" - moving "+str(self.is_moving)+" property"
        elif self.is_moving>1:
            text+=" - moving "+str(self.is_moving)+" properties"
        if self.is_activating==1:
            text+=" - activating "+str(self.is_activating)+" property (optional)"
        elif self.is_activating>1:
            text+=" - activating "+str(self.is_activating)+" properties (optional)"
        if self.is_exchanging==1:
            text+=" - exchanging "+str(self.is_exchanging)+" property"
        elif self.is_exchanging>1:
            text+=" - exchanging "+str(self.is_exchanging)+" properties"
        if self.is_renovating==1:
            text+=" - renovating "+str(self.is_renovating)+" property"
        elif self.is_renovating>1:
            text+=" - renovating "+str(self.is_renovating)+" properties"
        if self.is_rolling_tuna_boat:
            text+=" - rolling dice for tuna boat"
        return text
    
    def rearrange_buttons(self):
        buttons=[] #buttons to be rearranged, does not include button for active player
        for i in range(len(self.select_buttons)):
            if i!=self.turn:
                self.select_buttons[i].image.fill(WHITE)
                draw_text(self.select_buttons[i].image,"Player "+str(i+1),36,BLACK,self.select_buttons[i].rect.width//2,self.select_buttons[i].rect.height//4,'center')
                draw_text(self.select_buttons[i].image,"Money: "+str(self.players[i].money),18,BLACK,self.select_buttons[i].rect.width//2,self.select_buttons[i].rect.height//4+50,'center')
                buttons.append(self.select_buttons[i])
        
        x=BORDER+(SIDE-BORDER*2)//8
        y=BORDER+50 #under text at top of screen
        for i in range(len(buttons)):
            buttons[i].rect.x=x
            buttons[i].rect.y=y
            x+=(SIDE-BORDER*2)//2
            if i==1: #max of 4 buttons shown in 2x2 square, so after 2nd button (index 1) go to next row
                x=BORDER+(SIDE-BORDER*2)//8
                y+=(SIDE-BORDER*2-50)//2
           
    #reset variables for next player's turn
    def end_turn(self):
        #check if current player has built all landmarks and won game
        game_over=True
        for card in self.players[self.turn].landmarks:
            if not card.active:
                game_over=False
                break
            
        #if active player won, go to end screen
        if game_over:
            self.page='end'
        #otherwise, go to next player's turn
        else:
            #if current player rolled doubles with amusement park, keep turn the same
            if not(self.players[self.turn].landmarks[3].active and self.doubles):
                self.turn+=1
                if self.turn>=len(self.players):
                    self.turn=0
            self.has_rolled=False
            self.has_added=False
            self.has_rerolled=False
            self.has_bought=False
            
            #reset property-specific tags in case of error so that next player can take turn normally
            self.is_demolishing=0
            self.is_moving=0
            self.is_activating=0
            self.is_exchanging=0
            self.is_renovating=0
            self.is_rolling_tuna_boat=False
            if len(self.exchange_properties)>0:
                self.exchange_properties.clear()
            
            #page goes to next player
            self.page='player '+str(self.turn+1)
    
g=Game()
while g.running:
    g.new()

pygame.quit()

#FIX - player starts with extra properties, preset dice rolls
#income gain happens all at once and is shown after
#set card_num to -1 at start to show player screen in general before specific cards being activated