# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Fish", color="#049bff")
define mc = Character("[povname]", color="#be6ae6")
define b = Character("Brick", color="#ff7f44")
define t = Character("Teacher", color="#ff0000")
define cb = Character("Club President", color="#ff00ff")
define n = Character("Noona", color="#2938ff")
define m = Character("Mo", color="#b8fdb8")
define e = Character("Eriss", color="#ffb8b8")
define k = Character("Rock", color="#ffb8b8")
define bad_points = 0
define good_points = 0
define neutral_points = 0
define platonic_points = 0
define occult_end = False
define arcade_end = False
transform halfsize():
    zoom 0.9
image top_text = ParameterizedText(xalign=0.0, yalign=0.0, color="#ffffff", size=30)
   
label start:
    stop music fadeout 1.5
    play sound "mixkit-gear-fast-lock-tap-2857.wav"
    # So uhm yeah, this is a game.
    #jk anyways this is the START OF GAME (reminder to self, please remember to define everything before using it or else debugging will be a pain)
   
    $ bad_points = 0
    $ good_points = 0
    $ neutral_points = 0
    $ platonic_points = 0
    $ occult_end = False
    $ arcade_end = False
    image passive = "passive.png"
    image bg room = "BG PLACEHOLDER.jpg"
    image fish = "fish.png"

    scene bg room

    # Remember to define all the characters and sprites before using them... cause renpy will get angry if no. THANKS FUTURE MO

    show fish at center

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
    f "Plus, he's wasting his high school life, already a sophomore but nothing to show for it..."
    f "So I need you to do me a favor."
    mc "uhmmmm ok..."
    "You decide to humor the fish, even though you feel like you are losing your mind."
    "Of couese, you are not going to do anything crazy like helping a fish, but you feel like you should at least hear it out."
    f "I will give you $500 if you get this guy out of the house and become his friend."
    f "You seem pretty broke."
    "ah... $500 is a lot of money, and you are pretty broke."
    "Unfortunately you're also the type of person to be easily swayed by money..."


    menu option_2:
      "Accept the fish's request":
         $ good_points += 1
         jump accept_request
      "Decline the fish's request":
         $ bad_points += 1
         jump no_500_fish
      "Try throwing the fish back on the ground":
         $ neutral_points += 1 
         jump slam_fish

label slam_fish:
    hide top_text
    stop music fadeout 1
    "You decide to throw the fish back on the ground."
    play sound "Vine boom.mp3" volume 0.5
    show top_text "Vine Boom"
    "It doesn't seem to work, for some reason, your hands are still holding the fish."
    hide top_text
    "Maybe the fish is magic... i mean, it can talk so unless you are hallucinating, it must be magic."
    "You decide to try accepting the fish's request - anything to get it off your hands faster... its slimy and gross."
    jump accept_request

label accept_request:
    play music "1.043 - Temmie Village.flac" fadein 3.0 
    show top_text "Temmie Village - Undertale OST, by Toby Fox"
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
    f "goodbye, twerp. See you in a week."
    hide fish
    "The fish gives you a piece of paper with a timetable on it."
    "You look at the timetable and see that the owner is Brick, your classmate"
    "You remember that Brick seems to be a huge introvert and is in your art club and game club."
    "It also looks like you have the same history class."
    "Wait, how are you holding the paper if you are holding the fish?"
    stop music fadeout 3.0
    hide top_text
    "You look down and see that the fish is gone..."
    "How did it even give you the paper?"
    "You feel like you are losing your mind, but you decide to just go home and start planning how to become Brick's friend tomorrow."

    "The next morning at school..."
    "You get to school 15 minutes before classes start"
    mc " I don't really want to go to class yet, maybe the game club is open?"

    menu option_3:
      "Go to the game club":
         $ good_points += 1
         jump morning_game_club
      "Go to class":
         $ bad_points += 1
         jump ignore_game_club
      "Play games on your phone" if neutral_points > 0:
         $ neutral_points += 1
         jump ignore_play_games
    
label morning_game_club:
    "You decide to go to the game club."
    "There are a few people there, but you don't see Brick."
    "The club president brought some board games and is playing with a few other members."
    "OH... would you look at that!"
    mc "KITTTYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
    "You see the club president's cat sitting on a desk, pet carrier on the floor."

    menu option_4:
      "Pet the cat":
         $ good_points += 1
         jump pet_cat
      "Don't pet the cat":
         $ bad_points += 1
         jump ignore_cat

#These are sub-option for option 3's label of good points
label pet_cat:
    "You decide to pet the cat."
    "The cat is very fluffy and purrs when you pet it."
    "You no longer want to go to class at all and just want to pet the car"
    "You idly chat with the club members and pet the cat for a while."
    b "Hey kitty, here's your water."
    show passive at left,with moveinleft
    "You turn around and see Brick, he has a collapsible water bowl in his hands."
    "Looks like he went to the water fountain to fill it up."
    b "..."
    mc "..."
    "You feel like you should say something, but you also feel like-"
    "oh, you've both been distracted by the cat."
    "You both reach a silent understanding that you both love cats and that you both want to pet the cat."
    "Both of you pet the cat and you feel the urge to make small talk"
    mc "So, you like cats?"
    b "Yeah"
    mc "I like cats too."
    b "Do you have a cat?"
    mc "No, I don't, I'm too broke to have a cat."
    b "Oh. I have a fish so I can't get a cat."
    mc "Oh, maybe one day we will both get cats."
    b "Yeah."
    hide passive with moveoutleft
    "You both reach a mutual understanding and continue to pet the cat in a more comfortable silence."
    "You feel like you made a lot of progress and both of you head to class together in silence."
    jump class_morning



