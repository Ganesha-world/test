label family4:
    $ jane_outfit.CanonOutfit = JaneOutfitEnum.FASHION
    $ noelle_outfit.CanonOutfit = NoelleOutfitEnum.FASHION
    $ sarah_outfit.CanonOutfit = SarahOutfitEnum.FASHION
    $ kira_outfit.CanonOutfit = KiraOutfitEnum.FASHION

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












    play music audio.snowflake_lullaby_piano fadein 1.0
    scene kitchen_d2 with fade

    show Kira frown at kira_normal(far_right)
    show Jason neutral at jason_normal(close_left)
    $ musiccomment = False
    pause(0.25)
    voice "VoiceActing/Day 02/Kira/D02KiraL0001.ogg"
    show Kira at talking_stay
    k "Jason! You slept in - we’re almost done with breakfast."
    show Kira at normal_stay
    j "Sorry, sis, I was up late trying some new music."
    j "{i}In truth, I’m so tired this morning that if wasn’t so excited about the changes I’ve made so far, I don’t know if I would have gotten up at all.{/i}"
    j "{i}Checking them out helps to wake me up though - it’s clear that my plan is working. Everyone is already dressed in clothes which are a lot more relaxed than normal.{/i}"
    show Noelle neutral at noelle_normal(mid_right)
    if noelleshower:
        show Jason avoid
        j "{i}Mom is blushing furiously and trying her best not to look at me. I keep catching her glancing at everyone’s clothes and then back at me when she thinks I’m not looking.{/i}"
    else:
        show Noelle at talking_stay
        voice "VoiceActing/Day 02/Noelle/D02NoelleL0001.ogg"
        n "Jason, you really need to stop playing music at night. You’re bothering your sisters."
        show Noelle at normal_stay
        $ musiccomment = True
    show Kira neutral at kira_normal(far_right)
    if kirapanties:
        show Jason happy
        j "{i}Kira seems way more relaxed than usual. I haven’t seen her this comfortable since she finished her master’s degree. In record time with record grades, of course.{/i}"
    else:
        show Kira frown
        show Kira at talking_stay
        voice "VoiceActing/Day 02/Kira/D02KiraL0002.ogg"
        k "Jason, I need to read some notes for work! The music keeps me up, knock it off."
        show Kira at normal_stay
        $ musiccomment = True
    show Jane neutral at jane_normal(mid)
    if janepanties:
        show Jason happy_aroused
        j "{i}Unlike yesterday, Jane is looking at me without glaring. She’s actually smiling at me. She hasn’t done that in years.{/i}"
    else:
        show Jane frown
        show Jane at talking_stay
        voice "VoiceActing/Day 02/Jane/D02JaneL0001.ogg"
        a "Keeping me up all night isn’t cool, bro. The music is really getting on my nerves"
        show Jane at normal_stay
        $ musiccomment = True
    if musiccomment:
        show Jason avoid
        j "Ah, sorry. It’s really important music for a recital."
    show Sarah neutral at sarah_normal(mid_left)
    j "{i}Sarah looks so bright and happy that I can’t resist teasing her a little bit.{/i}"
    j "Hey Sarah, I’m late. Could you fetch me a plate? I’m feeling a little ruff this morning."
    if Sarah_c.points >= 2:
        show Sarah happy
        show Sarah at talking_stay
        voice "VoiceActing/Day 02/Sarah/D02SarahL0001.ogg"
        s "Um, sure Jason. I guess it’s alright. Here you go."
        show Sarah at normal_stay
    else:
        show Sarah frown
        show Sarah at talking_stay
        voice "VoiceActing/Day 02/Sarah/D02SarahL0002.ogg"
        s "Get it yourself, dork. Your music kept me up all night too."
        show Sarah at normal_stay

    j "{i}I can see from the way they’re dressed that the delimiter’s subliminal messages are working, but not perfectly. I need to be really careful - baby steps.{/i}"
    j "{i}But… if I move too slowly, I won’t get another chance to change their behavior.{/i}"
    j "{i}By the end of today, if they’re not onboard with my plan, they’re probably going to start noticing how much everyone else is changing and cause problems.{/i}"
    j "{i}I do my best to eat quickly; everyone else is almost finished. I want to race through my chores today, so I can get my sisters alone...and then finish up with Mom. I can’t wait.{/i}"
    play music "music/Jane's Theme.mp3" fadeout 1.0 fadein 1.0
    show Jane frown
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0002.ogg"
    a "Hey, uh, Jason…"
    show Jane at normal_stay
    j "Yeah, Jane?"
    show Jane lewd
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0003.ogg"
    a "Would you mind if I, um, uh…"
    j "{i}I’ve never seen my sister so nervous before. It’s like she doesn’t quite believe what she’s saying.{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0004.ogg"
    a "Can I help you with the dishes today?"
    show Jane at normal_stay
    j "What??"
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0005.ogg"
    a "Never mind. It’s stupid."
    show Jane at talking_stay
    show Jason happy_ad
    show Jason at talking_stay
    j "No, I mean...of course you can!"
    show Jason at normal_stay
    j "{i}My sister hasn’t helped me with chores since we were kids. This isn’t even something I told her to do while she was under - she probably would have broken out of the trance and punched me if I had.{/i}"
    show Noelle happy
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0002a.ogg.opus"
    n "Aww, it’s sweet to see you two getting along again. I think we’re all done eating. Jason, don’t forget to put the hand towel in the washer and get a replacement after you’re done this time."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0002b.ogg.opus"
    n "And remember - laundry day today! That means bedsheets, clothes, and everything else; it’s really starting to back up."
    show Noelle at normal_stay
    j "Okay Mom…"

    if noelleshower:
        j "{i}God, I thought after yesterday things would be different...still, at least I’ll have the memory of Mom getting off while watching me jerk off to distract me.{/i}"
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0003.ogg"
    n "The kitchen needs to be wiped down, too. Sweep and mop the floor and clear off the table. We’ll probably need a few other places cleaned up too; come and see me when you’re done."
    show Noelle at normal_stay
    show Jason neutral
    j "Fine."
    j "{i}Damn it. If I spend all day doing chores I won’t have a chance to take things further with anyone. At least Jane is going to help me with the dishes today… wait. That’s an opportunity.{/i}"
    j "I’ll make sure everything gets done."
    show Noelle happy
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0004.ogg"
    n "Thanks sweetie."
    show Noelle at normal_stay
    hide Kira with dissolve
    hide Noelle with dissolve
    hide Sarah with dissolve
    play music audio.deep_breaths_guitar fadein 1.0
    show Jane neutral at jane_normal(mid_right)
    j "{i}I bet Mom and Kira are going to stay in their rooms all day and catch up on work - and Sarah will probably do what she did yesterday, and spend hours desperately trying to get the internet working again.{/i}"
    j "{i}Which leaves me alone with Jane for at least the next little while...{/i}"
    show Jane happy
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0006.ogg"
    a "This is kinda fun!"
    show Jane at normal_stay
    j "It’s one of my daily chores. You’re welcome to help any time you want!"
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0007.ogg"
    a "Yeah, maybe! It’s sort of fun to do something girly once in awhile."
    show Jane at normal_stay
    j "{i}I shoot her a glare, but she doesn’t notice. She looks a bit nervous and uneasy, and I don’t think she even realized she basically just called me girly.{/i}"
    j "It’s not too bad, but it can get kind of boring. I generally listen to music while I’m working."
    j "{i}I casually take the delimiter out of my pocket and put it on the counter. It starts ticking.{/i}"
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Jane neutral
    voice "VoiceActing/Day 02/Jane/D02JaneL0008.ogg"
    a "Hey! I remember this… it’s… it’s..."
    j "It’s that song I wrote you to apologize."
    voice "VoiceActing/Day 02/Jane/D02JaneL0009.ogg"
    a "You played it...played it in my room...yesterday. Made me so...so sleepy..."
    j "Yeah, I played it for you. I was so nervous, it made my heart beat so loudly..."
    voice "VoiceActing/Day 02/Jane/D02JaneL0010.ogg"
    a "Mmmm…."
    j "I bet that you know what it feels like to be nervous. Doesn’t it make your heart race?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0011.ogg"
    a "Heart...race…"
    j "It’s so loud. Thump, thump, thump, thump…."
    show Jane hypno at jane_normal(mid_right)
    show Jane hypno_enter
    $ renpy.pause(random_true_float(1.0, 2.0))
    show Jane hypno
    voice "VoiceActing/Day 02/Jane/D02JaneL0012.ogg"
    a "Thump…"
    j "Yeah, you can really feel it, can’t you? But you don’t need to be nervous. Focus on your heart, keeping a steady rhythm, getting slower, easier, relaxed…"
    voice "VoiceActing/Day 02/Jane/D02JaneL0013.ogg"
    a "Relaxed…"
    j "{i}She still looks so tense. I can tell she’s slipping into the trance, but it’s not easy. It’s a good thing she ended up being the first one I hypnotized; she looks like she’s ready to snap.{/i}"
    j "That’s right. RELAX, Jane. Just listen to your heartbeat…"
    voice "VoiceActing/Day 02/Jane/D02JaneL0014.ogg"
    a "Relax… can’t relax…"
    j "Just close your eyes and listen to the beat. Listen to the song. Isn’t it relaxing? Doesn’t it feel good? Just let it relax you. Just sit down in this chair and relax."
    voice "VoiceActing/Day 02/Jane/D02JaneL0015.ogg"
    a "Relax…"
    j "That’s right. Just relax and listen to the music and the sound of my voice."
    voice "VoiceActing/Day 02/Jane/D02JaneL0016.ogg"
    a "Voice…"
    j "Yeah. Just listen to my voice. You can trust me. Focus on the sound of my voice and the rhythm of the song…"
    voice "VoiceActing/Day 02/Jane/D02JaneL0017.ogg"
    a "Listen… lisssss…"
    j "{i}She finally went under. That wasn’t easy.{/i}"
    j "{i}It’d be nice to get her to help out more with the chores, but I really need to figure out why she’s so nervous. This is such a risky spot to do this.{/i}"
    j "{i}I’d normally tell her to wake up if anyone came in, but she’s so on edge that I think she’ll do that on her own.{/i}"
    play music "music/Jane's Theme.mp3" fadeout 1.0 fadein 1.0
    jump a2A

label a2A:
    menu:
        "Why are you so nervous today?":
            jump a2A1
        "Whatever’s making you nervous, it’s okay.":
            jump a2A2
        "I order you to relax!":
            jump a2A3


label a2Aa:
    menu:
        "Why are you so nervous today?":
            jump a2A1
        "I order you to relax!":
            jump a2A3


label a2A1:
    j "Why are you so nervous today?"
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0018.ogg"
    a "Not nervous… afraid…"
    j "{i}My sister, the amazon queen - afraid?{/i}"
    j "What are you afraid of, sis?"
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0019.ogg"
    a "...."
    j "Jane? What are you afraid of? You know you can trust me. We’re cool."
    voice "VoiceActing/Day 02/Jane/D02JaneL0020.ogg"
    a "Afraid...of...you."
    j "{i}That doesn’t make any sense. She can’t be afraid of me; she used to beat me up every other day!{/i}"
    j "{i}When she first started learning how to box, she almost broke my jaw. Mom, of course, said it was my fault...{/i}"
    j "I don’t understand. Why are you afraid of me?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0021.ogg"
    a "Felt...bad…"
    j "You felt bad and that made you afraid?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0022.ogg"
    a "Felt...bad...wanted to...apologize."
    j "That’s okay, sis. You don’t need to apologize."
    j "{i}I’m not really sure what she wanted to apologize for, but I can tell it’s freaking her out.{/i}"
    show Jane hypno
    voice "VoiceActing/Day 02/Jane/D02JaneL0023.ogg"
    a "Wanted to...make up. Wanted to...do chores."
    j "That’s what made you afraid? What’s so scary about chores?"
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0024.ogg"
    a "...so... girly…"
    j "Why is being girly scary?"
    j "{i}Ignoring the fact that she just called me girly again...didn’t she say she yesterday that she wished she was MORE girly?{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0025.ogg"
    a "Because… because I like it…"
    j "That’s interesting."
    jump a2B


