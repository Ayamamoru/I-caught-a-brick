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

    scene bg room

    # Remember to define all the characters and sprites before using them. THANKS FUTURE MO

    show eileen happy


    f "You've created a new Ren'Py game."

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