label ignore_cat:
    "You decide not to pet the cat."
    "How can you resist the urge to pet the cat?"
    "You must be a monster."
    "You decide to join the club members and play some board games."
    "You play some games for a while, but you feel like you should probably go to class soon."
    "You look up while tidying up the game pieces and see Brick sitting in the corner of the room."
    "He's playing with the cat and seems to be having a good time."
    "You feel like you should make some small talk but the bell rings and you have no choice but to go to class."
    jump class_morning

# This is the end of the sub-option for option 3's label of good points
# Here is the label for the class morning (So I don't mix it up)
label class_morning:
    "The teacher is already in the classroom and is setting up for the class."
    "You decide to sit next to Brick, who is sitting in the back of the class."
    "The class is a boring lecture, so you idley doodle in your sketchbook"
    b "I like your drawing."
    "You look up and see Brick peering at your doodles subtly"
    mc "Oh, thanks."
    "The class continues with Brick looking at your doodles while you keep doodling."
    "It's a bit awkward, but it isn't too bad."
    "Class ends and you both pack up your things."
    "You wonder if the game club is open today or if you should head to the cafeteria for lunch."
    jump option_5



label ignore_play_games:
    "You decide to settle in the school courtyard and play some games on your phone."
    "You play some games for a while, but you feel like you should probably go to class soon."
    play music "32 - Run!.mp3" fadein 1.0 
    show top_text "Run! - Undertale OST, by Toby Fox"
    "What luck... it starts POURING RAIN... ON YOUR PHONE."
    "You quickly put your phone away and run to the school building."
    "THE DOORS ARE LOCKED."
    mc "HEYYYYYY OPEN THE DOOR"
    "You knock furiously on the door, but it looks like nobody hears you"
    "You see someone passing by to reach the water fountain and knock harder on the door."
    "You catch their attention and they open the door for you."
    stop music fadeout 1.0
    hide top_text
    mc "THANK YOU SO MUCH"
    b "Oh- no problem."
    "You're in such a hurry that you don't even notice who it is as you scurry off to the washroom to dry off."
    "Meanwhile Brick shrugs and continues filling up the bowl he was holding with water."
    "You dry off in the washroom and look at yourself in the mirror."
    "You look like a wet rat, ew."
    "You sigh and head to class, hoping that nobody will notice the water dripping off your hair."
    jump class_boring


# This is the label for ignoring the game club - LEads to a neutral point path


label ignore_game_club:
    "You decide to be a good student and head to class early."
    "The classroom is about half full, and you see Brick sitting in the back of the class."
    "You decide to sit next to him for now."
    "But you're suddenly reminded that you are also..."
    "AN INTROVERT."
    "You feel like you should talk to him, but you also feel like you should just sit quietly and not bother him."
    "You spend too much time thinking about it, and the teacher comes in to start class."
    "You have no choice but to sit quietly and wait until class ends"
    jump class_boring


label class_boring:
    "Your teacher drones on and on about the history of... something. You weren't paying attention. You feel your eyelids getting heavier."
    "You try to pay attention, but the lecture is so boring that you can't help but doze off."
    t "Please pay attention, class."
    "Your head jerks up slightly as you realize that you were about to fall asleep."
    "You look around and see that most of the class is also struggling to stay awake."
    mc "Oh jeez this class is so boring....."
    "You look over to the right, at Brick, who is also struggling to stay awake."
    "You sigh and hide behind your textbook, dozing off again."
    "You wake up to the sound of the bell ringing, signaling the end of class."
    mc "*waking up sounds idk man*"
    "You look around and see that most of the class is already packing up their things."
    "You quickly pack up your things and head out of the classroom."
    "You wonder if the game club is open today or if you should head to the cafeteria for lunch"

menu option_5:
    "Go check the game club":
            $ good_points += 1
            jump check_game_club
    "Head to the cafeteria":
            $ bad_points += 1
            jump ignore_game_club_cafeteria
    "Wander around the school":
            $ neutral_points += 1
            jump ignore_wander_around
    "Go to ??? club" if bad_points >= 3:
            $ bad_points += 1
            jump cult_club


label check_game_club:
    "You decide to go check the game club."


label ignore_game_club_cafeteria:
    "You decide to head to the cafeteria for lunch."
    "Your friends all have lunch-time extracurriculars today, so you just sit down at a random table"
    "You decide to develop your plan to become friends with Brick a little more"
    "You're not too confident in your social decisions so it seems better to plan it out first"
    "After about 25 minutes of contemplating, you manage to make a somewhat feasible plan"
    "Your plan is to go find him and talk for the rest of the lunch break"
    "On the way to the cafeteria, it seemed like the game club was open"
    "You decide to test your luck and see if Brick is there."
    "Just your luck! He's in the corner playing with the club president's cat"
    "You're at a loss for small talk topics so you decide to start a conversation about his fish"
    jump weird_game_club