label a2A2:
    j "Whatever’s making you nervous it’s okay. Nobody is going to judge you. You can relax."
    j "{i}She doesn’t say anything but sighs and some of the tension seems to flow out of her. She seems to rest a bit. She’s visibly relaxed.{/i}"
    $ Jane_c.add_points(1)
    jump a2Aa


label a2A3:
    j "I order you to relax!"
    show Jane hypno_frown
    "{i}Jane clenches her fists.{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0026.ogg"
    a "Fuck… you… can’t order me…"
    show Jason avoid
    j "{i}Oh, shit. If she wakes from the trance like this she’ll slug me. Her punches really hurt!{/i}"
    j "Uh… please relax?"
    j "{i}She seems to relax a bit but she’s definitely not any less nervous than she was before.{/i}"
    $ Jane_c.sub_points(1)
    jump a2B


label a2B:
    menu:
        "Why did you help me today?":
            jump a2B1
        "You look like a sexy housewife!":
            jump a2B2
        "You look really feminine doing that.":
            jump a2B3


label a2B1:
    j "Why did you help me today?"
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0027.ogg"
    a "Felt… guilty…"
    j "About the fact that we haven’t gotten along lately? It’s okay, sis - like I said yesterday, we’re cool."
    voice "VoiceActing/Day 02/Jane/D02JaneL0028.ogg"
    a "No...about...chores…"
    j "What about the chores?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0029.ogg"
    a "You do...all the chores…"
    j "Seriously? I’ve been doing them since we were kids."
    voice "VoiceActing/Day 02/Jane/D02JaneL0030.ogg"
    a "Used to do them...with you… I… miss that…"
    j "{i}I wish I’d known a few years ago that Jane missed doing chores with me! I could have saved so many hours over the years...as it is, my calluses have calluses.{/i}"
    j "If you wanted to do them with me why didn’t you?"
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0031.ogg"
    a "Chores are...girly…"
    j "So? You’re a girl."
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0032.ogg"
    a "Don’t want to be...girly…"
    j "Why not?"
    show Jane hypno
    voice "VoiceActing/Day 02/Jane/D02JaneL0033.ogg"
    a "Gotta...be...strong…"
    j "You know you can be girly and still be strong."
    voice "VoiceActing/Day 02/Jane/D02JaneL0034.ogg"
    a "Don’t...want to be...submissive."
    show Jason happy
    j "Ah."
    j "{i}So in her mind, feminine equals submissive. Interesting.{/i}"
    $ Jane_c.add_points(1)
    jump a2C


label a2B2:
    j "You look like a sexy housewife!"
    show Jane shocked
    "{i}Jane starts to shake; it’s clear that she’s struggling to keep her emotions in check.{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0035.ogg"
    a "You… jerk…!"
    show Jason avoid
    j "{i}Uh oh.{/i}"
    j "It’s a compliment. You look really hot."
    voice "VoiceActing/Day 02/Jane/D02JaneL0036.ogg"
    a "Grrr…."
    j "{i}Oh, shit.{/i}"
    j "I just wasn’t expecting it, because you’re such a tomboy. Some day, you’ll make a really sexy wife for, uh, for some guy…that’s all I meant!"
    if Jane_c.points >=3:
        jump a2janesurvive
    else:
        jump a2janebadend


label a2janebadend:
    show Jane angry
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0037.ogg"
    a "I should’ve known you couldn’t be cool, you jerk! What in the hell did you do to me?"
    show Jane at normal_stay
    j "I didn’t do anything! I swear! Just listen to the music...the heartbeat...thump, thump, thump. Let’s be cool..."
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0038.ogg"
    a "That’s it! That fucking music! You did something to me yesterday, too! I remember now!"
    play sound "music/Smashing.mp3"
    j "{i}In an instant the delimiter is in her hands and she smashes it against the counter. It only takes a second for all my hopes and dreams to go with it.{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0039.ogg"
    a "You absolute pervert! God you’re sick...you’re trying to twist my brain around! MOOOM!"
    scene black with fade
    pause 1
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show badend jason_sad
    $ achievement.grant("NEW_ACHIEVEMENT_1_5")
    $ achievement.Sync()
    pause
    return



label a2janesurvive:
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0040.ogg"
    a "Not… cool…"
    j "It’s a compliment!"
    voice "VoiceActing/Day 02/Jane/D02JaneL0041.ogg"
    a "Shouldn’t... say that stuff… to your sister…"
    j "Sorry. It won’t happen again."
    voice "VoiceActing/Day 02/Jane/D02JaneL0042.ogg"
    a "Better… not…"
    j "{i}Crap! That was close. I thought she was going to wake up for a minute there! I’ve got to watch what I say - she’s still really touchy about me hitting on her.{/i}"
    jump a2B


label a2B3:
    j "You look really feminine doing that."
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0043.ogg"
    a "Thanks…"
    show Jason shocked
    j "{i}Wait, what? She actually liked that?{/i}"
    j "You like being told you’re feminine?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0044.ogg"
    a "...Course… still... a girl…"
    j "{i}Huh. Maybe Jane just wanted to be a little more girly all along. I wonder if there’s something I could do with that?{/i}"
    show Jason neutral
    $ Jane_c.add_points(2)
    jump a2C


label a2C:
    j "Maybe you should help out with the chores more often."
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0045.ogg"
    a "Might… enjoy that…"
    show Jason happy_ad
    j "Wait, seriously?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0046.ogg"
    a "Mmmm…"
    j "You want to help me with the chores?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0047.ogg"
    a "Feel...bad…want to...help..."
    j "And it doesn’t help that it makes you feel a bit more girly, does it?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0048.ogg"
    a "Mmmm…."
    j "If I asked you to, would you do all of my chores?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0049.ogg"
    a "Yes…"
    j "{i}Well damn. I sort of want to take advantage of that...my back would thank me, that’s for sure. But if I do, someone might notice she’s doing something she wouldn’t normally do.{/i}"
    j "{i}On the other hand, if Jane is doing all my chores, I’ll have more time to work on Mom and my sisters…{/i}"
    jump a2D


label a2D:
    menu:
        "She should do them all!":
            jump a2D1
        "Split the work.":
            jump a2D2


label a2D1:
    $ janechores = True
    show Jason happy_ad
    j "Yeah sis, you should go ahead and do all of them from now on. It’ll make you feel good to be a little more feminine, right?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0050.ogg"
    a "Sure… do all the chores… feel good…"
    j "{i}Wow. That was easier than I thought! She feels good, and I feel great...looks like it’s win-win! I’m sure I made the right decision here.{/i}"
    jump a2E


label a2D2:
    show Jason neutral
    j "No… we’re twins. It’s cool if you wanna help me but we should split things equally, right? Both halves the same, just like it used to be."
    show Jane hypno_smile
    j "{i}Even through the trance, I can see her smile. It feels good - I know I made the right decision here.{/i}"
    j "{i}As much as I’d love to have someone do all my chores, that wouldn’t really be fair... plus I’m sure the rest of the family would be pretty suspicious.{/i}"
    $ Jane_c.add_points(1)
    jump a2E


label a2E:
    j "{i}It’s clear she likes being feminine. I wonder if I could push this a little further?{/i}"
    j "Jane, you like acting girly, right?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0051.ogg"
    a "Yeah…"
    j "Well there’s one thing still bothering me. You’re doing girly stuff but you don’t look very feminine. It doesn’t match up."
    voice "VoiceActing/Day 02/Jane/D02JaneL0052.ogg"
    a "I’m… feminine…"
    if janepanties:
        voice "VoiceActing/Day 02/Jane/D02JaneL0053.ogg"
        a "Wear… girly underwear…"
        j "Yeah, but that’s hidden. You don’t look like a girl on the outside."
        show Jane hypno_frown
        "{i}Jane doesn’t say anything but seems disturbed.{/i}"
    voice "VoiceActing/Day 02/Jane/D02JaneL0054.ogg"
    a "Don’t know how… to dress girly…"
    j "You don’t know how? At all?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0055.ogg"
    a "Just… ideas… never tried… wouldn’t know if it was right..."
    j "Why don’t you show me then? I could tell you."
    voice "VoiceActing/Day 02/Jane/D02JaneL0056.ogg"
    a "But...but…"
    "{i}She’s squirming in her seat.{/i}"
    j "What is it?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0057.ogg"
    a "You’ll get...pervy…"
    j "If you want to look feminine you need a guy to check you out and tell you if you look right. I’m the only guy here. Besides, you know you can stop me if I do anything you don’t like."
    show Jane hypno
    voice "VoiceActing/Day 02/Jane/D02JaneL0058.ogg"
    a "..."
    if Jane_c.points <= 4:
        jump fashionfail
    else:
        jump fashionyes


label fashionfail:
    show Jane hypno_frown
    voice "VoiceActing/Day 02/Jane/D02JaneL0059.ogg"
    a "No… you’re my brother… don’t want to like you looking at me…"
    show Jason avoid
    j "{i}Dammit. I guess she’s just not far enough along.{/i}"
    jump a2wakeup1


label fashionyes:
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0060.ogg"
    a "Okay… just…"
    j "Be cool?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0061.ogg"
    a "Yeah…"
    j "Of course."
    show Jason happy
    j "{i}Thank you God and female insecurity.{/i}"
    j "Okay Jane, I’m going to count to five, and then you’re going to wake up."
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0062.ogg"
    a "Mmm…"
    j "Five… as soon as you wake up, you’ll forget you were in a trance, but you’ll remember suggesting that I help you pick a new outfit."
    voice "VoiceActing/Day 02/Jane/D02JaneL0063.ogg"
    a "New...outfit…"
    j "Four. It was your idea to look more feminine."
    voice "VoiceActing/Day 02/Jane/D02JaneL0064.ogg"
    a "More...feminine...."
    j "Three. Choose a girly outfit, and show it off to me."
    voice "VoiceActing/Day 02/Jane/D02JaneL0065.ogg"
    a "Show...off…"
    j "Two. Just come to my room and show off what you’re wearing. We’ll find one that looks girly."
    voice "VoiceActing/Day 02/Jane/D02JaneL0066.ogg"
    a "Okay…"
    j "The more feminine you feel, the more turned on you’ll be. The more turned on you are, the more girly you want to be. Do you understand?"
    show Jane hypno_smile
    voice "VoiceActing/Day 02/Jane/D02JaneL0067.ogg"
    a "Yes…"
    j "{i}Holy moly, she’s blushing even through the trance. Well, here goes everything.{/i}"
    j "One."
    show Jane happy
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0068.ogg"
    a "-yawn- Ah, sorry Jason. Your music must be pretty boring, it makes me super sleepy. So yeah… you’re cool with helping me out with the outfit thing?"
    show Jane at normal_stay
    show Jason at talking_stay
    j "Yeah, totally! I mean, whatever. If I have to. I’ll just wait in my room, come on up whenever you’re ready."
    show Jason at normal_stay
    show Jane at talking_stay
    voice "VoiceActing/Day 02/Jane/D02JaneL0069.ogg"
    a "See you in a few, bro."
    show Jane at normal_stay
    $ persistent.janefashionshow = True
    jump a2jason1


label a2wakeup1:
    show Jason avoid
    j "{i}Damn. I felt like I could have gotten something else out of her. Oh well…{/i}"
    show Jason neutral
    j "You’ll wake up on the count of five. 5… 4… 3.. 2… 1… Wake!"
    jump family5


