







image white = "#FFF"
image black = "#000"

image ctc_swirl:
    zoom 0.1
    "images/UI/swirly.webp"
    yalign 0.915
    xalign 0.80
    subpixel True
    rotate 0
    linear 5 rotate 360
    repeat

image hide_btn:
    zoom 0.05
    "images/UI/hide_button.webp"


image r18_warning:
    "images/splash/r18_1920x1080.webp"
    zoom 0.5
image outbreaklogo:
    "images/splash/outbreakgames_1280x720.webp"
image kyungeki_splash:
    "images/splash/KW_logo_compact_splash_1920x1080.webp"
    zoom 0.5

image cy_credit:
    "images/UI/Credits_Cypress.webp"
    zoom 0.3
image ob_credit:
    "images/UI/Credits_Outbreak.webp"
    zoom 0.3
image kw_credit:
    "images/UI/kw_bw.webp"
    zoom 0.2
image ex_credit_support:
    "images/UI/Extra_-_Thank_You01.webp"
    zoom 0.335
image ex_credit_playing:
    "images/UI/Extra_-_Thank_You02.webp"
    zoom 0.335


image sd_logo:
    "images/splash/Logo.webp"
    zoom 0.3
image sd_logo_bg:
    "images/splash/Logo.webp"
    zoom 0.7
image sd_title = "images/splash/Title001.webp"


image narrator_box:
    "images/UI/DialogBox 75Opacity.webp"
    zoom 0.52
image jason_box:
    "images/UI/Jason.webp"
    zoom 0.52
image jane_box:
    "images/UI/Jane.webp"
    zoom 0.52
image kira_box:
    "images/UI/Kira.webp"
    zoom 0.52
image noelle_box:
    "images/UI/Noelle.webp"
    zoom 0.52
image sarah_box:
    "images/UI/Sarah.webp"
    zoom 0.52
image cypress_box:
    "images/UI/CypressZeta.webp"
    zoom 0.52











image bg badend:
    "images/BGS/badend.webp"
    zoom 1.0
image bg logo:
    "outbreakgames.webp"
    zoom 1.0



image badend sara_rule:
    "images/CGS/BadEnds/be_sarah.webp"
image badend noelle_footrub:
    "images/CGS/BadEnds/be_noelle.webp"
image badend kira_chair:
    "images/CGS/BadEnds/be_kira.webp"
image badend cold_outside:
    "images/CGS/BadEnds/be_cold.webp"
image badend covers:
    "images/CGS/BadEnds/be_covers.webp"
image badend cooking:
    "images/CGS/BadEnds/be_cooking.webp"
image badend jason_sad:
    "images/CGS/BadEnds/be_sad.webp"

image badend sara_rulet:
    "images/CGS/BadEnds/be_sarah.webp"
    zoom 0.3
image badend noelle_footrubt:
    "images/CGS/BadEnds/be_noelle.webp"
    zoom 0.3
image badend kira_chairt:
    "images/CGS/BadEnds/be_kira.webp"
    zoom 0.3
image badend cold_outsidet:
    "images/CGS/BadEnds/be_cold.webp"
    zoom 0.3
image badend coverst:
    "images/CGS/BadEnds/be_covers.webp"
    zoom 0.3
image badend cookingt:
    "images/CGS/BadEnds/be_cooking.webp"
    zoom 0.3
image badend jason_sadt:
    "images/CGS/BadEnds/be_sad.webp"
    zoom 0.3

image plug_frame first:
    "images/CGS/Popups/01.webp"
image plug_frame second:
    "images/CGS/Popups/02.webp"
image plug_frame noelle:
    "images/CGS/Popups/plug_noelle.webp"
image plug_frame sarah:
    "images/CGS/Popups/plug_sarah.webp"
image plug_frame jane:
    "images/CGS/Popups/plug_jane.webp"
image plug_frame kira:
    "images/CGS/Popups/plug_kira.webp"











