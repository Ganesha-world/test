










init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True


init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"









    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.2
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/DialogBox 75Opacity.webp", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor gui.text_xalign
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"


init -1 style input_prompt is default

init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

init -1 style input:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign









init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")








init -1 style emergency_hide_panel:
    color "#ff0000"

init -1 style emergency_hide_button:
    color "#ff0000"

    background None

init -501 screen quick_menu():


    zorder 100


    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("History") action ShowMenu('history')
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Prefs") action ShowMenu('preferences')










init -1 python:
    config.overlay_screens.append("quick_menu")


init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")
    color "#1558b9"

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")
    color "#3679db"













init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("New Game"):
                action Start()
        textbutton _("Load Game"):
            action ShowMenu("load")
        textbutton _("Settings"):
            action ShowMenu("preferences")

        if main_menu:
            textbutton "Extras":
                action ShowMenu("extras_navigation")

        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save Game") action ShowMenu("save")


        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()



        if renpy.variant("pc"):

            textbutton _("Help") action ShowMenu("help")

            textbutton _("Quit Game") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")









init -501 screen extras_navigation():
    tag menu
    use game_menu(_("Extras"), scroll="viewport"):
        style_prefix "about"
        vbox:
            textbutton "Bonus" action ShowMenu("extras_menu")
            textbutton _("CG Gallery") action ShowMenu("neu_gallery")
            textbutton "Music Room" action ShowMenu("music_room")
            textbutton _("About") action ShowMenu("about")











init -501 screen main_menu():
    tag menu
    add "slow_snowyday"

    add "images/UI/Filter2.webp"
    text "Click to Start":

        font "font/Cabin-Regular-TTF.ttf"
        size 55
        xalign 0.5
        yalign 0.8
    imagemap:
        ground "sd_logo_bg" xalign 0.5 yalign 0.1
        alpha False
        hotspot (0, 0, config.screen_width, config.screen_height) action Jump("nai")

label nai:
    scene slow_snowyday
    hide screen main_menu
    hide slow_snowyday
    call screen real_main_menu








init -501 screen real_main_menu():
    tag menu



    style_prefix "main_menu"

    add gui.main_menu_background
    add "slow_snowyday"
    add "images/UI/Filter.webp"
    add "sd_logo" xalign 0.7 yalign 0.07


    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.webp"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

init -1 style main_menu_title:
    size gui.title_text_size












init -501 screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:


    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.webp"



init -1 style game_menu_navigation_frame:

    xsize 280

    yfill True

init -1 style game_menu_content_frame:



    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:

    xsize 920


init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:

    spacing 10

init -1 style game_menu_label:


    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5


init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0

    yoffset -30









init -501 screen about():
    tag menu





    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size









