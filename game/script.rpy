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
image top_text = ParameterizedText(xalign=0.0, yalign=0.0, color="#ffffff", size=30)
   
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
    f "Hey. Thanks for picking me up."
    f "the floor is so dirty ew"
    f "though honestly I don't know what you expected to do with me."
    f "and your hands don't look very clean either."
    f "anyways, where are your manners, twerp?"
    f "introduce yourself to me, the great Fish."
    jump fish_talk

label ignore_fish:
    "You decide to ignore the fish and keep walking."
    f "HEY YOU"
    "The fish... yells at you?!?!?!?"
    f "what's your name, twerp?"
    "You feel perplexed and suddenly have the urge to pick up the fish"
    jump fish_talk

label fish_talk:
    play music "1.043 - Temmie Village.flac" fadein 3.0 volume 0.5

    show top_text "Temmie Village - Undertale OST, by Toby Fox"

    $ povname = renpy.input("What is your name?", length=50)
    $ povname = povname.strip()


    if not povname:
        $ povname = "Morter"
    
    mc "Uhmmmmmm I'm [povname]."
    f "Well, [povname], I am Fish."
    f "You look like a student, so I guess you go to school... though I don't know why you would go to school when you could just be a fish like me."
    f "which school do you go to?"
    mc "uhmmm I go to Athena High School."
    mc "since when can fish talk?"
    mc "and why do you keep insulting me?"
    f "I can talk because I am a fish with a very high IQ."
    f "and anyways, I am not insulting you, I am just stating facts."
    f "and you are a student, so I guess you are not very smart."
    f "But it's good that you go to Athena. I heard that they have a very good program for students who are not very smart."
    f "but I also have a request for you, [povname]."
    mc "what?!?!??!?!?!?!"
    "You feel a bit offended, but you also feel like you should hear the fish out... but you also start to feel that you must be absolutely insane to be talking to a fish."
    f "my owner is a very quiet person"
    f "He's too much of a coward to talk to people, so he just sits in his room all day and plays video games."
    f "The poor lad is so lonely he even talks to me, a fish."
    f "I'm not very keen on listening to him talk about his life though. I have my own life to live, you know?"
    f "So I need you to do me a favor."
    mc "uhmmmm ok..."
    "You decide to humor the fish, even though you feel like you are losing your mind."
    "Of couese, you are not going to do anything crazy like helping a fish, but you feel like you should at least hear it out."
    f "I will give you $500 if you get this guy out of the house and become his friend."
    f "You seem pretty broke."
    "ah... $500 is a lot of money, and you are pretty broke."


    menu option_2:
      "Accept the fish's request":
         $ good_points += 1
         jump accept_request
      "Decline the fish's request":
         $ bad_points += 1
         jump no_500_fish

label accept_request:
    "You decide to accept the fish's request."
    mc "let me see the monet first."
    f "I will give you the money once you complete the task."
    mc "I don't trust you, fish."
    f "I am a fish of my word, [povname]."
    f "I will give you the money once you complete the task."
    f "But if I really must, I can give you $50 as a down payment."
    "You feel like you should at least get something out of this, so you decide to accept the $50."
    mc "ok, I will do it."
    jump task_details
    
label no_500_fish:
    "You decide to decline the fish's request."
    mc "uhM, NO THANKS."
    f "You are a very rude person, [povname]."
    f "I was going to give you $500, but now I will not."
    mc "uhm"
    f "huh, you drive a hard bargain, [povname]."
    f "I wonder who taught you to haggle like that."
    mc "what?"
    f "Argh, fine, you will. I will give you $800 if you complete the task."
    f "and a $100 down payment."
    "You feel like that's a lot of money, and you are pretty broke."
    "you thought it was a scam but it seems like the fish is serious about this."
    mc "ok, I will do it."
    jump task_details

label task_details:
    f "the task is simple. I need you to get my owner out of the house and become his friend."
    f "I will give you his time table so go become his school friend."
    f "goodbye, twerp"
    hide eileen happy
    "The fish gives you a piece of paper with a timetable on it."
    "You look at the timetable and see that the owner is Brick, your classmate"
    "You remember that Brick seems to be a huge introvert and is in your art class and game club."
    "Wait, how are you holding the paper if you are holding the fish?"
    stop music fadeout 3.0
    hide top_text
    "You look down and see that the fish is gone..."
    "How did it even give you the paper?"
    "You feel like you are losing your mind, but you decide to just go home and start planning how to become Brick's friend tomorrow."

    show passive at right

    b "I am Brick, the best friend of Fish."
    b "also you frickin suck at this game, [povname]."
    
    return