label a2jason1:
    play music audio.habanera fadein 1.0
    scene jason_room_d with fade
    show Jason happy at jason_normal(mid_left)
    j "{i}It’s only been few minutes and I already feel like I’m gonna go crazy. What in the hell is she gonna wear? The tension is driving me up the wall.{/i}"
    "{i}KNOCK KNOCK{/i}"
    j "C-come in!"
    scene cgbg with dissolve
    show jshow1
    voice "VoiceActing/Day 02/Jane/D02JaneL0070.ogg"
    a "Hey… so, what do you think of this? It’s just my tennis outfit but I changed it a little... "
    $ achievement.grant("NEW_ACHIEVEMENT_1_12")
    $ achievement.Sync()
    j "Holy crap sis, you really work out. Those abs are amazing!"
    hide jshow1
    show jshow3
    voice "VoiceActing/Day 02/Jane/D02JaneL0071.ogg"
    a "I’m too buff for this, aren’t I? I look like a guy…"
    j "No way! Girls can work out and still be girly. You make it look really good!"
    hide jshow3
    show jshow2
    voice "VoiceActing/Day 02/Jane/D02JaneL0072.ogg"
    a "Thanks."
    j "But... it doesn’t work."
    voice "VoiceActing/Day 02/Jane/D02JaneL0073.ogg"
    a "Why not? Is… is it me? Am I too...masculine? Ugh, I knew this was a bad idea..."
    hide jshow2
    show jshow4
    j "No way! You look great, sis. It’s the outfit - it’s more feminine than the normal stuff you wear because it’s a female sports outfit… but that’s the problem. It’s just a sports outfit."
    hide jshow4
    show jshow5
    voice "VoiceActing/Day 02/Jane/D02JaneL0074.ogg"
    a "Yeah… it’s just a tennis outfit. I guess it isn’t very girly. I could do better."
    j "Yeah, show me the next one!"
    "{i}A few minutes pass…{/i}"
    hide jshow5
    show jshow6
    voice "VoiceActing/Day 02/Jane/D02JaneL0075.ogg"
    a "Okay, I’ve got another one."
    j "Whoa… I didn’t know you owned any skirts like that."
    hide jshow6
    show jshow7
    voice "VoiceActing/Day 02/Jane/D02JaneL0076.ogg"
    a "You’d know, perv. I catch you going through my laundry all the time."
    j "Uh…"
    voice "VoiceActing/Day 02/Jane/D02JaneL0077.ogg"
    a "-giggle- But yeah, I don’t own any. I borrowed this outfit from Sarah."
    j "I can tell, the skirt is really short. It looks really good. It’s really sexy."
    hide jshow7
    show jshow8
    voice "VoiceActing/Day 02/Jane/D02JaneL0078.ogg"
    a "You’re sure? My thighs are so huge… I mean, most girls don’t look like this. Aren’t girls supposed to have thigh gaps or whatever?"
    j "Most girls would kill for the legs you’ve got. You can tell you run all the time. You definitely look like a girl. Just more of a girl than they are."
    hide jshow8
    show jshow9
    voice "VoiceActing/Day 02/Jane/D02JaneL0079.ogg"
    a "Really?"
    j "Especially your ass. It’s perfect. It’s an ass just about every girl would kill to have. It’s big but it’s all muscle. I bet every girl you meet is jealous."
    hide jshow9
    show jshow10
    j "Ah, hell. I shouldn’t have said that. Now she’s going to explode, and…-"
    hide jshow10
    show jshow11
    voice "VoiceActing/Day 02/Jane/D02JaneL0080.ogg"
    a "That’s naughty, Jason. Don’t talk about your sister’s butt."
    j "{i}Oh god...she’s smiling. That’s a naughty smile! My twin sister is giving me a naughty smile! It’s really happening!{/i}"
    j "There’s… there’s just one problem with it. It’s not your outfit. You borrowed it. Don’t you have anything girly of your own?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0081.ogg"
    a "... Yeah. There’s one thing... I feel stupid putting it on, but I’ll let you look. But if you tell anyone I’ll beat the crap out of you, understand?"
    j "{i}For a second there I forgot she used to beat me up almost every day. Whatever she’s wearing she’s still my sister.{/i}"
    "{i}A few minutes later...{/i}"
    hide jshow11
    show jshow12
    voice "VoiceActing/Day 02/Jane/D02JaneL0082.ogg"
    a "I’ve had this for a while but I’ve never worn it. It feels kinda weird. What do you think?"
    j "Is- is that a prom dress?"
    hide jshow12
    show jshow13
    voice "VoiceActing/Day 02/Jane/D02JaneL0083.ogg"
    a "Yeah. I bought it but I was too nervous to wear it. The guy that asked me out didn’t even show up, so I feel kinda dumb. I mean, do I really look like the sort of person that could wear something like this?"
    j "Yes."
    j "{i}She’s blushing. I’m going to push my luck.{/i}"
    j "Without a doubt, you’re the sexiest and most feminine I’ve ever seen you in your life. You look amazing. You look way too classy for a boring high school dance. You’re...you’re a lady."
    hide jshow13
    show jshow14
    "{i}She's blushing hard.{/i}"
    j "You’re wearing makeup?"
    voice "VoiceActing/Day 02/Jane/D02JaneL0084.ogg"
    a "I-I borrowed it from Sarah…"
    j "It looks sexy as fuck. The dress looks great, but with the makeup… you’re the perfect girl. So beautiful and feminine - you’re such a girl, you really make me feel like a man."
    hide jshow14
    show jshow15
    voice "VoiceActing/Day 02/Jane/D02JaneL0085.ogg"
    a "Ffff-oh god. Th-thanks Jason. I’ve gotta go, um, think about things."
    $ janefashionshow = True
    scene jason_room_d with dissolve
    show Jason neutral at jason_normal(mid_left)
    show Jane lewd at jane_normal(mid_right)
    j "Wait!"
    hide Jane with easeoutright
    j "{i}Ah, dammit. She’s already gone. Gone to… oh wow. Is she gonna do what I think she is?{/i}"
    j "{i}I want to go check on her, but...yeah, even as far as I pushed her today, I don’t think she’d let me watch her do… what I think she’s doing. Wow.{/i}"
    j "{i}I’ve got to focus on someone else for a bit or I’m gonna explode.{/i}"
    jump family5





label family5:
    scene livingroom_d1 with fade

    show Jason neutral at jason_normal(mid)
    voice "VoiceActing/Day 02/Sarah/D02SarahL0003.ogg"
    s "What the hell! Where’s my makeup and who went through my closet! Jasooon! You better not be stealing my underwear again!"
    j "{i}Uh oh. For once I legitimately didn’t do anything wrong, but it’s not like anyone’s gonna believe that and Jane is… busy. Sarah’s gonna go straight for mom, my room is out… Kira!{/i}"
    j "{i}I’ve got to try and work on her anyway. Hopefully things will calm down by then.{/i}"





    play music audio.deep_breaths_piano fadein 1.0
    scene kira_room_d2d with fade
    show Jason neutral at jason_normal(mid_left)
    show Kira neutral at kira_normal(far_right)

    show Kira at talking_stay
    voice "VoiceActing/Day 02/Kira/D02KiraL0003.ogg"
    k "What are you doing in here, Jason?"
    show Kira at normal_stay
    j "I just need a place to hide for a few minutes. Jane borrowed some of Sarah’s stuff and she thinks I did it. I’ll be fine once they talk it out."
    show Kira frown
    show Kira at talking_stay
    voice "VoiceActing/Day 02/Kira/D02KiraL0004.ogg"
    k "Not gonna happen. I’m about to go take a shower and there’s no way I’m leaving you alone in my room. Just go out there and tell her it was Jane! You’ve got to stop being everyone’s punching bag!"
    show Kira at normal_stay
    j "{i}Wait… about to go take a shower? I can’t miss this chance.{/i}"
    if noelleshower:
        j "{i}Oh man, maybe she could let me watch her shower like mom did!{/i}"
    j "Okay, fine, I’ll get out in a second. Just listen to this first."
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Kira neutral
    voice "VoiceActing/Day 02/Kira/D02KiraL0005.ogg"
    k "Wait… that’s… that song…"
    j "Yeah. I made a few improvements last night."
    voice "VoiceActing/Day 02/Kira/D02KiraL0006.ogg"
    k "That’s pretty… nice… finally working hard…"
    j "That’s right, I am. But you don’t have to work right now, do you?"
    show Kira hypno at kira_normal(far_right)
    show Kira hypno_enter
    $ renpy.pause(random_true_float(1.0, 2.0))
    show Kira hypno
    voice "VoiceActing/Day 02/Kira/D02KiraL0007.ogg"
    k "No…"
    j "That’s right. You don’t have to work today. So just lay back on the bed and relax for a bit. Just listen to the beat of the song. Remember that? It just cycles through over and over and over again."
    show Kira hypno_smile
    voice "VoiceActing/Day 02/Kira/D02KiraL0008.ogg"
    k "Mmmm…"
    j "Just listen to the rhythm and the sound of my voice. Nothing else really matters right now, does it?"
    show Kira hypno
    voice "VoiceActing/Day 02/Kira/D02KiraL0009.ogg"
    k "No…"
    j "Good. Just listen. There’s nothing else in the room, nothing else around. Just the song and the sound of my voice. It makes you sleepy, doesn’t it? You just want to relax and fall asleep."
    voice "VoiceActing/Day 02/Kira/D02KiraL0010.ogg"
    k "Fall…"
    j "On the count of one you’ll fall into a deep slumber and the only thing you can hear will be the sound of my voice. 5...4...3...2...1… Sleep."
    voice "VoiceActing/Day 02/Kira/D02KiraL0011.ogg"
    k "..."
    j "{i}My sexy older sister is in a trance just as she was about to have a shower. I’ve got to be able to do something with that. Maybe I can put her a little deeper and try something.{/i}"
    play music "music/Kira's Theme alt.mp3" fadeout 1.0 fadein 1.0
    jump k2A

label k2A:
    menu:
        "Isn’t it great to relax a little?":
            jump k2A1
        "You seem happier today.":
            jump k2A2


label k2A1:
    j "Isn’t it great to relax a little, just this once? The blizzard is like a vacation!"
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0012.ogg"
    k "No… wasting time…"
    j "Kira, you can’t just work your entire life. What kind of person accomplished anything by doing nothing but work?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0013.ogg"
    k "Johann Glauber… George Davis… Waldo Semon… Francis Bacon..."
    j "Okay, okay, nevermind."
    j "{i}I have no idea who any of those people even are. This isn’t working.{/i}"
    $ Kira_c.sub_points(1)
    jump k2B


label k2A2:
    j "You seem happier today."
    show Kira hypno_smile
    voice "VoiceActing/Day 02/Kira/D02KiraL0014.ogg"
    k "Bored, but… yes."
    j "You’re bored?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0015.ogg"
    k "No projects to do… I feel bad but… resting is nice…"
    j "{i}If she’s bored maybe I can do something with that.{/i}"
    $ Kira_c.add_points(1)
    jump k2B


label k2B:
    menu:
        "I don’t remember you having any boyfriends.":
            jump k2B1
        "How often do you even get off?":
            jump k2B2


label k2B1:
    j "You know I don’t remember you ever having a boyfriend. Don’t you ever take time for relationships?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0016.ogg"
    k "Can’t afford to… takes too much time…"
    j "So when was the last time you got laid?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0017.ogg"
    k "... Five years…ago..."
    j "That was your first year of college, right? You haven’t done anything in all that time? Don’t you want to?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0018.ogg"
    k "... Yes… but no time…"
    j "Wow! You must spend a lot of time...with yourself...alone…"
    voice "VoiceActing/Day 02/Kira/D02KiraL0019.ogg"
    k "No...time…"
    j "Wait, you mean you haven’t...in five years??"
    voice "VoiceActing/Day 02/Kira/D02KiraL0020.ogg"
    k "Too...busy…"
    j "You haven’t even touched yourself in five years?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0021.ogg"
    k "Want to...but... no time…"
    j "{i}I sometimes struggle to get through a full day. Five years! I bet that my subliminal messages have particularly affected Kira...{/i}"
    j "You know that’s not healthy, right? You need to have some time to yourself. Time for relationships and sex and stuff like that. You could crash if you don’t, and then you won’t get ANY work done."
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0022.ogg"
    k "Yes… do need some time… but... no one wants me..."
    j "{i}I knew it! Of course she has desires, just like everyone else. Now I just have to convince her that I’m someone she can share them with...{/i}"
    $ Kira_c.add_points(1)
    jump k2C


label k2B2:
    j "How often do you even get off?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0023.ogg"
    k "Shouldn’t be… asking…"
    j "I mean, it can’t be very often, can it? You’re a workaholic."
    voice "VoiceActing/Day 02/Kira/D02KiraL0024.ogg"
    k "Don’t… ask… more…"
    j "{i}Damn, she’s gone silent. I shouldn’t have been so direct - it makes her clam up.{/i}"
    jump k2C


label k2C:
    menu:
        "Do you even want to be wanted?":
            jump k2C1
        "Flash me. It’d be hot.":
            jump k2C2
        "You should do what you want.":
            jump k2C3


label k2Ca:
    menu:
        "Flash me. It’d be hot.":
            jump k2C2
        "You should do what you want.":
            jump k2C3


