








label day1start:
    $ jane_outfit.CanonOutfit = JaneOutfitEnum.NORMAL
    $ noelle_outfit.CanonOutfit = NoelleOutfitEnum.NORMAL
    $ sarah_outfit.CanonOutfit = SarahOutfitEnum.NORMAL
    $ kira_outfit.CanonOutfit = KiraOutfitEnum.NORMAL

    scene bg house 9 with dissolve
    pause (1)
    scene bg house 10 with dissolve
    pause (1)
    scene bg house 9 with dissolve
    pause (1)
    scene bg house 10 with dissolve
    pause (1)
    scene bg house 9 with dissolve
    pause (1)
    scene bg house 10 with dissolve
    pause (1)

    play music audio.snowflake_lullaby_piano fadeout 1.0 fadein 1.0
    scene kitchen_d1 with fade
    show Noelle happy at noelle_normal(mid_right)
    show Jason happy at jason_normal(mid_left)
    pause(0.25)
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0010.ogg"
    n "Good morning sleepyhead."
    show Noelle at normal_stay
    j "Morning, Mom."
    show Jason neutral at jason_normal(far_left)
    show Jane neutral at jane_normal(mid_left)
    pause(0.25)
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0008.ogg"
    a "Were you going to sleep in all day? I’ve already had a full workout this morning and you’re just getting up. How lazy can you be?"
    show Jane at normal_stay
    show Jason avoid
    j "{i}I have a sneaking suspicion I shouldn’t tell her I was up all night setting up speakers and tweaking the subliminals so I can watch her take one of those post workout showers without getting in trouble.{/i}"
    show Sarah frown at sarah_normal(mid)
    pause(0.25)
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0006.ogg"
    s "Ugh, I can’t believe I’m TRAPPED with my family for half a week! I had a date!"
    show Sarah at normal_stay
    show Jason daydream
    j "{i}Even with the way they treat me, I would almost have enjoyed being stuck around all these sexy girls almost as much as I hated it. But things are different now.{/i}"
    j "{i}Last night I’d set up the delimiter to play through the air vents, and all night long my sisters and my Mom were exposed to subliminal messages.{/i}"
    j "{i}I had no idea if it had worked but I’m dying to find out. I can barely eat. All I can do is think about all the things I’m going to do if this worked.{/i}"
    $ full_shuffle = True
    menu:
        "Do it now! It’s time to take charge!":
            jump familyA1
        "Take it slow.":
            jump familyA2

label familyA1:
    play music "music/Jane's Theme alt fast.mp3" fadeout 1.0 fadein 1.0
    show Jason happy
    show Jason at talking_stay
    j "I can’t stand it! I need to find out if it worked! I’m going to go crazy just sitting here and wondering. Every day it’s 'Jason, stand up for yourself!' and 'Jason, grow a spine!' Today’s the day!"
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Jason at normal_stay
    show Noelle neutral at noelle_normal(far_right)
    show Kira neutral at kira_normal(mid_right)
    pause(0.25)
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0015.ogg"
    k "Hey, that sounds familiar. What is it?"
    show Kira at normal_stay

    show Noelle happy at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0011.ogg"
    n "Weren’t you playing that last night in your room? It was so loud. I could hear it everywhere in the house."
    show Noelle at normal_stay
    show Jane neutral at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0009.ogg"
    a "{i}*Yawn*{/i} It sounds… pretty nice…"
    show Jane at normal_stay
    show Jason happy
    show Jason at talking_stay
    j "That’s right. It sounds great. It’s just so soothing and comforting. It just makes you want to sleep, doesn’t it?"
    show Jason at normal_stay
    show Kira frown
    voice "VoiceActing/Day 01/Kira/D01KiraL0016.ogg"
    k "Can’t… busy…"
    show Noelle frown
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0012.ogg"
    n "Busy…"
    show Jason at talking_stay
    j "Just relax. Relax and listen for a bit."
    show Jason at normal_stay
    show Jane frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0010.ogg"
    a "Listen…"
    j "{i}Look at them. They’re in a trance, right? They’re already there? They look so blank. There’s so many. So sexy… I don’t think I can hold myself back. I’ve got to make them do something now!{/i}"
    j "That’s right. So sleepy. So hot. You just want to strip down…"
    show Kira angry
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0017.ogg"
    k "S-st- wait."
    show Kira at normal_stay
    show Jane angry
    show Noelle angry
    show Sarah angry
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0011.ogg"
    a "Strip? Strip!?"
    "{i}Jane grabbed the Delimiter!{/i}"
    play sound "music/Smashing.mp3"
    stop music fadeout 1.0
    show Jason avoid
    j "Uh… it’s like that song, you know? Like on the discovery chann-"
    play sound "music/RightHookSoundBible.wav"
    j "Owww!" with hpunch
    show Jane at normal_stay
    show Noelle neutral
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0013.ogg"
    n "Jason - were you trying to hypnotize us? You- you…"
    show Noelle at normal_stay
    show Kira frown
    show Jane frown
    show Noelle frown
    show Sarah frown
    j "Ah Shoot."
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0012.ogg"
    a "I’m going to make this the most miserable week of your life."
    show Jane at normal_stay
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0018.ogg"
    k "Disgusting."
    show Kira at normal_stay
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0007.ogg"
    s "Haha, what a loser!"
    show Sarah at normal_stay
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0014.ogg"
    n "Jason, I think once this blizzard is over it’s time to discuss you finding a nice apartment in the city, don’t you think?"
    show Noelle at normal_stay
    scene black with fade
    pause 1
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show badend jason_sad
    $ achievement.grant("Sad_Jason")
    $ achievement.Sync()
    j "{i}I blew it. I pushed too fast. I knew it was too fast and I just couldn’t stop myself. After a few miserable days It’ll be over. I’ll never have a chance like this again. Damn…{/i}"
    return

label familyA2:
    j "{i}No, it’s too soon. One night of subliminals isn’t nearly enough. Did it even work? I don’t really know.{/i}"
    j "{i}They’d say I’m spineless if they knew - well, they’d say a LOT of things if they knew, but I’m just cautious. I don’t know if I could control them all at once even if it did work.{/i}"
    show Noelle neutral

    voice "VoiceActing/Day 01/Noelle/D01NoelleL0015.ogg"
    n "Come on sweetie, it’s not that bad."
    show Noelle neutral at noelle_normal(far_right)
    show Kira frown at kira_normal(mid_right)
    pause(0.25)
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0019.ogg"
    k "Actually, Mom, it is. I’m missing the most important presentation of my LIFE."
    show Kira at normal_stay
    show Jane frown
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0013.ogg"
    a "Yeah! And I’m missing the game."
    show Jane at normal_stay
    show Sarah frown
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0008.ogg"
    s "And I had a date!"
    show Sarah at normal_stay
    show Kira angry
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0020.ogg"
    k "Argh! That’s not the SAME!"
    show Kira at normal_stay
    "{i}Kira leaves in a huff.{/i}"
    hide Kira with dissolve
    show Jason avoid
    j "If it helps I had a recital?"
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0014.ogg"
    a "Nobody cares, dork."
    show Jane at normal_stay
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0016.ogg"
    n "Jason, go and make sure your sister is okay, will you?"
    show Noelle at normal_stay
    j "Uh…"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0017.ogg"
    n "Please, honey, try not to make this any more difficult than it already is."
    show Noelle at normal_stay
    j "{i}Hmm. I don’t think it would work on all of them at once but I can at least check if it worked at all with Kira. At least in private I could laugh off the whole thing as a joke if it goes wrong.{/i}"
    show Jason happy_ad
    j "Sure thing, Mom!"




    play music audio.deep_breaths_piano fadein 1.0
    scene kira_room_d1d with fade
    show Jason avoid at jason_normal(mid_left)
    show Kira frown at kira_normal(far_right)

    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0021.ogg"
    k "Ugh...what are you doing here?"
    j "Uh, Mom said…"
    voice "VoiceActing/Day 01/Kira/D01KiraL0022.ogg"
    k "‘Mom said, Mom said’ - Geez, Jason, when are you going to stop doing everything you’re told, and start taking control of your life?"
    show Jason daydream
    j "{i}Sooner than you think...{/i}"
    show Jason happy
    j "I can leave if you like. I just thought you’d like to hear this, thought it might help you feel better."
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    voice "VoiceActing/Day 01/Kira/D01KiraL0023.ogg"
    k "Oh hey...that’s the… *yawn* That’s the music I heard last night…"
    show Kira at normal_stay
    j "Yes, I was up late practicing. Do you like it?"
    show Kira happy
    voice "VoiceActing/Day 01/Kira/D01KiraL0024.ogg"
    k "Mmmm...like it a...like it a lot…"
    show Jason happy
    j "{i}That’s promising. It - it really seems to be working! Okay, step two. Slow and steady.{/i}"
    j "{i}Time to really test this out.{/i}"
    j "I need this metronome to keep the rhythm though. It really adds something, doesn’t it?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0025.ogg"
    k "Yeah…"
    j "Watch it swing back and forth, back and forth…"
    show Kira hypno at kira_normal(far_right)
    show Kira hypno_enter
    $ renpy.pause(random_true_float(1.0, 2.0))
    show Kira hypno
    voice "VoiceActing/Day 01/Kira/D01KiraL0026.ogg"
    k "Back and forth… back…"
    j "That’s right, just watch the metronome."
    j "Kira, can you hear me?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0027.ogg"
    k "Of course...course I can...hear you."
    j "Good girl. You’re getting sleepy, aren’t you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0028.ogg"
    k "No...not sleepy...too much to do…"
    j "But Kira, we’re snowed in. The snow is so soft, and so heavy…"
    voice "VoiceActing/Day 01/Kira/D01KiraL0029.ogg"
    k "Soft...and...heavy…"
    j "The snow is so heavy, and it’s on all sides of the house. You’re surrounded by it, by the soft, heavy snow."
    voice "VoiceActing/Day 01/Kira/D01KiraL0030.ogg"
    k "Heavy...snow…"
    j "It’s just like one big fluffy pillow all over everything. So warm and soft and comforting. You just want to sink into it. It feels so good and relaxing. You don’t even want to move, do you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0031.ogg"
    k "Too… relaxed… to… move..."
    j "All you can do is listen to my voice, and listen to the music. Isn’t that right?"
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0032.ogg"
    k "Yesss...listen to music. Listen to...Jason."
    j "You like the music, don’t you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0033.ogg"
    k "Mmmmm...."
    j "It’s so soft, so gentle."
    show Kira hypno
    voice "VoiceActing/Day 01/Kira/D01KiraL0034.ogg"
    k "Gentle…"
    j "And so is my voice. You trust me, don’t you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0035.ogg"
    k "Trust…"
    j "Tell me that you trust me."
    voice "VoiceActing/Day 01/Kira/D01KiraL0036.ogg"
    k "Trust...Jason…"
    j "Good girl. You’ll tell me anything, won’t you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0037.ogg"
    k "Tell...anything…"
    j "You’ll never lie to me, will you?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0038.ogg"
    k "No…"
    show Jason neutral
    j "Good. I’m going to ask you some questions, and I want you to be completely honest."
    voice "VoiceActing/Day 01/Kira/D01KiraL0039.ogg"
    k "Okay...Jason…"
    play music "music/Kira's Theme alt.mp3" fadeout 1.0 fadein 1.0
    jump kA

