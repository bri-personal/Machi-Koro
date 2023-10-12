#game options/settings
TITLE="MACHI KORO"
HEIGHT=900
SIDE=HEIGHT
FPS=60

BORDER=SIDE//30 #border of cards from edges of window
BORDER_BTW=10 #border between cards

CARD_WIDTH=SIDE//6
CARD_HEIGHT=SIDE//4

#this is min value of WIDTH to keep cards and buttons separate
WIDTH=BORDER+6*CARD_WIDTH+5*BORDER_BTW + BORDER_BTW + BORDER+2*CARD_WIDTH+BORDER_BTW
      #for cards                       separator             for buttons

#define fonts
FONT_NAME='Arial'

#define colors
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(220,20,60)
GREEN=(50,205,50)
BLUE=(0,150,255)
YELLOW=(255,255,0)
PURPLE=(153,50,204)
GRAY=(128,128,128)
ORANGE=(255,128,0)
GOLD=(255,215,0)