image bg house 1 = "images/BGS/1-0.webp"
image bg house 2 = "images/BGS/1-1.webp"
image bg house 3 = "images/BGS/1-1-1.webp"
image bg house 4 = "images/BGS/1-2.webp"
image bg house 5 = "images/BGS/1-2-1.webp"
image bg house 6 = "images/BGS/1-3.webp"
image bg house 7 = "images/BGS/1-3-1.webp"
image bg house 8 = "images/BGS/1-3-2.webp"
image bg house 9 = "images/BGS/2-1.webp"
image bg house 10 = "images/BGS/2-2.webp"
image bg house 11 = "images/BGS/3-1.webp"
image bg house 12 = "images/BGS/3-1-1.webp"
image bg house 13 = "images/BGS/4-1.webp"
image bg house title = "images/splash/Title001.webp"
image bg house 14 = "images/BGS/1-3-3.webp"

image snowyday = Animation("images/BGS/1-1-1.webp", 0.7, "images/BGS/1-1.webp", 0.7)

image s_day1_snow:
    "images/BGS/1-1.webp" with dissolve
    pause random_true_float(2, 3)
    "images/BGS/1-1-1.webp" with dissolve
    pause random_true_float(2, 3)
    repeat

image s_night1_snow:
    "images/BGS/1-2.webp" with dissolve
    pause random_true_float(2, 3)
    "images/BGS/1-2-1.webp" with dissolve
    pause random_true_float(2, 3)
    repeat

image s_night2_snow:
    "images/BGS/1-3.webp" with dissolve
    pause random_true_float(2, 3)
    "images/BGS/1-3-1.webp" with dissolve
    pause random_true_float(2, 3)
    repeat

image slow_snowyday:
    "s_day1_snow" with dissolve
    pause random_true_float(10, 13)
    "s_night1_snow" with dissolve
    pause random_true_float(10, 13)
    "s_night2_snow" with dissolve
    pause random_true_float(10, 13)
    "images/BGS/1-3-2.webp" with dissolve
    pause random_true_float(5, 8)
    repeat


image bg house morning5animation = Animation(
    "images/BGS/3-1-1.webp", 1.0,
    "images/BGS/3-1.webp", 1.0,
    "images/BGS/3-1-1.webp", 1.0,
    "images/BGS/3-1.webp", 1.0,
    "images/BGS/3-1-1.webp", 1.0)





image kitchen_d1:
    "images/BGS/new/kitchen_d1_d.webp"
    zoom 0.67
image kitchen_d2:
    "images/BGS/new/kitchen_d2_d.webp"
    zoom 0.67
image kitchen_d3:
    "images/BGS/new/kitchen_d3_d.webp"
    zoom 0.67
image kitchen_d4:
    "images/BGS/new/kitchen_d4_d.webp"
    zoom 0.67
image kitchen_d5:
    "images/BGS/new/kitchen_d5_d.webp"
    zoom 0.67


image bathroom_d1d:
    "images/BGS/new/bathroom_d1_d.webp"
    zoom 0.67
image bathroom_d1n:
    "images/BGS/new/bathroom_d1_n.webp"
    zoom 0.67
image bathroom_d2d:
    "images/BGS/new/bathroom_d2_d.webp"
    zoom 0.67
image bathroom_d2n:
    "images/BGS/new/bathroom_d2_n.webp"
    zoom 0.67
image bathroom_d3d:
    "images/BGS/new/bathroom_d3_d.webp"
    zoom 0.67
image bathroom_d3n:
    "images/BGS/new/bathroom_d3_n.webp"
    zoom 0.67

image livingroom_d1:
    "images/BGS/new/living_room_d1.webp"
    zoom 0.67
image livingroom_d3:
    "images/BGS/new/living_room_d3.webp"
    zoom 0.67
image livingroom_d4:
    "images/BGS/new/living_room_d4.webp"
    zoom 0.67