label kA:
    menu:
        "What do you do for a living?":
            jump kA1
        "Why are you always so tightly wound?":
            jump kA2

label kA1:
    j "What do you do for a living?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0040.ogg"
    k "I’m the best… chemical engineer… country."
    j "Good girl. That was a nice easy one for you."
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0041.ogg"
    k "Good… girl… Easy…"
    $ Kira_c.add_points(1)
    jump kB

label kA2:
    j "Why are you always so tightly wound?"
    show Kira hypno_frown
    voice "VoiceActing/Day 01/Kira/D01KiraL0042.ogg"
    k "Gotta...get it...right."
    j "What do you mean?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0043.ogg"
    k "So much pressure...always gotta perform…"
    jump kB

label kB:
    menu:
        "You need to learn to relax.":
            jump kB1
        "You don’t need to perform. Not when you’re at home.":
            jump kB2
        "Do you want to suck my cock?":
            jump kB3

label kBa:
    menu:
        "You need to learn to relax.":
            jump kB1
        "Do you want to suck my cock?":
            jump kB3

label kB1:
    j "You need to learn to relax."
    voice "VoiceActing/Day 01/Kira/D01KiraL0044.ogg"
    k "No time...always busy."
    j "C’mon, sis. Surely there’s something you like to do to relax."
    voice "VoiceActing/Day 01/Kira/D01KiraL0045.ogg"
    k "Well…"
    j "Remember, you trust me. You can tell me anything."
    voice "VoiceActing/Day 01/Kira/D01KiraL0046.ogg"
    k "Sometimes…"
    j "What?"
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0047.ogg"
    k "{i}*giggles*{/i} No...too embarrassing…"
    jump kC

label kB2:
    j "You don’t need to perform. Not when you’re at home."
    voice "VoiceActing/Day 01/Kira/D01KiraL0048.ogg"
    k "Course...do."
    j "You really don’t. You might be the youngest chemical engineer in the city…"
    voice "VoiceActing/Day 01/Kira/D01KiraL0049.ogg"
    k "...country...."
    j "But here, you’re just part of the family. This is your home - this is where you can relax and just be yourself."
    voice "VoiceActing/Day 01/Kira/D01KiraL0050.ogg"
    k "...relax…"
    show Jason happy
    j "{i}Eventually I’ll get her so relaxed that she won’t even feel the need to wear clothes any more.{/i}"
    show Jason neutral
    $ Kira_c.add_points(1)
    jump kBa

label kB3:
    j "Do you want to suck my cock?"
    "{i}Kira’s eyes widen. She begins to shake, her mind straining against the trance.{/i}"
    show Kira frown at kira_normal(far_right)
    voice "VoiceActing/Day 01/Kira/D01KiraL0051.ogg"
    k "I’m your sister… can’t… what…?"
    show Jason avoid
    j "{i}Oh, shit. Gotta salvage this fast.{/i}"
    show Jason neutral
    j "Uh… that’s right. You like the sound of the clock."
    show Kira hypno_frown at kira_normal(far_right)
    voice "VoiceActing/Day 01/Kira/D01KiraL0052.ogg"
    k "Clock…?"
    j "Uh, yeah. Clock."
    voice "VoiceActing/Day 01/Kira/D01KiraL0053.ogg"
    k "Clock..."
    show Jason frown
    j "{i}That was too damn close. She almost woke up there and she doesn’t seem as deep in the trance as she did before. I can’t push her too far. I’ve got to be careful.{/i}"
    show Jason neutral
    $ Kira_c.sub_points(1)
    jump kB

label kC:
    menu:
        "I order you to tell me.":
            jump kC1
        "Hey - we’re siblings. We can totally trust each other. Don’t you trust me?":
            jump kC2
        "That’s okay. You don’t have to say anything you’re not comfortable with.":
            show Kira hypno_smile
            jump kC3

label kCa:
    menu:
        "I order you to tell me.":
            jump kC1
        "Hey - we’re siblings. We can totally trust each other. Don’t you trust me?":
            jump kC2

label kC1:
    j "I order you to tell me."
    show Kira hypno_frown at kira_normal(far_right)
    j "{i}Kira seems to shake and tremble a bit as the trance is strained.{/i}"
    voice "VoiceActing/Day 01/Kira/D01KiraL0054.ogg"
    k "You… order?"
    j "Uh-oh."
    voice "VoiceActing/Day 01/Kira/D01KiraL0056.ogg"
    k "You… can’t order… you…"
    j "Um, nevermind that. Just focus on the music."
    k "..."
    j "The soothing, soothing music."
    j "{i}Please please please work.{/i}"
    voice "VoiceActing/Day 01/Kira/D01KiraL0057.ogg"
    k "Music…"
    j "{i}Whew. Right, she’s a control freak. Can’t order her around. All those years of telling me to stand up for myself and the second I try she won’t let me, even in a trance.{/i}"
    j "{i}Go figure. I can’t make her into a different person, I guess. I’ve got to figure out how to work with her normal personality.{/i}"
    $ Kira_c.sub_points(1)
    jump kC

label kC2:
    j "Hey - we’re siblings. We can totally trust each other. Don’t you trust me?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0058.ogg"
    k "Trust...you…"
    j "So tell me, what do you do to relax?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0059.ogg"
    k "It’s silly…"
    jump kD

label kC3:
    j "That’s okay. You don’t have to say anything you’re not comfortable with."
    show Kira hypno
    "{i}She smiles silently.{/i}"
    $ Kira_c.add_points(1)
    jump kCa

label kD:
    menu:
        "I like silly.":
            jump kD1
        "Just tell me.":
            jump kD2
        "Is it naughty?":
            jump kD3

label kDa:
    menu:
        "I like silly.":
            jump kD1
        "Just tell me.":
            jump kD2

label kD1:
    j "I like silly."
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0060.ogg"
    k "Well...I like...silk panties…"
    show Jason happy_ad
    j "Silk panties?"
    show Jason neutral
    voice "VoiceActing/Day 01/Kira/D01KiraL0061.ogg"
    k "Like the...feel."
    j "There’s nothing silly about that."
    voice "VoiceActing/Day 01/Kira/D01KiraL0062.ogg"
    k "Feels so good...makes me feel…"
    j "What?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0063.ogg"
    k "...sexy."
    show Kira hypno
    $ Kira_c.add_points(1)
    jump kE

label kD2:
    j "Just tell me."
    show Kira hypno_lewd
    voice "VoiceActing/Day 01/Kira/D01KiraL0064.ogg"
    k "Okay...but you gotta...secret."
    j "Cross my heart and hope to die."
    voice "VoiceActing/Day 01/Kira/D01KiraL0065.ogg"
    k "I like…silk panties."
    show Jason happy_ad
    j "Silk panties?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0066.ogg"
    k "Told you it was...silly…"
    jump kE

label kD3:
    j "Is it naughty?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0068.ogg"
    k "No...well, a little…"
    j "Okay, now I’ve GOT to hear what it is."
    jump kDa

label kE:
    menu:
        "You should show me your panties.":
            jump kE1
        "You really need to learn to unwind.":
            jump kE2

label kE1:
    j "You should show me your panties."
    if Kira_c.points >= 2:
        jump kendgood
    else:
        jump kendbad

label kendbad:
    show Kira hypno_frown
    voice "VoiceActing/Day 01/Kira/D01KiraL0069.ogg"
    k "...no."
    j "Aw, c’mon sis. It’ll be fun."
    show Kira hypno
    voice "VoiceActing/Day 01/Kira/D01KiraL0070.ogg"
    k "Too...weird."
    show Jason happy
    j "Okay. But promise me you’re going to try to relax around the house from now on, okay?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0071.ogg"
    k "...fine."
    $ Kira_c.add_points(1)
    jump kirawake

label kendgood:
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0072.ogg"
    k "...okay."
    show Jason happy_aroused
    j "Really??"
    voice "VoiceActing/Day 01/Kira/D01KiraL0073.ogg"
    k "Sure…it’ll be...fun."
    scene cgbg with dissolve
    show kira_panties
    $ persistent.flashy = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_11")
    $ achievement.Sync()
    j "{i}Oh wow. They say you can’t make someone do anything while they’re hypnotized that they wouldn’t do while they’re awake - either I’ve just proved them wrong, or my sister has a bit of an exhibitionist streak!{/i}"
    $ kirapanties = True
    $ Kira_c.add_points(2)
    jump kirawake

label kE2:
    j "You really need to learn to unwind."
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0074.ogg"
    k "Mmm...unwind…"
    j "Maybe you’d be more relaxed if you didn’t work all the time."
    show Kira hypno_frown
    voice "VoiceActing/Day 01/Kira/D01KiraL0075.ogg"
    k "No...gotta...work…"
    j "I think you’d be happier if you spent more time relaxing."
    voice "VoiceActing/Day 01/Kira/D01KiraL0076.ogg"
    k "Must...work...hard…"
    j "{i}Wow. Even when she’s REALLY under, she still can’t let go.{/i}"
    j "Well maybe you can show me your panties?"
    $ Kira_c.sub_points(1)
    jump kE1

