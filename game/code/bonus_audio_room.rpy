init python:

    ba = MusicRoom(fadeout=1.0)




    ba.add("music/BonusAudio/BBA3_Noelle helps sarah plan an outfit.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/BA3_Kira Excercising.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/BA3_Sarah Teaching Jane how to kiss.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/BA3_Sarah-Acting Classes.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/BA3_Wins Jane From a Bet.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/BBA3_Noelle Reprograms Kira.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Noelle - Teaching Jason to Kiss.mp3", always_unlocked=True)



    ba.add("music/BonusAudio/Jane - Wrestling.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Jane - Wrestling - No SFX.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Jane - Photography Practice.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Kira - Best at Making Out.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Kira and Sarah - Shower.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Kira and Sarah - Shower TV.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Kira Exhibitionist Streak v2.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Kira Jane Sarah - Fashion Show.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Noelle - House Rules.mp3", always_unlocked=True)
    ba.add("music/BonusAudio/Noelle - You're The Boss.mp3", always_unlocked=True)



    ba.add("music/BonusAudio/BA4_Jane End.wav", always_unlocked=True)
    ba.add("music/BonusAudio/BA4_Kira End.wav", always_unlocked=True)
    ba.add("music/BonusAudio/BA4_Noelle End.wav", always_unlocked=True)
    ba.add("music/BonusAudio/BA4_Sarah End.wav", always_unlocked=True)






    page_max = 7
    story_page = 0

    class BonusStory:
        def __init__(self, title, track):
            self.title = title
            self.track = track

    bonus_stories = []

    bonus_stories.append(BonusStory(
    "Noelle Helps Sarah Plan an Outfit",
    "music/BonusAudio/BBA3_Noelle helps sarah plan an outfit.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira Exercising",
    "music/BonusAudio/BA3_Kira Excercising.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Sarah Teaching Jane How to Kiss",
    "music/BonusAudio/BA3_Sarah Teaching Jane how to kiss.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Sarah's Acting Classes",
    "music/BonusAudio/BA3_Sarah-Acting Classes.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Jane and a Bet",
    "music/BonusAudio/BA3_Wins Jane From a Bet.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Noelle Reprograms Kira",
    "music/BonusAudio/BBA3_Noelle Reprograms Kira.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Noelle Teaching Jason to Kiss",
    "music/BonusAudio/Noelle - Teaching Jason to Kiss.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Jane Wrestling",
    "music/BonusAudio/Jane - Wrestling.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Jane Wrestling - no SFX",
    "music/BonusAudio/Jane - Wrestling - No SFX.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Jane Photography Practice",
    "music/BonusAudio/Jane - Photography Practice.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira Best at Making Out",
    "music/BonusAudio/Kira - Best at Making Out.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira and Sarah Shower",
    "music/BonusAudio/Kira and Sarah - Shower.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira and Sarah Shower TV",
    "music/BonusAudio/Kira and Sarah - Shower TV.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira Exhibitionist Streak",
    "music/BonusAudio/Kira Exhibitionist Streak v2.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Kira Jane and Sarah Fashion Show",
    "music/BonusAudio/Kira Jane Sarah - Fashion Show.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Noelle House Rules",
    "music/BonusAudio/Noelle - House Rules.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Noelle You're the Boss",
    "music/BonusAudio/Noelle - You're The Boss.mp3"
    ))

    bonus_stories.append(BonusStory(
    "Jane Ending",
    "music/BonusAudio/BA4_Jane End.wav"
    ))

    bonus_stories.append(BonusStory(
    "Kira Ending",
    "music/BonusAudio/BA4_Kira End.wav"
    ))

    bonus_stories.append(BonusStory(
    "Noelle Ending",
    "music/BonusAudio/BA4_Noelle End.wav"
    ))

    bonus_stories.append(BonusStory(
    "Sarah Ending",
    "music/BonusAudio/BA4_Sarah End.wav"
    ))





image bcg jane_photo:
    "images/CGS/BonusAudio/bcg_janephotographypractice.webp"
    zoom 0.18
image bcg kira_makeout:
    "images/CGS/BonusAudio/bcg_kirabestatmakingout.webp"
    zoom 0.18
image bcg kira_exhibitionist:
    "images/CGS/BonusAudio/bcg_kiraexhibitioniststreak.webp"
    zoom 0.18
image bcg kira_jane_fashion:
    "images/CGS/BonusAudio/bcg_kirajanesarahfashionshow.webp"
    zoom 0.18
image bcg kira_sarah_shower:
    "images/CGS/BonusAudio/bcg_kirasarahshowertv.webp"
    zoom 0.18
image bcg noelle_sarah_plan:
    "images/CGS/BonusAudio/bcg_noellehelpssarahplan.webp"
    zoom 0.18
image bcg noelle_house_rules:
    "images/CGS/BonusAudio/bcg_noellehouserules.webp"
    zoom 0.18
image bcg noelle_boss:
    "images/CGS/BonusAudio/bcg_noelletheboss.webp"
    zoom 0.18
image bcg sarah_homework:
    "images/CGS/BonusAudio/bcg_sarahhomework.webp"
    zoom 0.18

image rando_bcg_bg:
    choice:
        "bcg jane_photo"
    choice:
        "bcg kira_makeout"
    choice:
        "bcg kira_exhibitionist"
    choice:
        "bcg kira_jane_fashion"
    choice:
        "bcg kira_sarah_shower"
    choice:
        "bcg noelle_sarah_plan"
    choice:
        "bcg noelle_house_rules"
    choice:
        "bcg noelle_boss"
    choice:
        "bcg sarah_homework"


screen bonus_audio_room:
    tag menu
    modal False
    add "#FFF"

    $ ah = story_page * page_max
    $ um = min(ah + page_max - 1, len(bonus_stories) - 1)

    add "rando_bcg_bg":
        yalign 1.0
        xalign 0.0

    frame:
        background None
        yalign 0.5
        xalign 0.9
        xsize 700
        ysize 650

        label "Bonus Stories":
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
                    textbutton bonus_stories[i].title:
                        style "check_button"
                        text_color "#000"

                        action ba.Play(bonus_stories[i].track)
            null height 80


















        hbox:
            yalign 1.0
            xalign 0.5
            spacing 40
            if story_page > 0:
                textbutton "Previous Page":
                    text_color "#000"
                    action SetVariable("story_page", story_page - 1)
            if (story_page + 1) * page_max < len(bonus_stories):
                textbutton "Next Page":
                    text_color "#000"
                    action SetVariable("story_page", story_page + 1)
            null height 20


            textbutton "Main Menu" action [bp.Stop(), ShowMenu("main_menu")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