image livingroom_d5:
    "images/BGS/new/living_room_d5.webp"
    zoom 0.67

image jason_room_d:
    "images/BGS/new/jason_room_d.webp"
    zoom 0.67
image jason_room_n:
    "images/BGS/new/jason_room_n.webp"
    zoom 0.67

image noelle_room_d1d:
    "images/BGS/new/noelle_room_d1_d.webp"
    zoom 0.67
image noelle_room_d2d:
    "images/BGS/new/noelle_room_d2_d.webp"
    zoom 0.67
image noelle_room_d3d:
    "images/BGS/new/noelle_room_d3_d.webp"
    zoom 0.67
image noelle_room_d4d:
    "images/BGS/new/noelle_room_d4_d.webp"
    zoom 0.67
image noelle_room_d5d:
    "images/BGS/new/noelle_room_d5_d.webp"
    zoom 0.67
image noelle_room_d1n:
    "images/BGS/new/noelle_room_d1_n.webp"
    zoom 0.67
image noelle_room_d2n:
    "images/BGS/new/noelle_room_d2_n.webp"
    zoom 0.67
image noelle_room_d3n:
    "images/BGS/new/noelle_room_d3_n.webp"
    zoom 0.67
image noelle_room_d4n:
    "images/BGS/new/noelle_room_d4_n.webp"
    zoom 0.67
image noelle_room_d5n:
    "images/BGS/new/noelle_room_d5_n.webp"
    zoom 0.67

image kira_room_d1d:
    "images/BGS/new/kira_room_d1_d.webp"
    zoom 0.67
image kira_room_d2d:
    "images/BGS/new/kira_room_d2_d.webp"
    zoom 0.67
image kira_room_d3d:
    "images/BGS/new/kira_room_d3_d.webp"
    zoom 0.67
image kira_room_d4d:
    "images/BGS/new/kira_room_d4_d.webp"
    zoom 0.67
image kira_room_d5d:
    "images/BGS/new/kira_room_d5_d.webp"
    zoom 0.67
image kira_room_d1n:
    "images/BGS/new/kira_room_d1_n.webp"
    zoom 0.67
image kira_room_d2n:
    "images/BGS/new/kira_room_d2_n.webp"
    zoom 0.67
image kira_room_d3n:
    "images/BGS/new/kira_room_d3_n.webp"
    zoom 0.67
image kira_room_d4n:
    "images/BGS/new/kira_room_d4_n.webp"
    zoom 0.67
image kira_room_d5n:
    "images/BGS/new/kira_room_d5_n.webp"
    zoom 0.67


image jane_room_d1d:
    "images/BGS/new/jane_room_d1_d.webp"
    zoom 0.67
image jane_room_d2d:
    "images/BGS/new/jane_room_d2_d.webp"
    zoom 0.67
image jane_room_d3d:
    "images/BGS/new/jane_room_d3_d.webp"
    zoom 0.67
image jane_room_d4d:
    "images/BGS/new/jane_room_d4_d.webp"
    zoom 0.67
image jane_room_d5d:
    "images/BGS/new/jane_room_d5_d.webp"
    zoom 0.67
image jane_room_d1n:
    "images/BGS/new/jane_room_d1_n.webp"
    zoom 0.67
image jane_room_d2n:
    "images/BGS/new/jane_room_d2_n.webp"
    zoom 0.67
image jane_room_d3n:
    "images/BGS/new/jane_room_d3_n.webp"
    zoom 0.67
image jane_room_d4n:
    "images/BGS/new/jane_room_d4_n.webp"
    zoom 0.67
image jane_room_d5n:
    "images/BGS/new/jane_room_d5_n.webp"
    zoom 0.67


image sarah_room_d1d:
    "images/BGS/new/sarah_room_d1_d.webp"
    zoom 0.67
image sarah_room_d2d:
    "images/BGS/new/sarah_room_d2_d.webp"
    zoom 0.67
