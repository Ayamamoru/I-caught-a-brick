# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Fish", color="#049bff")
define mc = Character("[povname]", color="#00e1ff")
define b = Character("Brick", color="#ff7f44")
define bad_points = 0
define good_points = 0
define neutral_points = 0
transform halfsize():
    zoom 0.9

label start:

    # So uhm yeah, this is a game.
    #jk anyways this is the START OF GAME (reminder to self, please remember to define everything before using it or else debugging will be a pain)
   
    $ bad_points = 0
    $ good_points = 0
    $ neutral_points = 0
    image passive = "passive.png"
    image bg room = "BG PLACEHOLDER.jpg"

    scene bg room

    # Remember to define all the characters and sprites before using them... cause renpy will get angry if no. THANKS FUTURE MO

    show eileen happy

    "You're walking down the street on your way back home from school."
    
    f "flop flop flop"

    "Huh? What was that sound? You look around..."
    "And see a fish flopping around on the ground."

    f "*fish sounds*"

    "You look around, but there is no water in sight... besides the sewer grate. Ew."
    "Well, it looks slimy... but you can't just leave it there..."

    menu option_1:
      "Ignore the fish and keep walking":
         $ bad_points += 1
         jump ignore_fish
      "Pick up the fish":
         $ good_points += 1
         jump help_fish

label help_fish:
    "You pick up the fish and..."
    "Well, you didn't really think that far"
    "You hold the fish in your hands utterly confused and helpless."
    jump fish_talk

label ignore_fish:
    "You decide to ignore the fish and keep walking."
    f "HEY YOU"
    "The fish... yells at you?!?!?!?"
    jump fish_talk

label fish_talk:
    $ povname = renpy.input("What is your name?", length=50)
    $ povname = povname.strip()


    if not povname:
        $ povname = "Morter"
    
    mc "Hello, Fish. I am [povname]."

    hide eileen happy

    show passive at right

    b "I am Brick, the best friend of Fish."
    b "also you frickin suck at this game, [povname]."
    
    return