label k2C1:
    j "Do you even want to be wanted?"
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0025.ogg"
    k "Yes… a lot… but no one wants…"
    j "That’s not true… I want you."
    voice "VoiceActing/Day 02/Kira/D02KiraL0026.ogg"
    k "No…"
    j "I swear."
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0027.ogg"
    k "But...you’re my...brother…"
    j "So? A hot girl is a hot girl, and you’re a super hot girl."
    show Kira hypno
    voice "VoiceActing/Day 02/Kira/D02KiraL0028.ogg"
    k "You’re just...going through...phase…"
    j "Yeah, if that were true my life would be a lot easier."
    j "Kira you really do turn me on. I…"
    j "{i}I take a deep breath. This could seriously backfire...{/i}"
    j "I jerk off thinking about you all the time. I can’t help it. I want you every time I look at you. Being in this house with you and never able to touch you is driving me insane."
    show Kira hypno_smile
    voice "VoiceActing/Day 02/Kira/D02KiraL0029.ogg"
    k "I really… do that to you…? Not… lying?"
    j "Really."
    "{i}She smiles.{/i}"
    voice "VoiceActing/Day 02/Kira/D02KiraL0030.ogg"
    k "Like… that…"
    jump k2Ca


label k2C2:
    show Jason happy_ad
    j "If you really want to get off you should flash me. I’d totally get off to that. I’d love looking at your ass. And your tits, too!"
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0031.ogg"
    k "Not… object…"
    j "Don’t you want to be one though, deep down? Just a thing people get off to? You wouldn’t have to worry anymore, wouldn’t have to think. You’d just be making me feel good for a while."
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0032.ogg"
    k "Eugh… no… don’t want to be wanted like that… don’t want to be…"
    show Jason avoid
    j "{i}Crap, she’s shaking off the trance. I don’t think I can salvage this one. I better wake her up before she wakes herself up.{/i}"
    jump k2wakeup1


label k2C3:
    show Jason neutral
    j "You should do what you want to do. You already know how I feel about you, right? Most brothers don’t feel like this about their sisters. You made that happen."
    j "{i}Well, I guess it was a group effort but she deserves as much credit as anyone.{/i}"
    j "You’ve got the power to turn me on any time you want. If you want to use that power I couldn’t stop you."
    voice "VoiceActing/Day 02/Kira/D02KiraL0033.ogg"
    k "You… want…"
    j "I want you to do what you want. You need to get off. You want to feel sexy and turn someone on. You haven’t gotten off in a long time, right? If you decide to use me to do that I’m helpless."
    j "I’d get turned on. I’d have to jerk off thinking about you; I wouldn’t have a choice."
    if Kira_c.points >= 3:
        jump k2yes
    else:
        jump k2no


label k2no:
    show Kira hypno_frown
    voice "VoiceActing/Day 02/Kira/D02KiraL0034.ogg"
    k "No… just want to work… shower… don’t want to get off…"
    j "{i}Damn, thought I had her. I don’t think I can get any further than this today.{/i}"
    jump k2wakeup1



label k2yes:
    show Kira hypno_smile
    voice "VoiceActing/Day 02/Kira/D02KiraL0035.ogg"
    k "Maybe… want… maybe… flash you… would like to...turn someone on…"
    j "Sure. Maybe you’ll go shower and I’ll be waiting in the living room next to the hallway."
    voice "VoiceActing/Day 02/Kira/D02KiraL0036.ogg"
    k "Towel… might slip… might see..."
    j "That’s right. It’s all your decision. Once you wake up you’ll forget that any of this happened. When you see me you’ll just do what you want to deep down."
    voice "VoiceActing/Day 02/Kira/D02KiraL0037.ogg"
    k "Naughty…"
    j "Alright. When I leave the room you’ll wake up and go right back to getting ready for a shower. You’ll wake up after I count down from five."
    j "Five. You want to tease me."
    voice "VoiceActing/Day 02/Kira/D02KiraL0038.ogg"
    k "Tease… yes…"
    j "Four. Teasing me makes you feel good. The more of it you do, the more you want to do."
    voice "VoiceActing/Day 02/Kira/D02KiraL0039.ogg"
    k "Want… more…"
    j "Three… two… one."
    show Kira neutral
    show Kira at talking_stay
    voice "VoiceActing/Day 02/Kira/D02KiraL0040.ogg"
    k "Oh… sorry, I zoned out. Anyway, I already told you this isn’t your hiding spot. I heard your song, now get out. I just had an… idea."
    show Kira at normal_stay
    j "Oh? Anything interesting?"
    show Kira lewd
    voice "VoiceActing/Day 02/Kira/D02KiraL0041.ogg"
    k "Hmm. You’ll see."
    scene black with fade
    j "{i}I quietly slip out of the room and immediately hear her moving inside.{/i}"
    j "{i}The living room seems to be empty for the moment. Now all I have to do is wait.{/i}"
    jump k2D


label k2D:
    play music audio.habanera fadein 1.0
    scene livingroom_d1 with fade
    show Jason neutral at jason_normal(close_left)
    j "{i}I can hear the sound of argument inside of Jane’s room as I head out to the living room… good.{/i}"
    j "{i}I don’t want Sarah stopping anything from happening. Mom’s here, but she’s watching some old movie - 'The Graduate'. Sounds boring.{/i}"
    j "{i}Kira leaves her room just after me, and I can hear the shower running a few seconds later.{/i}"
    show Noelle happy at noelle_normal(mid_right)
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0005.ogg"
    n "Hi Jason."
    show Noelle at normal_stay
    j "Hi mom."
    j "{i}I stand next to the entrance to the living room so that I can see the hallway out of the corner of my eye. It lets me look right at Kira’s door.{/i}"
    play sound "music/344360__amholma__door-open-close.wav"
    "{i}Kira leaves the bathroom in a towel.{/i}"
    scene cgbg with dissolve
    show kshow1
    voice "VoiceActing/Day 02/Kira/D02KiraL0042.ogg"
    k "Jason? What are you doing there?"
    j "{i}She’s whispering; I don’t think Mom can hear us. I whisper back.{/i}"
    j "Nothing..."
    hide kshow1
    show kshow2
    voice "VoiceActing/Day 02/Kira/D02KiraL0043.ogg"
    k "Come on, Jason? Didn’t you get in enough trouble peeping on Jane? Mom is gonna kick you out of the house."
    j "I’m not peeking..."
    hide kshow2
    show kshow3
    voice "VoiceActing/Day 02/Kira/D02KiraL0044.ogg"
    k "Look at your pants!"
    j "{i}As if I could be limp at a time like this. She doesn’t sound angry though, she sounds...sort of playful. More playful than I can ever remember my older sister sounding. I’m not sure that’s a good thing...{/i}"
    j "You’re my sister. I know I shouldn’t look but…"
    hide kshow3
    show kshow4
    voice "VoiceActing/Day 02/Kira/D02KiraL0045.ogg"
    k "Oops..."
    $ achievement.grant("NEW_ACHIEVEMENT_1_14")
    $ achievement.Sync()
    j "{i}I don’t have to fake the next thing I say.{/i}"
    j "'Ow!', {i}I say, trying to minimize my movement as I try not to grab my crotch. There’s always a point where you think you’re fully erect and it turns out you were wrong.{/i}"
    hide kshow4
    show kshow5
    voice "VoiceActing/Day 02/Kira/D02KiraL0046.ogg"
    k "Are you… that hard? For me?"
    j "I can’t help it! This really hurts!"
    hide kshow5
    show kshow6
    voice "VoiceActing/Day 02/Kira/D02KiraL0047.ogg"
    k "Oh? It does, does it? Think it’d hurt as much if I yelled for mom right now?"
    j "{i}Okay, bad. She isn’t in a trance right now. I didn’t exactly tell her to keep this a secret or anything.{/i}"
    j "I can’t help it… it wasn’t supposed to be like this."
    hide kshow6
    show kshow7
    voice "VoiceActing/Day 02/Kira/D02KiraL0048.ogg"
    k "Oh? So what was it supposed to be like? I could call mom at any second and get you thrown out of the house."
    j "{i}I’ve created a monster. Maybe unleashing the desires of someone whose been completely pent up for the past five years was a bad idea.{/i}"
    j "Please don’t."
    hide kshow7
    show kshow8
    voice "VoiceActing/Day 02/Kira/D02KiraL0049.ogg"
    k "Oops. Looks like I accidentally dropped my towel."
    j "Oh god."
    hide kshow8
    show kshow9
    voice "VoiceActing/Day 02/Kira/D02KiraL0050.ogg"
    k "You like my ass, Jason? I know you’re thinking about it all the time."
    j "{i}This is all wrong. I did this to get off, sure, but I’m supposed to be the one in charge for once. This is worse than Sarah flirting with me to do her homework.{/i}"
    j "{i}But I can’t stop staring at her ass.{/i}"
    j "I… do."
    voice "VoiceActing/Day 02/Kira/D02KiraL0051.ogg"
    k "Loser. I should tell mom right now that you’re standing here staring at my ass. You ripped my towel right off and started to grab me."
    j "No!"
    voice "VoiceActing/Day 02/Kira/D02KiraL0052.ogg"
    k "Haha - look how hard you are. Those jeans look like they’re about to rip open. You really get off to your own sister’s body?"
    j "...Yes."
    voice "VoiceActing/Day 02/Kira/D02KiraL0053.ogg"
    k "Fine. If you like my ass so much, take it out and show me. Show me your dick or I’ll yell and tell her you pulled my towel off."
    j "W-what?"
    voice "VoiceActing/Day 02/Kira/D02KiraL0054.ogg"
    k "Take. Out. Your. Dick. Look at my ass… at my tits… come on Jason, you little liar. You really get off to your own sister’s body? Take it out but don’t you dare touch it. Let me see."
    j "Mom could see what we’re doing!"
    voice "VoiceActing/Day 02/Kira/D02KiraL0055.ogg"
    k "Better do it quick then…"
    j "{i}I don’t want to do it. I really, truly, don’t want to do it. Not if she’s TELLING me to do it. But she’s standing right there, looking at me with that face, completely nude.{/i}"
    j "{i}Before I realize it my entire body is burning up and I’m already unzipped.{/i}"
    j "Dammit Kira! Here."
    hide kshow9
    show kshow10
    voice "VoiceActing/Day 02/Kira/D02KiraL0056.ogg"
    k "Oh my god. Haha. You little perv. You actually did it. It’s so cute. Bet you want to touch it, don’t you?"
    j "{i}I desperately want to look back to see if mom heard, but I can’t tear my eyes away.{/i}"
    j "Dammit... Kira… "
    voice "VoiceActing/Day 02/Kira/D02KiraL0057.ogg"
    k "Mmmm. You actually did it. You actually did it!"
    j "I feel humiliated but I can’t tear my eyes away."
    hide kshow10
    show kshow11
    voice "VoiceActing/Day 02/Kira/D02KiraL0058.ogg"
    k "Oh yes… you got hard for me… oh yes… you get off to ME! Ohyesohyesohyes!"
    hide kshow11
    show kshow8
    voice "VoiceActing/Day 02/Kira/D02KiraL0059.ogg"
    k "Whew. I can’t believe what you made me do. You’re such a pervert. Don’t worry - we’re gonna play again. Soon. See you later Jason."
    $ persistent.kirashower = True
    scene livingroom_d1 with fade
    show Jason avoid_aroused at jason_normal(close_left)
    show Noelle neutral at noelle_normal(mid_right)
    j "{i}Never again. I don’t just want to get off, if I’m still just doing everything my sisters tell me to do there’s no point to any of this.{/i}"
    j "{i}She was so pent up I don’t know if it’s possible to control her but I’ve got to do something about this tomorrow.{/i}"
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0006.ogg"
    n "Jason? Is something going on back there?"
    show Noelle at normal_stay
    j "No- no way mom! Everything’s fine back here!"
    j "{i}I don’t even wait to hear what she says back - I’m still completely exposed here. It’s time to run for my room.{/i}"
    jump jason2


label k2wakeup1:
    j "{i}Damn. I felt like I could have gotten something else out of her. Oh well…{/i}"
    j "You’ll wake up on the count of five. 5… 4… 3.. 2… 1… Wake!"
    k "... uh, where was I? Oh right. Don't hide in here."
    j "Alright, alright. I'm just going to hide in my room."
    "{i}What a waste of time.{/i}"
    jump jason2




