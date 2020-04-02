





transform zoom_cyp:
    xalign 0.5
    zoom 0.5

image metronome:
    contains:
        "images/UI/metronome_base.webp"
        xalign 0.5 yalign 0.0
        xanchor 0.5 yanchor 0.0
    contains:

        "images/UI/metronome_arm.webp"
        anchor (0.5, 0.5)
        pos (0.5, 313)
        rotate -35
        block:
            linear 0.6 rotate 35.0
            linear 0.6 rotate -35.0
            repeat
    contains:

        "images/UI/metronome_spiral.webp"
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 313)
        block:
            rotate 0
            linear 2.4 rotate -360
            repeat


define logodissolve = ComposeTransition(Pause(2.5), before=dissolve, after=dissolve)



define audio.da_capa = "music/ost/Da Capa al Fine _pizz_.ogg.opus"
define audio.deep_breaths_flute = "music/ost/Deep Breaths _Flute_.ogg.opus"
define audio.deep_breaths_guitar = "music/ost/Deep Breaths _Guitar_.ogg.opus"
define audio.deep_breaths_piano = "music/ost/Deep Breaths _Piano_.ogg.opus"
define audio.deep_breaths_strings = "music/ost/Deep Breaths _Strings_.ogg.opus"
define audio.habanera = "music/ost/habanera 3.ogg.opus"
define audio.metronome = "music/ost/Metronome.mp3"
define audio.snowflake_lullaby_piano = "music/ost/Snowflake Lullaby _Piano_.ogg.opus"
define audio.snowflake_lullaby_piano_strings = "music/ost/Snowflake Lullaby _Piano+Strings_.ogg.opus"
define audio.fanfare_130 = "music/ost/Successful Fanfare _130 bpm_.ogg.opus"
define audio.fanfare_145 = "music/ost/Successful Fanfare _145 bpm_.ogg.opus"
define audio.masterplan = "music/ost/The_Master_Plan.ogg.opus"







init python:
    achievement.Sync()

    def random_true_float(min, max):
        return renpy.random.uniform(min, max)

    renpy_menu = menu
    full_shuffle = False
    part_shuffle = False
    def menu(items):
        items = list(items)
        if full_shuffle:
            renpy.random.shuffle(items)
            return renpy_menu(items)
        elif part_shuffle:
            last = items.pop()
            renpy.random.shuffle(items)
            items.append(last)
            return renpy_menu(items)
        return renpy_menu(items)

    class Subject:
        def __init__(self):
            self.points = 0
        def add_points(self, amount):
            self.points += amount
        def sub_points(self, amount):
            self.points -= amount
            if self.points < 0:
                self.points = 0













define j = Character(
    'Jason',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="jason_box",
    window_xpos=0.315,
    window_ypos=0.88)
define a = Character(
    'Jane',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="jane_box",
    window_xpos=0.315,
    window_ypos=0.88,
    voice_tag="Jane")
define k = Character(
    'Kira',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="kira_box",
    window_xpos=0.315,
    window_ypos=0.88,
    voice_tag="Kira")
define n = Character(
    'Noelle',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="noelle_box",
    window_xpos=0.315,
    window_ypos=0.88,
    voice_tag="Noelle")
define s = Character(
    'Sarah',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="sarah_box",
    window_xpos=0.315,
    window_ypos=0.88,
    voice_tag="Sarah")
define c = Character(
    'Cypress',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="cypress_box",
    window_xpos=0.315,
    window_ypos=0.88)
define narrator = Character(
    ' ',
    ctc="ctc_swirl",
    ctc_position="fixed",
    window_background="narrator_box",
    window_xpos=0.315,
    window_ypos=0.88,
    italics = True)
define credits = Character(None, kind = nvl)



label splashscreen:
    scene black







    if not renpy.variant("small"):
        scene black
        pause 0.2

        $ renpy.movie_cutscene("images/splash/OB_splash.webm")
        scene white with dissolve
        pause 0.4
        $ renpy.movie_cutscene("images/splash/KW_splash.webm")
    else:
        show outbreaklogo at truecenter with logodissolve

        scene black with dissolve
        jump KW_splash
        label KW_splash:
            scene white
            show kyungeki_splash at truecenter with logodissolve
            scene white with dissolve

    return


label start:

    $ Jane_c = Subject()
    $ Kira_c = Subject()
    $ Sarah_c = Subject()
    $ Noelle_c = Subject()

    $ janepanties = False
    $ kirapanties = False
    $ noelleshower = False
    $ musiccomment = False
    $ janechores = False
    $ janefashionshow = False
    $ janeschlick = False
    $ sarahbuttjob = False
    $ noelleblowjob = False
    $ kirathighjob = False
    $ d3jane = False
    $ d3sarah = False
    $ d3noelle = False
    $ d3jane = False
    $ janeyeschange = False
    $ d4noellejane = False
    $ d4kirasarah = False
    $ kirasexchosen = False
    $ sarahsexchosen = False
    $ janesexchosen = False
    $ noellesexchosen = False

    $ jane_outfit = JaneOutfit()
    $ jason_outfit = JasonOutfit()
    $ noelle_outfit = NoelleOutfit()
    $ sarah_outfit = SarahOutfit()
    $ kira_outfit = KiraOutfit()



    $ config.font_replacement_map["font/Cabin-Regular-TTF.ttf", False, True] = ("font/Cabin-Italic-TTF.ttf", False, False)

    stop music

    jump opt_op
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