label kirawake:
    play music "music/Kira's Theme.mp3" fadeout 1.0 fadein 1.0
    scene kira_room_d1d with dissolve
    show Jason happy_aroused at jason_normal(mid_left)
    show Kira hypno at kira_normal(far_right)
    j "Okay Kira, I’m going to count down from 5. When I get to 1, you’re going to wake up, and it’s going to be like nothing ever happened, yeah?"
    show Kira hypno_smile
    voice "VoiceActing/Day 01/Kira/D01KiraL0077.ogg"
    k "...mmm…"
    j "When you wake up, you’re going to feel closer to me than before. When I come hang out with you, that’s going to make you happy. Do you understand?"
    voice "VoiceActing/Day 01/Kira/D01KiraL0078.ogg"
    k "...yesss…"
    j "And, uh, when it’s time for dinner, you’re going to volunteer to help me with the dishes. Do you agree?"
    show Kira hypno_frown
    voice "VoiceActing/Day 01/Kira/D01KiraL0079.ogg"
    k "...no."
    show Jason avoid
    j "Ah well, worth a try."
    j "5, 4, 3, 2, 1!"
    show Kira happy at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0080.ogg"
    k "Sorry, what were we talking about? I totally spaced out for a second there."
    show Kira at normal_stay
    show Jason happy
    show Jason at talking_stay
    j "Nothing really. I was just asking what you thought of my new song."
    show Jason at normal_stay
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0081.ogg"
    k "I really like it!"
    show Kira at normal_stay
    show Jason happy_ad
    show Jason at talking_stay
    j "Aw, thanks!"
    show Jason at normal_stay
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0082.ogg"
    k "Yeah, it’s weirdly relaxing."
    show Kira at normal_stay
    show Jason happy
    show Jason at talking_stay
    j "Do you mind if I show you some more music tomorrow?"
    show Jason at normal_stay
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0083.ogg"
    k "Might as well. Not like I’m getting any work done while we’re snowed in like this."
    show Kira at normal_stay
    show Jason at talking_stay
    j "Thanks, sis."
    show Jason at normal_stay
    show Kira neutral
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D01KiraL0084.ogg"
    k "No problem, pest. Now get out of here; I want to get a head-start on next year’s taxes."
    jump Family





label Family:
    play music audio.snowflake_lullaby_piano fadein 1.0
    scene livingroom_d1 with fade
    show Jason happy at jason_normal(mid_left)
    show Noelle neutral at noelle_normal(mid_right)
    play music "music/Jason's Theme.mp3" fadeout 1.0 fadein 1.0
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0018.ogg"
    n "So how is she?"
    show Noelle at normal_stay
    j "I think she’s just stressed."
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0019.ogg"
    n "Hmmm. She does work herself pretty hard."
    show Noelle at normal_stay
    show Jason neutral
    j "Yeah, I feel sorry for her."
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0020.ogg"
    n "Well, how about we give her a bit of a break around the house from now on."
    show Noelle at normal_stay
    j "That sounds like it might help."
    show Noelle happy
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0021.ogg"
    n "Great! So from now on, you can do her chores for her."
    show Noelle at normal_stay
    show Jason avoid
    j "Uh…"
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0022.ogg"
    n "Glad we got that sorted. Why don’t you start by getting the laundry from Sarah’s room?"
    show Noelle at normal_stay
    show Sarah neutral at sarah_easeinright(far_right)
    $ renpy.pause(0.25, hard=True)
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0009.ogg"
    s "Ew. I don’t want him poking around my underwear."
    show Sarah at normal_stay
    j "Hey!"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0023.ogg"
    n "Good point."
    show Noelle at normal_stay
    j "Hey!!"
    show Noelle happy
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0024.ogg"
    n "Why don’t you go with him?"
    show Noelle at normal_stay
    show Sarah frown
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0010.ogg"
    s "Ugh, fine."
    show Sarah at normal_stay
    show Jason daydream
    j "{i}Well, at least this gives me a chance to spend some one-on-one time with my younger sister...{/i}"




    play music audio.deep_breaths_flute fadein 1.0
    scene sarah_room_d1d with fade
    show Jason neutral at jason_normal(mid_left)
    show Sarah frown at sarah_normal(mid_right)
    play music "music/Sarah's Theme.mp3" fadeout 1.0 fadein 1.0
    j "So, was your date annoyed that you had to cancel?"
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0011.ogg"
    s "Ugh, I don’t even know! There’s no reception because of this stupid blizzard, and the internet is down. There’s nothing to doo…"
    show Sarah at normal_stay
    show Jason happy
    j "How about I show you one of the new songs I’m working on?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0012.ogg"
    s "Thrilling."
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Sarah neutral at sarah_normal(mid_right)
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0013.ogg"
    s "Hey, this is familiar. This is...was this playing last night?"
    show Sarah at normal_stay
    j "Yeah, I was practicing."
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0014.ogg"
    s "All… {i}*yawn*{/i} All night?"
    show Sarah at normal_stay
    j "This helps me keep the rhythm. It’s kind of nice, isn’t it?"
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0015.ogg"
    s "Mmm...kind of...nice."
    show Sarah at normal_stay
    j "It’s such a steady beat. Tick, tick, tick, tick."
    show Sarah hypno at sarah_normal(mid_right)
    show Sarah hypno_enter
    pause random_true_float(1.0, 2.0)
    show Sarah hypno
    voice "VoiceActing/Day 01/Sarah/D01SarahL0016.ogg"
    s "Tick...tick…"
    j "You like that, don’t you?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0017.ogg"
    s "Like...it…"
    j "You can feel all your worries float away with the beat."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0018.ogg"
    s "Mmm…"
    j "Let the music flow through you, let it relax every part of you, from your head to your feet. Each beat makes you more and more relaxed…"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0019.ogg"
    s "Relaxed…"
    j "You don’t want to think of anything except the music. The music and the sound of my voice. Listen to my voice…"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0020.ogg"
    s "I’m listening…"
    j "The beat is so consistent, so steady. Steady and reliable, just like me."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0021.ogg"
    s "Steady and...reliable."
    j "Steady and trustworthy. You trust me, don’t you?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0022.ogg"
    s "Yesssss…"
    j "Tell me that you trust me."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0023.ogg"
    s "Trust...Jason…"
    j "Good girl. You’ll answer all my questions honestly, won’t you?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0024.ogg"
    s "Answer...honestly…"
    j "You’ll never lie to me, will you?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0025.ogg"
    s "No…"
    j "Good. I’m going to ask you some questions, and I want you to be completely honest."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0026.ogg"
    s "Okay...Jason…"
    play music "music/Sarah's Theme alt.mp3" fadeout 1.0 fadein 1.0
    show Jason neutral
    j "{i}Great. It looks like she’s under. Let’s see how much I can learn about these dates of hers…{/i}"


label sA:
    menu:
        "Why do you go on so many dates?":
            jump sA1
        "What do you do on your dates?":
            jump sA2
        "How many dates before you put out?":
            jump sA3


label sAa:
    menu:
        "Why do you go on so many dates?":
            jump sA1
        "What do you do on your dates?":
            jump sA2


label sA1:
    j "Why do you go on so many dates?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0027.ogg"
    s "Cos…fun."
    j "They’re fun?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0028.ogg"
    s "Mmmm…."
    j "What’s fun about them?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0029.ogg"
    s "Cute guys…checking me out…plus…"
    j "Mmm?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0030.ogg"
    s "…like the company."
    j "{i}Interesting. Not quite the answers I was expecting.{/i}"
    jump sB

label sA2:
    j "What do you do on these dates?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0031.ogg"
    s "Y’know…"
    j "No, I don’t. What do you get up to?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0032.ogg"
    s "Just…just hang out…"
    j "You just hang out?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0033.ogg"
    s "Mmmm…"
    jump sC


label sA3:
    j "So how many times do you have to go on a date with a guy before you…y’know. Do it."

    show Sarah angry
    voice "VoiceActing/Day 01/Sarah/D01SarahL0034.ogg"
    s "What did you just ask me?"
    j "{i}Oh, shit.{/i}"
    show Sarah hypno_frown
    voice "VoiceActing/Day 01/Sarah/D01SarahL0035.ogg"
    s "What…what were we talking about?"
    j "{i}Ah, crap. I’ve got to put her under before she remembers what I said.{/i}"
    j "Shhh, it’s okay. Just listen to the delimiter…just listen to that lovely, soothing ticking. So steady…"
    show Sarah hypno
    voice "VoiceActing/Day 01/Sarah/D01SarahL0036.ogg"
    s "Steady…"
    j "That’s right. That nice, steady, regular ticking. Isn’t it lovely?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 01/Sarah/D01SarahL0037.ogg"
    s "Mmm…lovely…"
    j "{i}Phew. I’ve got to remember to be careful - I can’t push them too hard. Not yet, anyway.{/i}"
    $ Sarah_c.sub_points(1)
    jump sAa


label sB:
    menu:
        "Would you like it if you didn’t have to go out to be checked out?":
            jump sB1
        "Isn’t there enough company at home for you?":
            jump sB2

label sB1:
    j "What if you didn’t have to go out to be checked out? What if you could get some male attention without ever leaving your room…"
    "{i}Sarah stirs slightly.{/i}"
    show Sarah hypno_frown
    voice "VoiceActing/Day 01/Sarah/D01SarahL0038.ogg"
    s "No…wouldn’t like that…at all…"
    j "Why not?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0039.ogg"
    s "Only guy around here is…Jason…"
    j "What’s wrong with Jason?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0040.ogg"
    s "He’s my…brother. That would be gross."
    j "Nuts."
    $ Sarah_c.sub_points(1)
    jump sB


label sB2:
    j "Why do you need to go out? Can’t you just hang out at home?"
    show Sarah hypno_frown
    voice "VoiceActing/Day 01/Sarah/D01SarahL0041.ogg"
    s "Nooo…"
    j "Why not?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0042.ogg"
    s "Too…lonely."
    j "What are you talking about? There’s plenty of company at home - Mom, Kira…Jason."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0043.ogg"
    s "Nahhh. Everyone’s…always busy."
    j "So what do you want? Someone to just hang out with you all the time?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 01/Sarah/D01SarahL0044.ogg"
    s "Yeah. Like a…like a puppy…"
    j "Okay."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0045.ogg"
    s "I’d love a puppy…"
    j "You like dogs?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0046.ogg"
    s "I love dogs. Love…puppies."
    j "{i}I didn’t know Sarah loved puppies. Maybe there’s something I can do with this…{/i}"
    show Sarah hypno
    $ Sarah_c.add_points(1)
    jump sD

label sC:
    menu:
        "You don’t make out or hook up?":
            jump sC1
        "Why can’t you just hang out at home?":
            jump sC2
        "Back to earlier questions.":
            jump sC3


label sC1:
    j "You don’t make out or hook up?"
    show Sarah hypno
    voice "VoiceActing/Day 01/Sarah/D01SarahL0047.ogg"
    s "That’s…personal…"
    j "You can tell me. I’m your brother."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0048.ogg"
    s "No…"
    j "Fine."
    $ Sarah_c.sub_points(1)
    jump sC

label sC2:
    jump sB2

label sC3:
    jump sA

label sD:
    menu:
        "Would you have sex with a dog if we had one?":
            jump sD1
        "Puppies are so free, aren’t they?":
            jump sD2
        "Wouldn’t it be fun to act like a dog sometimes?":
            jump sD3