init -501 screen extras_menu():
    tag menu





    use game_menu(_("Extras"), scroll="viewport"):

        style_prefix "about"

        vbox:










            label "Costume Options"

            vbox:
                text "Jason's Costumes"
                hbox:
                    textbutton "Default":
                        action SetField(persistent, "jason_player_selected_outfit", None)
                        style "check_button"
                        text_size 18
                    if (persistent.d1u):
                        textbutton "Normal":
                            action SetField(persistent, "jason_player_selected_outfit", JasonOutfitEnum.NORMAL)
                            style "check_button"
                            text_size 18
                    if (persistent.d5u_JASON):
                        textbutton "Nude":
                            action SetField(persistent, "jason_player_selected_outfit", JasonOutfitEnum.NUDE)
                            style "check_button"
                            text_size 18
                        textbutton "Cat Disciple":
                            action SetField(persistent, "jason_player_selected_outfit", JasonOutfitEnum.CAT)
                            style "check_button"
                            text_size 18
                null height 20
                text "Jane's Costumes"
                hbox:
                    textbutton "Default":
                        action SetField(persistent, "jane_player_selected_outfit", None)
                        style "check_button"
                        text_size 18
                    if (persistent.d0u):
                        textbutton "Underwear":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.UNDERWEAR)
                            style "check_button"
                            text_size 18
                    if (persistent.d1u):
                        textbutton "Day 1":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.NORMAL)
                            style "check_button"
                            text_size 18
                    if (persistent.d2u):
                        textbutton "Day 2":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.FASHION)
                            style "check_button"
                            text_size 18
                    if (persistent.d3u):
                        textbutton "Day 3":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.DRESS)
                            style "check_button"
                            text_size 18
                    if (persistent.d4u):
                        textbutton "Day 4":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.SEXY)
                            style "check_button"
                            text_size 18
                    if (persistent.d5u_JANE):
                        textbutton "Day 5":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.SLUTTY)
                            style "check_button"
                            text_size 18
                        textbutton "Nude":
                            action SetField(persistent, "jane_player_selected_outfit", JaneOutfitEnum.NUDE)
                            style "check_button"
                            text_size 18
                null height 20
                text "Noelle's Costumes"
                hbox:
                    textbutton "Default":
                        action SetField(persistent, "noelle_player_selected_outfit", None)
                        style "check_button"
                        text_size 18
                    if (persistent.d0u):
                        textbutton "Underwear":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.UNDERWEAR)
                            style "check_button"
                            text_size 18
                        textbutton "Alt. Underwear":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.UNDERWEAR_ALT)
                            style "check_button"
                            text_size 18
                    if (persistent.d1u):
                        textbutton "Day 1":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.NORMAL)
                            style "check_button"
                            text_size 18
                    if (persistent.d2u):
                        textbutton "Day 2":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.FASHION)
                            style "check_button"
                            text_size 18
                    if (persistent.d3u):
                        textbutton "Day 3":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.DRESS)
                            style "check_button"
                            text_size 18
                    if (persistent.d4u):
                        textbutton "Day 4":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.SEXY)
                            style "check_button"
                            text_size 18
                    if (persistent.d5u_NOELLE):
                        textbutton "Day 5":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.SLUTTY)
                            style "check_button"
                            text_size 18
                        textbutton "Nude":
                            action SetField(persistent, "noelle_player_selected_outfit", NoelleOutfitEnum.NUDE)
                            style "check_button"
                            text_size 18
                null height 20
                text "Sarah's Costumes"
                hbox:
                    textbutton "Default":
                        action SetField(persistent, "sarah_player_selected_outfit", None)
                        style "check_button"
                        text_size 18
                    if (persistent.d0u):
                        textbutton "Underwear":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.UNDERWEAR)
                            style "check_button"
                            text_size 18
                    if (persistent.d1u):
                        textbutton "Day 1":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.NORMAL)
                            style "check_button"
                            text_size 18
                    if (persistent.d2u):
                        textbutton "Day 2":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.FASHION)
                            style "check_button"
                            text_size 18
                    if (persistent.d3u):
                        textbutton "Day 3":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.DRESS)
                            style "check_button"
                            text_size 18
                    if (persistent.d4u):
                        textbutton "Day 4":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.SEXY)
                            style "check_button"
                            text_size 18
                    if (persistent.d5u_SARAH):
                        textbutton "Day 5":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.SLUTTY)
                            style "check_button"
                            text_size 18
                        textbutton "Nude":
                            action SetField(persistent, "sarah_player_selected_outfit", SarahOutfitEnum.NUDE)
                            style "check_button"
                            text_size 18
                null height 20
                text "Kira's Costumes"
                hbox:
                    textbutton "Default":
                        action SetField(persistent, "kira_player_selected_outfit", None)
                        style "check_button"
                        text_size 18
                    if (persistent.d0u):
                        textbutton "Underwear":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.UNDERWEAR)
                            style "check_button"
                            text_size 18
                    if (persistent.d1u):
                        textbutton "Day 1":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.NORMAL)
                            style "check_button"
                            text_size 18
                    if (persistent.d2u):
                        textbutton "Day 2":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.FASHION)
                            style "check_button"
                            text_size 18
                    if (persistent.d3u):
                        textbutton "Day 3":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.DRESS)
                            style "check_button"
                            text_size 18
                    if (persistent.d4u):
                        textbutton "Day 4":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.SEXY)
                            style "check_button"
                            text_size 18
                    if (persistent.d5u_KIRA):
                        textbutton "Day 5":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.SLUTTY)
                            style "check_button"
                            text_size 18
                        textbutton "Nude":
                            action SetField(persistent, "kira_player_selected_outfit", KiraOutfitEnum.NUDE)
                            style "check_button"
                            text_size 18

                null height 50

            label "Bonus Stories"
            vbox:
                vbox:
                    textbutton "Bonus Room":
                        action ShowMenu("bonus_audio_room")
                    textbutton "Blooper Room":
                        action ShowMenu("blooper_audio_room")

                    if persistent.janesexchosen:
                        textbutton "Jane Bonus Ending":
                            action Start("jane_extra")

                    if persistent.sarahsexchosen:
                        textbutton "Sarah Bonus Ending":
                            action Start("sarah_extra")

                    if persistent.noellesexchosen:
                        textbutton "Noelle Bonus Ending":
                            action Start("noelle_extra")

                    if persistent.kirasexchosen:
                        textbutton "Kira Bonus Ending":
                            action Start("kira_extra")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size











init -501 screen save():
    tag menu


    use file_slots(_("Save"))


init -501 screen load():
    tag menu


    use file_slots(_("Load"))


init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:



            order_reverse True


            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.3

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                textbutton _("{#auto_page}A") action FilePage("auto")

                textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 50
    ypadding 3

init -1 style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")







init -1 style panic_style:
    xalign 0.5
    yalign 0.5