label jason2:
    play music audio.deep_breaths_flute fadein 1.0
    scene jason_room_d with fade
    show Jason neutral at jason_normal(mid_left)


    play sound "music/334988__paulocorona__knocking-on-door.wav"


    j "{i}Ah, crap. What have I done now?{/i}"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0004.ogg"
    s "Jaaas-on!"
    show Jason rolleyes
    j "I already did your homework, Sarah!"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0005.ogg"
    s "That’s not why I’m here! I want to hang out."
    show Jason wonder
    j "{i}With me? That’s a first.{/i}"
    j "What’s the trick?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0006.ogg"
    s "No trick! I just thought...it’d be fun."
    show Jason happy
    j "{i}It’s working! Sarah thinks hanging out with me is fun. Perfect…{/i}"
    j "Didn’t you just accuse me of stealing your stuff?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0007.ogg"
    s "Jane already gave it back. Come on, let’s hang out. You can play some of your music for me…"
    j "{i}I’m too used to the way we usually argue. Normally she’d be trying to get me to check her out and I’d be trying to avoid looking (and failing) so I wouldn’t end up doing whatever she wanted.{/i}"
    j "{i}Things are different now!{/i}"
    j "Alright, give me a minute, okay?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0008.ogg"
    s "Thanks Jason!"



    scene sarah_room_d2d with fade
    show Jason neutral at jason_normal(close_left)
    show Sarah neutral at sarah_normal(mid_right)
    play music "music/Sarah's Theme.mp3" fadeout 1.0 fadein 1.0
    j "Alright Sarah, I have the music right here."
    show Sarah frown
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0009.ogg"
    s "You’re still using that weird thing? Just pick up an iStereo already."
    show Sarah at normal_stay
    j "How? Most of my money somehow ends up going to you."
    j "{i}Plus no regular music player could do as much as this ‘weird thing’ can do…{/i}"
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0010.ogg"
    s "Well, dates don’t pay for themselves! If you don’t split the bill, people think you’re just being a leech."
    show Sarah at normal_stay
    j "So you leech off of me, instead..."
    show Sarah happy
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0011.ogg"
    s "All I do is ask nicely. You’re the one who gives it to me..."
    show Sarah at normal_stay
    j "{i}Well, this time should be different.{/i}"
    j "Fine. You’ve never done anything wrong, ever."
    show Sarah happy
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0012.ogg"
    s "-giggle- Damn right."
    show Sarah at normal_stay
    j "Anyway, this is a new song. I wrote it just for you."
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    show Sarah neutral
    voice "VoiceActing/Day 02/Sarah/D02SarahL0013.ogg"
    s "Hey… that sounds… better… than yesterday…"
    j "{i}The subliminals I play at night include suggestions to make them love the music even more. This should sound like the best thing she’s ever heard.{/i}"
    j "Yeah, it’s way more fun, isn’t it? It’s so easy to just relax and listen to."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0014.ogg"
    s "Relax… listen…"
    j "That’s right. Just listen to the song. Follow along with the beat. Tick… tick… tick…"
    show Sarah hypno at sarah_normal(mid_right)
    show Sarah hypno_enter
    $ renpy.pause(random_true_float(1.0, 2.0))
    show Sarah hypno
    voice "VoiceActing/Day 02/Sarah/D02SarahL0015.ogg"
    s "Tick… tick…"
    j "It’s so easy, so comforting. Focusing on anything else seems too hard. Keeping your head up, keeping your eyes open, thinking… you can feel all of that getting harder and harder."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0016.ogg"
    s "Harder…"
    j "You just want to relax and forget everything other than the sound of the song and my voice."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0017.ogg"
    s "Relax…"
    j "As I count down from five it’ll become so difficult to think that you’ll fall into a deep, obedient trance and fall asleep. Five… four… three… two… one… Sleep."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0018.ogg"
    s "..."
    show Sarah hypno
    show Jason happy
    j "{i}Alright, let’s see what tricks I can teach my 'puppy' to do today!{/i}"
    play music "music/Sarah's Theme alt.mp3" fadeout 1.0 fadein 1.0
    jump s2A

label s2A:
    menu:
        "Yesterday I told you to pretend to be a puppy when you were alone. Did you?":
            jump s2A1
        "Did you get off while imagining being a dog?":
            jump s2A2


label s2A1:
    j "Yesterday I told you to pretend to be a puppy when you were alone. Did you?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0019.ogg"
    s "Yes…"
    j "What did you do?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0020.ogg"
    s "Crawled around, said woof… it was… strange… but so much fun…"
    j "It’s not strange to pretend to be a puppy, Sarah. From now on it’ll feel natural whenever you do it."
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0021.ogg"
    s "Natural…"
    j "That’s right. Natural."
    $ Sarah_c.add_points(1)
    jump s2B


label s2A2:
    j "Did you get off while imagining being a dog?"
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0022.ogg"
    s "Eew."
    j "I mean, you were pretending to be a dog, right? Wasn’t that hot? Why not a bitch in heat?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0023.ogg"
    s "Gross… Jason…"
    j "{i}That didn’t wake her up but she doesn’t seem thrilled.{/i}"
    $ Sarah_c.sub_points(1)
    jump s2B


label s2B:
    menu:
        "Nice 'collar!'":
            jump s2B1
        "Did you enjoy pretending to be a puppy?":
            jump s2B2


label s2B1:
    j "Nice 'collar!'"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0024.ogg"
    s "Thanks… feels… good…"
    j "You know, puppies collars have little rings on them. Do you know why?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0025.ogg"
    s "For...leashes…"
    j "That’s right. Would you like a leash?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0026.ogg"
    s "Mmmm…"
    j "Remember, puppies wear leashes. It’d be fun to be a puppy, wouldn’t it?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0027.ogg"
    s "Fun...to be...a puppy…"
    j "Would you like to be led around on a leash?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0028.ogg"
    s "...yes."
    j "Really? I have a little ring with a bell on it right here. I made it last night. Want to try it on?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0029.ogg"
    s "Sure…"
    j "Hot."
    $ Sarah_c.add_points(1)
    jump s2C


label s2B2:
    j "Did you enjoy pretending to be a puppy?"
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0030.ogg"
    s "No… fun. But… didn’t enjoy…"
    j "It was fun but you didn’t enjoy it?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0031.ogg"
    s "All… alone…"
    j "Why is it better when you’ve got people with you?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0032.ogg"
    s "More attention... want to have fun with someone… else…"
    $ Sarah_c.add_points(1)
    jump s2B1

label s2C:
    menu:
        "You should focus on making others happy.":
            jump s2C1
        "You should focus on making me happy.":
            jump s2C2
        "You should focus on making yourself happy.":
            jump s2C3

label s2C1:
    j "You know what the problem is with this house, Sarah?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0033.ogg"
    s "No…"
    j "Everyone is overworked. Unhappy. Sad. Isn’t that bad?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0034.ogg"
    s "Bad…"
    j "Everyone needs something to cheer them up. We can’t get a real puppy, but you could be that puppy that helps make everyone happy sometimes, right?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0035.ogg"
    s "Could… pretend…."
    j "Puppies get a lot of attention and make people happy. So that’s what you should do. Make everyone in the house happy."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0036.ogg"
    s "Make everyone… happy…"
    show Jason happy_ad
    j "Good girl."
    $ Sarah_c.add_points(1)
    jump s2D


label s2C2:
    j "The truth is you’re not a very good puppy."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0037.ogg"
    s "Why…"
    j "Haven’t you ever watched a TV show with a dog? Every one is about a boy and his dog. Well I’m the only boy here. You should be a puppy that belongs to someone."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0038.ogg"
    s "Just… pretending…"
    j "Right, but if you want to be a good puppy you should pretend to be my dog, obedient to me. You should make me happy."
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0039.ogg"
    s "Nooo… not your puppy... you’d be... gross…"
    j "Dogs don’t care about incest, Sarah. There’s nothing to worry about."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0040.ogg"
    s "Eew…"
    j "{i}This isn’t going anywhere. I’m going to try something else.{/i}"
    $ Sarah_c.sub_points(1)
    jump s2D


label s2C3:
    show Jason happy
    j "You should focus on making yourself happy, Sarah. Be a puppy because it’s fun for you!"
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0041.ogg"
    s "Not… fun…"
    show Jason neutral
    j "Why isn’t it fun to be a puppy for your own enjoyment?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0042.ogg"
    s "Boring… lonely… just weird…"
    j "But it’s not weird when you’re doing it for someone else?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0043.ogg"
    s "No… like acting… it’s okay to be strange on stage…"
    $ Sarah_c.sub_points(1)
    jump s2D


label s2D:
    j "Alright Sarah, let’s pretend you’re a puppy again!"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0044.ogg"
    s "Woof!"
    j "{i}She's down on all fours again, just like yesterday. But she’s still fully clothed. Maybe I can push her a little further today?{/i}"
    j "It’s not bad but… you’re not making me very happy."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0045.ogg"
    s "Awroo?"
    j "Well it’s just… you’re being a puppy because you want everyone in the family to be happy, right?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0046.ogg"
    s "Woof!"
    j "Well, what would mom like? You can answer with words."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0047.ogg"
    s "Mom would want… lots of help…"
    j "And Kira?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0048.ogg"
    s "She’d want to relax… with puppy… when stressed…"
    j "How about Jane?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0049.ogg"
    s "She’d have fun… playing… ball…"
    j "Sure, but how about me?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0050.ogg"
    s "Play… music…?"
    j "Sure, but we’re just pretending, right? So what would I want if YOU were my puppy. What do I always want from you?"
    show Sarah hypno
    voice "VoiceActing/Day 02/Sarah/D02SarahL0051.ogg"
    s "...check...me out…"
    j "So you’re not making the whole family happy, right?"
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0052.ogg"
    s "No..."
    j "You could fix that pretty easily. Dogs don’t wear clothes; you could just act like a regular puppy and I’d enjoy it."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0053.ogg"
    s "...Just… pretending…"
    j "Would you say the same thing if Kira or Jane or mom wanted you to make them happy?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0054.ogg"
    s "...No…"
    j "So what should you do?"
    show Sarah hypno
    voice "VoiceActing/Day 02/Sarah/D02SarahL0055.ogg"
    s "...Strip… But..."
    j "What?"
    show Sarah hypno_frown
    voice "VoiceActing/Day 02/Sarah/D02SarahL0056.ogg"
    s "Too...weird."
    j "{i}Damn. I thought I had that. Well, might as well keep building towards it.{/i}"
    j "But if a puppy was wearing what you’re wearing now, they’d get all tangled up, wouldn’t they?"
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0057.ogg"
    s "Mmm..."
    j "So when you’re pretending to be a puppy, you should strip down to your underwear, right?"
    if Sarah_c.points >=4:
        jump s2okay
    else:
        jump s2nokay