label sDa:
    menu:
        "Would you have sex with a dog if we had one?":
            jump sD1
        "Wouldn’t it be fun to act like a dog sometimes?":
            jump sD3

label sD1:
    j "Would you have sex with a dog if we had one?"
    if Sarah_c.points <= 1:
        jump badendD
    else:
        jump continueD

label badendD:
    show Sarah shocked
    "{i}Sarah opens her eyes and stares at me in shock.{/i}"
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0049.ogg"
    s "What did you just ask me?"
    j "Uh…"
    show Sarah frown
    show Sarah at normal_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0050.ogg"
    s "Oh my god, Jason, what is wrong with you?"
    j "Shhh…just listen to the metronome…"
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0051.ogg"
    s "No! You’re sick, bro. I’m telling Mom!"
    j "Let the music roll over you…"
    show Sarah angry
    voice "VoiceActing/Day 01/Sarah/D01SarahL0052.ogg"
    s "No! MOM!"
    j "Ah, fuck."


    show Noelle angry at noelle_normal(far_right)

    show Sarah at normal_stay
    $ renpy.pause(0.25, hard=True)
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0025.ogg"
    n "Jason! What did you do?"
    show Noelle at normal_stay
    show Sarah angry
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0053.ogg"
    s "He asked if I’d have sex with a dog!"
    show Sarah at normal_stay
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0026.ogg"
    n "What??"
    show Noelle at normal_stay
    j "Hey guys, listen to the music. This nice, soothing…"
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0054.ogg"
    s "Oh my god - Mom, he’s trying to control us with his little gadget thing!"
    show Sarah at normal_stay
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0027.ogg"
    n "That is IT, young man! As if looking at your sister in the shower wasn’t bad enough, now THIS?"
    j "I'm gonna have to find my own place, aren't I?"
    scene black with fade
    pause 1
    show badend cold_outside with dissolve
    $ achievement.grant("Meat_Popsicle")
    $ achievement.Sync()
    pause
    return

label continueD:
    show Sarah hypno_frown
    voice "VoiceActing/Day 01/Sarah/D01SarahL0055.ogg"
    s "Noooo…"
    "{i}She starts to wake up.{/i}"
    j "Shh shh shh…listen to the metronome. The lovely, steady metronome…"
    show Sarah hypno
    voice "VoiceActing/Day 01/Sarah/D01SarahL0056.ogg"
    s "Mmmm…"
    j "Yeah, I don’t know why I thought that would work."
    $ Sarah_c.sub_points(1)
    jump sD

label sD2:
    show Jason happy
    j "Puppies are just so free, aren’t they?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 01/Sarah/D01SarahL0057.ogg"
    s "Mmm…so free…"
    j "They have no responsibilities, no obligations."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0058.ogg"
    s "No…obligations…"
    j "There’s no rules when you’re a puppy."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0059.ogg"
    s "No rules…"
    j "And puppies never get bored. Wouldn’t that be nice?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0060.ogg"
    s "So...nice…"
    show Jason neutral
    show Sarah hypno
    $ Sarah_c.add_points(1)
    jump sDa


label sD3:
    j "Wouldn’t it be fun to act like a dog sometimes?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0061.ogg"
    s "Sure…"
    j "Why don’t you do that right now?"
    if Sarah_c.points >= 2:
        jump ssucceed1
    else:
        jump sfail1



label sfail1:
    show Sarah hypno_frown
    voice "VoiceActing/Day 01/Sarah/D01SarahL0062.ogg"
    s "Noo…."
    j "Why not?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0063.ogg"
    s "It’d be weird…"
    j "What would be weird about it?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0064.ogg"
    s "You’re…here…"
    j "{i}Damn it.{/i}"
    j "Okay, but what if I wasn’t around?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0066.ogg"
    s "Fine…"
    j "Okay, so when you’re next alone, why don’t you pretend to be a puppy?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0067.ogg"
    s "Hmmm…"
    j "{i}I’m not sure whether that’s a yes or a no. I just wish she trusted me more than she does. Maybe if I try something positive again it'll work?{/i}"
    show Sarah hypno
    $ Sarah_c.add_points(1)
    jump sD

label ssucceed1:
    $ persistent.doggy = True
    show Sarah hypno_smile
    voice "VoiceActing/Day 01/Sarah/D01SarahL0068.ogg"
    s "…okay…"
    j "For real? Awesome."
    hide Sarah
    scene cgbg with dissolve
    show sarah_doggy
    $ achievement.grant("NEW_ACHIEVEMENT_1_9")
    $ achievement.Sync()
    j "Okay, how about you give me a little bark."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0069.ogg"
    s "Woof!"
    j "{i}Amazing.{/i}"
    j "That was fun, wasn’t it?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0090.ogg"
    s "Okay..."
    j "Let’s do that again. Just another little bark."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0071.ogg"
    s "Woof!"
    j "Now a few. Joyful little woofs, to show how happy you are!"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0072.ogg"
    s "Woof woof!"
    j "What else do dogs do?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0073.ogg"
    s "Woof!"
    j "Oh, that’s fantastic."
    j "Doggies like to run around on all fours, don’t they?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0074.ogg"
    s "Woof!"
    "{i}She gets down on all fours.{/i}"
    j "Doggies wag their tails, don’t they?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0075.ogg"
    s "Woof woof!"
    "{i}She wiggles her butt from side-to-side.{/i}"
    j "Good girl."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0076.ogg"
    j "{i}Sarah sits like a dog and looks up at me, her tongue poking out happily.{/i}"
    j "{i}Now that’s a sight I could look at all day.{/i}"
    $ Sarah_c.add_points(2)
    jump sE

label sE:
    menu:
        "Dogs don’t wear clothes. How about we take your clothes off?":
            jump sE1
        "Would the doggie like a bone?":
            jump sE2
        "That’s probably enough for now.":
            jump sE3


label sE1:
    j "Doggies don’t wear clothes, do they? How about we take those awful human clothes off you."
    if Sarah_c.points >=4:
        jump doggiefail1
    else:
        jump doggiefail2


label doggiefail1:
    voice "VoiceActing/Day 01/Sarah/D01SarahL0077.ogg"
    s "Grrrr…"
    j "{i}Holy shit. If she had fur, it’d be standing on end right now.{/i}"
    j "What’s wrong?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0078.ogg"
    s "Just...pretending…"
    j "Fair enough."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0079.ogg"
    s "Woof woof!"
    jump sE


label doggiefail2:
    voice "VoiceActing/Day 01/Sarah/D01SarahL0080.ogg"
    s "Noo. Ewww…"
    "{i}She begins to stir.{/i}"
    j "Shhh…listen to the beats. Aren’t they nice?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0081.ogg"
    s "Mmmm…nice…"
    j "Good girl."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0082.ogg"
    s "Good…girl…"
    j "{i}I’ve got to stop pushing so hard. I’ll get there, I know I will.{/i}"
    $ Sarah_c.sub_points(1)
    jump sE


label sE2:
    j "Would the doggie like a bone?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0083.ogg"
    s "Arf!"
    "{i}She tilts her head to the side inquisitively.{/i}"
    jump sF


label sE3:
    j "Okay Sarah, that’s probably enough for now."
    scene sarah_room_d1d with fade
    show Jason neutral at jason_normal(mid_left)

    show Sarah hypno_smile at sarah_normal(mid_right)
    voice "VoiceActing/Day 01/Sarah/D01SarahL0084.ogg"
    s "Woof!"
    j "That was fun though, wasn’t it?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0070.ogg"
    s "Mmmm…"
    j "It’s fun to pretend to be a doggie, isn’t it?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0086.ogg"
    s "Yeahh…"
    j "It sure would be nice to remember the fun we had while you’re awake, wouldn’t it?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0087.ogg"
    s "I dunno…might be a bit…weird."
    j "That’s a good point. But what if you just remembered the fun, and didn’t remember that you acted like a dog?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 01/Sarah/D01SarahL0088.ogg"
    s "Mmmm…"
    j "How about you wear a cloth collar around the house from now on? Whenever you look at it, you can remember how much fun it was to pretend to be a dog…"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0089.ogg"
    s "Oh yeah…"
    j "And next time I come into your room to hang out, you’ll remember what fun we had, won’t you?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0070.ogg"
    s "Mmmm…"
    j "Good girl."
    voice "VoiceActing/Day 01/Sarah/D01SarahL0091.ogg"
    s "Thanks…Jason…"
    j "{i}Well, that’s something I thought I’d never hear.{/i}"
    $ Sarah_c.add_points(1)
    jump family2


label sF:
    menu:
        "Pull down your pants and show her your boner.":
            jump sF1
        "Go to the kitchen and grab her some meat.":
            jump sF2
        "Never mind.":
            jump sF3

label sFz:
    menu:
        "Pull down your pants and show her your boner.":
            jump sF1
        "Never mind.":
            jump sF3

label sF1:
    j "{i}I stand up and begin to pull down my pants.{/i}"
    scene sarah_room_d1d with dissolve
    show Jason neutral at jason_normal(mid_left)
    show Sarah shocked at sarah_normal(mid_right)
    pause(0.25)
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0092.ogg"
    s "…oh my god, what the hell are you doing?"
    show Sarah at normal_stay
    j "{i}She's awake, dammit.{/i}"
    j "Uh…"
    show Sarah angry
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D01SarahL0093.ogg"
    s "You absolute perv!! Get out of my room!"
    j "{i}Crap. Well, at least I learned something about my little sis today.{/i}"
    $ Sarah_c.sub_points(1)
    jump family2


label sF2:
    j "Okay Sarah…stay."
    if Sarah_c.points >=3:
        jump sarahyah
    else:
        jump sarahnah


label sarahnah:
    voice "VoiceActing/Day 01/Sarah/D01SarahL0094.ogg"
    s "…nooo."
    j "What?"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0095.ogg"
    s "…you’re not the boss…of me…"
    j "{i}Ah well. It was worth a try.{/i}"
    jump sF3


label sarahyah:
    voice "VoiceActing/Day 01/Sarah/D01SarahL0097.ogg"
    s "Woof!"
    j "Good girl."
    j "{i}I quickly run to the kitchen and reappear a few seconds later with the bone from a leg of lamb.{/i}"
    j "Here you go!"
    voice "VoiceActing/Day 01/Sarah/D01SarahL0098.ogg"
    s "Woof woof!"
    "{i}Sarah begins enthusiastically gnawing on the bone while Jason watches with a smile.{/i}"
    j "{i}I’ll have to remember to clean that up. I can’t imagine what Sarah would think if she woke up to find a chewed-on bone in her room.{/i}"
    $ Sarah_c.add_points(1)
    jump sE3

