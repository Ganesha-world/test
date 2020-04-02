

label opt_op:
    scene black




    "This game is perverted fantasy where evil can win and do lewd things to good people. You bring that to real life it’s on you."
    "All characters in this game are step family and Jason and Jane are step-twins."
    "I know that doesn’t make sense, it’s not supposed to."
    "This game deals with many different adult themes and kinks. These represent fantasy and not reality, nor any of the real world beliefs of any of our staff."
    "You really, truly shouldn’t play this if you are underage. This is for adults only."
    if not renpy.variant("small"):
        "Remember you can press ‘H’ on your keyboard to hide the text box and see the images in the background in their full boxless glory."
        "Right click to open the save menu, select preferences and adjust music and voice acting levels. Outfits can be adjusted from the extras menu in the main-menu. This will make the game much more youtube friendly."
    "Would you like to watch the opening introduction by the creator, CypressZeta?"

    menu:
        "Yes":
            jump cypresstart
        "No":
            jump regstart

label cypresstart:
    show Cypress happy at zoom_cyp with dissolve
    c "Hello everypurrson out there! I am CypressZeta, the creator of this game and head of Outbreak Games!"
    c "I'm pawsitively delighted you're playing this game!"
    c "Say, that opening disclaimer thing probably had you asking questions, huh?"
    show Cypress derpy at zoom_cyp with dissolve
    c "How can everyone be step-family if they never mention it in game? How the heck are step-twins supposed to work?"
    c "Answer: Cat-magic."
    show Cypress lewd at zoom_cyp with dissolve
    c "Long ago there was nothing but void. I used cat-magic and made a world for the specific purpose of creating a hot faux-incest scenario!"
    c "The entire family was made from nothing already fully aged and with a history and everything. So Noelle didn't give birth to Jason. They're all step-family!"
    show Cypress derpy at zoom_cyp with dissolve
    c "...Technically."
    c "What about DNA you ask? Cat-magic. It's whatever you want it to be."

    show Cypress sad at zoom_cyp with dissolve
    c "I should feel sorry for everyone else I created in that world living, dying, suffering and so on. It's a full world with cities and history and everything."
    show Cypress happy at zoom_cyp with dissolve
    c "I don't."
    c "I am a cat. I don't have a conscience."
    c "They'd probably be really depressed to find out that their entire world exists so a boy can try to fuck his own family."
    c "Good!"
    c "Enjoy the game everynyan!"




    voice sustain
    $ achievement.grant("Cat_Cultist")
    $ achievement.Sync()
    jump regstart

