label s2okay:
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0058.ogg"
    s "Yes..."
    j "You’re such a good girl. You’re a great puppy! I’m going to count down from five, and when I get to one, you’ll wake up, okay?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0059.ogg"
    s "...okay…"
    j "Five. When I wake you up you’re going to remember everything we did yesterday, except being hypnotized."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0060.ogg"
    s "Mmm-hmm…"
    j "Four. It was your idea to pretend to be a puppy yesterday. Just like it is today. But you’re too shy to show anyone else so you decided to show me first. Understand?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0061.ogg"
    s "Show...you...first…."
    j "Three. And the more happy you make me the better you’ll feel. You’ll feel better and better about being a puppy, making others happy. You’ll want to try even harder to make others happy."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0062.ogg"
    s "Happy…"
    j "Two. Whenever I tell you you’re a good girl you’ll feel better than you ever have before. You’ll feel whatever good feeling you’re giving to the person you’re helping by being a puppy."
    j "Like relaxation for Kira, or rest for mom, or for me…"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0063.ogg"
    s "...Horny…"
    j "Right! You’re just feeling what we feel. Alright Sarah…one."
    play music audio.habanera fadein 1.0
    voice "VoiceActing/Day 02/Sarah/D02SarahL0064.ogg"
    show Sarah neutral at sarah_normal(mid_right)
    show Sarah at talking_stay
    s "Thanks Jason. I’m kinda nervous doing this, so I really appreciate you being willing to help me be a better puppy."
    show Sarah at normal_stay
    show Jason at talking_stay
    j "Hey, it’s no problem! So are you gonna…?"
    show Jason at normal_stay
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0065.ogg"
    s "S-sure. Here we go…"
    show Sarah at normal_stay
    scene cgbg with dissolve
    show spuppy1
    $ achievement.grant("NEW_ACHIEVEMENT_1_17")
    $ achievement.Sync()
    j "Wow! You look a lot more like a puppy like that. Nice panties, sis."
    hide spuppy1
    show spuppy2
    voice "VoiceActing/Day 02/Sarah/D02SarahL0066.ogg"
    s "Jason, you’re not supposed to talk about that stuff."
    j "Come on Sarah, it makes me really happy. And that’s what being a puppy is all about, right?"
    hide spuppy2
    show spuppy3
    voice "VoiceActing/Day 02/Sarah/D02SarahL0067.ogg"
    s "Yeah…"
    j "Come on, Sarah. That’s not what puppies say."
    hide spuppy3
    show spuppy4
    voice "VoiceActing/Day 02/Sarah/D02SarahL0068.ogg"
    s "Right! I mean… woof!"
    j "Good girl!"
    hide spuppy4
    show spuppy5
    voice "VoiceActing/Day 02/Sarah/D02SarahL0069.ogg"
    s "W-what did you say?"
    j "I said you’re a good girl. You’re really making me happy."
    hide spuppy5
    show spuppy6
    voice "VoiceActing/Day 02/Sarah/D02SarahL0070.ogg"
    s "Woof…?"
    j "{i}I make sure to sit so that she can see how 'happy' she’s making me.{/i}"
    j "See? I’m really happy. You’re a good girl for helping me out like this."
    hide spuppy6
    show spuppy7
    voice "VoiceActing/Day 02/Sarah/D02SarahL0071.ogg"
    s "Awoooo…"
    j "{i}If I had told her directly to get off to being nearly naked in front of me I don’t think she ever would have. But feeling what I feel? That’s just part of pretending to be a dog.{/i}"
    j "You’re a great puppy, Sarah. The best."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0072.ogg"
    s "Woof!"
    j "Okay Sarah, let’s try something else. Do you think you can do a 'puppy pose'? Just sit like a puppy begging for a bone."
    hide spuppy7
    show spuppy8
    voice "VoiceActing/Day 02/Sarah/D02SarahL0073.ogg"
    s "Awoo…?"
    hide spuppy8
    show spuppy9
    j "Good girl, Sarah! That’s making me REALLY happy! See?"
    hide spuppy9
    show spuppy10
    voice "VoiceActing/Day 02/Sarah/D02SarahL0074.ogg"
    s "-Pant-"
    j "Does the puppy want a bone, hmm?"
    hide spuppy10
    show spuppy11
    voice "VoiceActing/Day 02/Sarah/D02SarahL0075.ogg"
    s "Woof!"
    j "{i}I wish I could make her slobber on MY bone, but this little toy I whipped up last night should work well enough for now.{/i}"
    j "Okay, here’s your bone! Doesn’t it look tasty?"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0076.ogg"
    s "Woooof!"
    hide spuppy11
    show spuppy12
    j "Good girl! You’re doing the best job ever."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0077.ogg"
    s "-mmrfgh!"
    j "{i}She seems pretty turned on right now - about as much as I am? Maybe I can push it just a bit further.{/i}"
    j "You’ve been such a good girl. And you make a great puppy. But puppies don’t wear clothes, do they Sarah? You’re great but you could do a lot better. Think of how happy I’d be - how I’d feel."
    voice "VoiceActing/Day 02/Sarah/D02SarahL0078.ogg"
    s "... mmrrph."
    j "Was that an okay?"
    hide spuppy12
    show spuppy13
    j "{i}Oh wow. Yes, yes it was.{/i}"
    j "Wow, Sarah! You’re the best puppy I’ve ever seen! Good girl! Best girl! Best girl ever!"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0078.ogg"
    s "Mmmph!"
    hide spuppy13
    show spuppy14
    j "Who deserves headpats for being such a great puppy? It’s you!"
    voice "VoiceActing/Day 02/Sarah/D02SarahL0079.ogg"
    s "Mmmmph!"
    hide spuppy14
    show spuppy15
    j "{i}I managed to push her this far by just using her ability to feel what I feel… maybe I could push this a little further, but not today. The subliminals need to be improved for her to go any further.{/i}"
    j "Okay Sarah. I’m gonna go now. I think you’ll be a great puppy for everyone tomorrow. You shouldn’t feel embarrassed. And if you ever want to do this again just let me know."
    $ persistent.sarahnudepuppygirl = True
    voice "VoiceActing/Day 02/Sarah/D02SarahL0080.ogg"
    s "Mmph!"
    jump jason3


label s2nokay:
    show Sarah hypno_smile
    voice "VoiceActing/Day 02/Sarah/D02SarahL0081.ogg"
    s "No… too gross…"
    j "{i}Well that’s it. I’ve hit the edge of how far she’s willing to go. If I’d spun this a little differently maybe she would have done a little more.{/i}"
    j "Alright Sarah, just like yesterday. You’ll forget pretending to be a puppy. You’ll just remember that we had a lot of fun. Alright?"
    show Sarah hypno
    voice "VoiceActing/Day 02/Sarah/D02SarahL0082.ogg"
    s "Alright…"
    j "Five… four… three… two… one.. Wake!"
    show Sarah happy
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0083.ogg"
    s "Oh… that music was really good, Jason! Even better than yesterday!"
    show Sarah at normal_stay
    show Jason neutral
    j "Not good enough, I guess. See you tomorrow, sis."
    show Sarah at talking_stay
    voice "VoiceActing/Day 02/Sarah/D02SarahL0084.ogg"
    s "Okay! See ya!"
    jump jason3





label jason3:
    play music audio.deep_breaths_strings fadein 1.0
    scene jason_room_d with fade

    show Jason neutral at jason_normal(mid_left)
    j "{i}Oh man, after a day like that I can barely stand it! I need to get off - now!{/i}"
    j "God, I’m so horny…"
    show Noelle lewd at noelle_easeinright(far_right)
    $ renpy.pause(0.25, hard=True)
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0007.ogg"
    n "Is that so, young man?"
    show Noelle at normal_stay
    j "Mom!!"
    j "{i}Crap! Mom never comes into my room unless I’m in trouble. She can’t know what I’m up to...can she?{/i}"
    j "{i}She walks out of the room, expecting me to follow her.{/i}"
    scene noelle_room_d2d with fade
    show Jason neutral at jason_normal(close_left)
    show Noelle neutral at noelle_normal(mid_right)
    pause(0.25)
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0008.ogg"
    n "Jason, we need to talk."
    show Noelle at normal_stay
    jump n2A

label n2A:
    menu:
        "Sure thing, Mom.":
            jump n2B
        "Can it wait? I have something I need to do, pretty urgently…":
            jump n2A2
        "Not right now, Noelle. I need to jerk off.":
            jump n2A3


label n2A2:
    j "Can it wait? I have something I need to do, pretty urgently…"
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0009.ogg"
    n "No it can not!"
    show Noelle at normal_stay
    $ Noelle_c.add_points(1)
    jump n2B


label n2A3:
    j "Not right now, Noelle. I need to jerk off."
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0010.ogg"
    n "WHAT??"
    show Noelle at normal_stay
    j "Uh oh. I maybe should have thought that through a little better."
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0011.ogg"
    n "How dare you speak to me like that? I am your mother, and I will be treated with respect! What right do you think you have to call me by my first name?"
    show Noelle at normal_stay
    j "Sorry Mom…"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0012.ogg"
    n "That’s right: Mom! So, you want to stay in your room and...and...and do THAT, do you? Well, you’ll have plenty of time for it over the next week. Until this blizzard passes, you are grounded!"
    scene black with fade
    pause 1
    show badend covers with fade
    j "{i}No! Stuck in my room for the next week, I have no way to influence the girls...I can play them music until the snow starts to melt, but without specific instructions, there’s no way to turn it to my advantage…{/i}"
    return


label n2B:
    if janechores:
        jump choreend
    else:
        jump choreless


label choreend:
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0013.ogg"
    n "I was just downstairs, and I found Jane vacuuming…"
    show Noelle at normal_stay
    j "Uh oh."
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0014.ogg"
    n "Now, correct me if I’m wrong...but I believe that’s one of your chores, isn’t it?"
    j "Well…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0015.ogg"
    n "I know being stuck in the blizzard means your sisters are bored, but no one is THAT bored."
    j "I can explai-..."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0016.ogg"
    n "I also noticed that she was showing a lot more skin than usual. In fact, ALL of your sisters have been showing a lot more skin lately…"
    show Jason avoid
    j "{i}Crap! I really hoped she wouldn’t notice. And she won’t let me get a word in edgeways…{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0017.ogg"
    n "And then I remembered the strange music that we’ve all been hearing at night lately…"
    show Noelle at normal_stay
    show Jason happy
    j "{i}Ah ha! The perfect opportunity.{/i}"
    show Jason at talking_stay
    j "Yeah, actually, I was meaning to tell you about that. Why don’t we listen to some music now?"
    j "{i}The delimiter is exactly what I need to get out of this situation…{/i}"
    j "Listen to the sticky thumping of the beat, Mom. It…-"
    show Jason at normal_stay
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0018.ogg"
    n "I knew it!"
    j "{i}Mom leans forward and grabs the delimiter. No!{/i}"
    show Noelle lewd
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0019.ogg"
    n "You’ve been controlling us with this, haven’t you? I knew everyone had been acting strangely. Oh, Jason...what did I ever do to end up with a son like you?"
    j "{i}God, I’m finished. She’s going to destroy it, and then I...wait. She’s not destroying it. She’s examining it....{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0020.ogg"
    n "This is quite a clever little device. If I’m not mistaken, I just need to twist this dial, and…"
    show Noelle at normal_stay
    j "Mom? Mom, what are you...what are you…"
    jump n2badend

label n2badend:
    scene black with fade
    j "{i}Oh, crap. I’ve been listening to the music at night as well - way more than the rest of my family! I wonder what Mom said when I blacked out. I wonder what she told me to do!{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0021.ogg"
    n "Jason? How about another foot rub, honey?"
    scene cgbg with fade
    show badend noelle_footrub
    $ achievement.grant("NEW_ACHIEVEMENT_1_13")
    $ achievement.Sync()
    j "Of course, mother!"
    j "{i}Hmmm. It can’t have been that bad. After all, I trust Mom - after all, she raised me single-handedly! And she works so hard, and us kids don’t appreciate her nearly enough.{/i}"
    j "{i}I should spend more time making sure she’s taking care of. Yes, if I do that, I’m sure everything will be just...fine…{/i}"
    scene black with fade
    show bg badend at truecenter
    pause
    return


label choreless:
    play music "music/Noelle's Alternate Theme.mp3" fadeout 1.0 fadein 1.0
    j "Okay Mom - but do you mind if we listen to some music while we talk?"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0022.ogg"
    n "Fine! But please be quick. I would really like to discuss something with you."
    show Noelle at normal_stay
    j "{i}I turn the delimiter on in my pocket, and start the metronome without Mom realizing.{/i}"
    play sound "music/MetSlow.ogg"
    show metronome
    $ renpy.pause(11.0)
    hide metronome
    j "It’s quite nice, isn’t it?"
    show Noelle neutral
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0023.ogg"
    n "Yes, it’s...fine. Would you please...focus...?"
    j "Of course, Mom - I mean, as much as I can. It’s hard to, with that annoying clacking noise coming through the vents."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0024.ogg"
    n "Clacking...noise…?"
    j "Yes, can’t you hear it? It’s so steady...so consistent…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0025.ogg"
    n "Steady…"
    j "Clack...clack...clack...clack…"
    show Noelle hypno at noelle_normal(mid_right)
    show Noelle hypno_enter
    $ renpy.pause(random_true_float(1.0, 2.0))
    show Noelle hypno
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0026.ogg"
    n "Clack…"
    j "It’s so steady, so reliable. It really has a way of getting in your head…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0027.ogg"
    n "Clack...getting in...head...."
    j "Just listen to my voice, let Jason’s soothing voice distract you from the clacking."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0028.ogg"
    n "Distract…"
    j "Yes, listen to what I say. You can trust what I say. Trust and relax…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0029.ogg"
    n "Trust...and…relax."
    j "Whew! She’s under. Now I need to work out what she wanted to talk to me about…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0030.ogg"
    n "Wanted...to discuss..."
    j "What is it, Mom?"
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0031.ogg"
    n "...urges…"
    j "{i}Oooh, this could be good.{/i}"
    j "Are you having urges, Mom?"
    show Noelle shocked
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0032.ogg"
    n "No!"
    j "{i}Ah, crap. She’s starting to stir.{/i}"
    jump n2Bz