image sarah_room_d3d:
    "images/BGS/new/sarah_room_d3_d.webp"
    zoom 0.67
image sarah_room_d4d:
    "images/BGS/new/sarah_room_d4_d.webp"
    zoom 0.67
image sarah_room_d5d:
    "images/BGS/new/sarah_room_d5_d.webp"
    zoom 0.67
image sarah_room_d1n:
    "images/BGS/new/sarah_room_d1_n.webp"
    zoom 0.67
image sarah_room_d2n:
    "images/BGS/new/sarah_room_d2_n.webp"
    zoom 0.67
image sarah_room_d3n:
    "images/BGS/new/sarah_room_d3_n.webp"
    zoom 0.67
image sarah_room_d4n:
    "images/BGS/new/sarah_room_d4_n.webp"
    zoom 0.67
image sarah_room_d5n:
    "images/BGS/new/sarah_room_d5_n.webp"
    zoom 0.67
















init python early:


    class JaneOutfitEnum:
        NUDE = 1
        NORMAL = 2
        FASHION = 3
        DRESS = 4
        SLUTTY = 5
        SEXY = 6
        UNDERWEAR = 7

    class JasonOutfitEnum:
        NUDE = 1
        NORMAL = 2
        CAT = 3

    class NoelleOutfitEnum:
        NUDE = 1
        NORMAL = 2
        FASHION = 3
        DRESS = 4
        SLUTTY = 5
        SEXY = 6
        UNDERWEAR = 7
        UNDERWEAR_ALT = 8

    class SarahOutfitEnum:
        NUDE = 1
        NORMAL = 2
        FASHION = 3
        DRESS = 4
        SLUTTY = 5
        SEXY = 6
        UNDERWEAR = 7

    class KiraOutfitEnum:
        NUDE = 1
        NORMAL = 2
        FASHION = 3
        DRESS = 4
        SLUTTY = 5
        SEXY = 6
        UNDERWEAR = 7



    class JaneOutfit:
        
        def __init__(self):
            self.CanonOutfit = JaneOutfitEnum.NORMAL
        
        def outfit(self):
            if persistent.jane_player_selected_outfit != None:
                return persistent.jane_player_selected_outfit
            return self.CanonOutfit

    class JasonOutfit:
        def __init__(self):
            self.CanonOutfit = JasonOutfitEnum.NORMAL
        def outfit(self):
            if persistent.jason_player_selected_outfit != None:
                return persistent.jason_player_selected_outfit
            return self.CanonOutfit

    class NoelleOutfit:
        def __init__(self):
            self.CanonOutfit = NoelleOutfitEnum.NORMAL
        def outfit(self):
            if persistent.noelle_player_selected_outfit != None:
                return persistent.noelle_player_selected_outfit
            return self.CanonOutfit

    class SarahOutfit:
        def __init__(self):
            self.CanonOutfit = SarahOutfitEnum.NORMAL
        def outfit(self):
            if persistent.sarah_player_selected_outfit != None:
                return persistent.sarah_player_selected_outfit
            return self.CanonOutfit

    class KiraOutfit:
        def __init__(self):
            self.CanonOutfit = KiraOutfitEnum.NORMAL
        def outfit(self):
            if persistent.kira_player_selected_outfit != None:
                return persistent.kira_player_selected_outfit
            return self.CanonOutfit


image Jason old = "images/Jason B_eye1_mouth1_clothes_pose2.webp"
image Jane old = "images/Jane B_eye4_mouth2_clothed_pose1.webp"













image Cypress happy:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/cypress_e1.webp",
    )
image Cypress derpy:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/cypress_e2.webp",
    )
image Cypress angry:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/cypress_e3.webp",
    )
image Cypress lewd:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/cypress_e4.webp",
    )
image Cypress sad:
    LiveComposite(
        (992, 1403),
        (0, 0), "images/Character_parts/cypress_e5.webp",
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