label sF3:
    j "Actually, never mind."
    jump sE3






label family2:
    scene livingroom_d1 with fade
    show Jason neutral at jason_normal(mid_left)
    show Noelle neutral at noelle_normal(mid_right)
    pause(0.25)
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0029.ogg"
    n "You took your time…"
    show Noelle at normal_stay
    j "Yeah, Sarah and I got to chatting."
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0030.ogg"
    n "Hmmm…"
    show Noelle at normal_stay
    j "Where’s Jane?"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0031.ogg"
    n "Jason, I am not comfortable with how much interest you’re showing in your sisters…"
    show Noelle at normal_stay
    j "Mo-om, I told you. That was an accident…"
    show Noelle neutral
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0032.ogg"
    n "Hmmm... why don’t you go and apologize to your sister. Then I want to talk to you."
    show Noelle at normal_stay
    show Jason daydream
    j "{i}Uh-oh. That’s never good. Although, now that I know the delimiter works… maybe I’ll be able to turn that conversation to my advantage. Maybe.{/i}"
    j "{i}I’ve never heard of someone getting the upper hand with her. How would she react if I were the first?{/i}"
    j "Sure thing, Mom. I’ll be right back."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0033.ogg"
    n "I’ll be waiting."




    play music audio.deep_breaths_guitar fadein 1.0
    scene jane_room_d1d with fade
    show Jason neutral at jason_normal(mid_left)
    show Jane frown at jane_normal(far_right)
    play music "music/Jane's Theme.mp3" fadeout 1.0 fadein 1.0
    j "Hey Jane."
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0015.ogg"
    a "I’m not talking to you. Perv."
    show Jane at normal_stay
    show Jason happy
    j "I’m here to apologise."
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0016.ogg"
    a "I don’t want to hear it."
    show Jane at normal_stay
    j "Jane, I’m…"
    show Jane angry
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0017.ogg"
    a "I said get out!"
    show Jane at normal_stay
    show Jason happy_ad
    j "Actually, no you didn’t."
    show Jane frown
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0018.ogg"
    a "Fuck you."
    show Jane at normal_stay
    show Jason neutral
    j "I really am sorry. I wrote you a song as an apology."
    voice "VoiceActing/Day 01/Jane/D01JaneL0019.ogg"
    a "For real?"
    show Jason happy_ad
    j "Sure. Just listen…"
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome

    voice "VoiceActing/Day 01/Jane/D01JaneL0020.ogg"
    a "Hey...I’ve heard this before…"
    j "Yeah, I was working on it all night."
    show Jane happy
    voice "VoiceActing/Day 01/Jane/D01JaneL0021.ogg"
    a "It sounds...good…"
    show Jason happy
    j "Thanks."
    show Jane frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0022.ogg"
    a "I’m still...still mad, though."
    show Jason neutral
    j "I know you’re angry. I was so nervous to come up here, it made my heart race."
    voice "VoiceActing/Day 01/Jane/D01JaneL0023.ogg"
    a "...huh?"
    j "I can hear it thumping now, can’t you?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0024.ogg"
    a "No…"
    j "Ssshhh, listen closely. Listen to my heart beating. Thump, thump, thump, thump…"
    voice "VoiceActing/Day 01/Jane/D01JaneL0025.ogg"
    a "That’s...that’s not…"
    j "Sshhh, just listen. Can’t you hear it? Thump, thump, thump…"
    voice "VoiceActing/Day 01/Jane/D01JaneL0026.ogg"
    a "Thump…"
    j "That’s right. Shut your eyes and focus on the sound. It’s so smooth, so steady. Thump, thump, thump, thump."
    voice "VoiceActing/Day 01/Jane/D01JaneL0027.ogg"
    a "Thump...thump…"
    j "Isn’t it so nice and relaxing?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0028.ogg"
    a "So...nice…"
    j "Doesn’t it just make you want to lie down on your bed, and not have to think any more?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0029.ogg"
    a "Yes..."
    show Jane hypno at jane_normal(far_right)
    show Jane hypno_enter
    pause random_true_float(1.0, 2.0)
    show Jane hypno
    "{i}Jane lies down.{/i}"
    j "Good...just lie down and listen to the nice, steady beat of my heart. Thump, thump, thump, thump. It’s so steady, so reliable. You can tell that I’ve calmed down, can’t you?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0030.ogg"
    a "Mmmm…"
    j "You can tell that I’m nice and relaxed. Not mad any more. No one’s mad, are they?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0031.ogg"
    a "I’m...mad…"
    j "It’s hard to be mad when you’re so relaxed, isn’t it? How can you be mad, with such a steady heartbeat. Thump, thump, thump, thump."
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0032.ogg"
    a "Thump...thump…"
    j "That’s it. Just lie down, nice and calm, and let’s have a little chat."
    j "{i}Whew. That was much harder than the other two. I’d better stop her from being mad at me before I can get much further.{/i}"
    play music "music/Jane's Theme alt slow.mp3" fadeout 1.0 fadein 1.0
    jump aA


label aA:
    menu:
        "What can I do to make it up to you?":
            jump aA1
        "Why are you mad at me?":
            jump aA2
        "(Joking) Do you want to watch me in the shower?":
            jump aA3

label aA1:
    j "What can I do to make it up to you?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0033.ogg"
    a "Be...cool…"
    j "What do you mean?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0034.ogg"
    a "We used to be...close. Now...so...weird. Just...be cool."
    j "{i}Huh. I had figured that she was totally fine with how far apart we’d drifted. Now I really felt bad for peeking on her in the shower.{/i}"
    j "Sorry. I mean that - sorry for peeking on you."
    voice "VoiceActing/Day 01/Jane/D01JaneL0035.ogg"
    a "That’s...okay."
    j "{i}Maybe I should have also felt guilty for everything I was ABOUT to do to her, but I didn’t.{/i}"
    j "I just...I feel like you can be a bit of a dick sometimes."
    voice "VoiceActing/Day 01/Jane/D01JaneL0036.ogg"
    a "You’re...a dick…"
    j "I mean it. You and Mom and Sarah and Kira are always ganging up on me. Why don’t you be cool?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0037.ogg"
    a "Because…"
    "{i}Jane begins to stir.{/i}"
    j "{i}Crap. I may have pushed it too far. Who’d have thought it would take a trance and me looking at her in the shower to finally have this conversation?{/i}"
    "{i}Jane settles down again.{/i}"
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0038.ogg"
    a "...fine."
    j "Fine what?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0039.ogg"
    a "Fine. You...be cool...I’ll...be cool."
    j "Cool."
    voice "VoiceActing/Day 01/Jane/D01JaneL0040.ogg"
    a "Cool."
    $ Jane_c.add_points(1)
    jump aB


label aA2:
    j "Why are you mad at me?"
    show Jane frown
    "{i}Jane stirs.{/i}"
    voice "VoiceActing/Day 01/Jane/D01JaneL0041.ogg"
    a "Why am I...why am I mad??"
    "{i}She sits up, furious.{/i}"
    show Jane angry
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0042.ogg"
    a "You know exactly why I’m mad, you little creep! You walked in on me in the shower!"
    play sound "music/Smashing.mp3"
    j "No!!"
    j "So many months of work...wasted!"
    voice "VoiceActing/Day 01/Jane/D01JaneL0043.ogg"
    a "Now get out of my room, and tell Mom that I don’t want to see you for the rest of the weekend! No, scratch that - for the rest of my LIFE!"
    scene black with fade
    pause 1
    scene cgbg
    show badend covers
    j "{i}Without my delimiter, the rest of the blizzard was just like the rest of my life. Boring, lame, and...frustrating.{/i}"
    return


label aA3:
    show Jane hypno_smile
    "{i}Jane laughs.{/i}"
    voice "VoiceActing/Day 01/Jane/D01JaneL0044.ogg"
    a "You’re...a dick."
    j "{i}When we were kids, if one of us was mad at the other, all we had to do was make them laugh and all was forgiven. It was sort of an unwritten rule.{/i}"
    j "I am sorry though."
    "{i}Jane sighs.{/i}"
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0045.ogg"
    a "Just...be cool, okay?"
    j "Okay."
    $ Jane_c.add_points(2)
    jump aB



label aB:
    j "{i}Time to get to work.{/i}"
    menu:
        "Why are you so sports-obsessed?":
            jump aB1
        "We used to be close. What happened?":
            jump aB2
        "So what time are you going to be showering in the morning?":
            jump aB3



label aBa:
    menu:
        "Why are you so sports-obsessed?":
            jump aB1
        "We used to be close. What happened?":
            jump aB2


label aB1:
    j "Why are you so sports-obsessed?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0046.ogg"
    a "Like to keep...fit…"
    j "Yeah, but the way you do it - it’s almost an obsession."
    voice "VoiceActing/Day 01/Jane/D01JaneL0047.ogg"
    a "You...you reckon?"
    j "Yeah, it’s insane. You’re always at a practice, or in a game, or just down at the gym. Are you practicing to become a body-builder?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0048.ogg"
    a "Body...builder?"
    j "Yeah. You training to be the next Arnold Schwarzenegger?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0049.ogg"
    a "You think I look like...a guy?"
    j "{i}Well that wasn’t what I’d meant, but sure. I could do something with that.{/i}"
    j "Sort of, yeah. I mean, look at what you’re wearing - it’s hardly feminine, is it?"
    "{i}Jane sits up and looks at her sports gear.{/i}"
    voice "VoiceActing/Day 01/Jane/D01JaneL0050.ogg"
    a "I guess...not…"
    jump aC


label aB2:
    j "We used to be close. What happened?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0051.ogg"
    a "You got...weird."
    j "I got weird? What do you mean?"
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0052.ogg"
    a "Started...checking me out. Perving…"
    j "{i}Uh, okay. I might be guilty of that. I’d thought I was being subtle, but I suppose when I was younger, I didn’t quite get how subtlety worked.{/i}"
    j "Oh."
    voice "VoiceActing/Day 01/Jane/D01JaneL0053.ogg"
    a "That’s why I never...dress…"
    a "…"
    a "…"
    j "What?"
    if Jane_c.points <= 1:
        jump aB4
    else:
        jump aB5

label aB4:
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0054.ogg"
    a "...nothing."
    j "Huh. I wonder what she was going to say."
    jump janewake1

label aB5:
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0055.ogg"
    a "...feminine."
    j "What?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0056.ogg"
    a "That’s why...always...dress...masculine."
    j "{i}I had wondered.{/i}"
    j "Well, I’m going to be cool from now on, okay?"
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0057.ogg"
    a "...okay."
    j "So you can totally dress more feminine around the house, and it won’t be no thing. Cool?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0058.ogg"
    a "...cool."
    $ Jane_c.add_points(1)
    jump aC