label n2Bz:
    menu:
        "You wanted to discuss my urges?":
            jump n2B1
        "No, I’m pretty sure you wanted to discuss your urges.":
            jump n2B2


label n2B1:
    j "You wanted to discuss my urges?"
    show Noelle hypno
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0033.ogg"
    n "That’s...right…"
    show Jason neutral
    j "{i}Good. She’s calmed down a bit. God, she’s so freaking repressed.{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0034.ogg"
    n "You can’t...have…"
    j "I can’t have urges?"
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0035.ogg"
    n "That’s...right. Hide your...feelings…"
    show Jason avoid
    j "-sigh-"
    j "Okay, Mom. I will. Thanks for the chat."
    j "{i}God, there’s no point in even keeping her under any more. Mom’s such a prude - I might be getting somewhere with my sisters, but there’s no way I’ll be able to break through her icy walls.{/i}"
    j "{i}I doubt anything even turns her on anymore - no idea what happened to make her such a bitch about it. I bet she’s feeling some deep-seated guilt about sex, and just projecting it onto me. Ugh.{/i}"
    j "Was there anything else you wanted to talk about?"
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0036.ogg"
    n "More...chores…"
    j "What? Why?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0037.ogg"
    n "Keep you...from getting...distracted…"
    j "{i}Ugh. I’d better stop this before it gets any worse.{/i}"
    j "Okay Mom, I’m going to count down from five, and you’re going to wake up."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0038.ogg"
    n "Mmmm…"
    j "Five. When you wake up, you’ll remember that we had a chat about sex. Four. You told me to stop checking out my sisters and hide my feelings deep inside, and I agreed."
    j "Three - you feel like you really got to me, and we’ll never have to talk about sex again. Two...you were thinking of giving me some more chores, but you decided that your words had done enough."
    j "One!"
    show Noelle neutral
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0039.ogg"
    n "Anyway, I hope that helped."
    show Noelle at normal_stay
    show Jason at talking_stay
    j "It did, Mom! It really did."
    show Jason at normal_stay
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0040.ogg"
    n "And...and if you ever feel like you’re going to get led down the path of…-"
    show Noelle at normal_stay
    show Jason at talking_stay
    j "I won’t, Mom! I promise."
    show Jason at normal_stay
    j "{i}Whew. What a day. Still no progress on Mom - I think my efforts there will be best spent making sure she doesn’t suspect anything of my sisters and I.{/i}"
    j "{i}I just wish there was some way I could have used her guilt, instead of having it work against me!{/i}"
    jump n2end


label n2B2:
    j "No, I’m pretty sure you wanted to discuss your urges."
    if noelleshower:
        jump showeryes
    else:
        jump showerno



label showerno:
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0041.ogg"
    n "No!"
    j "Of course you did. I know you have sexual urges, deep inside...deep, deep inside. Maybe we could work towards unlocking them…"
    show Noelle shocked
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0042.ogg"
    n "Jason, I...I can’t believe you’d say that to me!"
    j "{i}Oh, crap. Mom’s awake. And she’s mad…{/i}"
    show Noelle angry
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0043.ogg"
    n "Spying on your sister was one thing, but I am your MOTHER! You cannot talk to me like this - maybe some time alone in your room will teach you a lesson. For the next week, you are GROUNDED!"
    scene black with fade
    pause 1
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show badend jason_sad
    $ achievement.grant("NEW_ACHIEVEMENT_1_5")
    $ achievement.Sync()
    j "{i}Oh no! If I’m stuck in my room, I won’t be able to talk to my sisters. I can play my music with its subliminals all night long...but without me there to put them under and reinforce the message, it won’t actually DO anything.{/i}"
    j "{i}I’ll spend the rest of my life alone and horny, while my sisters are just outside my door...ripe for the plucking.{/i}"
    j "{i}I guess I shouldn’t have pushed it so far.{/i}"
    return


label showeryes:
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0044.ogg"
    n "I’m...worried…"
    j "Worried?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0045.ogg"
    n "About...you…"
    j "About me?? Why?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0046.ogg"
    n "Know how...teenage boys...are…"
    jump n2C

label n2C:
    menu:
        "Is this about yesterday in the shower? Because we said that was a one-time thing...":
            jump n2C1
        "Do you? Because I promise, it’s worse than you’re imagining.":
            jump n2C2
        "I imagine it can’t be easy being a single mother of three, either…":
            jump n2C3


label n2C1:
    j "Is this about yesterday in the shower? Because we said that was a one-time thing..."
    show Noelle shocked
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0047.ogg"
    n "...Jason!"
    j "{i}Oh, shit. She hasn’t woken up, but she looks maaaad.{/i}"
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0048.ogg"
    n "Promised...to never…speak of…"
    show Jason avoid
    j "{i}Crap. I did say that.{/i}"
    show Jason happy
    j "It’s okay, Mom...we don’t have to talk about it. How about we just head up to the shower, and…"
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0049.ogg"
    n "No!"
    show Noelle at normal_stay
    j "{i}She looks even angrier than before...aaaaand I don’t think she’s still under.{/i}"
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0050.ogg"
    n "I can’t believe that you would betray my trust like that! I was trying to help you - you said we would never discuss it again, and now here you are...here you are…"
    show Noelle at normal_stay
    j "{i}I’ve never seen Mom lost for words before.{/i}"
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0051.ogg"
    n "Well, I will let you know that I have been wracked with guilt since we did that, and I CERTAINLY wasn’t coming here to do it again!{nw}"
    n "Now that you’ve broken our agreement not to talk about it, I don’t know if I can trust you any more!"
    j "Mom…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0052.ogg"
    n "Don’t you ‘Mom’ me! I was coming here to tell you that I don’t want to be alone with you again - now that I know what dirty thoughts you’re having, I don’t think I can control...{nw}"
    n "I mean, I don’t think YOU can control yourself!"
    j "{i}Oh, crap. It sounds like she was really worked up before she came in...I could have taken advantage of that! Instead…{/i}"
    scene black with fade
    pause 1
    scene cgbg
    show badend covers
    pause
    return


label n2C2:
    j "Do you? Because I promise, it’s worse than you’re imagining."
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0053.ogg"
    n "Is...it…?"
    j "{i}She sounds concerned. Maybe I can use this to my advantage.{/i}"
    $ Noelle_c.add_points(1)
    jump n2D


label n2C3:
    j "I imagine it can’t be easy being a single mother of three, either…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0054.ogg"
    n "Can be...hard..."
    j "I bet it can. How about we talk about it?"
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0055.ogg"
    n "That sounds...nice…"
    j "And then, we can talk about how hard it is to be a teenage boy. But you go first."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0056.ogg"
    n "So much...pressure…"
    j "That sounds really hard!"
    j "{i}I don’t know if they give away medals for ‘sympathetic listening’, but after this conversation, I know I’ll at least be a contender.{/i}"
    j "{i}Mom spent almost half an hour telling me about the struggles she goes through at work, and what it’s like to have your children grow up...which, of course, led perfectly into what I really wanted to talk about.{/i}"
    $ Noelle_c.sub_points(2)
    jump n2D


label n2D:
    menu:
        "All these hormones, racing through my body...what we did yesterday in the shower helped, but only a little.":
            jump n2C1
        "I’m so horny, all the time. I was actually about to jerk off before you came in.":
            jump n2D2
        "I’m constantly broke. You make a lot of money - how about giving me some of it?":
            jump n2D3


label n2D2:
    j "I’m so horny, all the time. I was actually about to jerk off before you came in."
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0057.ogg"
    n "You were... you..."
    j "{i}God, just asking me that made her go red. She must be so embarrassed...wait, no. She’s breathing faster. She’s almost panting…{/i}"
    j "{i}Oh my god, is she EXCITED by the idea?{/i}"
    j "{i}Is...is that what she called me to her room for?{/i}"
    $ Noelle_c.add_points(1)
    jump n2E


label n2D3:
    j "I’m constantly broke. You make a lot of money - how about giving me some of it?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0058.ogg"
    n "Mmm…"
    j "{i}Well, that seemed to make her uncomfortable. I guess it makes sense - the only thing Mom likes talking about less than sex is money.{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0059.ogg"
    n "No...money’s...tight…"
    j "{i}Bullshit it is. Let’s see how effective my subliminal messages have been…{/i}"
    j "Wouldn’t it be super HOT to give your son some money…"
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0060.ogg"
    n "No…"
    j "Wouldn’t it make you feel so feminine and desirable to slip Jason some cash?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0061.ogg"
    n "Not...really…"
    j "Imagine giving your son a huge wad of twenties and fifties. Wouldn’t that make you a horny, sexy, fuckable Mommy-slut?"
    show Noelle shocked
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0062.ogg"
    n "Jason!"
    show Noelle at normal_stay
    j "{i}Whoops. May have pushed that a little far. I think she’s awake.{/i}"
    j "Uh, never mind. Go back to…-"
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0063.ogg"
    n "How DARE you speak to me that way? If you want money, you’ll have to earn it - instead of spending your days wasting time on music, and...and...silly little inventions like this!"
    j "No!"
    play sound "music/Smashing.mp3"
    j "{i}I tried to grab it out of her hands, but she was too fast! The delimiter went flying across the room, and then smashed into a million pieces...{/i}"
    j "{i}There goes my hope of turning my family into my own personal sex slaves.{/i}"
    scene black with fade
    pause 1
    show plug_frame first
    pause 0.14
    show plug_frame second
    pause 0.14
    hide plug_frame
    show badend jason_sad
    $ achievement.grant("NEW_ACHIEVEMENT_1_5")
    $ achievement.Sync()
    j "{i}All that time, all that effort...and I didn’t even get the money I was pushing for.{/i}"
    return


label n2E:
    menu:
        "I couldn’t stop thinking about yesterday. What we did in the shower - what YOU did - it was so hot…":
            jump n2C1
        "I have such a vivid imagination. I keep thinking about really sexy stuff.":
            jump n2E2
        "It’s not my fault. After all the skin being shown around the house…":
            jump n2E3



label n2E2:
    j "I have such a vivid imagination. I keep thinking about really sexy stuff."
    show Noelle hypno_frown
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0064.ogg"
    n "Don’t...want to...hear…"
    j "{i}Oh. I thought she’d be really excited to hear my fantasies. I have a great one involving her, Kira, Sarah, and a whole bushel of strawberries...but apparently not. Maybe I’ll try something else.{/i}"
    $ Noelle_c.sub_points(1)
    jump n2E


label n2E3:
    j "It’s not my fault. After all the skin being shown around the house…"
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0065.ogg"
    n "I know…"
    j "I mean, I’m a teenage boy! What am I meant to do when my sisters are walking around half-naked."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0066.ogg"
    n "Mmm...not your...fault…"
    j "You’re damned right it’s not!"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0067.ogg"
    n "Language…"
    j "Sorry Mom. But yeah - being surrounded by sexy teenagers, it’s really hard."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0068.ogg"
    n "It’s...hard…"
    j "{i}Uh, not actually the 'it' that I meant. But even through the trance, Mom is pretty blatantly checking out my cock. It seems pretty clear what she wants…{/i}"
    $ Noelle_c.add_points(1)
    jump n2F


label n2F:
    menu:
        "I’m so hard. Maybe we should go back to the shower and repeat what we did yesterday…":
            jump n2F1
        "I’m just...I’m just a raging ball of hormones, about to pop. I need to jerk off, or I don’t even know what I’m going to do.":
            jump guiltyboobs
        "And that’s not all!":
            jump n2F3


