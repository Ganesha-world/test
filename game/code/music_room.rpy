init python:


    mr = MusicRoom(fadeout=1.0)


    mr.add("music/Title Theme.mp3", always_unlocked=True)
    mr.add("music/Jason's Theme.mp3", always_unlocked=True)
    mr.add("music/Sarah's Theme.mp3", always_unlocked=True)
    mr.add("music/Sarah's Theme alt.mp3", always_unlocked=True)
    mr.add("music/Noelle's Theme.mp3", always_unlocked=True)
    mr.add("music/Noelle's Alternate Theme.mp3", always_unlocked=True)
    mr.add("music/Jane's Theme.mp3", always_unlocked=True)
    mr.add("music/Jane's Theme alt slow.mp3", always_unlocked=True)
    mr.add("music/Jane's Theme alt fast.mp3", always_unlocked=True)
    mr.add("music/Kira's Theme.mp3", always_unlocked=True)
    mr.add("music/Kira's Theme alt.mp3", always_unlocked=True)


    mr.add("music/ost/Da Capa al Fine _pizz_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Deep Breaths _Flute_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Deep Breaths _Guitar_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Deep Breaths _Piano_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Deep Breaths _Strings_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/habanera 3.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Snowflake Lullaby _Piano_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/Snowflake Lullaby _Piano+Strings_.ogg.opus", always_unlocked=True)
    mr.add("music/ost/The_Master_Plan.ogg.opus", always_unlocked=True)




scene bg house 1


screen music_room:
    tag menu
    modal False


    add "music_room_bg"




    frame:
        yalign 0.5
        xalign 0.5
        xsize 900
        ysize 650

        vbox:
            yalign 0.5
            xalign 0.2
            spacing 5

            textbutton "Title Theme":
                action mr.Play("music/Title Theme.mp3")
            textbutton "Jason's Theme":
                action mr.Play("music/Jason's Theme.mp3")
            textbutton "Sarah's Theme":
                action mr.Play("music/Sarah's Theme.mp3")
            textbutton "Sarah Hypnotized":
                action mr.Play("music/Sarah's Theme alt.mp3")
            textbutton "Noelle's Theme":
                action mr.Play("music/Noelle's Theme.mp3")
            textbutton "Noelle Hypnotized":
                action mr.Play("music/Noelle's Alternate Theme.mp3")
            textbutton "Jane's Theme":
                action mr.Play("music/Jane's Theme.mp3")
            textbutton "Jane's Hypnotized":
                action mr.Play("music/Jane's Theme alt slow.mp3")
            textbutton "Jane's Hypnotized Chaos":
                action mr.Play("music/Jane's Theme alt fast.mp3")
            textbutton "Kira's Theme":
                action mr.Play("music/Kira's Theme.mp3")
            textbutton "Kira Hypnotized":
                action mr.Play("music/Kira's Theme alt.mp3")
            null height 20


        vbox:
            yalign 0.5
            xalign 0.8
            spacing 5

            textbutton "Da Capa al Fine":
                action mr.Play("music/ost/Da Capa al Fine _pizz_.ogg.opus")
            textbutton "Deep Breaths - Flute":
                action mr.Play("music/ost/Deep Breaths _Flute_.ogg.opus")
            textbutton "Deep Breaths - Guitar":
                action mr.Play("music/ost/Deep Breaths _Guitar_.ogg.opus")
            textbutton "Deep Breaths - Piano":
                action mr.Play("music/ost/Deep Breaths _Piano_.ogg.opus")
            textbutton "Deep Breaths - Strings":
                action mr.Play("music/ost/Deep Breaths _Strings_.ogg.opus")
            textbutton "Habanera":
                action mr.Play("music/ost/habanera 3.ogg.opus")
            textbutton "Snowflake Lullaby - Piano":
                action mr.Play("music/ost/Snowflake Lullaby _Piano_.ogg.opus")
            textbutton "Snowflake Lullaby - Piano and Strings":
                action mr.Play("music/ost/Snowflake Lullaby _Piano+Strings_.ogg.opus")
            textbutton "The Master Plan":
                action mr.Play("music/ost/The_Master_Plan.ogg.opus")


        hbox:
            yalign 1.0
            xalign 0.5
            spacing 20

            textbutton "Next Track" action mr.Next()
            textbutton "Previous Track" action mr.Previous()
            null height 20


            textbutton "Main Menu" action ShowMenu("main_menu")




    on "replace" action mr.Play()


    on "replaced" action Play("music", "music/Title Theme.mp3")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