init -1 style panic_btn:
    color "#ee3900"

init -501 screen cat_panic():
    tag menu
    add "images/UI/CypressSwole.webp"
    vbox:
        style "panic_style"
        text "Jane points: [Jane_c.points]\n"
        text "Sarah points: [Sarah_c.points]\n"
        text "Noelle points: [Noelle_c.points]\n"
        text "Kira points: [Kira_c.points]"












init -501 screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                        vbox:
                            textbutton "Mute Jane":
                                action ToggleVoiceMute("Jane")
                                style "mute_all_button"
                            textbutton "Mute Kira":
                                action ToggleVoiceMute("Kira")
                                style "mute_all_button"
                            textbutton "Mute Sarah":
                                action ToggleVoiceMute("Sarah")
                                style "mute_all_button"
                            textbutton "Mute Noelle":
                                action ToggleVoiceMute("Noelle")
                                style "mute_all_button"

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All Sound"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.webp"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.webp"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450










init -501 screen history():
    tag menu



    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advance dialogue and activates the interface.")

    hbox:
        label ("Left Trigger\nLeft Shoulder")
        text _("Roll back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Roll forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Access the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 250
    right_padding 20

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.webp", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = 6

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.webp"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







init -1 style pref_vbox:
    variant "medium"
    xsize 450



init -501 screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Menu") action ShowMenu()
        textbutton _("Auto") action Preference("auto-forward", "toggle")


init -1 style window:
    variant "small"

    background "gui/DialogBox 75Opacity.webp"

    xalign 0.2

init -1 style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

init -1 style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

init -1 style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 340

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 400

init -1 style slider_pref_vbox:
    variant "small"
    xsize None

init -1 style slider_pref_slider:
    variant "small"
    xsize 600





transform -1 credits_scroll(speed):



    ypos 720


    linear speed ypos -1500

init -1 style credit_spacing:
    xalign 0.5
    spacing 5

init -1:
    image cred1 = Text("Head of Development:", text_align=0.5)
    image cred2 = Text("Cypress Zeta", text_align=0.5)

init -501 screen Credits():
    tag menu
    add "#FFF"

    frame at credits_scroll(25):
        background None
        xalign 0.5

        has vbox:
            style "credit_spacing"
            null height 20
            spacing 20

        vbox:
            xalign 0.5
            hbox:

                spacing 20
                vbox:
                    text "{b}A{/b}":
                        color "#000"
                        ypos 46
                vbox:
                    add "cy_credit"
                vbox:
                    text "{b}Game{/b}":
                        color "#000"
                        ypos 46
            null height 80
        vbox:
            style "credit_spacing"
            text "{b}Cast{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "Diana Lockheart               Noelle":
                color "#000"
            text "Silica                                    Jane":
                color "#000"
            text "Shiyon                                 Kira":
                color "#000"
            text "                                              Sarah":
                color "#000"
            text ""
        vbox:
            style "credit_spacing"
            text "{b}Art{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "FreeGlass":
                color "#000"
                xalign 0.5
            text "Brellom":
                color "#000"
                xalign 0.5
            text "Idlecum":
                color "#000"
                xalign 0.5
            text "Short Blue Imp":
                color "#000"
                xalign 0.5
            text ""
        vbox:
            style "credit_spacing"
            text "{b}Concept Art{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "Mindwipe":
                color "#000"
                xalign 0.5
            text "NinjaKitty":
                color "#000"
                xalign 0.5
            text "SleepyMaid":
                color "#000"
                xalign 0.5
            text "Short Blue Imp":
                color "#000"
                xalign 0.5
            text ""
        vbox:
            style "credit_spacing"
            text "{b}Programming{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "polisummer":
                color "#000"
                xalign 0.5
            text "tippi":
                color "#000"
                xalign 0.5
            text ""
        vbox:
            style "credit_spacing"
            text "{b}Music{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "Nathaniel Platier":
                color "#000"
                xalign 0.5
            text ""
        vbox:
            style "credit_spacing"
            text "{b}Special Thanks{/b}{size=+20}":
                color "#000"
                xalign 0.5
            text "Hexun for coding a useful tool":
                color "#000"
                xalign 0.5
            text "Pan":
                color "#000"
                xalign 0.5
            text "And an anonymous writing friend. You know who you are.":
                color "#000"
                xalign 0.5
        hbox:
            xalign 0.5
            spacing 10
            vbox:
                xalign 0.5
                yalign 0.5
                add "ob_credit"
            vbox:
                xalign 0.5
                yalign 0.5
                add "kw_credit"
            null height 80






        vbox:
            xalign 0.0
        vbox:






            hbox:

                imagebutton:
                    idle "ex_credit_playing"
                    hover "ex_credit_playing"
                    action MainMenu(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