label regstart:











    $ jane_outfit.CanonOutfit = JaneOutfitEnum.NUDE
    $ jason_outfit.CanonOutfit = JasonOutfitEnum.NORMAL
    $ noelle_outfit.CanonOutfit = NoelleOutfitEnum.NORMAL
    $ sarah_outfit.CanonOutfit = SarahOutfitEnum.NORMAL
    $ kira_outfit.CanonOutfit = KiraOutfitEnum.NORMAL


    play sound "music/HavingAShowerSoundBible.mp3"
    show jane_shower:
        subpixel True
        yalign 1.0
        linear 8 yalign 0.0
    with fade
    $ renpy.pause(7, hard=True)

    scene bathroom_d1d with hpunch
    stop sound fadeout 1.0
    voice "VoiceActing/Day 01/Jane/D00JaneL0001.ogg"
    a "JASON!!!"
    play music audio.masterplan fadein 1.0

    show Jason avoid_aroused at jason_normal(far_left)
    show Jane angry at jane_normal(far_right)
    pause(0.25)


    show Jason at talking_stay
    j "Oh… Uh, hey Jane! I didn't know you were in here."

    show Jason at normal_stay
    show Jane frown
    voice "VoiceActing/Day 01/Jane/D00JaneL0002.ogg"
    a "You creepy little pervert! I can’t believe you!"
    show Jane angry
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D00JaneL0003.ogg"
    a "I'm your SISTER, you freak! Stop trying to watch me in the shower!"
    show Jane at normal_stay
    j "Oh, were you using the shower? I didn't know, uh-"
    show Jane frown
    show Jane at talking_stay
    voice "VoiceActing/Day 01/Jane/D00JaneL0004.ogg"
    a "Don't lie to me! How long were you standing there?"
    j "Maybe a minute?"
    show Jane angry
    voice "VoiceActing/Day 01/Jane/D00JaneL0005.ogg"
    a "Ugh!"
    play sound "music/RightHookSoundBible.wav"
    j "Oww!" with hpunch
    voice "VoiceActing/Day 01/Jane/D00JaneL0006.ogg"
    a "Go play with your Oboe, you creep! I'm telling Mom!! "
    hide Jane with easeoutright
    "{i}Meet my twin sister, Jane. We used to be really close but a few years ago things changed a lot.{/i}"
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show popup_pin
    "{i}She got really into sports and stopped wanting to hang out. She grew up, and really started to grow OUT.{/i}"
    "{i}Maybe it’s the exercise or everything she eats, but she’s no longer my skinny opposite. Now she’s got the body of an amazonian goddess.{/i}"
    j "{i}My name's Jason - Jane and I used to be just like one another, but now we couldn’t be more different. A few years ago she discovered sports and I discovered music. Now she's strong and taut and I’m not.{/i}"
    j "{i}I'm more into cooking, dance, playing the flute. That sort of thing. And I don't think I'm exactly weak... but my sister can beat me in a fight.{/i}"
    j "{i}...Pretty easily, actually. It isn’t right. We used to be almost the same person in two bodies. Now she’s totally different and she’s like a stranger. Sometimes I wish I could just make her do what I want.{/i}"
    j "{i}Sometimes I dream of her being my slave, totally submissive, happily wearing the girly clothes she hates and doing everything I want...{/i}"
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0001.ogg"
    n "JASON!!"
    hide popup_pin with dissolve
    show Jason avoid
    show Noelle frown at noelle_normal(far_right)
    j "Oh… Hi Mom."
    j "{i}This is my mom, Noelle. Not that I’d ever dream of calling her by her first name.{/i}"
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0002.ogg"
    n "I raised you to be better than that, young man!"
    j "{i}If a human being could be the living incarnation of an idea, she’d be the incarnation of the words 'control freak'.{/i}"
    j "{i}She's the head of Business Development for the Ivory Peaks corporation. She makes her employees color code their post-it notes.{/i}"
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0003.ogg"
    n "You're lucky I'm running late for work, but mark my words - when I come home, you and I are having a very long conversation."

    show Noelle at normal_stay
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show popup_noelle_maid
    j "{i}Sometimes I wonder what would happen if she just let loose once in a while.{/i}"
    j "{i}She’s been in charge her whole life. Just once I’d like to see what she’d do if she weren’t the one running things. Hmm. Maybe in something a little skimpy, bent over my knee...{/i}"
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0004.ogg"
    n "Jason! Hey! Are you even listening to me? Pay attention!"
    hide popup_noelle_maid with dissolve
    show Noelle at normal_stay
    show Jason neutral
    j "Sorry, mom."
    show Noelle angry
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0005.ogg"
    n "Hmmmph. Well you’ll be sorry once I get home! Now go downstairs and help Sarah with her homework."
    j "Yes, Mom."




    scene sarah_room_d1d with fade
    show Jason avoid at jason_normal(mid_left)
    show Sarah neutral at sarah_normal(mid_right)
    pause(0.25)
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D00SarahL0001.ogg"
    s "Hey big bro!"
    show Sarah at normal_stay
    j "Hey Sarah."
    j "{i}Jane and I are the middle of four. This is my younger sister, Sarah. She can be a bit of a brat, but she's not too bad.{/i}"

    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D00SarahL0002.ogg"
    s "So Mom said you'd take care of this stuff for me. I need the exercises from chapters two and three done before tomorrow morning."

    show Sarah at normal_stay
    show Jason neutral
    j "What? I'm not going to do it for you."
    show Sarah frown
    show Sarah at talking_stay
    voice "VoiceActing/Day 01/Sarah/D00SarahL0003.ogg"
    s "Oh really? It would be so helpful, big brother. It's so hard...can't you help me out just a little?"
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show popup_sarah_tease
    j "{i}Sarah’s eyes gleam like a shark whenever she asks me to do something. She thinks she can control me just by leaning forward and flashing me a little cleavage like every other guy she meets.{/i}"
    j "{i}Unfortunately she’s right… she can. I wish I had some power over her, just once.{/i}"
    j "{i}Sigh.{/i}"
    hide popup_sarah_tease with dissolve
    j "Fine. But you owe me one, okay?"
    show Sarah happy
    voice "VoiceActing/Day 01/Sarah/D00SarahL0004.ogg"
    s "{i}*giggles*{/i} Of course! Anything you want, bro. Do you mind doing it in the kitchen? I've got a date tonight, and I need to get changed."
    show Sarah at normal_stay
    show Jason daydream
    j "{i}Lucky bastard.{/i}"




    scene kitchen_d1 with fade
    show Jason neutral at jason_normal(mid_left)
    j "{i}My life is hell - I’m surrounded by all these hot women I’ll never be able to touch. Hell, they barely tolerate me as family.{/i}"
    j "{i}But that’s why I’ve been working on a way to get some control. Things are gonna change around here.{/i}"
    show Kira frown at kira_normal(mid_right)
    j "Hey Kira."
    show Kira neutral
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D00KiraL0001.ogg"
    k "Oh god, don't tell me you're doing Sarah's homework. Not again!"
    j "Well...yeah."
    voice "VoiceActing/Day 01/Kira/D00KiraL0002.ogg"
    k "God, Jason. If you're always doing the hard work for her, she's never going to learn! Do you think I became one of the best chemical engineers in the country by getting other people to do my homework for me?"

    j "{i}This is Kira. She's my oldest sister. She's one of the best and youngest chemical engineers in the country. Something she’ll be happy to remind you of - again, and again, and again...{/i}"
    voice "VoiceActing/Day 01/Kira/D00KiraL0003alt.ogg"
    k "Stop acting like one of her little boy-toys, Jason!"
    show Jason avoid
    j "I don't!"
    show Kira frown
    voice "VoiceActing/Day 01/Kira/D00KiraL0004.ogg"
    k "Mmm-hmm. So who did the chores last week?"
    j "Well, that was... {i}*sigh*{/i} Me."
    show Kira neutral
    voice "VoiceActing/Day 01/Kira/D00KiraL0005.ogg"
    k "Exactly. She can’t just get by because she flirts with guys. Especially not you! Our family is better than that. YOU are supposed to be better than that. What kind of big brother are you?"
    j "{i}She's a total control freak - even worse than Mom, sometimes.{/i}"
    j "You’re right, Kira. Sorry."
    voice "VoiceActing/Day 01/Kira/D00KiraL0006.ogg"
    k "Now move; I've got a huge presentation in the morning, and I need some calories to get me through the night."

    show Jason neutral
    j "You're not going to sleep?"
    voice "VoiceActing/Day 01/Kira/D00KiraL0007.ogg"
    k "Of COURSE not! I need to spend as much time as I can getting everything perfect."
    show Kira at normal_stay
    j "{i}I can just imagine it.{/i}"
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show popup_kira_m
    show Jason daydream
    j "{i}I don't think she's ever had a boyfriend. Hell, I don't think she's ever kissed a guy - her whole life has just been work, work work.{/i}"
    j "{i}I bet she has a masturbation schedule, and if she goes thirty seconds over time, she stops immediately.{/i}"
    voice "VoiceActing/Day 01/Kira/D00KiraL0008.ogg"
    k "Damn! So close. Now, back to being the best chemical engineer in the country..."
    show Kira angry
    show Kira at talking_stay
    voice "VoiceActing/Day 01/Kira/D00KiraL0009.ogg"
    k "God, Jason - are you even listening?"
    hide popup_kira_m with dissolve
    j "Uh..."
    show Kira neutral
    voice "VoiceActing/Day 01/Kira/D00KiraL0010.ogg"
    k "How do you think I became one of the youngest chemical engineers in the country?"
    j "Um..."
    voice "VoiceActing/Day 01/Kira/D00KiraL0011.ogg"
    k "Ugh… just move. I don't have time for this. I need to get ready for work!"
    show Jason happy
    j "Oh yeah? What do you do?"
    show Kira frown
    voice "VoiceActing/Day 01/Kira/D00KiraL0012.ogg"
    k "What? You know I'm the youngest chemical engineer in the… you’re mocking me, aren’t you?"
    j "{i}She looks like she's ticked off.{/i}"
    show Kira angry
    voice "VoiceActing/Day 01/Kira/D00KiraL0013.ogg"
    k "Damn it Jason, I don't have time for this! Play your silly games with someone else!"
    show Kira at normal_stay
    hide Kira with dissolve
    j "{i}Three hot sisters and a hot mom and all of them despise me. Sometimes it feels like nothing is going to change and I’m going to be stuck like this forever.{/i}"
    j "{i}They’re barely even here anymore. They’re only ever around long enough to make me do all their work and then head out the door.{/i}"
    j "{i}And the plan I’ve been putting together won’t work if they don’t slow down a bit...{/i}"
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0006.ogg"
    n "Jason!"
    show Jason avoid
    j "What did I do now?"
    show Noelle angry at noelle_normal(mid_right)
    show Jason shocked
    j "Mom? I thought you were at an afternoon business meeting."
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0007.ogg"
    n "Not today. There’s a blizzard on the way - we’re going to be snowed in for the next three or four days, if not a week."
    show Jason happy
    j "{i}Three or four days? Maybe a whole week? Wait, that could be enough time to try it out! Things could change at last!{/i}"
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0008.ogg"
    n "Wipe that stupid grin off of your face. Don’t just stand there! I want you to inventory everything we have in the pantry. And tell your sisters! They can’t go anywhere in this."
    show Jason avoid
    j "Yes Mom."
    show Jason happy
    j "{i}For the first time in a long time I don’t even mind doing inventory. I have my chance.{/i}"


    scene jason_room_d with fade
    show Jason daydream_aroused at jason_normal(mid_left)
    j "Whew."
    j "{i}It took most of the day just to get everything ready. Everyone was angry and they took out most of it on me. Normally I’d just fall into bed and fantasize that things had gone differently.{/i}"
    j "{i}A house where I’m in charge and they all do whatever I say. Well, after today, that’s not going to be a fantasy any more.{/i}"
    j "{i}Behold, the fruits of my labor. A little audio device.{/i}"
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Jason daydream_aroused
    j "{i}It probably doesn’t even work, but I’ve been looking for an opportunity to test it. It’s a combination of things.{/i}"
    j "{i}Kira’s work on brain chemistry, some marketing techniques I picked up from Mom, and Sarah’s manipulative seduction. Even Jane's aggressive sports tactics contributed.{/i}"
    j "{i}I’ve been around all of them for years and I know their work so well I could do it. I’ve done the math, and I mixed everything I learned from their work with something of my own. My music.{/i}"
    j "{i}Playing instruments is my jam, but that’s not all I’ve been working on. I don’t have a degree yet, but I’m basically an audio engineer. I used all my skills to make this: it’s a portable delimiter.{/i}"
    j "{i}It plays music with heavy subliminals - if you can expose someone to it for long enough, you can put them into a trance. And then once they’re under...{/i}"
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show popup_lineup
    j "{i}...you can get them to do whatever you want.{/i}"
    voice "VoiceActing/Day 01/Sarah/D00SarahL0005.ogg"
    s "I am under your command."
    voice "VoiceActing/Day 01/Jane/D00JaneL0007.ogg"
    a "I am under your command."
    voice "VoiceActing/Day 01/Kira/D00KiraL0014.ogg"
    k "I am under your command."
    voice "VoiceActing/Day 01/Noelle/D00NoelleL0009.ogg"
    n "I am under your command."
    hide popup_lineup with dissolve
    show Jason happy_aroused
    j "{i}Well, that’s the theory. I haven’t had a chance to test it yet: I need to run it for a few days straight before the subliminals really work their way into a person's mind.{/i}"
    j "{i}With no one in this family knowing how to stay home and sleep at night I’ve never had the chance. But if we’re going to be snowed in for a few days, this might just be the opportunity of a lifetime.{/i}"
    j "{i}All I have to do is hook up some speakers and put them on the air vents. Getting kicked up to this cold, cramped attic is actually working out for once!{/i}"
    scene bg house 1 with fade
    pause (1)
    scene bg house 2 with dissolve
    pause (1)
    scene bg house 3 with dissolve
    pause (1)
    scene bg house 4 with dissolve
    pause (1)
    scene bg house 5 with dissolve
    pause (1)
    scene bg house 6 with dissolve
    pause (1)
    scene bg house 7 with dissolve
    pause (1)
    scene bg house 8 with dissolve
    pause (1)
    scene bg house 14 with dissolve
    pause (1)
    scene black with fade

    stop music fadeout 1.0

    $ persistent.d0u = True
    show text "END OF DAY ZERO" at truecenter with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    show text "FIVE DAYS REMAIN" at truecenter with dissolve
    $ achievement.grant("Moral_Event_Horizon")
    $ achievement.Sync()
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    jump day1start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