label aB3:
    j "So what time are you going to be showering in the morning?"
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0059.ogg"
    a "Ha."
    jump aBa

label aC:
    menu:
        "You know what’d be cool? If we started having showers together in the morning.":
            jump aC1
        "Are you even wearing anything feminine right now?":
            jump aC2




label aC1:
    j "You know what’d be cool? If we started having showers together in the morning."
    voice "VoiceActing/Day 01/Jane/D01JaneL0060.ogg"
    a "...not...funny…"
    j "No, I’m serious. Wouldn’t that make you feel super feminine? Having a naked man pressed against your nude, soapy body…"
    voice "VoiceActing/Day 01/Jane/D01JaneL0061.ogg"
    a "Gross…"
    j "I mean, I’m your brother. It’s not like it’s some stranger."
    voice "VoiceActing/Day 01/Jane/D01JaneL0063.ogg"
    a "You’re so...weird..."
    j "She’s not even stirring...maybe that means she’s sort of into this? I’m going to see how far I can push it."
    jump aD


label aC2:
    j "Are you even wearing anything feminine right now?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0064.ogg"
    a "...yeah."
    j "Oh yeah? What?"
    if Jane_c.points >= 2:
        jump janeyes
    else:
        jump janeno


label janeno:
    voice "VoiceActing/Day 01/Jane/D01JaneL0065.ogg"
    a "My...underwear."
    show Jason happy_ad
    j "{i}What.{/i}"
    j "Oh yeah?"
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0066.ogg"
    a "...yeah."
    j "Can I...see?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0067.ogg"
    a "...no."
    j "Oh."
    $ Jane_c.sub_points(1)
    jump janewake1



label janeyes:
    voice "VoiceActing/Day 01/Jane/D01JaneL0068.ogg"
    a "My...underwear."
    show Jason happy_ad
    j "Oh yeah?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0069.ogg"
    a "...yeah."
    show Jason neutral
    j "{i}There were a few different ways I could play this, but I know Jane...and Jane is competitive.{/i}"
    j "I don’t believe you."
    show Jane shocked
    voice "VoiceActing/Day 01/Jane/D01JaneL0070.ogg"
    a "What??"
    "{i}She begins to stir slightly.{/i}"
    show Jason avoid
    j "{i}Shit shit shit shit.{/i}"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0071.ogg"
    a "Thought...gonna be...cool…"
    j "{i}Well, it’s definitely worth the risk.{/i}"
    j "I’m being cool. I thought you were going to be cool."
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0072.ogg"
    a "Being...cool…"
    j "Okay then. If we’re really being cool with each other, why don’t you show me?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0073.ogg"
    a "Mmm...no…"
    j "I understand. You’re chicken."
    "{i}Jane stirs again.{/i}"
    show Jane hypno
    voice "VoiceActing/Day 01/Jane/D01JaneL0074.ogg"
    a "Not...chicken…"
    j "Go on then."
    voice "VoiceActing/Day 01/Jane/D01JaneL0075.ogg"
    a "Promise...to be...cool?"
    j "Of course."
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0076.ogg"
    a "Fine…"
    scene cgbg with dissolve
    show jane_girly
    $ persistent.girly = True
    $ achievement.grant("Lingere_Jane")
    $ achievement.Sync()
    j "Wow."
    j "{i}Stay cool, J. Stay cool.{/i}"
    j "Yeah, I dunno if I’d really call that ‘feminine’."
    j "{i}Okay, I'm lying. That's pretty feminine. I mean I can see her nipples through that! God that's so hot. Still, she'll react better if I tell her it isn't.{/i}"
    voice "VoiceActing/Day 01/Jane/D01JaneL0077.ogg"
    a "...no?"
    j "I mean, I think feminine underwear, I think frilly stuff. Thongs, lacy bras, that kind of stuff."
    voice "VoiceActing/Day 01/Jane/D01JaneL0078.ogg"
    a "I have…"
    j "What?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0079.ogg"
    a "Nothing."
    j "{i}I bet she was going to say that she has some more feminine underwear. Pity she cut off when she did. Still, I can’t complain too much; I got way further than I expected.{/i}"
    j "{i}Maybe because she knows that I already saw her in the nude this morning, she was more comfortable with me seeing her body.{/i}"
    $ Jane_c.add_points(1)
    jump janewake2


label aD:
    menu:
        "There’s nothing weird about having a shower with your brother.":
            jump aD1
        "After all, it’s not like we’d be fucking. Although...wouldn’t that make you feel REALLY feminine, getting fucked?":
            jump aD2
        "Let’s go and have a shower right now.":
            jump aD3



label aD1:
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0080.ogg"
    a "Yes...is…"
    j "Nah. We’re family! We used to shower together all the time as kids, remember?"
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0081.ogg"
    a "Mmm…"
    j "There wasn’t anything weird about it then. Why would there be anything weird about it now?"
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0082.ogg"
    a "Because...boobs…"
    show Jane hypno
    j "Yeah, but you’re my sister. I don’t even notice your tits."
    show Jane hypno_frown
    voice "VoiceActing/Day 01/Jane/D01JaneL0083.ogg"
    a "You’re so...full...of shit…"
    j "I don’t think this is working. I’m going to try something else."
    $ Jane_c.sub_points(1)
    jump aC





label aD2:
    voice "VoiceActing/Day 01/Jane/D01JaneL0084.ogg"
    a "Ew…"
    j "I mean, what could possibly be more feminine than feeling a big, meaty cock slipping between your wet folds…"
    show Jane shocked
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0085.ogg"
    a "What??"
    "{i}She blinkingly wakes up.{/i}"
    show Jason avoid
    j "{i}Uh-oh.{/i}"
    show Jane angry
    voice "VoiceActing/Day 01/Jane/D01JaneL0086.ogg"
    a "God, I should have known you couldn’t just be cool! Get out!"
    j "But…"
    voice "VoiceActing/Day 01/Jane/D01JaneL0087.ogg"
    a "I said get out!!"
    play sound "music/Smashing.mp3"
    stop music
    j "No!!"
    scene black with fade
    pause 1
    scene cgbg
    show badend covers
    j "{i}So many months of work...wasted!{/i}"
    j "{i}Without my delimiter, the rest of the blizzard was just like the rest of my life. Boring, lame, and...frustrating.{/i}"
    return


label aD3:
    show Jane hypno_smile
    voice "VoiceActing/Day 01/Jane/D01JaneL0088.ogg"
    a "Ha ha ha…"
    j "{i}Well, it was worth a try.{/i}"
    jump aC



label janewake1:
    show Jason neutral at jason_normal(mid_left)
    show Jane hypno at jane_normal(far_right)
    j "Okay Jane, I’m going to count down from 5."
    voice "VoiceActing/Day 01/Jane/D01JaneL0089.ogg"
    a "O...kay…"
    j "When I get to five, you’ll be wide awake, and it’ll be like we never had this conversation. Got it?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0090.ogg"
    a "Got...it…"
    j "5. All you’ll remember is that I apologized and we bonded."
    voice "VoiceActing/Day 01/Jane/D01JaneL0091.ogg"
    a "Bonded…"
    j "4. From now on, you and I are going to be cool. We’re going to be close, like we used to be. No more secrets, right?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0092.ogg"
    a "No...more...secrets…"
    j "3. All you’re going to remember is that we hung out and made each other laugh."
    voice "VoiceActing/Day 01/Jane/D01JaneL0093.ogg"
    a "Hung...out…"
    j "2. And you’re going to feel weird about the fact that you don’t dress more feminine. Tomorrow you’ll wear some more form-fitting clothes."
    j "It’s going to feel good to dress feminine around the house, isn’t it?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0094.ogg"
    a "Yess. Feminine...around the house…"
    j "Good girl."
    voice "VoiceActing/Day 01/Jane/D01JaneL0095.ogg"
    a "Good...girl…"
    j "1."
    play music "music/Jane's Theme.mp3" fadeout 1.0 fadein 1.0
    show Jane neutral
    "{i}Jane snaps awake, and looks around groggily.{/i}"
    show Jason at talking_stay
    j "So yeah, like I was saying - I’m so sorry, and I hope you can forgive me."
    show Jason at normal_stay
    show Jane happy
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0096.ogg"
    a "Of course I can forgive you. You’re my twin brother! Just...be cool, okay?"
    show Jane at normal_stay
    show Jason at talking_stay
    j "For sure. You too, hey sis?"
    show Jason at normal_stay
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0097.ogg"
    a "Now shoo. I want to get changed."
    $ janepanties = False
    jump Family3




label janewake2:
    scene jane_room_d1d with fade
    show Jason happy_aroused at jason_normal(mid_left)
    show Jane hypno at jane_normal(far_right)
    j "Okay sis, I’m going to count down from 5."
    voice "VoiceActing/Day 01/Jane/D01JaneL0098.ogg"
    a "O...kay…"
    j "When I get to one, you’ll be wide awake, and it’ll be like we never had this conversation. Got it?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0099.ogg"
    a "Got...it…"
    j "You won’t even care that you’re in your underwear. After all, there’s nothing weird about wearing underwear around your brother, is there?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0100.ogg"
    a "Nothing...weird…"
    j "5. You’ll remember that I came in while you were already in a bra and panties. There’s nothing strange about that, is there?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0101.ogg"
    a "Nothing...strange..."
    j "4. You’ll remember me apologizing, and us just hanging out and making each other laugh."
    voice "VoiceActing/Day 01/Jane/D01JaneL0102.ogg"
    a "Hanging...out..."
    j "3. We’re going to be extra close from now on. Close like twins should be."
    voice "VoiceActing/Day 01/Jane/D01JaneL0103.ogg"
    a "Extra...close..."
    j "2. And you’re going to feel weird about the fact that you don’t dress more feminine. Tomorrow you’ll wear some more form-fitting clothes."
    j "It’s going to feel good to dress feminine around the house, isn’t it?"
    voice "VoiceActing/Day 01/Jane/D01JaneL0104.ogg"
    a "Yess. Feminine...around the house…"
    j "Good girl."
    voice "VoiceActing/Day 01/Jane/D01JaneL0105.ogg"
    a "Good...girl…"
    j "1."
    show Jane happy
    "{i}Jane snaps awake, and looks around groggily.{/i}"
    show Jason at talking_stay
    j "So yeah, like I was saying - I’m so sorry, and I hope you can forgive me."
    show Jason at normal_stay
    "{i}Jane smiles wider.{/i}"
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0106.ogg"
    a "Of course I can forgive you. You’re my twin brother! Just...be cool, okay?"
    show Jane at normal_stay
    show Jason at talking_stay
    j "For sure. You too, hey sis?"
    show Jason at normal_stay
    show Jane happy
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D01JaneL0107.ogg"
    a "Now scram. I should get dressed."
    $ janepanties = True
    jump Family3