label n2F1:
    j "I’m so hard. Maybe we should go back to the shower and repeat what we did yesterday…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0069.ogg"
    n "Noo…"
    j "{i}I can’t tell if she’s being serious or playful. That’s the trouble with having a hard-ass for a Mom; you never get to witness her playful side.{/i}"
    j "C’mon, Mom...didn’t you have fun? It’s exactly what we both need right now."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0070.ogg"
    n "Mmmm...we shouldn’t…"
    jump n2F

label guiltyboobs:
    j "I’m just...I’m just a raging ball of hormones, about to pop. I need to jerk off, or I don’t even know what I’m going to do."
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0071.ogg"
    n "Let...mama...help…"
    j "{i}Yes!!{/i}"
    j "There’s always so much flesh on view. I’m just a teenage boy - what am I meant to do?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0072.ogg"
    n "Please…"
    j "I spend so much time jerking off, but it doesn’t help. I need to touch someone - I need to look at real girls, real women. And since the only ones around here are my sisters…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0073.ogg"
    n "No…"
    j "Uh oh. I hope I didn’t push that too far."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0074.ogg"
    n "Not...sisters…"
    j "{i}God, she’s red in the face.{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0075.ogg"
    n "Use...me…"
    j "What?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0076.ogg"
    n "Use...me...to...to…"
    j "You want me to use your body to get off to?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0077.ogg"
    n "Ungh...yes!"
    j "I dunno, Mom. Isn’t that wrong?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0078.ogg"
    n "Wrong to...think about...your sisters."
    j "Well, if you insist."
    jump n2H


label n2F3:
    j "And that’s not all!"
    show Noelle hypno_smile
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0079.ogg"
    n "What...else…"
    j "I mean, you must have noticed that my sisters have been acting a bit weird lately…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0080.ogg"
    n "Yess…"
    j "Sarah is always using her body to get what she wants…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0081.ogg"
    n "Shouldn’t...look…"
    j "You know I can’t help it, Mom. I’m just a guy - she practically flashes me sometimes!"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0082.ogg"
    n "Poor...boy…"
    j "I’m such a boob man, and I’m just surrounded by boobs all day…"
    j "{i}Well, a boob man, and an ass man, and a legs man...{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0083.ogg"
    n "Surrounded...boobs…"

    if janepanties:
        j "Jane is acting so feminine...so girly…"
        voice "VoiceActing/Day 02/Noelle/D02NoelleL0084.ogg"
        n "Mmm…"
        j "I mean, I’m a man! I can’t help it, can I?"
        voice "VoiceActing/Day 02/Noelle/D02NoelleL0085.ogg"
        n "Can’t...help it…"
        $ Noelle_c.add_points(1)
    if kirapanties:
        j "You know Kira wears silk panties, right?"
        voice "VoiceActing/Day 02/Noelle/D02NoelleL0086.ogg"
        n "Silk...panties…"
        j "Do you know how I know that? She showed them to me! She showed me her panties. Now tell me, what am I meant to do after that?"
        voice "VoiceActing/Day 02/Noelle/D02NoelleL0087.ogg"
        n "No...choice…"
        $ Noelle_c.add_points(1)
    j "So what am I supposed to do?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0088.ogg"
    n "Mama’s...here…"
    j "What do you mean?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0089.ogg"
    n "I want to...help. Let...mama...help…"
    j "What were you thinking? I’m so hard, and I need relief right away…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0090.ogg"
    n "Jerk off…"
    j "I can’t do that, not with you in the room! Besides, it doesn’t help - I need a real woman to help me…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0091.ogg"
    n "Jerk...off...on mama’s tits…"
    j "{i}Yes!! Oh my god, this is actually happening.{/i}"
    j "For real?"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0092.ogg"
    n "Only thing...that’ll...help…"
    j "{i}The horny bitch. I bet she came in specifically to get me to do that. God, this is going to be great - I’m going to wake her up and get to work…{/i}"
    jump wakeuptopless


label n2H:
    menu:
        "Let’s go to the bathroom and do what we did yesterday.":
            jump n2F1
        "Take off your top. I’m going to jerk off on your tits, right here.":
            jump n2H2
        "I want you to blow me. Open wide…":
            jump n2H3


label n2H2:
    j "Take off your top. I’m going to jerk off on your tits, right here."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0093.ogg"
    n "...okay…"
    j "{i}Holy shit, it worked! She’s unbuttoning her top.{/i}"
    j "Wait!"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0094.ogg"
    n "Okay."
    j "{i}God, Mom really gets off on being told what to do...when she’s in the exact right mood, of course. I’m going to wake her up - I want to do this for real.{/i}"
    jump wakeuptopless



label n2H3:
    j "I want you to blow me. Open wide…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0095.ogg"
    n "No…"
    j "I’m not asking, Mom, I’m telling."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0096.ogg"
    n "No! No...that’s...wrong…"
    j "{i}I’m so close. I can feel it. I just gotta push a little…{/i}"
    show Noelle shocked
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0097.ogg"
    n "Oh! OH!"
    j "{i}Oh my god - she’s cumming. Mom is cumming, just at the idea of blowing me. Wow.{/i}"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0098.ogg"
    n "Was...was I sleeping?"
    show Jason avoid
    j "{i}Ah, shit! She woke up.{/i}"
    show Noelle shocked
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0099.ogg"
    n "Wait. I wasn’t sleeping. I was...oh my god! Jason! You...you hypnotized me!!"
    show Noelle at normal_stay
    show Jason at talking_stay
    j "No! No, I swear!"
    show Jason at normal_stay
    show Noelle lewd
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0100.ogg"
    n "I remember everything - you used this little...this little machine to hypnotize me! You little sneak - you’re the reason I’ve been thinking about sex all day! That’s why we...{nw}"
    n "why we did what we did in the shower! Your little machine has been making me fantasize about blowing you!"
    show Noelle at normal_stay
    j "Actually…"
    show Noelle angry
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0101.ogg"
    n "Shut up!"
    show Noelle at normal_stay
    j "{i}I was going to tell her that no, the machine hadn’t told her to think about blowing me...but I don’t think that’d be super helpful right now.{/i}"
    j "{i}Still, that’s pretty damn hot! It looks like I was really close...before she woke up.{/i}"
    show Noelle frown
    show Noelle at talking_stay
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0102.ogg"
    n "Give me that! Hang on, this...this doesn’t look that complicated. If I just twiddle with this...and…"
    jump n2badend


label wakeuptopless:
    scene cgbg with dissolve
    show nboobs1
    $ achievement.grant("NEW_ACHIEVEMENT_1_21")
    $ achievement.Sync()
    j "Good girl… Now, I’m going to count down from five. When I get to one, I want you to wake up."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0103.ogg"
    n "Mmmm…"
    j "Five. You won’t remember me hypnotizing you, or the music. All you’ll remember is that we had a chat about how frustrating it is to be a teenager, and you agreed to... help me out."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0104.ogg"
    n "Mmm…"
    j "{i}She sounds so turned on. I can’t WAIT for her to wake up.{/i}"
    j "Four. You’ll let me cum on your tits, and you’ll find it to be the sexiest thing you’ve ever experienced."
    j "Three. You’ll love knowing that I’m getting off looking at YOU, my eyes on you. You’ll be so turned on…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0105.ogg"
    n "Oh!"
    j "{i}I’m so close to fulfilling another fantasy. Should I push it? Ah, it’s not much of a risk - Mom’s starting to make it pretty clear where her proclivities lie…{/i}"
    j "Two. You’ll feel so submissive and obedient, and you’ll love it. You’ll want to obey my every command. Obeying my commands turns you on."
    hide nboobs1
    show nboobs2
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0106.ogg"
    n "Yess…"
    j "One."
    hide nboobs2
    show nboobs3
    play music audio.habanera fadein 1.0
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0107.ogg"
    n "Okay Jason, let’s do this. But you have to be quick!"
    j "{i}She sounds breathless, like she just ran half a mile...god, I can’t believe how much of a total horndog my prudish Mom turned out to be.{/i}"
    j "{i}I wonder how much of that is the subliminal messages...and how much is just...her?{/i}"
    j "Okay Mom. Get ready."
    hide nboobs3
    show nboobs4
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0108.ogg"
    n "...okay."
    j "{i}Damn. I could get used to this.{/i}"
    hide nboobs4
    show nboobs5
    j "Oh, god...you’re so fucking sexy."
    hide nboobs5
    show nboobs6
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0109.ogg"
    n "Yes...yes, get hard for me. Get hard for mama. Get hard looking at Mom’s huge tits…"
    j "I’m so hard. Are you wet?"
    hide nboobs6
    show nboobs7
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0110.ogg"
    n "Oh baby, I’m so wet…"
    j "I want you to squeeze your tits together."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0111.ogg"
    n "Will it...should I…"
    j "Get your tits ready. For me. Because I told you to."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0112.ogg"
    n "Nngh…"
    hide nboobs7
    show nboobs8
    j "Doesn't it feel good? I want you to cum for me."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0113.ogg"
    n "Oh baby...I want YOU to cum for ME…"
    j "I’m going to cum all over you. I’m gonna cum on your big, sexy tits."
    hide nboobs8
    show nboobs9
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0114.ogg"
    n "Wait!"
    j "{i}Fuck! What did I do wrong now?{/i}"
    hide nboobs9
    show nboobs10
    j "Oh. OH! Ohh…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0115.ogg"
    n "I...I…"
    j "Do you want me to cum on you?"
    hide nboobs10
    show nboobs11
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0116.ogg"
    n "Yes…"
    j "What do we say?"
    hide nboobs11
    show nboobs12
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0117.ogg"
    n "Yes...please…"
    j "Cum for me. Cum right now."
    hide nboobs12
    show nboobs13
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0118.ogg"
    n "OH! Oh, oh god! Oh baby I’m cumming for you. I’m cumming for you, looking at your big, hard, sexy cock. I want it to cum all over me. Please! Fuck. Oh god, Jason, please...I want you to cum all over me."
    hide nboobs13
    show nboobs14
    j "I’m cumming! Mom, I’m cumming!"
    hide nboobs14
    show nboobs15
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0119.ogg"
    n "Yes! Yes! Yes! Yesssss…"
    hide nboobs15
    show nboobs16
    j "Oh my god. Oh my GOD. Oh, Mom…"
    hide nboobs16
    show nboobs17
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0120.ogg"
    n "Oh, Jason…"
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0121.ogg"
    n "..."
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0122.ogg"
    n "..."
    n "..."
    j "{i}I don’t think I’ve ever seen my Mom speechless before. I know for a fact I’ve never seen her speechless and topless with my cum dripping off her tits. Holy fuck that was hot…{/i}"
    hide nboobs17
    show nboobs18
    voice "VoiceActing/Day 02/Noelle/D02NoelleL0123.ogg"
    n "I’m...I’m going to go have a shower."
    $ persistent.noelleboobs = True
    $ Noelle_c.add_points(2)
    scene noelle_room_d2d with dissolve
    show Jason neutral at jason_normal(mid)
    play music "music/Jason's Theme.mp3" fadeout 1.0 fadein 1.0
    j "{i}She didn’t even put her top back on; if either of my sisters had been in the hallway, they would have seen Mom’s huge tits bouncing unfettered, covered in my spunk.{/i}"
    j "{i}I bet I could go and watch her. I bet I could go and watch her in the shower, and she wouldn’t even say a thing. I could cum onto her again, while she’s washing my first load off…{/i}"
    j "{i}It’s tempting. But it’s getting late, and I have a big day tomorrow...so I think I’m going to have a good night’s sleep, and see how much further everyone is after another night of music pumping directly into their brains.{/i}"
    j "{i}It’s so fucking hot to know that I could probably go down the hall and cum on my Mom while she showers.{/i}"
    j "{i}But here’s the thing - I don’t even need to. I just came, and I know it’s not even going to be too long before she comes begging to let me cum on her again...{/i}"
    j "{i}Now that’s what I call a good couple of days.{/i}"
    j "{i}I currently have [Kira_c.points] Kira [Sarah_c.points] Sarah [Noelle_c.points] Noelle [Jane_c.points] Jane points.{/i}"
    jump n2end

label n2end:
    $ persistent.d2u = True
    scene black with fade

    show text "END OF DAY TWO" at truecenter with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    show text "THREE DAYS REMAIN" at truecenter with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    stop music
    jump D3Start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
