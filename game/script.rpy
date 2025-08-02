# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Fish", color="#049bff")
define mc = Character("[povname]", color="#00e1ff")
define b = Character("Brick", color="#ff7f44")


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    f "You've created a new Ren'Py game."

    $ povname = renpy.input("What is your name?", length=20)
    $ povname = povname.strip()


    if not povname:
        $ povname = "Morter"
    
    mc "Hello, Fish. I am [povname]."
    
    b "I am Brick, the best friend of Fish."
    b "also you frickin suck at this game, Morter."
    
    return