label Family3:
    scene bathroom_d1n with fade
    play music audio.deep_breaths_guitar fadein 1.0
    show Jason neutral at jason_normal(far_left)
    show Noelle neutral at noelle_normal(far_right)
    play music "music/Noelle's Theme.mp3" fadeout 1.0 fadein 1.0
    j "{i}It took me a while to find Mom again. She was in the bathroom - she wasn’t having a shower or anything like that, she was just folding towels.{/i}"
    j "Hey Mom. You wanted to talk?"
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0034.ogg"
    n "Oh, yes. Let’s go to the kitchen."
    show Noelle at normal_stay
    j "{i}I can’t put her under in the kitchen; there’s too much of a chance that someone will walk in.{/i}"
    j "Before we do, can I just show you something?"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0035.ogg"
    n "In here?"
    show Noelle at normal_stay
    j "Of course. The acoustics in here are amazing. Let me shut the door so you can hear it better."
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0036.ogg"
    n "Mmmm…"
    j "Doesn’t that sound good?"
    show Noelle happy
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0037.ogg"
    n "Sounds...good…"
    j "Listen to it echoing off the tiles. Really listen, let the music take over your mind."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0038.ogg"
    n "Take...over...mind…"
    j "It even makes that dripping tap sound good."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0039.ogg"
    n "Dripping...tap…?"
    j "Yeah, the dripping tap. Can’t you hear it?"
    j "Drip, drip, drip, drip…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0040.ogg"
    n "That’s...not…"
    j "Of course it is. It just doesn’t sound like a dripping tap, because it goes so well with the music. Right? Listen to its steady rhythm. Drip, drip, drip, drip."
    show Noelle hypno at noelle_normal(far_right)
    show Noelle hypno_enter
    pause random_true_float(1.0, 2.0)
    show Noelle hypno
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0041.ogg"
    n "Drip...drip…"
    j "It’s impossible to think about anything else, isn’t it?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0042.ogg"
    n "Impossible…to think..."
    j "The music and the dripping are bouncing off every wall, closing in, completely surrounding you. But it feels good, safe…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0043.ogg"
    n "Good...safe…"
    j "You’re safe here. Safe with your son, who you trust."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0044.ogg"
    n "Trust...son…"
    j "You trust me, don’t you?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0045.ogg"
    n "Mmmm…"
    j "You love being alone in here, with your only son. Surrounded by the music, accompanied by your trusting, loving son...and the dripping tap. Drip, drip, drip."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0046.ogg"
    n "Drip…"
    j "You can talk to me about anything, because you completely trust me."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0047.ogg"
    n "Yes...trust…"
    j "{i}I think this is the first time in my life I’ve ever seen her relaxed. She’s normally determined to show everyone she’s the boss. It’s weird. Good, but weird.{/i}"
    j "{i}She isn’t like my sisters… she’s much scarier. Part of me wants to apologize and run away, part of me wants to push her as hard as I can.{/i}"
    j "Great. Now, what did you want to talk about?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0048.ogg"
    n "Wanted to talk...about...Jane…"
    play music "music/Noelle's Alternate Theme.mp3" fadeout 1.0 fadein 1.0
    jump nA


label nA:
    menu:
        "It’s okay Mom, I talked to Jane. Everything is fine.":
            jump nA1
        "What did you want to talk about?":
            jump nA2
        "Are you sure you don’t want to talk about sex?":
            jump nA3



label nA1:
    j "It’s okay Mom, I talked to Jane. Everything is fine."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0049.ogg"
    n "Hmmm…"
    j "No, for real. We made up, and she said that she forgave me."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0050.ogg"
    n "I don’t...know…"
    j "I promise. Everything worked out totally fine."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0051.ogg"
    n "If you…say so..."
    j "{i}Phew.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0052.ogg"
    n "Still want to...talk…"
    $ Noelle_c.add_points(1)
    jump nA2


label nA2:
    j "What did you want to talk about?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0053.ogg"
    n "About...this morning…"
    j "Yeah?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0054.ogg"
    n "Shouldn’t have...done that…"
    j "I know. It was wrong of me to spy on my sister in the shower."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0055.ogg"
    n "Should...talk…"
    jump nB



label nA3:
    j "Are you sure you don’t want to talk about sex?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0056.ogg"
    n "About...sex…?"
    play music "music/Noelle's Theme.mp3" fadeout 1.0 fadein 1.0
    j "Yeah. I mean, we could be in here for weeks - months, even. We need to work out how we’re going to deal with this."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0057.ogg"
    n "Deal with...this…?"
    j "You’re all women, I’m a man. It makes sense that you wanted to talk - you wanted to make sure I was up for sexually pleasing my sisters AND you."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0058.ogg"
    n "What??"
    j "{i}Uh-oh.{/i}"
    j "I mean…"
    "{i}Noelle wakes up.{/i}"
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0059.ogg"
    n "How can you THINK of your family in that way? I don’t know where I went wrong with you, Jason..."
    j "I...uh...listen to the dripping tap. Drip, drip, drip…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0060.ogg"
    n "There IS no dripping tap! I take good care of this house, and you just sit around and play music all day."
    j "Listen to the music…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0061.ogg"
    n "No! In fact, if I ever hear that music again, you are grounded for the rest of your days!"
    j "{i}She's too fast for me; the delimiter is gone before I realize what happened.{/i}"
    j "Wait!"
    scene black with fade
    pause 1
    scene cgbg
    show badend covers
    j "{i}Yeah, I didn’t really think that one through. There goes my chances of ever getting anywhere with Mom...or my sisters…{/i}"
    j "{i}And that means...{/i}"
    return



label nB:
    menu:
        "I just want to say I’m really sorry.":
            jump nB1
        "I’m not sorry for what I did.":
            jump nB2
        "I think YOU should apologize.":
            jump nB3



label nB1:
    j "I just want to say I’m really sorry."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0062.ogg"
    n "Okay…"
    j "I promise, I’ll never do anything like that again. What I did was bad, and it was entirely my fault."
    show Noelle hypno_frown
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0063.ogg"
    n "Mmmm…"
    j "Do you forgive me?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0064.ogg"
    n "We’ll...see…"
    $ Noelle_c.sub_points(1)
    jump nC




label nB2:
    j "I’m not sorry for what I did."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0065.ogg"
    n "Why...not…?"
    j "It didn’t hurt anyone."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0066.ogg"
    n "Sisters...privacy…"
    j "Well, okay. It wouldn’t have hurt anyone if I didn’t get caught."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0067.ogg"
    n "Don’t do...again…"
    j "Okay Mom. I won’t do it again."
    "{i}I won’t get caught again, anyway.{/i}"
    jump nC



label nB3:
    j "I think YOU should apologize."
    show Noelle shocked
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0068.ogg"
    n "What??"
    "{i}She stirs slightly.{/i}"
    j "Sshhh...shhh...listen to the drip, drip, drip."
    show Noelle hypno
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0069.ogg"
    n "Drip…"
    j "Good. That’s so nice and calming, isn’t it?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0070.ogg"
    n "Mmmm…"
    j "Now, Mom, I think you should apologise."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0071.ogg"
    n "Why…?"
    j "All my life, you’ve been a busy businesswoman, running around. You never had time to raise me, to teach me what was and wasn’t okay. You were barely there when I was young, were you?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0072.ogg"
    n "Barely...there…"
    j "No one was around to teach me right from wrong, no one was there to show me what a growing boy should and shouldn’t do. Where were you?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0073.ogg"
    n "Working…"
    j "You weren’t there, were you?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0074.ogg"
    n "Wasn’t...there…"
    j "And so yeah, I think you should apologize. For screwing up my childhood, and leaving me confused, with desires I don’t even understand."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0075.ogg"
    n "Confused...desires…"
    j "{i}I actually think my childhood was pretty normal, to be honest. But I know Mom sometimes feels guilty about how hard she works. Besides, it plays into her control freak nature - if there’s something wrong in her house, of COURSE it’s her fault.{/i}"
    j "{i}She has no way of knowing that I’m just naturally a perv.{/i}"
    j "Well?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0076.ogg"
    n "Well...what…?"
    j "Well, are you going to apologize?"
    "{i}Noelle stirs briefly, then stops.{/i}"
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0077.ogg"
    n "I’m...sorry…"
    show Jason happy
    j "{i}Wow. I didn’t really expect that to work.{/i}"
    $ Noelle_c.add_points(3)
    jump nC

label nC:
    menu:
        "Is that all you wanted to talk to me about?":
            jump nC1
        "I hope you feel better.":
            jump nC2
        "I promise I’ll never do it again.":
            jump nC3

label nC1:
    j "Is that all you wanted to talk to me about?"
    if Noelle_c.points >= 3:
        jump noellesucceed
    else:
        jump wakeupfail

label noellesucceed:
    show Noelle hypno_frown
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0078.ogg"
    n "Want to...make sure…"
    j "Make sure of what?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0079.ogg"
    n "Make sure...doesn’t happen...again…"
    j "You know I can’t promise that."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0080.ogg"
    n "I...know…"
    jump nD

label nC2:
    j "I hope you feel better."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0081.ogg"
    n "Little...better…"
    j "That’s good."
    $ Noelle_c.sub_points(1)
    jump wakeupfail

label nC3:
    j "I promise I’ll never do it again."
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0082.ogg"
    n "Good...boy…"
    j "Thanks, Mom."
    $ Noelle_c.sub_points(1)
    jump wakeupfail

label nD:
    menu:
        "I’m a teenage boy. I have needs.":
            jump nD1
        "I can only promise to try.":
            jump nD2