label ignore_wander_around:
    "You decide to wander around the school for a bit."
    "There isn't much going on. The school year has only just begun, so all the freshmen were calleed to the club fair"
    "The hallways are much quieter since many of the non-freshmen have extracurriculars at lunch"
    "You wander around and peek into a few classrooms, checking out club activities"
    "There isn't much to see though, so after a long while you think it might be best to head to class early"
    "You remember the game club is likely still open too"

menu option_7:
    "Head to class early":
        $ neutral_points += 1
        jump early_after_class
    "Check out the game club":
        $ good_points += 1
        jump check_game_club
        
label cult_club:
    "You decide to go to the ??? club."
    "You walk to the club room and knock on the door."
    "The door opens and you see a group of people sitting in a circle, chanting something."
    "You shrug and slip inside, closing the door behind you."
    play music "28 - Premonition.mp3" fadein 1.0 
    show top_text "Premonition - Undertale OST, by Toby Fox"
    mc "Hi everyone."
    "The group stops chanting and looks at you. The club vice president Eriss greets you."
    e "Hey club president, we were just practicing our chant."
    mc "Sorry for interrupting, just figured we should get the meeting started."
    e "Oh, no problem, we were just waiting for you."
    "You sit down in the circle and look around at the other members."
    mc "We have some new members today - Welcome to the occult club everyone!"
    mc "I have an encounter to share with you all."
    "You proceed to tell the club about your encounter with the fish."
    e "Wow, that's really interesting."
    e "I wonder if the fish is a sign from the gods."
    mc "I don't know, but it was definitely a weird experience."
    e "Maybe we should try to use the fish as a medium for our next ritual."
    mc "That's not a bad idea."
    e "We could try to summon the fish spirit and ask it for guidance."
    mc "Sure, we can try that. Let's set up a ritual for next week's meeting."
    "You spend the rest of the meeting discussing the fish and its possible significance."
    stop music fadeout 1.0
    hide top_text
    $ occult_end = True

    "After the meeting, you feel like you made some progress with the occult club."


    "There's some time before the next block of classes, so you decide to head to the game club to see if Brick is there."
    "You find Brick sitting in the corner of the room, playing with the club president's cat."

menu option_6:
    "Ask Brick about his fish" if occult_end == True:
            $ bad_points += 1
            jump weird_game_club
    "Make small talk and get to know him" if occult_end == False:
            $ platonic_points += 1
            jump convo_chat
    "Join the other club members and play a board game":
            $ good_points += 1
            $ occult_end = False

label weird_game_club:
    "You put aside your nerves and approach Brick"
    mc "Hey Brick, do you have a fish?"
    b "Uhm yeah, I do"
    b "why?"
    mc "oh I was just curious - I really like fish ya know"
    mc "What type of fish is it?"
    b "I don't actually know, I got it from the side of the road"
    mc "huh?"
    b "This guy was selling fish on the side of the road so my sister got me one"
    b "I've had my fish for like 6 years"
    mc "Oh wow. That's a long time."
    mc "My childhood fish never lived over a month... poor souls..."
    b "..."
    mc "Anyways - What's your fish's name?"
    b "Oh, I never gave it a name"
    mc "huh?"
    b "I always just called my fish 'Fish'"
    b "I was waiting to think of a really good name for it but I never did"
    b "And it feels weird to rename it now so uhm"
    b "Yeah my fish's name is just Fish"
    mc "oh, well hey that's still cool"
    "You feel like you should try to talk more about the actual fish, and not it's onomatology"
    mc "Maybe it was just me but do you ever talk to your fish?"
    mc "I used to talk to my fishes"
    b "What?"
    b "Oh. How did you know? Yeah, I talk to my fish."
    mc "isn't that kinda weird?"
    "You accidently slip up and quickly change the topic, not wanting to accidently offend Brick"
    mc "Oh, what do you say to it?"
    b "Uhm....."
    b "Just whatever?"
    b "My sister went to university a few years ago so I don't really have anyone to talk to most of the time"
    b "So I just say whatever comes to mind"
    mc "That's nice"
    mc "Do you think your fish understands you?"
    b "Well no... I mean, it's a fish"
    mc "But what if it could talk?"
    b "Uhm, I never really thought of that"
    mc "But wouldn't that be cool???"
    b "Maybe?"

    "Your conversation is cut short by the bell for the afternoon block of classes"

    if occult_end == False:
        "Unfortunatly, you can't contine your conversation because you don't have the same class as Brick"
    "You feel like you didn't gain much information, but any progress is progress."

    if occult_end == True:
        "Unfortunatly, you can't continue your investigation because you don't have the same class as Brick"
    "You head to class, still pondering the fish"


label convo_chat:


    show passive at right

    b "I am Brick, the best friend of Fish."
    b "also you frickin suck at this game, [povname]."
    
    return
