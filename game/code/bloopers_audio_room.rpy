init python:

    bp = MusicRoom(fadeout=1.0)




    bp.add("music/BonusAudio/Snow Daze Bloopers/Jane/Jane_Bloops_1.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Jane/IS THAT A FRIGGIN LION.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Jane/Jason's Line.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Jane/You Wreckin.ogg", always_unlocked=True)


    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/A Challenging Kira.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/D09KiraL0003.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/If anyone complains ill letcha know.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/jason shops at hot topic.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/Outtake01.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/Outtake02.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/post hypnosis talk disorder.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/Same TBH.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/shuck fit.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Kira/When Your Sisters Call The Cops.ogg", always_unlocked=True)


    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/1.wav", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper2.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper3.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/D05NoelleBlooper.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Noelle/D05NoelleBlooper2.ogg", always_unlocked=True)


    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/1.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/enthusiatic gnawing.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/ghost blowjob wooo wooooo.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/hypnosis gon awry.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/mad libbing.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/please put this on the bad end screen.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/Sarah Gets Cum In Her Hair And Comments On It After Jason Leaves.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/sarah reacts to playing the game.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/sarah researches her character.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/SarahOuttake01.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/sonic clock.ogg", always_unlocked=True)
    bp.add("music/BonusAudio/Snow Daze Bloopers/Sarah/squeak.ogg", always_unlocked=True)


    page_max = 7
    blooper_page = 0

    class BlooperStory:
        def __init__(self, title, track):
            self.title = title
            self.track = track

    blooper_stories = []


    blooper_stories.append(BlooperStory(
    "Jane Blooper #1",
    "music/BonusAudio/Snow Daze Bloopers/Jane/Jane_Bloops_1.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "IS THAT A FRIGGIN LION",
    "music/BonusAudio/Snow Daze Bloopers/Jane/IS THAT A FRIGGIN LION.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Jason's Line",
    "music/BonusAudio/Snow Daze Bloopers/Jane/Jason's Line.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "You Wreckin",
    "music/BonusAudio/Snow Daze Bloopers/Jane/You Wreckin.ogg"
    ))


    blooper_stories.append(BlooperStory(
    "A Challenging Kira",
    "music/BonusAudio/Snow Daze Bloopers/Kira/A Challenging Kira.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Kira Bloop",
    "music/BonusAudio/Snow Daze Bloopers/Kira/D09KiraL0003.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "If Anyone Complains I'll Letcha Know",
    "music/BonusAudio/Snow Daze Bloopers/Kira/If anyone complains ill letcha know.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Jason Shops at Hot Topic",
    "music/BonusAudio/Snow Daze Bloopers/Kira/jason shops at hot topic.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Kira Outtake 01",
    "music/BonusAudio/Snow Daze Bloopers/Kira/Outtake01.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Kira Outtake 02",
    "music/BonusAudio/Snow Daze Bloopers/Kira/Outtake02.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Post Hypnosis Talk Disorder",
    "music/BonusAudio/Snow Daze Bloopers/Kira/post hypnosis talk disorder.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Same tbh",
    "music/BonusAudio/Snow Daze Bloopers/Kira/Same TBH.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Shuck Fit",
    "music/BonusAudio/Snow Daze Bloopers/Kira/shuck fit.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "When Your Sisters Call The Cops",
    "music/BonusAudio/Snow Daze Bloopers/Kira/When Your Sisters Call The Cops.ogg"
    ))


    blooper_stories.append(BlooperStory(
    "Noelle Bloop",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/1.wav"
    ))
    blooper_stories.append(BlooperStory(
    "Noelle Day 4 Blooper #1",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Noelle Day 4 Blooper #2",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper2.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Noelle Day 4 Blooper #3",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/D04NoelleBlooper3.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Noelle Day 5 Blooper #1",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/D05NoelleBlooper.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Noelle Day 5 Blooper #2",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/D05NoelleBlooper2.ogg"
    ))


    blooper_stories.append(BlooperStory(
    "Sarah Bloop",
    "music/BonusAudio/Snow Daze Bloopers/Noelle/1.wav"
    ))
    blooper_stories.append(BlooperStory(
    "Enthusiastic Gnawing",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/enthusiatic gnawing.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Hypnosis Gone Awry",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/hypnosis gon awry.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Mad Libbing",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/mad libbing.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Please Put This on the Bad End Screen",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/please put this on the bad end screen.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Sarah Gets Cum in Her Hair",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/Sarah Gets Cum In Her Hair And Comments On It After Jason Leaves.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Sarah Reacts to Playing The Game",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/sarah reacts to playing the game.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Sarah Researches Her Character",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/sarah researches her character.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Sarah Outtake 01",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/SarahOuttake01.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Sonic Clock",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/sonic clock.ogg"
    ))
    blooper_stories.append(BlooperStory(
    "Squeak",
    "music/BonusAudio/Snow Daze Bloopers/Sarah/squeak.ogg"
    ))


image bloop HI2:
    "images/CGS/Extended/HomeInvasion02.webp"
image bloop HI3:
    "images/CGS/Extended/HomeInvasion03.webp"
image bloop HI4:
    "images/CGS/Extended/HomeInvasion04.webp"
image bloop HI5:
    "images/CGS/Extended/HomeInvasion05.webp"

image rando_hi_bg:
    choice:
        "bloop HI2"
    choice:
        "bloop HI3"
    choice:
        "bloop HI4"
    choice:
        "bloop HI5"




screen blooper_audio_room:
    tag menu
    modal False
    add "#FFF"

    $ ah = blooper_page * page_max
    $ um = min(ah + page_max - 1, len(blooper_stories) - 1)

    add "rando_hi_bg":
        yalign 1.0
        xalign 0.0

    frame:
        background None
        yalign 0.5
        xalign 0.9
        xsize 700
        ysize 650

        label "Bloopers":
            text_color "#000"
            yalign 0.1
            xalign 0.0
        null height 80


        hbox:
            yalign 0.5
            xalign 0.2
            spacing 8
            vbox:
                for i in range(ah, um + 1):
                    textbutton blooper_stories[i].title:
                        style "check_button"
                        text_color "#000"

                        action bp.Play(blooper_stories[i].track)
            null height 80

        hbox:
            yalign 1.0
            xalign 0.5
            spacing 40
            if blooper_page > 0:
                textbutton "Previous Page":
                    text_color "#000"
                    action SetVariable("blooper_page", blooper_page - 1)
            if (blooper_page + 1) * page_max < len(blooper_stories):
                textbutton "Next Page":
                    text_color "#000"
                    action SetVariable("blooper_page", blooper_page + 1)
            null height 20


            textbutton "Main Menu" action [bp.Stop(), ShowMenu("main_menu")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