label nD1:
    j "I’m a teenage boy. I have needs."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0083.ogg"
    n "But...wrong…"
    j "I know it’s wrong. But what else am I supposed to do?"
    show Noelle hypno_frown
    "{i}Noelle stirs slightly.{/i}"
    j "{i}Shit. I hope she doesn’t snap out of it - I guess I should have thought twice before asking my Mom about what I was meant to jerk off to.{/i}"
    j "{i}Still, fortune favors the bold.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0084.ogg"
    n "Internet...porn…?"
    j "The internet is down, Mom."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0085.ogg"
    n "Magazines?"
    j "How am I supposed to keep dirty magazines around when you search my room every few days?"
    j "{i}It’s true. I told you she was a control freak.{/i}"
    j "You caused this problem, Mom, and it’s your job to fix it."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0086.ogg"
    n "I’m...sorry…"
    j "Sorry isn’t good enough. We could be locked in here for days - what am I meant to look at to get off?"
    show Noelle hypno
    j "{i}Mom stirs again and blushes.{/i}"
    j "{i}Mom definitely isn’t used to being talked to like this. Normally she’d have tossed me outside by now. She’s responding to authority - I’ll have to remember that.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0087.ogg"
    n "You could…"
    n "..."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0088.ogg"
    n "You could…"
    j "What?"
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0089.ogg"
    n "You could...watch me...shower…"
    j "What??"
    show Jason happy_ad
    j "{i}Wow!! I did NOT expect that. Mom must be feeling REALLY guilty about not being around when I was a kid.{/i}"
    show Jason neutral
    j "What do you mean?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0090.ogg"
    n "If you need to...look…"
    j "Yeah…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0091.ogg"
    n "Want to...protect...your sisters…"
    j "Well…"
    jump nF

label nD2:
    j "I can only promise to try."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0092.ogg"
    n "Do you...promise...try?"
    jump nE

label nE:
    menu:
        "Yes.":
            jump nE1
        "No.":
            jump nE2

label nE1:
    j "I promise to try, Mom."
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0093.ogg"
    n "Thanks...Jason…."
    j "I love you."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0094.ogg"
    n "Love you...too…"
    j "Was there anything else?"
    $ Noelle_c.sub_points(2)
    jump wakeupfail

label nE2:
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0095.ogg"
    n "Why...not…?"
    j "Because I’m a teenage boy, in a house surrounded by women. I have needs, Mom."
    jump nD1

label nF:
    menu:
        "I guess if I watched you in the shower, I wouldn’t have to peek at them any more.":
            jump nF1
        "What if you all had a shower together so I could watch?":
            jump nF2

label nF1:
    j "I guess if I watched you in the shower, I wouldn’t have to peek at them any more."
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0096.ogg"
    n "O...kay…"
    show Jason happy_ad
    j "For real? Okay?"
    show Noelle hypno
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0097.ogg"
    n "Just this...once. Get it out of...system…"
    j "Of course. It’d just be the one time."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0098.ogg"
    n "Leave sisters...alone…"
    show Jason daydream_aroused
    j "Oh yeah. If we do this, I won’t spy on anyone in the shower again."
    j "{i}I mean, if everything goes according to plan...I won’t have to.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0099.ogg"
    n "Okay…"
    show Jason happy_aroused
    j "Wow."
    jump wakeupshower

label nF2:
    j "What if you all had a shower together so I could watch?"
    play music "music/Noelle's Theme.mp3" fadeout 1.0 fadein 1.0
    show Noelle angry
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0100.ogg"
    n "What??"
    "{i}She begins to stir.{/i}"
    j "{i}Ah crap. May have pushed that too far.{/i}"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0101.ogg"
    n "Jason, here I am offering to help...but you just had to push it, didn’t you?"
    show Noelle at normal_stay
    j "Uh…"
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0102.ogg"
    n "And what are we doing talking in here? I told you I wanted to discuss this in the kitchen! What will your sisters think if they find us alone in here?"
    show Noelle angry
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0103.ogg"
    n "Follow me, young man!"
    scene black with fade
    pause 1
    scene cgbg
    show badend cooking
    $ achievement.grant("NEW_ACHIEVEMENT_1_8")
    $ achievement.Sync()
    j "{i}After that, probably out of guilt about what she suggested, Mom refused to chat with me alone. Without being able to put Mom under, I couldn’t get away with controlling my sisters.{/i}"
    j "{i}All my plans for the blizzard collapsed and life returned to normal…{/i}"
    return

label wakeupshower:
    play music audio.habanera fadein 1.0
    show Noelle hypno_smile
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0104.ogg"
    n "Mmm…"
    j "Okay Mom, I’m going to count down from 5. When I reach 1, you’re going to wake up and let me watch you while you shower."
    show Noelle hypno
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0105.ogg"
    n "Okay…"
    j "You’ll remember that we had a chat, you felt responsible for my perversions, and you came up with the solution of watching YOU shower, so I wouldn’t have to bother my sisters. Got it?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0106.ogg"
    n "Got...it…"
    j "You’ll feel closer to me as a person, and any time I want to talk, you’ll be happy to chat."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0107.ogg"
    n "O...kay…"
    j "And you’ll love the feeling of my eyes on you when you’re in the shower. It’ll feel so wrong, but so good. You might even get…"
    j "{i}Should I say it? Or would that be pushing things too far?{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0108.ogg"
    n "Turned...on…"
    show Jason happy_ad
    j "{i}Wow! Apparently I don’t even have to. Maybe Mom has a bit of an exhibitionist streak, deep down inside. That’d certainly explain some of the clothes she wears to work.{/i}"
    j "5, 4, 3, 2, 1."
    show Noelle lewd
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0110.ogg"
    n "Okay Jason, let’s do this. Remember...this is something we can never repeat, and we definitely can’t tell anyone."
    show Noelle at normal_stay
    show Jason happy
    show Jason at talking_stay
    j "Of course, Mom."
    show Jason at normal_stay
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0111.ogg"
    n "Now I’m going to leave the door open, so you have a better view. After we’re done here, I want you to make sure there’s no water left on the bathroom floor."
    show Jason at talking_stay
    j "Fine, Mom."
    show Jason at normal_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0112.ogg"
    n "And you can never, ever, tell anyone."
    j "Got it."
    show Noelle neutral
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0113.ogg"
    n "Okay."
    show Noelle at normal_stay
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0114.ogg"
    n "Turn around so I can get undressed."
    show Jason avoid
    j "What? But…"
    show Jason neutral
    j "{i}Ah, it’s not worth arguing. I don’t want to do ANYTHING that could make her change her mind now.{/i}"
    hide Noelle with dissolve
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0115.ogg"
    n "Okay…"
    j "{i}She sounds nervous. I guess this isn’t something that happens every day.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0117.ogg"
    n "I’m going to...let’s...I mean…"
    j "It’s cool, Mom. You’re doing the right thing."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0116.ogg"
    n "Okay."
    "{i}She gets in the shower, revealing everything.{/i}"
    scene cgbg with fade
    show nshowg1
    j "{i}Wow. WOW. This was everything I wanted, and more. If the shower wasn’t so loud, I’d turn the music on and put her under while she’s naked.{/i}"
    hide nshowg1
    show nshowg2
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0118.ogg"
    n "Is this...is this what you need?"
    j "It sure is!"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0119.ogg"
    n "So are you going to…"
    j "{i}Wait. Is she asking what I think she’s asking?{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0121.ogg"
    n "I mean, if you want to. If you think I’m…"
    j "Oh trust me Mom, I want to. You’re so hot."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0122.ogg"
    n "Oh. Well...thanks."
    hide nshowg2
    show nshowg4
    j "Are you sure you don’t mind if I do?"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0123.ogg"
    n "Well why else would we be doing this?"
    j "Hey, you don’t have to ask me twice."
    hide nshowg4
    show nshowg5
    j "{i}I pull out my cock and start jerking off. Mom moves left and right a bit, showing off her body.{/i}"
    j "{i}Holy shit, I can’t believe she’s watching me. I think she’s getting turned on…{/i}"
    j "You know, Mom, if you want to play with yourself while we do this…"
    hide nshowg5
    show nshowg3
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0124.ogg"
    n "What?? Jason, that’s totally inappropriate."
    j "I mean...it’d help me. It’d help this go faster."
    hide nshowg3
    show nshowg6
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0125.ogg"
    n "Oh! Oh, well. Well, in that case...maybe…"
    hide nshowg6
    show nshowg7
    "{i}She reaches between her legs.{/i}"
    j "{i}This is better than my wildest fantasies.{/i}"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0126.ogg"
    n "Mmmm…"
    hide nshowg7
    show nshowg8
    j "God, Mom, you’re so freaking hot…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0127.ogg"
    n "Oh, Jason…"
    hide nshowg8
    show nshowg9
    j "Oh, Mom!"
    hide nshowg9
    show nshowg10
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0128.ogg"
    n "Oh, Jason!"
    hide nshowg10
    show nshowg11
    j "I want you to cum for me, Mom. I want you to cum…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0129.ogg"
    n "Oh, Jason, I’m cumming! Momma’s cumming for you!"
    hide nshowg11
    show nshowg13
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0130.ogg"
    n "Jason!"
    hide nshowg13
    show nshowg14
    j "Wow. That was amazing."
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0131.ogg"
    n "Jason, that was…"
    n "…"
    n "…"
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0132.ogg"
    n "Make sure you clean this up before your sisters find anything, okay?"
    "{i}She quickly washes the cum off of herself in the shower.{/i}"
    j "Of course, Mom."
    hide nshowg14
    show nshowg12
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0133.ogg"
    n "And we can never, ever do this again."
    j "Of course."
    $ achievement.grant("X_to_Jason")
    $ achievement.Sync()
    j "{i}At least, that’s what you think…{/i}"
    hide Jason
    hide Noelle
    $ noelleshower = True
    $ persistent.noelleshower = True
    jump endday1

label wakeupfail:
    voice "VoiceActing/Day 01/Noelle/D01NoelleL0134.ogg"
    n "That’s...all…"
    j "Okay Mom. Thanks for the chat. I’m going to count to 5 - when I reach 5, I want you to wake up, and only remember we had a good talk, and nothing unusual happened."
    show Jason avoid
    j "{i}Actually, nothing much unusual did happen. Sort of feels like a waste.{/i}"
    show Jason neutral
    j "1...2...3...4...5."
    $ noelleshower = False
    jump endday1




label endday1:
    $ persistent.d1u = True
    scene jason_room_d with fade
    play music "music/Jason's Theme.mp3" fadeout 1.0 fadein 1.0
    show Jason neutral at jason_normal(mid_left)
    j "{i}Whew. That was a hell of a day. I made some good progress, but I still have a long way to go.{/i}"
    j "{i}Tonight I’m going to play the delimiter through the vents again...that should make everyone even more pliable for tomorrow’s sessions.{/i}"
    j "{i}I currently have [Kira_c.points] Kira [Sarah_c.points] Sarah [Noelle_c.points] Noelle [Jane_c.points] Jane points.{/i}"

    scene black with fade
    stop music

    show text "END OF DAY ONE" at truecenter with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    show text "FOUR DAYS REMAIN" at truecenter with dissolve
    $ achievement.grant("Flash_Fever")
    $ achievement.Sync()
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    jump family4
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
